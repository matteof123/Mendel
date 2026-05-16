# Mendel — Email 1 Library

_Last updated: 2026-05-16_
_Status: pre-launch — awaiting campaign launch (~2026-05-26 per strategy call)_
_Language: Spanish (Mexico priority, "tú" form). Professional Services version targets LatAm-wide._

## Overview

Three independent variants of Email 1 for Mendel's cold outbound, each adapted across six priority industries. Same fundamental message (problem → solution → social proof → ask) delivered through three distinct voices. Pick any two for parallel A/B campaign tests, or use C as a follow-up touch.

Principles applied across all three:
- **Peer-framed openers.** Never accuse the prospect's company of having a problem. State the pain as something observed across peers in the same industry / geography.
- **Soft value-probing CTAs.** Ask if the topic is relevant or worth reviewing — never push for "15 minutes" cold.
- **Customer logos as social proof.** Only confirmed Mendel customers named (see verification table below).
- **No accusation in subject lines.** Topic-led, personalized via `{{firstName}}` / `{{companyName}}`, never spammy.
- **Hard rules:** no em dashes, no exclamation marks, no currency words ($ / peso / cost / fee), no signature in body, no bracket placeholders.

---

## Variable schema

| Variable | Example | Source |
|---|---|---|
| `{{firstName}}` | Carlos | Lead first name from enrichment |
| `{{companyName}}` | Soriana | Lead company from enrichment |
| `{{titlePlural}}` | CFOs | Persona plural — set per campaign |
| `{{vertical}}` | tech | Industry word — set per campaign |
| `{{country}}` | México | Geography — set per campaign |

Signature (sender name + tagline) handled by EmailBison `{SENDER_EMAIL_SIGNATURE}` — never include in body.

## Customer name index

| Customer | Status | Where used |
|---|---|---|
| Mercado Libre | Confirmed (Slack 2026-05-06, sender tagline) | Tech |
| KPMG | Confirmed (sender tagline) | Professional Services |
| AB InBev | Confirmed (sender tagline) | Tech, Manufacturing |
| Walmart | Verify with Alan against `CLIENTES ACTUALES MENDEL.xlsx` | Retail & CPG |
| OXXO / FEMSA | Verify with Alan | Retail & CPG |
| Viva Aerobus | Verify with Alan | Logistics |
| Pharma customer | None confirmed — use anonymous industry framing | Pharma |

## When to use which variant

| Variant | Voice | Word count | Best for |
|---|---|---:|---|
| **A** — Peer-framed (Alejandro) | Conversational, soft, peer-CFO insight | ~95-100 | Warm first-touch, finance leaders open to peer signals |
| **B** — Architectural / design-limit | Direct, founder-confident, contrasts incumbent stack | ~95-100 | CFOs who pattern-match on architecture, tech-literate buyers |
| **C** — Ultra-short peer-pattern | Compressed, mobile-first, value-probing | ~55-70 | Time-poor buyers, follow-up touches, mobile-dominant readers |

---

# VARIANT A — Peer-framed (Alejandro voice)

## Structure

| Section | Role | Variable per industry? |
|---|---|:---:|
| 1. Greeting | `Hola {{firstName}},` | No |
| 2. Peer-framed problem (with stated pain) | `Platicando con {{titlePlural}} de [industria] en [geo], casi todos cuentan lo mismo: [pain].` | Yes |
| 3. Solution (verbs + outcome) | `Mendel resuelve eso [doing X, Y, Z]. [Outcome sentence].` | Yes |
| 4. Objection defusion | `[Acknowledgment of likely objection]. [Specific counter].` | Yes (pick obj type) |
| 5. Social proof | `Es la misma arquitectura que usan [Customer] hoy.` | Yes |
| 6. CTA | `¿Vale revisarlo aplicado a {{companyName}}?` | No |

## A.1 Tech / Software

**Subject options:**
- `{{firstName}}, automatización IA en {{companyName}}`
- `{{firstName}}, finanzas con IA`
- `Para {{firstName}}: cierre mensual`

