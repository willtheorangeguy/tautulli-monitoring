# tautulli-monitoring — Configuration

The relay publishes port 9487 on BIND_IP, which defaults to 127.0.0.1. The Compose file sets activity polling to 30 seconds, inventory to 300 seconds and metadata to 1800 seconds. Prometheus must use the bearer token in metrics-token.

## Dashboard variables

| Dashboard | Variable | Type | Default or query |
|---|---|---|---|
| `tautulli-application.json` | `prometheus_ds` | datasource | `prometheus` |
| `tautulli-application.json` | `job_tautulli` | textbox | `tautulli` |
| `tautulli-application.json` | `instance` | query | `label_values(up{job="${job_tautulli}"}, instance)` |

## Prometheus jobs

The supplied [scrape example](../examples/prometheus-scrape.yml) defines `tautulli`. Copy its entries into your own scrape_configs and replace documentation hostnames. Job names can change if the dashboard variables change with them.

## Environment example

Start from [.env.example](../.env.example). Keep the resulting .env and all secret files outside version control.
