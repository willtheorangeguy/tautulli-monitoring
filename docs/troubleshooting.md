# Troubleshooting

| Symptom | Check |
| --- | --- |
| Scrape 401 | check the bearer token file. |
| Relay reports tautulli_relay_up=0 | inspect upstream reachability and metric format. |
| Tautulli panels stale | check exporter poll age and Tautulli API key. |

## First checks

Check the selected Grafana data source and dashboard variables in [configuration](configuration.md). For Prometheus, inspect the target state and the exact job and instance labels before changing panel queries.