**Body:**
```
Hola {{firstName}},

Platicando con {{titlePlural}} en tech en México, casi todos cuentan lo mismo: el área de tech crece más rápido que finanzas, y el equipo termina validando tickets en vez de cerrar el mes.

Mendel resuelve eso poniendo un agente de IA que audita cada transacción contra política antes del cargo. Lo que llega a finanzas son reportes ya listos, no tickets sueltos, y el ERP queda reconciliado en tiempo real.

Si ya operan con Concur + AMEX no es para reemplazarlos: Mendel los integra junto a CFDI y ERP en una sola plataforma, con las capacidades LatAm que esos tools no traen.

Es la misma arquitectura que usan Mercado Libre y AB InBev hoy.

¿Vale revisarlo aplicado a {{companyName}}?
```

## A.2 Retail & CPG

**Subject options:**
- `{{firstName}}, control multi-tienda en {{companyName}}`
- `{{firstName}}, CFDIs y ERP`
- `Para {{firstName}}: cierre por tienda`

**Body:**
```
Hey {{firstName}},

Hablando con {{titlePlural}} de retail en México, casi todos cuentan lo mismo: con cientos de tiendas y miles de CFDIs al mes, el cierre del banco llega antes que el cierre interno.

Mendel resuelve eso aplicando políticas por tienda en el momento del cargo, recuperando los CFDIs automáticamente y mandándolos al ERP ya validados. El equipo cierra el mes el mismo día, sin hojas paralelas.

Si ya operan con Concur o la tarjeta del banco, no es para reemplazarlos: Mendel los integra junto a CFDI y ERP en una sola plataforma, con las capacidades LatAm que los globales no traen.

Es la misma arquitectura que usan Walmart y OXXO hoy.

¿Tiene sentido verlo aplicado a {{companyName}}?
```

## A.3 Logistics & Transportation

**Subject options:**
- `{{firstName}}, flotilla en {{companyName}}`
- `{{firstName}}, conductores y CFDIs`
- `Para {{firstName}}: gastos de campo`

**Body:**
```
Buenas {{firstName}},

Conversando con {{titlePlural}} en logística en México, la mayoría cuenta lo mismo: tarjetas de flotilla, casetas, combustible y viáticos repartidos entre conductores, sin visibilidad hasta el cierre del mes.

Mendel resuelve eso con reglas que se aplican en el momento del cargo: por conductor, por proveedor y por horario. Combustible y per-diems quedan auditados antes de la conciliación, no después.

Si ya usan tarjetas de flotilla del banco, no es para reemplazarlas: Mendel las integra junto a viáticos, CFDIs y ERP, con políticas que las tarjetas tradicionales no aplican.

Es la misma arquitectura que usa Viva Aerobus hoy.

¿Hace sentido echarle un ojo para {{companyName}}?
```

## A.4 Manufacturing & Industrial

**Subject options:**
- `{{firstName}}, control multi-planta en {{companyName}}`
- `{{firstName}}, SAP y CFDIs`
- `Para {{firstName}}: cierre entre plantas`

**Body:**
```
Hola {{firstName}},

Platicando con {{titlePlural}} de manufactura en México, todos describen el mismo patrón: spend operativo disperso entre plantas, reconciliación manual contra SAP, y deductibilidad que se pierde por CFDIs que nunca llegan.

Mendel resuelve eso con control de políticas multi-planta en tiempo real, recuperación automática de CFDIs entre plantas y reconciliación directa contra SAP S/4HANA. El cierre deja de depender de ajustes manuales por planta.

Sé que integrar con SAP suena pesado. Por diseño Mendel se conecta nativo a S/4HANA, no se le monta encima.

Es la misma arquitectura que usa AB InBev hoy.

¿Vale revisarlo aplicado a {{companyName}}?
```

## A.5 Pharmaceutical & Healthcare

⚠️ No confirmed pharma customer logo — verify with Alan before launch.

**Subject options:**
- `{{firstName}}, trazabilidad de HCPs en {{companyName}}`
- `{{firstName}}, reporte de transparencia`
- `Para {{firstName}}: fuerza de ventas`

