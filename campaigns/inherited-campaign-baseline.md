# Inherited Campaign Baseline — Mendel (agency + SmartLead freelancer)

_Compiled 2026-05-12. Source: Affan Shaikh's analysis doc [Mendel Top-Performing Campaign Analysis](https://docs.google.com/document/d/1oG1o2MfrIgYIkryB3WLeZjtfmspagVwFr0zZQueBEzY/edit), built 2026-05-05 from Mendel's legacy SmartLead instance._

This is the pre-Kinetyca baseline — what the black-box agency and SmartLead freelancer were running before Kinetyca took over. Captured here as the reference our new infrastructure must beat. None of these campaigns will continue once Kinetyca's Zapmail-based infrastructure goes live (~2026-05-26).

## Campaign-by-campaign breakdown

### 1. Finance Report V2 — Argentina (best performer)

| Metric | Value | Rate |
|---|---:|---|
| Total Leads | 1,706 | — |
| Emails Sent | 7,451 | — |
| Unique Leads Contacted | 1,668 | 97.8% of total |
| Total Replies | 210 | **2.82%** reply rate (of sent) |
| Positive Replies | 10 | 0.60% of unique leads |
| Bounces | 116 | 1.56% bounce rate |
| Blocked Leads | 233 | 13.6% of total |
| Completed Leads | 1,472 | 86.3% of total |

**Verdict:** Strongest reply rate in the entire baseline (2-4x better than other campaigns). The structural pattern (operational mid-market Argentina with real finance teams) is the one to replicate in Mexico.

**Targeting:**
- Industries: Manufacturing, energy, construction, logistics, retail, media, healthcare
- Job titles: Analysts, controllers, finance managers, tax specialists, accountants
- Geography: Argentina

---

### 2. Finance Report V2 — Mexico (highest absolute positives)

| Metric | Value | Rate |
|---|---:|---|
| Total Leads | 5,082 | — |
| Emails Sent | 27,486 | — |
| Unique Leads Reached | 7,099 | — |
| Replies | 382 | 1.39% reply rate |
| Positive Replies | 74 | **1.04%** of unique leads |
| Bounces | 1,466 | **5.33% bounce rate (over our 3% safety threshold)** |
| Interested Leads | 74 | — |
| Completed | 3,430 | 67% of total leads |
| Blocked | 1,646 | 32% of total leads |

**Verdict:** Highest absolute positive count (74) but bounce rate 5.33% is unsafe. The Mexico/CDMX data on the legacy SmartLead instance is poor — Kinetyca rebuild must run mandatory waterfall (BlitzAPI → Debounce → FindyMail → LeadMagic → BounceBan) before any send.

**Targeting:**
- Industries: Mostly manufacturing + automotive
- Job titles: Finance Directors, Finance Managers, Controllers, "Contralors", fewer junior analysts
- Geography: Mexico City, Guadalajara, Monterrey, Guanajuato

---

### 3. A30: Industry Campaign — Blended — All — STS (Argentina)

| Metric | Value | Rate |
|---|---:|---|
| Total Leads | 5,258 | — |
| Emails Sent | 30,157 | — |
| Replies | 184 | 0.61% reply rate |
| Positive Replies | 47 | **25.5% quality** (positive ÷ replies) |
| Bounces | 215 | 0.71% bounce rate |
| Sender Bounces | 120 | deliverability concern |

**Verdict:** Lower reply rate but excellent positive-quality conversion (25.5% of replies are qualified). Suggests the hook + subject is doing the filtering work — fewer replies but higher intent.

**Targeting:**
- Geography: Argentina (Buenos Aires + province)
- Industry mix: agriculture, oil & gas, manufacturing, logistics, construction
- Job titles: Admin & Ops teams, HR teams, Finance teams, Procurement, Accountants, CEOs / Founders

---

### 4. A30: Industry Campaign — Blended — All — Risky (Argentina)

| Metric | Value | Rate |
|---|---:|---|
| Total Leads | 3,299 | — |
| Emails Sent | 18,249 | — |
| Unique Leads Reached | 2,872 | 87% of leads |
| Replies | 65 | **0.36% reply rate (worst)** |
| Positive Replies | 13 | 0.45% of unique leads |
| Bounces | 463 | 2.53% bounce rate |
| Sender Bounces | 178 | — |
| OOO Replies | 199 | — |

