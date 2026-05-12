# Mendel — Client Brain

Mendel is the all-in-one corporate spend management platform for enterprise companies in Latin America. CFOs are the primary buyers. Mexico is the priority market (90% of growth focus). The Outreach Magic engagement is replacing a black-box agency and a freelancer-on-SmartLead with a fully owned email + LinkedIn machine.

_Last synced: 2026-05-12_

---

## Active Campaigns
<!-- Sync: 2026-05-12 -->

**Status: PRE-LAUNCH** — no Kinetyca-owned campaigns are live yet. Email infrastructure (Zapmail + EmailBison + Scaledmail + Winnr) is being built. Database build is at 80% (4 of 5 sub-tasks done in ClickUp). Launch target: **~2026-05-26** (3 weeks from the May 5 strategy call).

**Inherited baseline (agency + SmartLead freelancer, being phased out):**
The agency/freelancer ran 7 campaigns on the legacy SmartLead instance. Aggregate baseline: ~31,300 unique leads contacted, ~7,000+ unique reaches by sequence, reply rates ranged **0.36% – 2.82%**, positive replies ranged **0.45% – 1.04%** of unique leads. Argentina campaigns outperformed Mexico campaigns on reply rate despite Mexico being the strategic priority. Full breakdown in [campaigns/inherited-campaign-baseline.md](campaigns/inherited-campaign-baseline.md).

| Inherited campaign | Geo | Leads | Sent | Reply % | Positive | Bounce % |
|---|---|---:|---:|---:|---:|---:|
| Finance Report V2 — ARG | Argentina | 1,706 | 7,451 | 2.82% | 10 (0.60%) | 1.56% |
| Finance Report V2 | Mexico | 5,082 | 27,486 | 1.39% | 74 (1.04%) | 5.33% |
| A30 Industry Blended — STS | Argentina | 5,258 | 30,157 | 0.61% | 47 | 0.71% |
| A30 Industry Blended — Risky | Argentina | 3,299 | 18,249 | 0.36% | 13 (0.45%) | 2.53% |
| Finance Team Waterfall | Mexico | — | — | — | — | — |
| CFOs Batch 2 | Mexico | — | — | — | — | — |
| Sales Leaders | Mexico | — | — | — | — | — |

Bounce on the Mexico "Finance Report V2" campaign (5.33%) is above our 3% safety threshold and is one of the reasons we are rebuilding infrastructure from scratch on Zapmail.

---

## What's Working
<!-- Sync: 2026-05-12 -->

**From inherited campaign analysis (May 5):**
- **Argentina Finance Report V2** is the structural winner: 2.82% reply rate, the highest in the entire history. Industries: manufacturing, energy, construction, logistics, retail, media, healthcare. Titles: analysts, controllers, finance managers, tax specialists, accountants. **Implication for our build:** keep ARG as a parallel-but-secondary lane; the same persona structure (operational mid-market with real finance teams) should be tested in Mexico.
- **Mexico Finance Report V2** has the highest absolute positive count (74 positive on 7,099 unique leads = 1.04%). Industries: manufacturing + automotive heavy. Titles: Finance Directors / Managers / Controllers / "Contralors". Geo: CDMX, Guadalajara, Monterrey, Bajío. **Implication:** Finance Director / Controller persona on operational/industrial companies is our highest-probability Mexico segment.
- **A30 STS Argentina** quality conversion of replies → positives is 25.5% (47 positive out of 184 replies). Despite lower top-line reply rate, replies are higher-quality than other campaigns. **Implication:** broader industry mix can work if subject + hook is strong enough to filter out time-wasters.

## What's Not Working
<!-- Sync: 2026-05-12 -->

- **Mexico "Finance Report V2" bounce rate at 5.33%** — over our 3% safety threshold. The Mexico/CDMX data quality on the legacy SmartLead instance is poor. **Action:** mandatory full waterfall (BlitzAPI → Debounce → FindyMail → LeadMagic → BounceBan) on every Mexico lead before send.
- **"A30 Industry Blended — Risky"** at 0.36% reply / 0.45% positive — too broad targeting (electricity transmission + packaging + plastics + medical devices + food & beverage). **Implication:** narrow industry blending. One industry vertical per campaign, not five.
- **Sender bounces (120 on STS, 178 on Risky)** signal sender-side warmup or list-quality issues. **Implication:** Zapmail rebuild with proper warmup is the right call.
- **Geography mismatch:** 4 of 7 inherited campaigns target Argentina, but per Alan's strategy 90% of growth focus is Mexico. **Implication:** invert the ratio. Mexico-first, Argentina secondary.

---

## Recent Call Notes
<!-- Sync: 2026-05-12 -->

