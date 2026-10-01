# tautulli-monitoring — Architecture

Tautulli API -> upstream exporter -> allowlist relay -> authenticated /metrics -> Prometheus -> Grafana.

## Components

- [compose.yml](../compose.yml): container deployment
- [dashboards/](../dashboards): Grafana dashboard definitions
- [entrypoint.py](../entrypoint.py): loads the Tautulli API secret
- [examples/](../examples): deployment and scrape examples
- [metrics_relay.py](../metrics_relay.py): authenticated metrics filtering

## Data interpretation

The relay keeps only approved metric names and labels and returns tautulli_relay_up=0 if filtering fails. The raw exporter endpoint stays private. Library play totals include retained history and are sampled as gauges.