**Body:**
```
Hey {{firstName}},

Hablando con {{titlePlural}} de farma en México, casi todos cuentan el mismo dolor: las tarjetas de la fuerza de ventas, los viáticos con HCPs y los reembolsos necesitan trazabilidad completa, y armar el reporte de transparencia se vuelve un proyecto mensual.

Mendel resuelve eso aplicando política por representante en cada cargo y dejando la auditoría corriendo en tiempo real. El reporte de transparencia sale listo para exportar, sin armarlo a mano.

Entiendo que sumar un sistema con datos sensibles suena complejo. Mendel se diseñó para escenarios regulados: controles por rol, ERP nativo, audit-ready desde día uno.

Operaciones farma con fuerza distribuida operan sobre esa arquitectura hoy.

¿Tiene sentido verlo aplicado a {{companyName}}?
```

## A.6 Professional Services (Consulting / Audit / Legal)

**Subject options:**
- `{{firstName}}, gasto multi-país en {{companyName}}`
- `{{firstName}}, billable y CFDI`
- `Para {{firstName}}: viaje de partners`

**Body:**
```
Hola {{firstName}},

Conversando con {{titlePlural}} de servicios profesionales en LatAm, la mayoría cuenta el mismo dolor: viaje de partners, gastos billables por cliente y operación multi-país, gestionado entre tarjetas, hojas y reembolsos manuales.

Mendel resuelve eso capturando cada gasto billable por engagement desde el momento del cargo, con CFDI integrado y reconciliación directa al ERP. Los partners aprueban desde el móvil y los reembolsos manuales desaparecen.

Sé que el proceso actual funciona. La pregunta es cuántas horas y cuánta deductibilidad se pierden cada mes que ya no vuelven.

Es la misma arquitectura que usa KPMG hoy.

¿Vale revisarlo aplicado a {{companyName}}?
```

---

# VARIANT B — Architectural / design-limit-led

## Structure

| Section | Role | Variable per industry? |
|---|---|:---:|
| 1. Greeting | `Hola {{firstName}},` | No |
| 2. Architectural fact about incumbent stack | `[Incumbent stack] se diseñó para [old purpose]. Funciona si [old need].` | Yes |
| 3. Peer-framed shift + Mendel approach | `Cuando hablo con {{titlePlural}} en [industry] en {{country}}, muchos ya están [moving the architecture]: [3 capabilities].` | Yes |
| 4. Social proof woven into outcome | `Eso es lo que corre [Customer] hoy, y es por eso que [outcome].` | Yes |
| 5. CTA | `¿Tendría sentido para {{companyName}}?` | No |

Objection is preempted by the architectural framing (no separate paragraph needed). Direct, founder-confident voice. ~95 words.

## B.1 Tech / Software

**Subject options:**
- `{{firstName}}, Concur + AMEX en {{companyName}}`
- `{{firstName}}, control real-time`
- `Para {{firstName}}: stack de finanzas`

**Body:**
```
Hola {{firstName}},

Concur + AMEX se diseñó para reportar gastos después de que pasan. Funciona bien si lo que necesitas es visibilidad post-cierre.

Cuando hablo con {{titlePlural}} en tech en México, muchos ya están moviendo el control antes de la transacción: un agente de IA evalúa cada cargo contra política, recupera el CFDI y reconcilia con el ERP en tiempo real.

Eso es lo que corre Mercado Libre hoy, y es por eso que finanzas pasa de validar tickets a aprobar reportes ya listos.

¿Tendría sentido para {{companyName}}?
```

## B.2 Retail & CPG

**Subject options:**
- `{{firstName}}, Concur + tarjetas`
- `{{firstName}}, control multi-tienda`
- `Para {{firstName}}: cierre por tienda`

**Body:**
```
Hola {{firstName}},

Concur + la tarjeta del banco se diseñó para reportar después del estado de cuenta. Funciona si solo necesitas el report mensual.

Cuando hablo con {{titlePlural}} de retail en México, muchos ya están controlando antes de la transacción: política por tienda en el momento del cargo, recuperación automática de CFDIs y reconciliación al ERP en tiempo real.

Eso es lo que corren Walmart y OXXO hoy, y es por eso que el mes cierra el mismo día, sin hojas paralelas.

¿Vale la pena revisarlo para {{companyName}}?
```