**Most recent first. Full transcripts in [call-summaries/](call-summaries/).**

### 2026-05-05 — Strategy / Mendel - Kinetyca (62 min)
Attendees: Alan Karpovsky (Mendel), Matteo Fois, David. Decisions: build unified company + contact database in Clay merging multiple sources (BlitzAPI Mexico + Mendel SmartLead legacy + Discolike + later Apollo); Claygent for contact discovery as differentiator; segmented email + LinkedIn campaigns with A/B testing; periodic refreshes + evergreen + conference scraping; sentiment-analysis workflow for auto-reply qualification → HubSpot; warmup + launch ~3 weeks from May 5 (i.e. **~May 26**). [→ Full summary](call-summaries/2026-05-05-strategy-mendel-kinetyca.md)

### 2026-04-28 — Onboarding / Mendel - Kinetyca (66 min)
Attendees: Alan Karpovsky, Matteo Fois, David. Confirmed: black-box agency + SmartLead freelancer phased out. Target: mid-market + enterprise Mexico, CFOs primary. Differentiators: real-time policy engine BEFORE transaction + CFDI automated retrieval (Mexico-specific). New email infrastructure (Zapmail) decided. [→ Full summary](call-summaries/2026-04-28-onboarding-mendel-kinetyca.md)

---

## Recent Slack Updates
<!-- Sync: 2026-05-12 -->

**Channel:** `#mendel-project` (active since 2026-04-30). Members: Matteo, David, Affan (Kinetyca), Alan Karpovsky (Mendel).

**Critical DNC instructions (Alan, 2026-05-06)** — full list in [knowledge/dnc-blocklist.md](knowledge/dnc-blocklist.md):
- Do NOT contact: SmartLead DNC list, agency DNC list, current customers (list shared in ClickUp), banks (regex below), government (.gob.mx/.gob.cl/.gob.ar/.gov.ar/.mil.ar), competitors (Clara, Jeeves, Xpendit, Cardda, Caju, ContaSimples, AMEX, SAP Concur, RindeGastos, BUK, Argo, Voll, PayTrack, OnFly, Brex, Ramp, Emburse, Mesh, Pleo), Mercado Libre (all regional domains).
- Banks regex (Mexico): `\.(bbva|banorte|santander|citibanamex|banamex|hsbc|scotiabank|azteca|inbursa|bajio|afirme|mifel)\.(mx|com\.mx)$`

**Open requests to client (still pending as of 2026-05-12):**
- Agency DNC list (Alan to share via HubSpot/email — Affan re-pinged 2026-05-12)
- HubSpot invite to Mendel workspace (Alan to send — Affan re-pinged 2026-05-12)

**Goal restated by Alan (2026-05-08):** "100 extra qualified leads per Q"

