# 📊 Analytics

Repository analytics and traffic tracking documentation for PowerFxSnippets.

## Table of Contents

- [📊 Analytics](#-analytics)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
    - [Purpose](#purpose)
  - [Quick Navigation](#quick-navigation)
  - [Data Sources](#data-sources)
    - [Available Metrics](#available-metrics)
  - [Metrics Categories](#metrics-categories)
    - [1. Traffic Metrics](#1-traffic-metrics)
    - [2. Referrer Sources](#2-referrer-sources)
    - [3. Popular Content](#3-popular-content)
    - [4. Community Engagement](#4-community-engagement)
  - [Access Instructions](#access-instructions)
    - [Step-by-Step Guide](#step-by-step-guide)
    - [Screenshot Reference](#screenshot-reference)
  - [Limitations](#limitations)
  - [Related Documentation](#related-documentation)
  - [History](#history)

---

## Overview

The PowerFxSnippets repository uses GitHub's native analytics to track repository traffic, understand user engagement, and make data-driven decisions for content improvements. This documentation provides guidance on accessing, interpreting, and utilizing repository metrics.

### Purpose

- 📈 Monitor repository growth and engagement
- 🎯 Identify popular content and categories
- 🌐 Understand traffic sources and referrers
- 📊 Track community health (stars, forks, contributors)
- 📋 Inform content strategy and prioritization

---

## Quick Navigation

| Document | Purpose |
|----------|---------|
| [Baseline Metrics](baseline-metrics.md) | Initial snapshot captured February 2, 2026 |
| [Dashboard Template](dashboard-template.md) | Reusable template for weekly/monthly reports |
| [Reporting Schedule](reporting-schedule.md) | Weekly, monthly, quarterly reporting cadence |

---

## Data Sources

All metrics are sourced from **GitHub Insights**, GitHub's built-in analytics platform for repositories.

### Available Metrics

| Metric Type | Source | Update Frequency |
|-------------|--------|------------------|
| Views & Visitors | GitHub Insights → Traffic | Hourly |
| Clones | GitHub Insights → Traffic | Hourly |
| Referrers | GitHub Insights → Traffic | Daily |
| Popular Content | GitHub Insights → Traffic | Daily |
| Stars/Forks/Watchers | Repository main page | Real-time |
| Issues/PRs | Repository tabs | Real-time |

---

## Metrics Categories

### 1. Traffic Metrics

Track how users discover and interact with the repository:

- **Total Views**: Total page views (including repeats)
- **Unique Visitors**: Unique users who viewed the repository
- **Total Clones**: Git clone operations performed
- **Unique Cloners**: Unique users who cloned the repository

### 2. Referrer Sources

Understand where traffic originates:

- Direct traffic
- Search engines (Google, Bing, etc.)
- Social media (Twitter/X, LinkedIn, etc.)
- Referring sites (Microsoft Documentation, Power Platform blogs, etc.)

### 3. Popular Content

Identify most-viewed content:

- Top 10 most-viewed files/directories
- View counts per path
- Category distribution analysis

### 4. Community Engagement

Monitor community growth signals:

- ⭐ GitHub Stars
- 🍴 Forks
- 👁️ Watchers
- 🐛 Open Issues
- 🔄 Open Pull Requests

---

## Access Instructions

### Step-by-Step Guide

1. **Navigate to the repository**
   - Go to `https://github.com/PowerAppsDarren/PowerFxSnippets`

2. **Access Insights**
   - Click the **"Insights"** tab in the top navigation bar

3. **View Traffic Data**
   - In the left sidebar, click **"Traffic"**
   - Review the Views and Clones graphs
   - Scroll to see Top Referrers and Popular Content tables

4. **Document Community Metrics**
   - Return to the main repository page
   - Note the Stars, Forks, and Watchers counts (top right)
   - Click Issues tab for open issues count
   - Click Pull Requests tab for open PRs count

### Screenshot Reference

```
Repository Page
├── Insights (Tab)
│   └── Traffic (Sidebar)
│       ├── Views graph (14-day)
│       ├── Clones graph (14-day)
│       ├── Top Referrers table
│       └── Popular Content table
├── Stars ⭐ (Top right)
├── Forks 🍴 (Top right)
└── Watchers 👁️ (Top right)
```

---

## Limitations

⚠️ **Important considerations when using GitHub Insights:**

| Limitation | Details |
|------------|---------|
| **14-Day Window** | Traffic data is only available for the past 14 days. Historical data beyond this window is not accessible via the web UI. |
| **UTC+0 Timezone** | All timestamps are in UTC+0 timezone. |
| **Hourly Updates** | Views and clones update hourly; referrers and popular content update daily. |
| **Anonymous Data** | Visitor data is anonymized; individual user identification is not possible. |
| **Web UI Only** | Standard GitHub Free/Team plans only offer Insights via web UI. API access requires GitHub Enterprise or automation scripts. |

---

## Related Documentation

- [Main Documentation](../README.md) - Repository documentation index
- [Contributing Guidelines](../../CONTRIBUTING.md) - How to contribute snippets
- [Release Notes](../../RELEASE-NOTES-v2.0.0.md) - Version history and changes

---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-02-02 | @PowerAppsDarren | Initial analytics documentation setup; baseline metrics captured |

---

*Last updated: February 2, 2026*
