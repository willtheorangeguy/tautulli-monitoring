# tautulli-monitoring — Dashboard Usage

Import the JSON files using **Grafana → Dashboards → New → Import**. Set the data source and variables listed in [configuration](./configuration.md).

## Tautulli Application Overview

Source: [tautulli-application.json](../dashboards/tautulli-application.json). Refresh: `30s`.

<!-- Screenshot: after adding tautulli-application.png to .github/icons/tautulli-monitoring/, replace this comment with ![Tautulli Application Overview](https://raw.githubusercontent.com/willtheorangeguy/.github/main/icons/tautulli-monitoring/tautulli-application.png). -->

### Panels

| Panel | Type | What it shows |
|---|---|---|
| Service Health | stat | Scrape, Tautulli API, Plex connection, and relay must all report healthy. |
| Active Sessions | stat | Active playback sessions reported by Tautulli. |
| Transcodes | stat | Sessions requiring transcoding. |
| Session Bandwidth | stat | Total active-session bandwidth converted by upstream from kbps to bytes per second. |
| Active Libraries | stat | Libraries currently active in Plex; excludes retained historical libraries. |
| Known Users | stat | Users known to Tautulli; viewer identities are not exported. |
| Recorded Plays | stat | Recorded library play totals, including retained library history. |
| Recorded Watch Time | stat | Recorded watch duration across tracked libraries; not media runtime. |
| Sessions by Playback Decision | timeseries | Tautulli's direct play, direct stream, copy, and transcode session decisions. |
| Player States | timeseries | Playing, paused, and buffering sessions. |
| Bandwidth by Network Scope | timeseries | LAN, WAN, and total bandwidth. Total includes its components; series are not stacked. |
| Sessions by Network Location | timeseries | Sessions on LAN, WAN, and relay. |
| Sessions by Media Type | timeseries | Current movie, episode, track, live, and clip playback counts. |
| Recorded Plays by Library | bargauge | Historical library play totals retained by Tautulli. |
| Recorded Watch Time by Library | bargauge | Historical watch duration, not total playable duration. |
| Top-level Items by Library | bargauge | Movies, shows, or artists depending on the library type. These distinct units are not summed. |
| Seasons / Albums by Library | bargauge | Parent items: seasons in show libraries and albums in music libraries. |
| Episodes / Tracks by Library | bargauge | Child items: episodes in show libraries and tracks in music libraries. |
| Tracked and Active Libraries | timeseries | Tracked records include retained library history; active count is separate. |
| Aggregate User Inventory | timeseries | User inventory flags are overlapping categories, not current viewers. |
| Recorded Library Plays Over Time | timeseries | Stored lifetime totals sampled into Prometheus. No rate is derived from this mutable gauge. |
| Recorded Watch Time Over Time | timeseries | Stored lifetime watch duration, including retained history. |
| Metrics Health History | timeseries | Independent scrape, API, Plex, and relay health. |
| Activity Poll Age | timeseries | Age of the last successful activity poll. Inventory refreshes every five minutes. |
| Activity Poll Duration | timeseries | Duration of the exporter activity poll. |
| Encrypted Sessions | timeseries | Sessions with encrypted connections to Plex. |
| Plex Update Available | stat | Exporter-reported update status, refreshed every 30 minutes. |

<!-- Screenshot: add a focused panel or section image here after uploading it to .github/icons/tautulli-monitoring/. -->

### Reading the results

The relay keeps only approved metric names and labels and returns tautulli_relay_up=0 if filtering fails. The raw exporter endpoint stays private. Library play totals include retained history and are sampled as gauges.

### Query reference

These expressions are copied from the dashboard JSON. Grafana substitutes the dashboard variables at runtime.

#### Service Health

```promql
min(up{job="${job_tautulli}",instance="$instance"}) * min(tautulli_up{job="${job_tautulli}",instance="$instance"}) * min(tautulli_plex_reachable{job="${job_tautulli}",instance="$instance"}) * min(tautulli_relay_up{job="${job_tautulli}",instance="$instance"})
```

#### Active Sessions

```promql
tautulli_sessions_active{job="${job_tautulli}",instance="$instance"}
```

#### Transcodes

```promql
sum(tautulli_sessions_by_decision{job="${job_tautulli}",instance="$instance",decision="transcode"})
```

#### Session Bandwidth

```promql
tautulli_session_bandwidth_bytes{job="${job_tautulli}",instance="$instance",scope="total"}
```

#### Active Libraries

```promql
sum(tautulli_library_active{job="${job_tautulli}",instance="$instance"})
```

#### Known Users

```promql
tautulli_users{job="${job_tautulli}",instance="$instance"}
```

#### Recorded Plays

```promql
sum(tautulli_library_plays{job="${job_tautulli}",instance="$instance"})
```

#### Recorded Watch Time

```promql
sum(tautulli_library_play_duration_seconds{job="${job_tautulli}",instance="$instance"})
```

#### Sessions by Playback Decision

```promql
tautulli_sessions_by_decision{job="${job_tautulli}",instance="$instance"}
```

#### Player States

```promql
tautulli_sessions_by_state{job="${job_tautulli}",instance="$instance"}
```

#### Bandwidth by Network Scope

```promql
tautulli_session_bandwidth_bytes{job="${job_tautulli}",instance="$instance"}
```

#### Sessions by Network Location

```promql
tautulli_sessions_by_location{job="${job_tautulli}",instance="$instance"}
```

#### Sessions by Media Type

```promql
tautulli_sessions_by_media_type{job="${job_tautulli}",instance="$instance"}
```

#### Recorded Plays by Library

```promql
sort_desc(tautulli_library_plays{job="${job_tautulli}",instance="$instance"})
```

#### Recorded Watch Time by Library

```promql
sort_desc(tautulli_library_play_duration_seconds{job="${job_tautulli}",instance="$instance"})
```

#### Top-level Items by Library

```promql
tautulli_library_items{job="${job_tautulli}",instance="$instance"}
```

#### Seasons / Albums by Library

```promql
tautulli_library_seasons{job="${job_tautulli}",instance="$instance"}
```

#### Episodes / Tracks by Library

```promql
tautulli_library_episodes{job="${job_tautulli}",instance="$instance"}
```

#### Tracked and Active Libraries

```promql
tautulli_libraries{job="${job_tautulli}",instance="$instance"}
sum(tautulli_library_active{job="${job_tautulli}",instance="$instance"})
```

#### Aggregate User Inventory

```promql
tautulli_users{job="${job_tautulli}",instance="$instance"}
tautulli_users_active{job="${job_tautulli}",instance="$instance"}
tautulli_users_home{job="${job_tautulli}",instance="$instance"}
```

#### Recorded Library Plays Over Time

```promql
sum(tautulli_library_plays{job="${job_tautulli}",instance="$instance"})
```

#### Recorded Watch Time Over Time

```promql
sum(tautulli_library_play_duration_seconds{job="${job_tautulli}",instance="$instance"})
```

#### Metrics Health History

```promql
up{job="${job_tautulli}",instance="$instance"}
tautulli_up{job="${job_tautulli}",instance="$instance"}
tautulli_plex_reachable{job="${job_tautulli}",instance="$instance"}
tautulli_relay_up{job="${job_tautulli}",instance="$instance"}
```

#### Activity Poll Age

```promql
time() - tautulli_exporter_last_successful_poll_timestamp_seconds{job="${job_tautulli}",instance="$instance"}
```

#### Activity Poll Duration

```promql
tautulli_exporter_poll_duration_seconds{job="${job_tautulli}",instance="$instance"}
```

#### Encrypted Sessions

```promql
tautulli_sessions_secure{job="${job_tautulli}",instance="$instance"}
```

#### Plex Update Available

```promql
tautulli_plex_update_available{job="${job_tautulli}",instance="$instance"}
```