**Verdict:** Worst performer. Targeting is too scattered (electricity transmission + energy + power generation + manufacturing + packaging + plastics + medical devices + food/beverage). **Rule for Kinetyca rebuild:** one industry vertical per campaign, not five.

**Targeting:**
- Geography: Argentina
- Industry: electricity transmission, energy, power generation, manufacturing, packaging, plastics, medical devices, food/beverage
- Job titles: Admin & Ops, HR, Procurement, Logistics, Accountants, CEOs & Founders

---

### 5. Finance Team Waterfall Personalization (Mexico)

Performance metrics not extracted in source doc. Two best-performing sequences referenced: one with 27 replies, one with 28 replies.

**Targeting:**
- Geography: Mexico
- Industry: automotive, energy, pharma, food & beverage, mining, manufacturing, retail, financial services / tech
- Job titles: Controllers, Finance Managers

---

### 6. CFOs Batch 2 (Mexico)

Performance metrics not extracted. Two best-performing sequences referenced: 18 replies, 17 replies.

**Targeting:**
- Geography: Mexico
- Industry: logistics, transport, retail/consumer, technology, fintech, financial services, manufacturing, energy/infrastructure, automotive, pharmaceuticals
- Job titles: Treasury + CFO-level (Finance Director, Head of Finance, Corporate Treasury)

---

### 7. Sales Leaders (Mexico)

Performance metrics not extracted. Two best-performing sequences: 15 replies, 20 replies.

**Targeting:**
- Geography: Mexico
- Industry: Tech, IT, Retail, Consumer, Financial Services, Automotive, Logistics + Transport
- Job titles: Commercial Director, National Sales Director, VP of Marketing & Sales, LATAM Field Sales Director, Modern Trade Sales Manager, Commercial Planning Manager, Marketing & BD Director, Senior Cloud Sales, Senior Director of Global Account Mgmt, Sales Supervisor, Operations & BD Director, Supply Chain Director, Business Strategy & Customer Retention Manager, Sales Control Specialist, Sales Director

**Note:** This is the bottom-up persona path (VP Sales pulling Mendel for the sales force). Alan called it a "long-shot" — finance is still the decider. Keep as a secondary segment but don't lead with it.

---

## Patterns observed across all 7 campaigns

### What works
- **Argentina Finance personas (analysts, controllers, finance managers)** produce the highest reply rate when paired with operational industries (manufacturing, energy, logistics).
- **Mexico Finance Directors / Controllers in manufacturing + automotive** produce the highest absolute positive count.
- **Tighter industry focus** (STS Argentina with 5-industry mix) outperforms wider blends (Risky Argentina with 8+ industries) on positive-quality conversion.

### What doesn't work
- **Mexico data quality is bad** on the legacy SmartLead instance — 5.33% bounce on Finance Report V2 confirms the company-domain + email-verification pass was missing or weak. Kinetyca must run full waterfall on every Mexico lead.
- **Geography mix is inverted:** 4 of 7 campaigns are Argentina-led, but Mendel's strategy is 90% Mexico growth focus. Rebalance.
- **Sender-side bounces (120 STS, 178 Risky)** suggest warmup wasn't healthy on the agency's senders. Zapmail rebuild + structured warmup fixes this.
- **Broad industry mixes** dilute messaging — Kinetyca rule: one vertical per campaign.

### What to carry forward into Kinetyca campaigns
1. **Finance Director / Controller in manufacturing + automotive (Mexico)** — proven positive segment, just need better data + tighter copy.
2. **Argentina Finance Report V2 hook structure** — whatever angle produced 2.82% reply, replicate the framing in Mexico Spanish.
3. **CFDI invoice recovery angle** — Mexico-specific, no global competitor matches. Lead with this in Mexico copy.
4. **Real-time spend control "BEFORE the transaction"** — universal differentiator, works in both Spanish + English.
5. **Mendel Viajes (corporate travel)** — secondary. Don't lead with it. Use as the Email 2 service offer for travel-heavy verticals (logistics, professional services with billable travel).

## Reference

Source doc: [Mendel Top-Performing Campaign Analysis](https://docs.google.com/document/d/1oG1o2MfrIgYIkryB3WLeZjtfmspagVwFr0zZQueBEzY/edit) (Affan Shaikh, 2026-05-05). Drive folder: [Mendel client folder](https://drive.google.com/drive/folders/1vesXSIB0EWuMufGPE3L0VZx_GnZaP9l_).
