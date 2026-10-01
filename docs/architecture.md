# Architecture

This project connects its data source to its Grafana dashboard through the components shown below.

## Overview

This diagram shows the data path for this project.

```mermaid
graph LR
  A[Tautulli API] -->|queried by| B[scabraha tautulli-exporter]
  B -->|filtered by| C[Allowlist relay]
  C -->|exposes metrics to| D[Prometheus]
  D -->|queried by| E[Grafana dashboard]
```

## Components

### Data source

Tautulli API -> scabraha/tautulli-exporter -> allowlist relay -> authenticated /metrics -> Prometheus -> Grafana.

### Dashboard

`dashboards/tautulli-application.json` contains the Grafana dashboard definition.

## Data flow

Tautulli API -> scabraha/tautulli-exporter -> allowlist relay -> authenticated /metrics -> Prometheus -> Grafana. Grafana evaluates dashboard queries against the selected data source and label values.

## Directory layout

```text
.
├── dashboards/  Grafana dashboard JSON files
├── examples/  Scrape and deployment examples
├── metrics_relay.py  Tautulli metric filtering relay
├── docs/        Documentation source
└── README.md    Project overview and quick links
```