## B.3 Logistics & Transportation

**Subject options:**
- `{{firstName}}, tarjetas de flotilla`
- `{{firstName}}, control por conductor`
- `Para {{firstName}}: combustible y CFDIs`

**Body:**
```
Hola {{firstName}},

Las tarjetas de flotilla del banco se diseñaron para pagar combustible. Visibilidad por conductor y políticas por proveedor no estaban en el alcance original.

Cuando hablo con {{titlePlural}} en logística en México, muchos ya están moviendo el control al momento del cargo: reglas por conductor, por proveedor y por horario, con CFDIs y per-diems auditados antes del cierre.

Eso es lo que corre Viva Aerobus hoy, y es por eso que la conciliación pasa de manual a automática.

¿Te resuena para {{companyName}}?
```

## B.4 Manufacturing & Industrial

**Subject options:**
- `{{firstName}}, SAP y CFDIs`
- `{{firstName}}, tres sistemas, un cierre`
- `Para {{firstName}}: spend multi-planta`

**Body:**
```
Hola {{firstName}},

El stack típico en manufactura, Concur, tarjetas del banco y SAP, se construyó como tres sistemas separados. Cada integración entre ellos es un punto de falla.

Cuando hablo con {{titlePlural}} de manufactura en México, muchos ya están consolidando: control de políticas multi-planta en tiempo real, recuperación automática de CFDIs entre plantas, y reconciliación nativa contra SAP S/4HANA.

Eso es lo que corre AB InBev hoy, y es por eso que el cierre deja de depender de ajustes manuales por planta.

¿Tendría sentido para {{companyName}}?
```

## B.5 Pharmaceutical & Healthcare

⚠️ No confirmed pharma customer logo — verify with Alan.

**Subject options:**
- `{{firstName}}, transparencia y HCPs`
- `{{firstName}}, trazabilidad farma`
- `Para {{firstName}}: auditoría en tiempo real`

**Body:**
```
Hola {{firstName}},

Las herramientas tradicionales de expense management no se diseñaron pensando en compliance farma. Trazabilidad por HCP y reporte de transparencia terminan siendo proyectos manuales mensuales.

Cuando hablo con {{titlePlural}} de farma en México, muchos ya están moviendo esa trazabilidad al momento del cargo: política por representante, auditoría en tiempo real, reporte de transparencia listo para exportar.

Eso es lo que corren operaciones farma con fuerza distribuida hoy, y es por eso que el reporte deja de armarse a mano.

¿Te interesa ver cómo aplicaría a {{companyName}}?
```

## B.6 Professional Services (Consulting / Audit / Legal)

**Subject options:**
- `{{firstName}}, gasto billable`
- `{{firstName}}, multi-país y CFDI`
- `Para {{firstName}}: engagement billable`

**Body:**
```
Hola {{firstName}},

Capturar gasto billable por engagement nunca fue para lo que se diseñó Concur. Tampoco soporta CFDI ni operación multi-país de forma nativa.

Cuando hablo con {{titlePlural}} de servicios profesionales en LatAm, muchos ya están consolidando: gasto billable capturado en el momento del cargo, multi-país, con CFDI integrado y reconciliación directa al ERP.

Eso es lo que corre KPMG hoy, y es por eso que los partners aprueban desde el móvil y los reembolsos manuales desaparecen.

¿Vale la pena para {{companyName}}?
```

---

# VARIANT C — Ultra-short peer-pattern

## Structure

| Section | Role | Variable per industry? |
|---|---|:---:|
| 1. Greeting | `Hola {{firstName}},` | No |
| 2. Peer-framed observation | `Cuando hablo con {{titlePlural}} de [industria] en [geo], casi todos describen lo mismo: [pain].` | Yes |
| 3. Solution (one sentence) | `Mendel [actions and capabilities].` | Yes |
| 4. Social proof (one sentence) | `Es lo que corre [Customer] hoy.` | Yes |
| 5. Soft CTA (value probe) | `¿Tendría sentido para {{companyName}}?` (rotate from CTA library) | No |

Total ~55-70 words. Mobile-scannable in 5-7 seconds.

## C.1 Tech / Software

