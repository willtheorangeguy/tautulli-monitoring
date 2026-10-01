# Tautulli metrics relay and application dashboard

Portable monitoring bundle with example configuration. Replace example addresses and token paths for your installation; no live credentials are included.

## Requirements

The upstream scabraha/tautulli-exporter and the included filtering relay. The relay publishes bounded metrics with a bearer token.

## Dashboards

- `dashboards/tautulli-application.json`

Import the JSON in Grafana using **Dashboards > New > Import**. Select your data source from the dashboard variable(s) at the top. Update the Prometheus job variables to match your `scrape_configs` job names; use the Instance selector when present. The dashboard's JSON is also suitable for file provisioning after you have selected or provisioned data source UIDs.

Expected default job labels:

- `tautulli-application.json`: tautulli

## Monitoring code

See the code and example configuration in this folder, if present. Keep API keys and metrics bearer tokens in local secret files or another secret manager; never commit them. Scrape examples use documentation addresses and must be edited for your network.

## Before publishing

Test against the application and Grafana versions you intend to support. Add a license you choose and check attribution for upstream components. No release or Grafana catalog upload has been performed.

## Run the filtering relay

This Compose setup pins an upstream scabraha/tautulli-exporter image; the relay code here is original. Copy `.env.example` to `.env`, set the Tautulli URL, create `api-key` and `metrics-token` files beside `compose.yml`, then run `docker compose up -d`. Set `BIND_IP` to an address your Prometheus server can reach. Scrape the relay as job `tautulli` with a bearer token matching `metrics-token`. Keep the raw upstream endpoint private. Run `python -m unittest discover -s . -p test_metrics_relay.py` before release.

A sample `scrape_configs` fragment is in `examples/prometheus-scrape.yml`; replace the example hosts and token paths.
