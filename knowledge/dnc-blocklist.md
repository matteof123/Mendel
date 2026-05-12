# Mendel — DNC / Blocklist

_Last updated: 2026-05-12 | Source: Alan Karpovsky in #mendel-project on 2026-05-06_

Critical instruction from Mendel: **never contact** any company that falls into the categories below. Repeated in Slack multiple times — this is non-negotiable.

## Sources to combine

1. **SmartLead DNC list** — from legacy SmartLead instance (Alan to share)
2. **Agency DNC list** — from the black-box agency (Alan to share, still pending as of 2026-05-12)
3. **HubSpot active customers** — exported by Alan, file [`CLIENTES ACTUALES MENDEL.xlsx`](https://t9011374495.p.clickup-attachments.com/t9011374495/79d698a7-5eb1-4d48-874d-482b3082ebbc/CLIENTES%20ACTUALES%20MENDEL.xlsx) (attached to ClickUp 868jea2v0)
4. **Manual blocklists** — banks, government, competitors, Mercado Libre (below)

Match on **company domain** (extract root: "acme" from "acme.com"), not company name. Apply at company-level in Clay BEFORE contact-level enrichment.

## Mercado Libre (marquee customer — all regional domains)

Mercado Libre is Mendel's flagship customer. Embarrassing to contact anyone there.

- `mercadolibre.com.ar`, `mercadolibre.com.mx`, `mercadolibre.com.co`, `mercadolibre.com.cl`, `mercadolibre.com.pe`, `mercadolibre.com.uy`
- `mercadolivre.com.br` (Brazil — Portuguese "livre" spelling)
- Any other regional variant (`mercadolibre.com.*`, `mercadolivre.*`)

## Government

Block these regex patterns at the domain level:

- **Mexico:** `*.gob.mx`
- **Argentina:** `*.gob.ar`, `*.gov.ar`, `*.mil.ar` (military)
- **Chile:** `*.gob.cl`

## Banks (regex patterns provided by Alan)

```regex
\.(?:bna|galicia|macro|bbva|santander|bancoprovincia|bancopatagonia|hsbc|credicoop|supervielle|icbc)\.(?:com\.ar|ar)$|
\.(?:bancoestado|bancochile|bci|scotiabank|itau|falabella|ripley|consorcio|bice|security)\.(?:cl)$|
\.(?:bbva|banorte|santander|citibanamex|banamex|hsbc|scotiabank|azteca|inbursa|bajio|afirme|mifel)\.(?:mx|com\.mx)$
```

**Argentina banks:** BNA, Galicia, Macro, BBVA, Santander, Banco Provincia, Banco Patagonia, HSBC, Credicoop, Supervielle, ICBC

**Chile banks:** Banco Estado, Banco Chile, BCI, Scotiabank, Itaú, Falabella, Ripley, Consorcio, BICE, Security

**Mexico banks:** BBVA, Banorte, Santander, Citibanamex, Banamex, HSBC, Scotiabank, Azteca, Inbursa, Banco Bajío, Afirme, Mifel

## Competitors (direct + indirect)

Block all corporate domains for these companies (each may have multiple regional TLDs):

| Competitor | Notes |
|---|---|
| Clara | LatAm SMB/mid-market spend management — most direct competitor |
| Jeeves | Cross-border corporate cards |
| Xpendit | Expense management |
| Cardda | Corporate cards |
| Caju (caju.com.br) | Brazil — corporate benefits + spend |
| ContaSimples | Brazil |
| American Express (AMEX) | Card incumbent |
| SAP Concur | Expense incumbent |
| RindeGastos | Expense management |
| BUK | HR/benefits + spend |
| Argo | Spend management |
| Voll | Brazil |
| PayTrack | Brazil |
| OnFly | Brazil — travel |
| Brex | US — corporate cards |
| Ramp | US — spend management |
| Emburse | Expense management |
| Mesh | Spend management |
| Pleo | EU — corporate cards |

Apply substring + domain match (e.g. `clara.*`, `*clara.com`, `concur.*`).

## Operational rules

- Block at **company level** in Clay before contact-level enrichment. Saves enrichment cost.
- Re-apply block right before push to Smartlead/EmailBison as a final safety check.
- Add the same blocklist to the **SmartLead campaigns** that are still running (until Kinetyca-owned campaigns replace them).
- Mendel sends ongoing "please add to DNC" unsubscribe requests forwarded by Alan in Slack — add these to DNC immediately when received (Alan's 2026-05-07 19:59 message references the steady stream of these).

## Reference task

ClickUp: [Implement the blocklist (868jea2v0)](https://app.clickup.com/t/868jea2v0) — assigned Affan, due ~2026-05-13.