**Subject options:**
- `{{firstName}}, IA en finanzas`
- `{{firstName}}, una idea para {{companyName}}`
- `Para {{firstName}}: control de spend`

**Body:**
```
Hola {{firstName}},

Cuando hablo con {{titlePlural}} en tech en México, casi todos describen el mismo patrón: tech escala más rápido que finanzas, y revisar gastos termina siendo apagar fuegos.

Mendel automatiza ese control con un agente de IA antes del cargo: política en tiempo real, CFDIs recuperados y ERP reconciliado.

Es lo que corre Mercado Libre hoy.

¿Tendría sentido para {{companyName}}?
```

## C.2 Retail & CPG

**Subject options:**
- `{{firstName}}, control por tienda`
- `{{firstName}}, una idea para {{companyName}}`
- `Para {{firstName}}: CFDIs en retail`

**Body:**
```
Hola {{firstName}},

Cuando hablo con {{titlePlural}} de retail en México, casi todos cuentan lo mismo: cientos de tiendas y miles de CFDIs por mes, con un cierre que llega después del estado de cuenta.

Mendel aplica política por tienda en cada cargo, recupera los CFDIs automáticamente y reconcilia con el ERP en tiempo real.

Es lo que corren Walmart y OXXO hoy.

¿Es algo que valga la pena revisar para {{companyName}}?
```

## C.3 Logistics & Transportation

**Subject options:**
- `{{firstName}}, gestión de flotilla`
- `{{firstName}}, una idea para {{companyName}}`
- `Para {{firstName}}: per-diems y CFDIs`

**Body:**
```
Hola {{firstName}},

Cuando hablo con {{titlePlural}} en logística en México, la mayoría describe el mismo dolor: flotilla, combustible, casetas y viáticos repartidos entre conductores, sin visibilidad hasta el cierre.

Mendel aplica reglas por conductor, proveedor y horario en el momento del cargo, con CFDIs integrados al ERP.

Es lo que corre Viva Aerobus hoy.

¿Te resuena para {{companyName}}?
```

## C.4 Manufacturing & Industrial

**Subject options:**
- `{{firstName}}, control multi-planta`
- `{{firstName}}, una idea para {{companyName}}`
- `Para {{firstName}}: SAP y CFDIs`

**Body:**
```
Hola {{firstName}},

Cuando hablo con {{titlePlural}} de manufactura en México, casi todos describen el mismo patrón: spend operativo disperso entre plantas, reconciliación manual contra SAP, y deductibilidad perdida por CFDIs que nunca llegan.

Mendel consolida políticas multi-planta, recupera CFDIs entre plantas y se conecta nativo a SAP S/4HANA.

Es lo que corre AB InBev hoy.

¿Tendría sentido para {{companyName}}?
```

## C.5 Pharmaceutical & Healthcare

⚠️ No confirmed pharma customer logo — verify with Alan.

**Subject options:**
- `{{firstName}}, trazabilidad farma`
- `{{firstName}}, una idea para {{companyName}}`
- `Para {{firstName}}: reporte de transparencia`

**Body:**
```
Hola {{firstName}},

Cuando hablo con {{titlePlural}} de farma en México, casi todos describen el mismo dolor: fuerza de ventas con HCPs, viáticos médicos y reembolsos que necesitan trazabilidad para reporte de transparencia.

Mendel aplica política por representante, audita en tiempo real y deja el reporte listo para exportar.

Es lo que corren operaciones farma con fuerza distribuida hoy.

¿Te interesa ver cómo aplicaría a {{companyName}}?
```

## C.6 Professional Services

**Subject options:**
- `{{firstName}}, gasto billable`
- `{{firstName}}, una idea para {{companyName}}`
- `Para {{firstName}}: multi-país y CFDI`

**Body:**
```
Hola {{firstName}},

Cuando hablo con {{titlePlural}} de servicios profesionales en LatAm, la mayoría cuenta lo mismo: viaje de partners, gastos billables por cliente y operación multi-país, gestionado entre tarjetas, hojas y reembolsos manuales.

Mendel captura cada gasto billable por engagement en el momento del cargo, multi-país, con CFDI y reconciliación al ERP.

Es lo que corre KPMG hoy.

¿Es algo que valga la pena para {{companyName}}?
```

