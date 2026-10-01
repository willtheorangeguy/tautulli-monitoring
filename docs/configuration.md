# Configuration

## Precedence

This repository combines dashboard defaults with settings for external services. It defines no shared command-line, environment variable and configuration-file override order; each external service resolves its own settings.

## Integration settings

The relay publishes port 9487 on BIND_IP, which defaults to 127.0.0.1. The Compose file sets activity polling to 30 seconds, inventory to 300 seconds and metadata to 1800 seconds. Prometheus must use the bearer token in metrics-token.

## Dashboard variables

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `tautulli-application.json / prometheus_ds` | datasource | `prometheus` | Grafana data source selected by the dashboard. |
| `tautulli-application.json / job_tautulli` | textbox | `tautulli` | Dashboard variable whose value selects a scrape job, instance or endpoint. |
| `tautulli-application.json / instance` | query | `label_values(up{job="${job_tautulli}"}, instance)` | Queries the data source for available values. |

## Prometheus jobs

The supplied [scrape example](https://github.com/willtheorangeguy/tautulli-monitoring/blob/HEAD/examples/prometheus-scrape.yml) defines `tautulli`. Copy its entries into your own scrape_configs and replace documentation hostnames. Job names can change if the dashboard variables change with them.

## Environment example

Start from [.env.example](https://github.com/willtheorangeguy/tautulli-monitoring/blob/HEAD/.env.example). Keep the resulting .env and all secret files outside version control.

## Examples

The complete scrape job examples are in [`examples/prometheus-scrape.yml`](https://github.com/willtheorangeguy/tautulli-monitoring/blob/HEAD/examples/prometheus-scrape.yml). Copy the relevant job into your Prometheus configuration and replace the example targets.
