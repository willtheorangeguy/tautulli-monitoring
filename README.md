<h1 align="center">tautulli-monitoring</h1>
<h4 align="center">An authenticated filtering relay around scabraha/tautulli-exporter plus a Grafana dashboard for playback and library activity.</h4>

<div align="center">
  <img alt="GitHub Issues" src="https://img.shields.io/github/issues/willtheorangeguy/tautulli-monitoring">
  <img alt="GitHub Pull Requests" src="https://img.shields.io/github/issues-pr/willtheorangeguy/tautulli-monitoring">
  <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-blue">
  <img alt="gitleaks workflow" src="https://github.com/willtheorangeguy/tautulli-monitoring/actions/workflows/gitleaks.yml/badge.svg">
  <img alt="testing workflow" src="https://github.com/willtheorangeguy/tautulli-monitoring/actions/workflows/testing.yml/badge.svg">
</div>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#support">Support</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

<!-- Screenshot: after adding tautulli-monitoring/overview.png to .github/icons/, replace this comment with ![Dashboard overview](https://raw.githubusercontent.com/willtheorangeguy/.github/main/icons/tautulli-monitoring/overview.png). -->

An authenticated filtering relay around scabraha/tautulli-exporter plus a Grafana dashboard for playback and library activity.

## Key Features

- Playback and bandwidth summaries.
- Library activity and retained play history.
- Filtering relay with bounded metric labels.
- Separate API, Plex and relay health indicators.

## Installation

Docker Compose, Tautulli API key, upstream scabraha/tautulli-exporter, Prometheus and Grafana. Copy .env.example to .env and set TAUTULLI_URL. Put the API key in api-key and an independent bearer token in metrics-token beside compose.yml. Run docker compose up -d, adapt examples/prometheus-scrape.yml and import the dashboard. See [installation](docs/installation.md) for more detail.

## Usage

Import [tautulli-application.json](dashboards/tautulli-application.json) in Grafana using **Dashboards → New → Import**. Choose the data source and match the dashboard variables to your monitoring labels. See [dashboard usage](docs/usage.md).

## Documentation

Full documentation lives in [docs/](docs/README.md): [Quickstart](docs/quickstart.md) · [Configuration](docs/configuration.md) · [Architecture](docs/architecture.md) · [Dashboard usage](docs/usage.md) · [Troubleshooting](docs/troubleshooting.md).

## Support

Open a [GitHub Discussion](https://github.com/willtheorangeguy/tautulli-monitoring/discussions/new) or file an [issue](https://github.com/willtheorangeguy/tautulli-monitoring/issues/new/choose).

## Contributing

Contributions welcome. See the org-wide [Contributing Guide](https://github.com/willtheorangeguy/.github/blob/main/CONTRIBUTING.md) and [Code of Conduct](https://github.com/willtheorangeguy/.github/blob/main/CODE_OF_CONDUCT.md).

## License

MIT — see [LICENSE.md](LICENSE.md).
