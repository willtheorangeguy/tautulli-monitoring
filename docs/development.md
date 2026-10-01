# tautulli-monitoring — Development

The implementation and dashboard definitions are in the repository root. Tautulli API -> upstream exporter -> allowlist relay -> authenticated /metrics -> Prometheus -> Grafana.

## Local checks

The repository CI workflow runs `python -m unittest discover -s . -p test_metrics_relay.py`. Run it from the repository root after changing the relevant source or dashboard JSON.

When editing dashboards, export the final JSON from Grafana and keep data source variables, job names and panel descriptions in sync with [configuration](./configuration.md).

[entrypoint.py](../entrypoint.py) loads the Tautulli API key from a mounted file before starting the upstream exporter. [metrics_relay.py](../metrics_relay.py) is the local allowlist and bearer-protected endpoint. The [Compose file](../compose.yml) mounts both files into pinned upstream images. Update [test_metrics_relay.py](../test_metrics_relay.py) when altering allowed names, labels or failure behavior.
