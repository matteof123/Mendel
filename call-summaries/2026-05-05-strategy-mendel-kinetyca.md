# Strategy / Mendel - Kinetyca
**Date:** 2026-05-05
**Attendees:** Alan Karpovsky (Mendel), Matteo Fois (Kinetyca), David (Kinetyca)
**Duration:** 62 min
**Source:** Fireflies (id: 01KQWMN1BF23X7082PK3FJVDRQ)
**Recording:** [fireflies link](https://app.fireflies.ai/view/Strategy-Mendel-Kinetyca::01KQWMN1BF23X7082PK3FJVDRQ)

## Summary
Strategy presentation walking Alan through the full Kinetyca workflow: a unified Clay-based "brain" merging multiple data sources (BlitzAPI Mexico companies, Mendel's legacy SmartLead lead history, Discolike lookalike scraping, eventually Apollo) deduped by domain, enriched via the email waterfall, then split into segmented email + LinkedIn campaigns with A/B testing. Outreach is supplemented by evergreen re-engagement of past contacts and event/conference attendee scraping. Reply qualification uses sentiment analysis to route positives back to HubSpot for sales follow-up. Launch target: ~3 weeks from this call, around 2026-05-26.

## Key Discussion Points
- **Database build philosophy:** company-level first (not contact-level). Out of company list, find contacts via Claygent AI — that's the differentiator. Apollo deferred to phase 2.
- **Data sources merged into Master Sheet in Clay:**
  1. BlitzAPI — Mexico companies (~9,000)
  2. Mendel SmartLead legacy — ~78,000 leads, deduped to company-level ~30k
  3. Discolike — lookalike scraping based on Mendel's current customer logos
  4. Apollo (phase 2)
- **Dedupe key:** company domain (extract "acme" from "acme.com"), not company name (varies across sources). Source TAG preserved in destination row.
- **Outreach automation flow:** Clay → Smartlead/EmailBison (paused) → reply received → sentiment analysis → if positive → push to HubSpot for sales rep follow-up.
- **Evergreen + conference scraping:** automated re-engagement of past contacts and scraping of event/sponsor lists feeds new leads continuously.
- **Email infrastructure rationale:** new isolated setup on Zapmail allows clean warmup and quick issue isolation if one sender or domain has deliverability problems. Doesn't poison legacy SmartLead.

## Campaign Feedback
- Alan reviewed the inherited campaign baseline (Affan's analysis doc). Acknowledged Argentina Finance Report V2 (2.82% reply rate) is the strongest pattern. Mexico Finance Report V2 has the most absolute positives (74) despite lower reply rate.
- Alan confirmed messaging strategy should emphasize: real-time spend control + CFDI invoice recovery + ERP integration. Less emphasis on Mendel Viajes (travel) — secondary product.
- Spanish-language sequences for Mexico/AR/CL are mandatory. English only for LatAm-HQ with US executives.

## ICP / Positioning Insights
- Alan re-confirmed CFO + Controller + Finance Director + Director de Administración y Finanzas as primary titles. Tax Manager included for the CFDI angle.
- Mercado Libre is Mendel's marquee customer — all their regional domains (Argentina, Brazil "mercadolivre", Mexico) must be DNC'd to prevent embarrassing outreach.
- Industries confirmed: logistics, transportation, manufacturing, retail/CPG, construction, automotive, restaurants/chains, healthcare/pharma, distribution. Not tech startups.

## Decisions Made
- Build the database in Kinetyca's Clay instance (cheaper, shared across clients). Mendel can migrate to their own Clay later if desired. Free for Mendel to use ours.
- Clay is the brain. Positive replies flow from Clay → HubSpot. Evergreen feeds itself.
- Launch ~3 weeks from May 5 (target 2026-05-26).
- Add sentiment-analysis workflow for automated reply qualification.

## Action Items

| Person | Task | Reference |
|---|---|---|
| Alan Karpovsky | Export DNC lists + customers + domains from HubSpot for dedupe | Fireflies 55:40, 58:48 |
| Alan Karpovsky | Review Spanish sequence copy when shared (must match Mendel features) | Fireflies 56:22 |
| Matteo Fois | Share campaign smartly analysis doc with Alan for transparency | Fireflies 54:02 |
| Matteo Fois | Send new sequences + database samples to Mendel for review | Fireflies 56:31 |
| Matteo Fois | Request HubSpot access during database build for data integration | Fireflies 57:58 |
| Matteo Fois | Provide Clay template access + coordinate eventual migration to Mendel's Clay | Fireflies 58:16 |
| Matteo Fois | Build automated reply handling + sentiment analysis → HubSpot funnel | Fireflies 48:37 |
| Matteo Fois | Coordinate warmup + launch ~3 weeks (target 2026-05-26) | Fireflies 52:59 |
