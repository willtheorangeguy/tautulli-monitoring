"""Authenticated, fail-closed allowlist for upstream Tautulli metrics."""
import hmac
import math
import os
import re
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

SCALAR = {
    'tautulli_session_count', 'tautulli_sessions_secure', 'tautulli_plex_reachable',
    'tautulli_libraries_total', 'tautulli_users_total', 'tautulli_users_active',
    'tautulli_users_home', 'tautulli_up', 'tautulli_exporter_poll_duration_seconds',
    'tautulli_exporter_last_successful_poll_timestamp_seconds',
    'tautulli_plex_update_available',
}
LABELS = {name: set() for name in SCALAR}
LABELS.update({
    'tautulli_sessions_by_decision': {'decision'},
    'tautulli_sessions_by_state': {'state'},
    'tautulli_sessions_by_location': {'location'},
    'tautulli_sessions_by_media_type': {'media_type'},
    'tautulli_session_bandwidth_bytes': {'scope'},
    'tautulli_exporter_poll_failures_total': {'step'},
    'tautulli_plex_version_info': {'version', 'server_name'},
    'tautulli_plex_update_info': {'version', 'release_date', 'platform'},
})
for suffix in ('items', 'seasons', 'episodes', 'plays', 'play_duration_seconds',
               'last_accessed_timestamp_seconds', 'active', 'size_bytes'):
    LABELS['tautulli_library_' + suffix] = {'name', 'type'}
SAMPLE = re.compile(r'^([a-zA-Z_:][a-zA-Z0-9_:]*)(?:\{(.*)\})?\s+(\S+)(?:\s+\S+)?$')
LABEL = re.compile(r'([a-zA-Z_][a-zA-Z0-9_]*)="(?:\\.|[^"\\])*"')
RENAMES = {
    'tautulli_session_count': 'tautulli_sessions_active',
    'tautulli_libraries_total': 'tautulli_libraries',
    'tautulli_users_total': 'tautulli_users',
}


def sanitize(raw):
    lines = []
    seen = set()
    for line in raw.splitlines():
        if line.startswith('#'):
            parts = line.split()
            if len(parts) >= 3 and parts[1] in ('HELP', 'TYPE') and parts[2] in LABELS:
                lines.append(line.replace(parts[2], RENAMES.get(parts[2], parts[2]), 1))
            continue
        if not line.strip():
            continue
        match = SAMPLE.fullmatch(line)
        if not match:
            raise ValueError('Invalid upstream metric exposition')
        name, labels, value = match.groups()
        if name not in LABELS:
            continue
        if set(LABEL.findall(labels or '')) != LABELS[name]:
            raise ValueError('Unexpected labels on allowlisted metric')
        if not math.isfinite(float(value)):
            raise ValueError('Nonfinite upstream sample')
        lines.append(RENAMES.get(name, name) + line[len(name):])
        seen.add(name)
    if 'tautulli_up' not in seen:
        raise ValueError('Missing upstream health metric')
    return '\n'.join(lines) + '\n'


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != '/metrics':
            self.send_error(404)
            return
        if not hmac.compare_digest(self.headers.get('Authorization', ''), 'Bearer ' + self.server.token):
            self.send_error(401)
            return
        try:
            with urllib.request.urlopen(self.server.upstream, timeout=10) as response:
                body = sanitize(response.read().decode())
            body += '# HELP tautulli_relay_up Whether upstream filtering succeeded.\n# TYPE tautulli_relay_up gauge\ntautulli_relay_up 1\n'
        except Exception:
            # Do not log exception URLs or return stale/synthetic application data.
            body = '# HELP tautulli_relay_up Whether upstream filtering succeeded.\n# TYPE tautulli_relay_up gauge\ntautulli_relay_up 0\n'
        data = body.encode()
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; version=0.0.4; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *args):
        pass


if __name__ == '__main__':
    server = ThreadingHTTPServer(('0.0.0.0', 9487), Handler)
    server.token = Path('/run/secrets/metrics_token').read_text().strip()
    if not server.token:
        raise RuntimeError('Empty bearer secret')
    server.upstream = os.getenv('UPSTREAM_URL', 'http://tautulli-exporter:9487/metrics')
    server.serve_forever()