**Discovery document sent to Alan (2026-05-12):** [Discovery Questions Mendel - Kinetyca](https://docs.google.com/document/d/1BZQc3QKpGTHXDEJIQxvPuEmRZm_Hmbm2d226ZY92e3M/edit). Already filled with deep UVP, ICP, problem framing, sales objections, competitor positioning. Use as ground truth for copy.

---

## ClickUp This Week
<!-- Sync: 2026-05-12 -->

**List:** `Clients Space > Retainers > Mendel` ([app.clickup.com/list/901113677831](https://app.clickup.com/901113677831))

**Database Building milestone (parent 868jea2rf) — 80% complete, due 2026-05-13:**
- ✅ Setup Clay Accesses — done
- ✅ Identify data source + contact strategy — done
- ✅ Create the first Clay Tables (Internal Approval) — done 2026-05-12
- ✅ Create the initial Company and Contacts Database — done 2026-05-12
- ⏳ Implement the blocklist (868jea2v0) — TO DO, assigned Affan, due ~May 13

**Status reported by Affan (2026-05-12):**
- Claygent AI contact-discovery (3rd step) in progress, expected complete 2026-05-13
- Next: company + contact-level blocklist → email waterfall enrichment → HeyReach LinkedIn setup
- Backend: Slack channel done; HubSpot invite still pending from client

---

## Open Action Items
<!-- Sync: 2026-05-12 -->

| Owner | Task | Source | Due |
|---|---|---|---|
| Alan (Mendel) | Share agency DNC list | Slack 2026-05-12 (re-ping) | ASAP |
| Alan (Mendel) | Send HubSpot invite (affan@kinetyca.com) | Slack 2026-05-12 | ASAP |
| Alan (Mendel) | Fill Discovery Questions doc (sent 2026-05-12) | Slack 2026-05-12 | This week |
| Alan (Mendel) | Review Spanish sequence copy when shared | Strategy call 2026-05-05 (56:22) | Pre-launch |
| Affan | Implement blocklist in Clay (ClickUp 868jea2v0) | ClickUp | 2026-05-13 |
| Affan | Finish Claygent contact discovery | Slack 2026-05-12 | 2026-05-13 |
| Affan | Run email waterfall on enriched contacts | Strategy call | Pre-launch |
| Affan | Set up HeyReach LinkedIn campaigns | Strategy call | Pre-launch |
| Matteo | Build sentiment-analysis workflow (reply → HubSpot) | Strategy call 2026-05-05 (48:37) | Pre-launch |
| Matteo | Coordinate warmup + final launch (~May 26) | Strategy call 2026-05-05 (52:59) | 2026-05-26 |
| Matteo | Share Smartlead analysis doc with Alan for transparency | Strategy call 2026-05-05 (54:02) | ASAP |
| Matteo | Send new sequences + database samples to Mendel for review | Strategy call 2026-05-05 (56:31) | Pre-launch |
| Matteo | Send copy sample for approval (the one gate before all-leads write) | Standard rule | Pre-launch |

---

## ICP Snapshot

- **Geography:** Mexico (90% growth focus), Argentina, Chile
- **Size:** 500+ employees (sweet spot: 150+ Mexico per Discovery doc), USD $50M+ annual operational spend; multi-entity / multi-country a strong plus
- **Industries:** Retail/CPG, Logistics & Transportation, Manufacturing, Pharmaceutical/Healthcare, Professional Services — plus per Discovery doc: construction, automotive, restaurants/chains, distribution, food & beverage
- **Decision-makers:** CFO (primary), VP/Director of Finance, Director of Administración y Finanzas, Treasurer, Controller, Head of Accounting, Tax Manager. Secondary: Travel Manager (Mendel Viajes only), Operations Director, Logistics/Fleet Manager, Procurement, CEO/GM (for mid-market only).
- **Excluded:** <100 employees, US/EU-only with no LatAm subsidiary, current Mendel customers, banks, government, competitors (full list in [knowledge/dnc-blocklist.md](knowledge/dnc-blocklist.md))

## Top 5 Verticals (priority order)

1. **Retail & CPG (Mexico)** — OXXO/FEMSA, Walmart logos. Distributed stores, supplier ecosystem, CFDI volume.
2. **Logistics & Transportation** — Viva Aerobus logo. Fleet card controls, fuel + repair CFDI, driver per-diems.
3. **Manufacturing & Industrial** — Multi-plant, ERP-heavy (SAP S/4HANA), nearshoring tailwind.
4. **Pharmaceutical & Healthcare** — HCP entertainment compliance angle, sales rep cards, transparency reporting.
5. **Professional Services (Consulting/Audit/Legal)** — KPMG logo. Billable expense capture, partner travel, multi-country engagements.

## Three Specific Differentiators

1. **One platform across six modules** — Cards + Expenses + Reimbursements + Invoice Payments + Travel + ERP, plus AI. SAP Concur+AMEX is fragmented. Clara stops at SMB. Edenred is prepaid.
2. **Real-time policy engine BEFORE the transaction** — rules by employee/role/BU/merchant/amount/category/time/country/channel; competitors detect post-hoc.
3. **CFDI invoice recovery for Mexican tax law** — automated retrieval, SAT validation, +30% deductibility lift. No global competitor matches.

## Quantified Proof Points (Mendel one-pager metrics)

- 150+ admin hours saved per month
- +20% reduction in non-deductible expenses
- 30+ hours of invoice reconciliation saved
- +US$20K saved in admin expenses
- +30% deductibility lift (CFDI recovery)
- 100% of expenses audited in real time
- 6+ hours productivity per employee per month
- Same-day month-end close (vs. prior 5+ days)

## Competitors (and Mendel's positioning)

- **SAP Concur + AMEX:** one platform vs. fragmented stack; LatAm-native vs. global tools that miss CFDI / multi-entity LatAm complexity.
- **Clara:** enterprise tier (deeper controls, ERP, travel, multi-country) vs. Clara's SMB / mid-market focus.
- **Edenred:** credit-based + full spend management vs. prepaid HR-benefits-only.

## Common Objections + Responses

1. *"We already use SAP Concur / AMEX / our bank."*
   → Mendel doesn't replace just a card or expense tool; it connects spend, policy, cards, reimbursements, invoices, travel, and ERP reconciliation in one platform with LatAm capabilities those tools lack.
2. *"Implementation will be complex."*
   → Mendel is built for enterprise complexity — ERP integrations, multi-country operations, large customers across MX/AR/CL. Goal: reduce complexity, not add.
3. *"Our current process works well enough."*
   → Hidden costs: manual hours, slow close, lost CFDIs, no real-time control, employee friction, leakage. Mendel quantifies these.

## Status Quo to Displace

- Employees paying out-of-pocket and waiting for reimbursement
- Corporate cards reserved for C-levels only (most employees outside system)
- SAP Concur + Excel + email + AMEX statements

## Outbound Stack

- **Email:** EmailBison + Zapmail (new infrastructure being built) + Scaledmail + Winnr
- **LinkedIn:** HeyReach (to be set up after database completes)
- **Sourcing waterfall:** BlitzAPI → Debounce → FindyMail → LeadMagic → BounceBan
- **Copy:** Gemini Flash per-lead personalization (~$2-3 / 400 leads)
- **Database/orchestration:** Clay (Master company + contact table, dedupe by domain, multi-source TAG)
- **CRM:** HubSpot (Mendel-side; Clay → HubSpot via Make/Zap for positive replies only)
- **Prior outbound to phase out:** agency black-box + freelancer SmartLead

## Copy Constraints (Hard Rules)

- 50–80 words per email
- No em dashes
- No exclamation marks
- No spam words (free, guarantee, etc.)
- Subject lines: max 3 words, lowercase except company / person names
- Email 1 = Lead Magnet (a benchmark PDF or 30-day spend leakage assessment)
- Email 2 = Service Offer (Mendel demo)
- Two independent threads
- No signature in body — `{SENDER_EMAIL_SIGNATURE}` handles it
- No bracket placeholders, no empty variables
- No currency in copy ($, €, dollar, peso, price, cost, fee)
- Spanish-language version mandatory for Mexico/Argentina/Chile; English version only for LatAm-HQ companies with US executives

## Lead Magnets / Content Assets

- Mendel vs Concur benchmark PDF
- Mendel vs Edenred one-pager
- Mendel vs T&E one-pager
- Invoice Recovery one-pager (+30% deductibility)
- Mendel Viajes pitch deck
- Mendel Expenses + Viajes 2026 full deck
- 30-day Spend Leakage Audit (proposed irresistible offer)

## Q2-2026 Goal

100+ qualified sales meetings per quarter with target ICPs. Alan restated 2026-05-08: "100 extra qualified leads per Q".

## Open Items (Onboarding Action Items, Apr 28 — superseded by table above)

Original onboarding action items from the Apr 28 call have largely converged with the live action item table above. Detailed historical context preserved in [call-summaries/2026-04-28-onboarding-mendel-kinetyca.md](call-summaries/2026-04-28-onboarding-mendel-kinetyca.md).

## Status

- Onboarding completed Apr 28, 2026
- GTM playbook generated May 4, 2026
- Strategy call completed May 5, 2026
- New email infrastructure being built on Zapmail + EmailBison + Scaledmail + Winnr
- Database build at 80% complete (ClickUp), due 2026-05-13
- Launch target: ~2026-05-26
- Drive folder: https://drive.google.com/drive/folders/1vesXSIB0EWuMufGPE3L0VZx_GnZaP9l_
- Miro GTM board: https://miro.com/app/board/uXjVHbaxxPY=/
- ClickUp list: https://app.clickup.com/901113677831
- Slack channel: #mendel-project (C0B0SG4QXHT)

## Related Files

- [`call-summaries/2026-04-28-onboarding-mendel-kinetyca.md`](call-summaries/2026-04-28-onboarding-mendel-kinetyca.md)
- [`call-summaries/2026-05-05-strategy-mendel-kinetyca.md`](call-summaries/2026-05-05-strategy-mendel-kinetyca.md)
- [`campaigns/outbound-campaigns.md`](campaigns/outbound-campaigns.md) — operational source of truth
- [`campaigns/inherited-campaign-baseline.md`](campaigns/inherited-campaign-baseline.md) — agency campaign analysis
- [`knowledge/dnc-blocklist.md`](knowledge/dnc-blocklist.md) — full blocklist + regex
- `Mendel_GTM_Playbook_May2026.pdf` — full playbook
- `generate_gtm_playbook.py` — reportlab generator
- `README.md` — public repo overview
- [Discovery Questions Mendel - Kinetyca](https://docs.google.com/document/d/1BZQc3QKpGTHXDEJIQxvPuEmRZm_Hmbm2d226ZY92e3M/edit) — Alan's UVP + ICP master doc (sent 2026-05-12)
- [Mendel Top-Performing Campaign Analysis](https://docs.google.com/document/d/1oG1o2MfrIgYIkryB3WLeZjtfmspagVwFr0zZQueBEzY/edit) — agency baseline analysis (Affan, 2026-05-05)
