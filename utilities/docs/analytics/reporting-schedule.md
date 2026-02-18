# 📅 Reporting Schedule

Analytics reporting cadence and procedures for PowerFxSnippets.

---

## Table of Contents

- [Weekly Reporting](#weekly-reporting)
- [Monthly Reporting](#monthly-reporting)
- [Quarterly Reporting](#quarterly-reporting)
- [Ad-Hoc Reporting](#ad-hoc-reporting)
- [Reporting Checklist](#reporting-checklist)
- [Schedule Overview](#schedule-overview)
- [History](#history)

---

## Weekly Reporting

### Schedule

| Attribute | Value |
|-----------|-------|
| **Frequency** | Every Monday |
| **Time** | 9:00 AM UTC |
| **Scope** | Traffic metrics, top referrers, popular content (7-day window) |
| **Owner** | Repository maintainer or designated analytics lead |

### Process

1. **Data Collection** (Monday 9:00 AM UTC)
   - Access [GitHub Insights → Traffic](https://github.com/PowerAppsDarren/PowerFxSnippets/graphs/traffic)
   - Record views, visitors, clones, cloners
   - Document top 5 referrers
   - Identify top 10 popular content items

2. **Report Generation**
   - Copy [`dashboard-template.md`](./dashboard-template.md)
   - Fill in data for the past 7 days
   - Add week-over-week comparisons
   - Generate insights and recommendations

3. **Distribution**
   - Create GitHub Discussion post with "analytics" label
   - Post summary to team communication channel (if applicable)
   - Link to full report in repository

### Report Storage

- **Location**: `utilities/docs/analytics/reports/`
- **Naming**: `YYYY-MM-DD-weekly-report.md`
- **Example**: `2026-02-09-weekly-report.md`

---

## Monthly Reporting

### Schedule

| Attribute | Value |
|-----------|-------|
| **Frequency** | First Monday of each month |
| **Time** | 9:00 AM UTC |
| **Scope** | Comprehensive metrics including community engagement, content quality, contributor stats |
| **Owner** | Repository maintainer |

### Process

1. **Data Collection** (First Monday 9:00 AM UTC)
   - Collect all traffic metrics (aggregate 4 weeks of data)
   - Document community metrics (stars, forks, watchers)
   - Count open/closed issues and PRs
   - Review contributor activity

2. **Report Generation**
   - Use [`dashboard-template.md`](./dashboard-template.md) with extended sections
   - Add month-over-month trend analysis
   - Include content quality metrics
   - Identify top contributors

3. **Distribution**
   - Create GitHub Discussion post
   - Update [`baseline-metrics.md`](./baseline-metrics.md) with new monthly data
   - Send summary to stakeholders

### Additional Metrics (Monthly)

| Metric | Source | Purpose |
|--------|--------|---------|
| Contributor Count | Insights → Contributors | Track community growth |
| PR Merge Rate | PR history | Measure contribution quality |
| Issue Resolution Time | Issue history | Track responsiveness |
| Content Additions | File diff | Track repository growth |

---

## Quarterly Reporting

### Schedule

| Attribute | Value |
|-----------|-------|
| **Frequency** | First Monday of January, April, July, October |
| **Time** | 9:00 AM UTC |
| **Scope** | Strategic review including content gaps, category performance, community health |
| **Owner** | Repository maintainer + core contributors |

### Process

1. **Strategic Review** (Quarterly, First Monday)
   - Analyze 3-month trends
   - Identify content gaps and opportunities
   - Review category performance
   - Assess community health indicators

2. **Report Generation**
   - Extended dashboard template with trend analysis
   - Year-over-year comparisons (if available)
   - Strategic recommendations for next quarter
   - Content roadmap suggestions

3. **Distribution**
   - GitHub Discussion with extended summary
   - Update main [`README.md`](../../README.md) stats section
   - Present findings to core contributor team

### Strategic Metrics (Quarterly)

| Area | Metrics |
|------|---------|
| **Growth** | Quarter-over-quarter traffic growth, star velocity |
| **Engagement** | Average time on content, return visitor rate |
| **Quality** | Validation pass rate, issue resolution rate |
| **Community** | New contributor rate, PR acceptance rate |
| **Content** | Category coverage, popular vs. underserved topics |

---

## Ad-Hoc Reporting

### Triggers

| Trigger | When to Report |
|---------|----------------|
| **Major Releases** | Within 48 hours of v2.0.0+ releases |
| **Traffic Spikes** | When daily views exceed 2x the 14-day average |
| **Community Milestones** | At 100, 250, 500, 1000 stars |
| **Viral Content** | When single content piece exceeds 100 views in 24 hours |
| **External Features** | When featured in blogs, newsletters, or conferences |

### Process

1. **Immediate Documentation**
   - Capture relevant metrics
   - Document the event/trigger
   - Screenshot key data points

2. **Quick Analysis**
   - Identify cause of spike/milestone
   - Compare to baseline metrics
   - Assess impact on other metrics

3. **Communication**
   - Create GitHub Discussion or announcement
   - Thank community if applicable
   - Share insights learned

---

## Reporting Checklist

Use this checklist for every report to ensure consistency:

### Pre-Report

- [ ] Confirm report type (Weekly/Monthly/Quarterly/Ad-Hoc)
- [ ] Identify report owner
- [ ] Set calendar reminder for next report

### Data Collection

- [ ] Access GitHub Insights → Traffic
- [ ] Collect traffic metrics (views, visitors, clones)
- [ ] Document top 5 referrers
- [ ] Identify top 10 popular content items
- [ ] Record community metrics (stars, forks, watchers)
- [ ] Count open issues
- [ ] Count open PRs

### Analysis

- [ ] Calculate period-over-period changes
- [ ] Identify trends (up/down/stable)
- [ ] Note any anomalies or unusual patterns
- [ ] Compare to previous baselines

### Report Creation

- [ ] Fill in dashboard template
- [ ] Update all `[value]` placeholders
- [ ] Generate 3-5 key insights
- [ ] Provide actionable recommendations
- [ ] Proofread for accuracy

### Distribution

- [ ] Create GitHub Discussion (with "analytics" label)
- [ ] Post to appropriate channels
- [ ] Link to full report in repository
- [ ] Archive report in `utilities/docs/analytics/reports/`

### Post-Report

- [ ] Update baseline metrics (if monthly/quarterly)
- [ ] Schedule follow-up actions
- [ ] Document any process improvements needed

---

## Schedule Overview

| Report Type | Frequency | Next Due | Owner | Storage |
|-------------|-----------|----------|-------|---------|
| **Weekly** | Every Monday | 2026-02-09 | Analytics Lead | `reports/YYYY-MM-DD-weekly-report.md` |
| **Monthly** | 1st Monday | 2026-03-02 | Maintainer | Updated `baseline-metrics.md` |
| **Quarterly** | Jan/Apr/Jul/Oct | 2026-04-06 | Maintainer + Contributors | Discussion + README update |
| **Ad-Hoc** | As triggered | - | Maintainer | Discussion only |

### 2026 Reporting Calendar

| Month | Weekly Reports | Monthly Report | Quarterly Report |
|-------|----------------|----------------|------------------|
| **February** | 2nd, 9th, 16th, 23rd | - | - |
| **March** | 2nd, 9th, 16th, 23rd, 30th | March 2 | - |
| **April** | 6th, 13th, 20th, 27th | - | April 6 |
| **May** | 4th, 11th, 18th, 25th | May 4 | - |
| **June** | 1st, 8th, 15th, 22nd, 29th | June 1 | - |
| **July** | 6th, 13th, 20th, 27th | - | July 6 |

*All dates are Mondays at 9:00 AM UTC*

---

## Timezone Reference

All reporting times are in **UTC+0**:

| UTC Time | EST (UTC-5) | PST (UTC-8) |
|----------|-------------|-------------|
| 09:00 | 04:00 | 01:00 |
| 12:00 | 07:00 | 04:00 |
| 15:00 | 10:00 | 07:00 |

---

## History

| Date | Author | Changes |
|------|--------|---------|
| 2026-02-02 | @PowerAppsDarren | Initial reporting schedule established with weekly, monthly, quarterly, and ad-hoc cadences |

---

*Last updated: February 2, 2026*
*Timezone: UTC+0*
