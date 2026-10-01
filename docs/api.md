# API

Tautulli API -> upstream exporter -> allowlist relay -> authenticated /metrics -> Prometheus -> Grafana.

## Interfaces

- The relay serves bearer protected `/metrics`. It exposes `tautulli_relay_up` as its filtering status. See [metrics_relay.py](https://github.com/willtheorangeguy/tautulli-monitoring/blob/HEAD/metrics_relay.py) for the metric allowlist and label rules.

## Prometheus scrape reference

See [examples/prometheus-scrape.yml](https://github.com/willtheorangeguy/tautulli-monitoring/blob/HEAD/examples/prometheus-scrape.yml) for the target, job name and authorization settings.

## Allowlist and failures

The relay allows scalar playback, user and health metrics; bounded session breakdowns; and library metrics labeled by library name and type. It renames `tautulli_session_count` to `tautulli_sessions_active`, `tautulli_libraries_total` to `tautulli_libraries`, and `tautulli_users_total` to `tautulli_users`. Unexpected labels, malformed samples, nonfinite values or a missing `tautulli_up` cause filtering to fail. The response then contains `tautulli_relay_up 0` without stale application values. See [metrics_relay.py](https://github.com/willtheorangeguy/tautulli-monitoring/blob/HEAD/metrics_relay.py) for the full allowlist.
