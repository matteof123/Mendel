# Mendel — Outbound Campaigns

_Operational source of truth for what's running, what's planned, and how copy + targeting evolves over time._

---

## Sync Update — 2026-05-12

**Status: PRE-LAUNCH.** No Kinetyca-owned campaigns are live yet. Email infrastructure is being built; database is at 80% completion. Launch target: **~2026-05-26**.

The agency black-box and SmartLead freelancer continue to run in parallel until Kinetyca's infrastructure replaces them. See [inherited-campaign-baseline.md](inherited-campaign-baseline.md) for the legacy campaign analysis.

### Metrics as of 2026-05-12 (Kinetyca-owned campaigns)

| ID | Campaign | Status | Leads | Sent | Replies | Interested | Bounced | Completion % |
|----|----------|--------|------:|-----:|--------:|-----------:|--------:|-------------:|
| — | (none yet) | not launched | 0 | 0 | 0 | 0 | 0 | 0% |

**Change vs previous sync:** N/A (first sync).

### Infrastructure build status (2026-05-12)

| Component | Status | Owner | Notes |
|---|---|---|---|
| Zapmail (email infra, Growth plan) | Set up | Alan (owner) / Matteo (ops) | Credentials shared via 1Password 2026-04-30 |
| Scaledmail | Set up | Alan / Matteo | — |
| Winnr | Set up | Alan / Matteo | — |
| Clay Master company table | Done 2026-05-12 | Affan | BlitzAPI Mexico + Mendel SmartLead deduped by domain |
| Clay contact discovery (Claygent) | In progress | Affan | Expected complete 2026-05-13 |
| Blocklist (companies + contacts) | To do | Affan | ClickUp 868jea2v0, due 2026-05-13 |
| Email waterfall enrichment | Not started | Affan | After Claygent + blocklist |
| EmailBison campaigns | Not created | Matteo | After enrichment |
| HeyReach LinkedIn campaigns | Not created | Affan | After EmailBison launch |
| HubSpot invite (for reply routing) | Pending (Alan) | Alan | Re-pinged 2026-05-12 |
| Sentiment-analysis workflow (positive replies → HubSpot) | Not built | Matteo | Pre-launch |

### Planned campaign structure for launch (~2026-05-26)

Based on inherited baseline analysis + strategy call decisions:

| # | Campaign | Geo | Persona | Industry segment | Language | Channel |
|---|----------|-----|---------|------------------|----------|---------|
| 1 | Finance MX — Industrial Manufacturing | Mexico | CFO / Controller / Finance Director | Manufacturing, automotive, mining | Spanish | Email + LinkedIn |
| 2 | Finance MX — Retail / CPG | Mexico | CFO / Controller / Finance Director | Retail, consumer goods, food/bev | Spanish | Email + LinkedIn |
| 3 | Finance MX — Logistics / Transport | Mexico | CFO / Controller / Logistics Manager | Logistics, transportation, distribution | Spanish | Email + LinkedIn |
| 4 | Finance MX — Pharma / Healthcare | Mexico | CFO / Controller / Tax Manager | Pharma, healthcare | Spanish | Email + LinkedIn |
| 5 | Finance MX — Professional Services | Mexico | CFO / Controller | Consulting, audit, legal | Spanish | Email + LinkedIn |
| 6 | Finance AR — Industrial (proven pattern) | Argentina | Controller / Finance Manager / Analyst | Manufacturing, energy, logistics | Spanish | Email + LinkedIn |
| 7 | Travel MX — Logistics + Prof Services | Mexico | Travel Manager + CFO | Logistics, consulting, legal | Spanish | Email (Mendel Viajes) |

Sequence template: 2 emails per campaign, independent threads. Email 1 = lead magnet (Mendel vs Concur benchmark PDF, or 30-day Spend Leakage Audit). Email 2 = service offer (Mendel demo).

### Copy guidelines (to be applied at launch)

Anchored on the Discovery doc (2026-05-12) + GTM playbook (2026-05-04). Hard rules per `.claude/rules/copy-rules.md`:

- 50-80 words per email
- No em dashes, no exclamation marks, no spam words
- Subject max 3 words, lowercase except company / person names
- Spanish for Mexico/AR/CL; English only for LatAm-HQ companies with US-based execs
- No currency mentions ($ / peso / dollar / price / cost / fee)
- No signature in body (handled by `{SENDER_EMAIL_SIGNATURE}`)
- No bracket placeholders, no empty variables
- Email 1 hooks must lead with aspiration / methodology / peer benchmark — never accusation about the prospect having a problem

### Interested Replies — Email — 2026-05-12

| # | Person | Title | Company | Campaign | City/Region | Quote |
|---|--------|-------|---------|----------|-------------|-------|
| — | (none yet — pre-launch) | | | | | |

### LinkedIn Campaigns — 2026-05-12

| Campaign | Sender | Leads | Contacted | Conn Sent | Conn Accepted | Conn Rate | Msgs Sent | Replies | Response Rate |
|----------|--------|------:|----------:|----------:|--------------:|----------:|----------:|--------:|--------------:|
| — | (not yet set up) | 0 | 0 | 0 | 0 | — | 0 | 0 | — |

HeyReach setup is scheduled after email infrastructure launches (~late May / early June). Sender profiles: TBD — Mendel-side senders to be confirmed during build.

### LinkedIn Interested Replies — 2026-05-12

| # | Person | Title | Company | Campaign | Sender | Reply |
|---|--------|-------|---------|----------|--------|-------|
| — | (none yet) | | | | | |

> Added: 2026-05-12 (first sync after onboarding 2026-04-28 + strategy 2026-05-05)

---

## Reference Files

- [inherited-campaign-baseline.md](inherited-campaign-baseline.md) — analysis of the 7 legacy SmartLead campaigns
- [../knowledge/dnc-blocklist.md](../knowledge/dnc-blocklist.md) — DNC + competitor + bank + gov blocklist
- [../call-summaries/2026-04-28-onboarding-mendel-kinetyca.md](../call-summaries/2026-04-28-onboarding-mendel-kinetyca.md)
- [../call-summaries/2026-05-05-strategy-mendel-kinetyca.md](../call-summaries/2026-05-05-strategy-mendel-kinetyca.md)
- [Discovery Questions Mendel - Kinetyca (Google Doc)](https://docs.google.com/document/d/1BZQc3QKpGTHXDEJIQxvPuEmRZm_Hmbm2d226ZY92e3M/edit)
- [Mendel Top-Performing Campaign Analysis (Google Doc)](https://docs.google.com/document/d/1oG1o2MfrIgYIkryB3WLeZjtfmspagVwFr0zZQueBEzY/edit)
- ClickUp Mendel list: https://app.clickup.com/901113677831
- Drive folder: https://drive.google.com/drive/folders/1vesXSIB0EWuMufGPE3L0VZx_GnZaP9l_