---

# Libraries

## Objection defusion library (used in Variant A)

| # | Objection trigger | Defusion template |
|---|---|---|
| **1** | Existing stack (Concur, AMEX, bank cards, fleet cards) | `Si ya operan con [stack], Mendel no [los/las] reemplaza: integra [things] en un solo lugar, con capacidades LatAm que [esos tools / los globales] no traen.` |
| **2** | Implementation complexity (SAP, ERP, multi-country, compliance) | `Sé que [implementing X] suena pesado. Por diseño Mendel se conecta nativo a [SAP / ERP], no se le agrega encima; por eso operaciones [type] en LatAm ya corren sobre esto.` |
| **3** | Current process works well enough | `Sé que el proceso actual funciona. La pregunta es cuántas horas y cuánta deductibilidad se pierden cada mes que ya no vuelven.` |

| Industry | Default objection used |
|---|---|
| Tech | #1 |
| Retail | #1 |
| Logistics | #1 |
| Manufacturing | #2 |
| Pharma | #2 |
| Professional Services | #3 |

## CTA library (value-probing, rotate to taste)

All ask about relevance / value, not for time:
- `¿Tendría sentido para {{companyName}}?`
- `¿Es algo que valga la pena revisar para {{companyName}}?`
- `¿Te resuena para {{companyName}}?`
- `¿Te interesa ver cómo aplicaría a {{companyName}}?`
- `¿Vale la pena profundizar en esto?`
- `¿Quieres que te mande más info?`
- `¿Vale revisarlo aplicado a {{companyName}}?`
- `¿Tiene sentido verlo aplicado a {{companyName}}?`
- `¿Hace sentido echarle un ojo para {{companyName}}?`

## Subject line library (per industry × variant)

### Tech / Software
- `{{firstName}}, automatización IA en {{companyName}}`
- `{{firstName}}, IA en finanzas`
- `{{firstName}}, Concur + AMEX en {{companyName}}`
- `{{firstName}}, control real-time`
- `{{firstName}}, finanzas con IA`
- `{{firstName}}, una idea para {{companyName}}`
- `Para {{firstName}}: stack de finanzas`
- `Para {{firstName}}: cierre mensual`
- `Para {{firstName}}: control de spend`

### Retail & CPG
- `{{firstName}}, control multi-tienda en {{companyName}}`
- `{{firstName}}, CFDIs y ERP`
- `{{firstName}}, Concur + tarjetas`
- `{{firstName}}, control por tienda`
- `{{firstName}}, una idea para {{companyName}}`
- `Para {{firstName}}: cierre por tienda`
- `Para {{firstName}}: CFDIs en retail`

### Logistics & Transportation
- `{{firstName}}, flotilla en {{companyName}}`
- `{{firstName}}, conductores y CFDIs`
- `{{firstName}}, tarjetas de flotilla`
- `{{firstName}}, control por conductor`
- `{{firstName}}, gestión de flotilla`
- `{{firstName}}, una idea para {{companyName}}`
- `Para {{firstName}}: gastos de campo`
- `Para {{firstName}}: combustible y CFDIs`
- `Para {{firstName}}: per-diems y CFDIs`

### Manufacturing & Industrial
- `{{firstName}}, control multi-planta en {{companyName}}`
- `{{firstName}}, SAP y CFDIs`
- `{{firstName}}, tres sistemas, un cierre`
- `{{firstName}}, control multi-planta`
- `{{firstName}}, una idea para {{companyName}}`
- `Para {{firstName}}: cierre entre plantas`
- `Para {{firstName}}: spend multi-planta`
- `Para {{firstName}}: SAP y CFDIs`

### Pharmaceutical & Healthcare
- `{{firstName}}, trazabilidad de HCPs en {{companyName}}`
- `{{firstName}}, reporte de transparencia`
- `{{firstName}}, transparencia y HCPs`
- `{{firstName}}, trazabilidad farma`
- `{{firstName}}, una idea para {{companyName}}`
- `Para {{firstName}}: fuerza de ventas`
- `Para {{firstName}}: auditoría en tiempo real`
- `Para {{firstName}}: reporte de transparencia`

