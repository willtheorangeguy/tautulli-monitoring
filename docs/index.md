# Tautulli Monitoring

An authenticated filtering relay around scabraha/tautulli-exporter plus a Grafana dashboard for playback and library activity.

## Key features

- Playback and bandwidth summaries.
- Library activity and retained play history.
- Filtering relay with bounded metric labels.
- Separate API, Plex and relay health indicators.

## Quick start

Open Grafana and import `dashboards/tautulli-application.json` through **Dashboards → New → Import**. Select the configured data source and match the dashboard variables to your labels. See [Getting started](getting-started.md) for prerequisites and setup.

## Where to next

<div class="wt-grid" markdown>

[:material-rocket-launch: **Getting started**<br>Set up the required integrations](getting-started.md){ .wt-card }

[:material-download: **Installation**<br>Install and connect the required services](installation.md){ .wt-card }

[:material-tune: **Configuration**<br>Review scrape examples and dashboard variables](configuration.md){ .wt-card }

[:material-sitemap: **Architecture**<br>Follow metrics from source to dashboard](architecture.md){ .wt-card }

[:material-view-dashboard: **Dashboard usage**<br>Import and use the dashboard](usage.md){ .wt-card }

</div>

## Support

{{ support() }}
