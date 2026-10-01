# Getting started

## Prerequisites

Docker Compose, Tautulli API key, upstream scabraha/tautulli-exporter, Prometheus and Grafana.

## Set up

Copy .env.example to .env and set TAUTULLI_URL. Put the API key in api-key and an independent bearer token in metrics-token beside compose.yml. Run docker compose up -d, adapt examples/prometheus-scrape.yml and import the dashboard.

The example Prometheus scrape job names are `tautulli`.

## Confirm data

In Prometheus, check `up{job="tautulli"}` and inspect a panel query in Grafana.
For missing data, see [Troubleshooting](troubleshooting.md).