### Professional Services
- `{{firstName}}, gasto multi-país en {{companyName}}`
- `{{firstName}}, billable y CFDI`
- `{{firstName}}, gasto billable`
- `{{firstName}}, multi-país y CFDI`
- `{{firstName}}, una idea para {{companyName}}`
- `Para {{firstName}}: viaje de partners`
- `Para {{firstName}}: engagement billable`
- `Para {{firstName}}: multi-país y CFDI`

---

# Usage guidance

## A/B/C testing strategy

**Phase 1 (week 1 of launch):** Run **Variant A vs Variant B** head-to-head on the same Mexico CFO segment. Keep audience, sender, day, and time constant. Test for:
- Open rate (subject line + first preview line)
- Reply rate (overall engagement)
- Positive reply rate (qualified interest)

**Phase 2 (week 2-3):** Pick winner of A/B. Use **Variant C** as the Email 2 follow-up touch for non-openers, and use the winner's Email 2/3 sequence for non-replier follow-up.

**Phase 3 (week 3+):** Roll winner to all 6 industries, rotate subject lines within each industry to find the strongest topic angle per segment.

## Subject line rotation

Pick 2 subjects per industry per campaign. Run both, measure opens. Lock the winner before scaling. Never run more than 2 subjects simultaneously per segment — too many variables.

## Spintax (optional, post-A/B)

Once the winning variant is locked, light spintax can be applied to the static connector phrases to reduce same-text detection at scale. Spintax markers (`{option1|option2|option3}`) should only be applied to:
- Greetings: `{Hola|Hey|Buenas}`
- Connectors: `{Platicando|Hablando|Conversando}`, `{todos|casi todos|la mayoría}`
- Verb synonyms in social proof: `{operan|corren|funcionan}`, `{hoy|actualmente}`
- CTA stems: `{Vale|Tiene sentido|Hace sentido}`, `{revisarlo|verlo|echarle un ojo}`

Never spin: customer names, product names (Concur, AMEX, SAP, ERP, CFDI), industry-specific 3-beat capabilities, merge variables.

## Hard rules check (all variants comply)

- No em dashes
- No exclamation marks
- No currency words ($ / € / dollar / peso / cost / fee / price)
- No spam triggers (free, guaranteed, urgent, etc.)
- No signature in body (use `{SENDER_EMAIL_SIGNATURE}` system variable)
- No bracket placeholders in final copy
- No accusatory framing about the prospect's company
- One question per email (the CTA)

## Status notes

- **No live Kinetyca campaigns yet.** Launch target: ~2026-05-26 per strategy call with Alan (2026-05-05).
- **Database build status:** 80% complete in Clay (ClickUp `868jea2rf`). Blocklist implementation due 2026-05-13.
- **Customer logo verification pending.** Before launch, verify Walmart, OXXO, Viva Aerobus, McDonald's against `CLIENTES ACTUALES MENDEL.xlsx` (ClickUp `868jea2v0`).
- **Pharma logo gap.** No confirmed pharma customer; either request one from Alan or keep anonymous "operaciones farma con fuerza distribuida" framing.
- **Spanish for MX/AR/CL.** Professional Services version uses LatAm framing for multi-country firms with US-based execs (rare; mostly Spanish-language).

## Related files

- [`../CLAUDE.md`](../CLAUDE.md) — Mendel client brain
- [`outbound-campaigns.md`](outbound-campaigns.md) — operational source of truth
- [`inherited-campaign-baseline.md`](inherited-campaign-baseline.md) — agency campaign analysis (the baseline to beat)
- [`../knowledge/dnc-blocklist.md`](../knowledge/dnc-blocklist.md) — DNC + competitor + bank + gov blocklist
- [`../call-summaries/2026-04-28-onboarding-mendel-kinetyca.md`](../call-summaries/2026-04-28-onboarding-mendel-kinetyca.md)
- [`../call-summaries/2026-05-05-strategy-mendel-kinetyca.md`](../call-summaries/2026-05-05-strategy-mendel-kinetyca.md)
