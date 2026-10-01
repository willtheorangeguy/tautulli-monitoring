# tautulli-monitoring — Installation

## Requirements

Docker Compose, Tautulli API key, upstream scabraha/tautulli-exporter, Prometheus and Grafana.

## Procedure

Copy .env.example to .env and set TAUTULLI_URL. Put the API key in api-key and an independent bearer token in metrics-token beside compose.yml. Run docker compose up -d, adapt examples/prometheus-scrape.yml and import the dashboard.

The files under [examples](../examples) are reference configuration. Replace example addresses, token paths and bind addresses for your deployment.

Next, review [configuration](./configuration.md) and [dashboard usage](./usage.md).

## Compose lifecycle

From the repository root run `docker compose up -d --build` when Compose builds a local image, or `docker compose up -d` for prebuilt images. Inspect container output with `docker compose logs`. Keep credential files out of Git.
