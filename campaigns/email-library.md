# Mendel — Email Sequence Library

_Last updated: 2026-05-16_
_Status: pre-launch — awaiting campaign launch (~2026-05-26)_
_Language: Spanish (Mexico priority, "tú" form). Professional Services version uses LatAm framing._
_Designed for: machine consumption (AI-driven prompt generation, EmailBison upload)._

## Overview

Email sequence for Mendel's cold outbound. Each email has:
1. A **master template** with static parts containing spintax `{a|b|c}` and clearly marked variable slots `{{VARIABLE_NAME}}`.
2. A **variable definition list** explaining what each slot represents.
3. **Per-industry variable fills** (6 industries).
4. **Per-industry rendered examples** (spintax resolved to one option, variables filled — these are the send-ready emails).

### Rule (strict)

- **Anything that varies per industry → variable** (`{{vertical}}`, `{{country}}`, `{{INDUSTRY_PAIN}}`, etc.).
- **Anything static → spintax** (`{Hola|Hey|Buenas}`, `{Platicando|Hablando|Conversando}`, etc.).
- **Rendered examples** show spintax resolved (one option picked) and industry variables filled. Merge variables (`{{firstName}}`, `{{companyName}}`) stay as merge tags.

### Universal principles

- Peer-framed openers (no accusation of prospect's company).
- Value-probing CTAs (no cold "15 minutes" asks).
- Customer logos as social proof (only confirmed customers).
- Topic-led subject lines personalized via `{{firstName}}` / `{{companyName}}`.
- Hard rules: no em dashes, no exclamation marks, no currency words, no signature in body, no bracket placeholders, one question per email.

## Universal merge variables (filled per lead by EmailBison)

| Variable | Example | Source |
|---|---|---|
| `{{firstName}}` | Carlos | Lead enrichment |
| `{{companyName}}` | Soriana | Lead enrichment |
| `{{titlePlural}}` | CFOs | Persona plural — set per campaign |
| `{{vertical}}` | tech | Industry word — set per campaign |
| `{{country}}` | México | Geography — set per campaign |

Sender name + tagline handled by EmailBison `{SENDER_EMAIL_SIGNATURE}`. The sender is the Mendel sender (configured per campaign). Never put a sender name or sign-off in the body.

## Customer name index

| Customer | Status | Used in |
|---|---|---|
| Mercado Libre | Confirmed | Tech |
| KPMG | Confirmed | Professional Services |
| AB InBev | Confirmed | Tech, Manufacturing |
| Walmart | Verify with Alan against `CLIENTES ACTUALES MENDEL.xlsx` | Retail & CPG |
| OXXO / FEMSA | Verify with Alan | Retail & CPG |
| Viva Aerobus | Verify with Alan | Logistics |
| Pharma customer | None confirmed — anonymous framing | Pharma |

## Sequence overview

| Email | Goal | Thread | Word count |
|---|---|---|---:|
| **Email 1** (3 variants: A, B, C) | Plant problem + solution + soft ask for relevance | New thread | A: ~95-100 / B: ~95 / C: ~55-70 |
| **Email 2** | Offer benchmark walkthrough; trigger engagement reply that leads to meeting | Same thread as Email 1 | ~45-55 |

---

# EMAIL 1

## Email 1 — Variant overview

| Variant | Voice | Word count | Best for |
|---|---|---:|---|
| **A** — Peer-framed | Conversational, peer-CFO insight, full objection paragraph | ~95-100 | Warm first-touch, finance leaders open to peer signals |
| **B** — Architectural | Direct, founder-confident, contrasts incumbent stack | ~95-100 | CFOs who pattern-match on architecture, tech-literate buyers |
| **C** — Ultra-short | Compressed peer-pattern, mobile-first, value-probe | ~55-70 | Time-poor buyers, follow-up touches, mobile-dominant readers |

## VARIANT A — Peer-framed

### Master template

```
{Hola|Hey|Buenas} {{firstName}},

{Platicando|Hablando|Conversando} con {{titlePlural}} {de|en} {{vertical}} en {{country}}, {casi todos|todos|la mayoría} {cuentan|describen|comparten} {lo mismo|el mismo patrón|el mismo cuadro|el mismo dolor}: {{INDUSTRY_PAIN}}.

Mendel resuelve eso {{SOLUTION_VERB_PHRASE}}. {{OUTCOME_SENTENCE}}.

{{OBJECTION_DEFUSION}}.

Es la misma arquitectura que {usan|usa} {{CUSTOMER_LOGOS}} hoy.

¿{Vale|Tiene sentido|Hace sentido} {revisarlo|verlo|echarle un ojo} aplicado a {{companyName}}?
```

### Variable definitions

| Variable | Definition |
|---|---|
| `{{INDUSTRY_PAIN}}` | Industry-specific pain stated as peer observation. One clause. |
| `{{SOLUTION_VERB_PHRASE}}` | Mendel's action as gerund + capabilities. Starts with "poniendo", "aplicando", "capturando", etc. |
| `{{OUTCOME_SENTENCE}}` | What the team gets after Mendel. Concrete, one sentence. |
| `{{OBJECTION_DEFUSION}}` | Acknowledgment of likely objection + Mendel's specific counter. Pick objection #1, #2, or #3. |
| `{{CUSTOMER_LOGOS}}` | One or two confirmed Mendel customer names relevant to the industry. |

### Industry fills

#### Tech / Software

| Variable | Value |
|---|---|
| `{{vertical}}` | tech |
| `{{country}}` | México |
| `{{titlePlural}}` | CFOs |
| `{{INDUSTRY_PAIN}}` | el área de tech crece más rápido que finanzas, y el equipo termina validando tickets en vez de cerrar el mes |
| `{{SOLUTION_VERB_PHRASE}}` | poniendo un agente de IA que audita cada transacción contra política antes del cargo |
| `{{OUTCOME_SENTENCE}}` | Lo que llega a finanzas son reportes ya listos, no tickets sueltos, y el ERP queda reconciliado en tiempo real |
| `{{OBJECTION_DEFUSION}}` | Si ya operan con Concur + AMEX no es para reemplazarlos: Mendel los integra junto a CFDI y ERP en una sola plataforma, con las capacidades LatAm que esos tools no traen |
| `{{CUSTOMER_LOGOS}}` | Mercado Libre y AB InBev |

**Rendered:**
```
Hola {{firstName}},

Platicando con {{titlePlural}} en tech en México, casi todos cuentan lo mismo: el área de tech crece más rápido que finanzas, y el equipo termina validando tickets en vez de cerrar el mes.

Mendel resuelve eso poniendo un agente de IA que audita cada transacción contra política antes del cargo. Lo que llega a finanzas son reportes ya listos, no tickets sueltos, y el ERP queda reconciliado en tiempo real.

Si ya operan con Concur + AMEX no es para reemplazarlos: Mendel los integra junto a CFDI y ERP en una sola plataforma, con las capacidades LatAm que esos tools no traen.

Es la misma arquitectura que usan Mercado Libre y AB InBev hoy.

¿Vale revisarlo aplicado a {{companyName}}?
```

#### Retail & CPG

| Variable | Value |
|---|---|
| `{{vertical}}` | retail |
| `{{country}}` | México |
| `{{titlePlural}}` | CFOs |
| `{{INDUSTRY_PAIN}}` | con cientos de tiendas y miles de CFDIs al mes, el cierre del banco llega antes que el cierre interno |
| `{{SOLUTION_VERB_PHRASE}}` | aplicando políticas por tienda en el momento del cargo, recuperando los CFDIs automáticamente y mandándolos al ERP ya validados |
| `{{OUTCOME_SENTENCE}}` | El equipo cierra el mes el mismo día, sin hojas paralelas |
| `{{OBJECTION_DEFUSION}}` | Si ya operan con Concur o la tarjeta del banco, no es para reemplazarlos: Mendel los integra junto a CFDI y ERP en una sola plataforma, con las capacidades LatAm que los globales no traen |
| `{{CUSTOMER_LOGOS}}` | Walmart y OXXO |

**Rendered:**
```
Hey {{firstName}},

Hablando con {{titlePlural}} de retail en México, casi todos cuentan lo mismo: con cientos de tiendas y miles de CFDIs al mes, el cierre del banco llega antes que el cierre interno.

Mendel resuelve eso aplicando políticas por tienda en el momento del cargo, recuperando los CFDIs automáticamente y mandándolos al ERP ya validados. El equipo cierra el mes el mismo día, sin hojas paralelas.

Si ya operan con Concur o la tarjeta del banco, no es para reemplazarlos: Mendel los integra junto a CFDI y ERP en una sola plataforma, con las capacidades LatAm que los globales no traen.

Es la misma arquitectura que usan Walmart y OXXO hoy.

¿Tiene sentido verlo aplicado a {{companyName}}?
```

#### Logistics & Transportation

| Variable | Value |
|---|---|
| `{{vertical}}` | logística |
| `{{country}}` | México |
| `{{titlePlural}}` | CFOs |
| `{{INDUSTRY_PAIN}}` | tarjetas de flotilla, casetas, combustible y viáticos repartidos entre conductores, sin visibilidad hasta el cierre del mes |
| `{{SOLUTION_VERB_PHRASE}}` | con reglas que se aplican en el momento del cargo: por conductor, por proveedor y por horario |
| `{{OUTCOME_SENTENCE}}` | Combustible y per-diems quedan auditados antes de la conciliación, no después |
| `{{OBJECTION_DEFUSION}}` | Si ya usan tarjetas de flotilla del banco, no es para reemplazarlas: Mendel las integra junto a viáticos, CFDIs y ERP, con políticas que las tarjetas tradicionales no aplican |
| `{{CUSTOMER_LOGOS}}` | Viva Aerobus |

**Rendered:**
```
Buenas {{firstName}},

Conversando con {{titlePlural}} en logística en México, la mayoría cuenta lo mismo: tarjetas de flotilla, casetas, combustible y viáticos repartidos entre conductores, sin visibilidad hasta el cierre del mes.

Mendel resuelve eso con reglas que se aplican en el momento del cargo: por conductor, por proveedor y por horario. Combustible y per-diems quedan auditados antes de la conciliación, no después.

Si ya usan tarjetas de flotilla del banco, no es para reemplazarlas: Mendel las integra junto a viáticos, CFDIs y ERP, con políticas que las tarjetas tradicionales no aplican.

Es la misma arquitectura que usa Viva Aerobus hoy.

¿Hace sentido echarle un ojo para {{companyName}}?
```

#### Manufacturing & Industrial

| Variable | Value |
|---|---|
| `{{vertical}}` | manufactura |
| `{{country}}` | México |
| `{{titlePlural}}` | CFOs |
| `{{INDUSTRY_PAIN}}` | spend operativo disperso entre plantas, reconciliación manual contra SAP, y deductibilidad que se pierde por CFDIs que nunca llegan |
| `{{SOLUTION_VERB_PHRASE}}` | con control de políticas multi-planta en tiempo real, recuperación automática de CFDIs entre plantas y reconciliación directa contra SAP S/4HANA |
| `{{OUTCOME_SENTENCE}}` | El cierre deja de depender de ajustes manuales por planta |
| `{{OBJECTION_DEFUSION}}` | Sé que integrar con SAP suena pesado. Por diseño Mendel se conecta nativo a S/4HANA, no se le monta encima |
| `{{CUSTOMER_LOGOS}}` | AB InBev |

**Rendered:**
```
Hola {{firstName}},

Platicando con {{titlePlural}} de manufactura en México, todos describen el mismo patrón: spend operativo disperso entre plantas, reconciliación manual contra SAP, y deductibilidad que se pierde por CFDIs que nunca llegan.

Mendel resuelve eso con control de políticas multi-planta en tiempo real, recuperación automática de CFDIs entre plantas y reconciliación directa contra SAP S/4HANA. El cierre deja de depender de ajustes manuales por planta.

Sé que integrar con SAP suena pesado. Por diseño Mendel se conecta nativo a S/4HANA, no se le monta encima.

Es la misma arquitectura que usa AB InBev hoy.

¿Vale revisarlo aplicado a {{companyName}}?
```

#### Pharmaceutical & Healthcare

⚠️ No confirmed pharma customer logo — verify with Alan.

| Variable | Value |
|---|---|
| `{{vertical}}` | farma |
| `{{country}}` | México |
| `{{titlePlural}}` | CFOs |
| `{{INDUSTRY_PAIN}}` | las tarjetas de la fuerza de ventas, los viáticos con HCPs y los reembolsos necesitan trazabilidad completa, y armar el reporte de transparencia se vuelve un proyecto mensual |
| `{{SOLUTION_VERB_PHRASE}}` | aplicando política por representante en cada cargo y dejando la auditoría corriendo en tiempo real |
| `{{OUTCOME_SENTENCE}}` | El reporte de transparencia sale listo para exportar, sin armarlo a mano |
| `{{OBJECTION_DEFUSION}}` | Entiendo que sumar un sistema con datos sensibles suena complejo. Mendel se diseñó para escenarios regulados: controles por rol, ERP nativo, audit-ready desde día uno |
| `{{CUSTOMER_LOGOS}}` | Operaciones farma con fuerza distribuida _(anonymous — verify with Alan)_ |

**Rendered:**
```
Hey {{firstName}},

Hablando con {{titlePlural}} de farma en México, casi todos cuentan el mismo dolor: las tarjetas de la fuerza de ventas, los viáticos con HCPs y los reembolsos necesitan trazabilidad completa, y armar el reporte de transparencia se vuelve un proyecto mensual.

Mendel resuelve eso aplicando política por representante en cada cargo y dejando la auditoría corriendo en tiempo real. El reporte de transparencia sale listo para exportar, sin armarlo a mano.

Entiendo que sumar un sistema con datos sensibles suena complejo. Mendel se diseñó para escenarios regulados: controles por rol, ERP nativo, audit-ready desde día uno.

Operaciones farma con fuerza distribuida operan sobre esa arquitectura hoy.

¿Tiene sentido verlo aplicado a {{companyName}}?
```

#### Professional Services (Consulting / Audit / Legal)

| Variable | Value |
|---|---|
| `{{vertical}}` | servicios profesionales |
| `{{country}}` | LatAm |
| `{{titlePlural}}` | CFOs |
| `{{INDUSTRY_PAIN}}` | viaje de partners, gastos billables por cliente y operación multi-país, gestionado entre tarjetas, hojas y reembolsos manuales |
| `{{SOLUTION_VERB_PHRASE}}` | capturando cada gasto billable por engagement desde el momento del cargo, con CFDI integrado y reconciliación directa al ERP |
| `{{OUTCOME_SENTENCE}}` | Los partners aprueban desde el móvil y los reembolsos manuales desaparecen |
| `{{OBJECTION_DEFUSION}}` | Sé que el proceso actual funciona. La pregunta es cuántas horas y cuánta deductibilidad se pierden cada mes que ya no vuelven |
| `{{CUSTOMER_LOGOS}}` | KPMG |

**Rendered:**
```
Hola {{firstName}},

Conversando con {{titlePlural}} de servicios profesionales en LatAm, la mayoría cuenta el mismo dolor: viaje de partners, gastos billables por cliente y operación multi-país, gestionado entre tarjetas, hojas y reembolsos manuales.

Mendel resuelve eso capturando cada gasto billable por engagement desde el momento del cargo, con CFDI integrado y reconciliación directa al ERP. Los partners aprueban desde el móvil y los reembolsos manuales desaparecen.

Sé que el proceso actual funciona. La pregunta es cuántas horas y cuánta deductibilidad se pierden cada mes que ya no vuelven.

Es la misma arquitectura que usa KPMG hoy.

¿Vale revisarlo aplicado a {{companyName}}?
```

---

## VARIANT B — Architectural / design-limit-led

### Master template

```
{Hola|Hey|Buenas} {{firstName}},

{{INCUMBENT_DESIGN_LIMIT}}. {{INCUMBENT_QUALIFIER}}.

{Cuando hablo|Cuando converso|En las conversaciones} con {{titlePlural}} {de|en} {{vertical}} en {{country}}, {muchos|varios|la mayoría} ya {están|están moviendo|están migrando hacia} {{ARCHITECTURAL_SHIFT}}.

Eso es lo que {corre|opera|funciona en} {{CUSTOMER_LOGOS}} hoy, y es por eso que {{OUTCOME_SENTENCE}}.

¿{Tendría sentido|Vale la pena revisarlo|Te resuena} para {{companyName}}?
```

### Variable definitions

| Variable | Definition |
|---|---|
| `{{INCUMBENT_DESIGN_LIMIT}}` | Architectural fact about the incumbent stack. Neutral observation. |
| `{{INCUMBENT_QUALIFIER}}` | "Funciona si..." qualifier acknowledging the incumbent's legitimate use case. |
| `{{ARCHITECTURAL_SHIFT}}` | Mendel's approach as a shift: starts with "el control..." or "consolidando..." + 3 capabilities. |
| `{{CUSTOMER_LOGOS}}` | Confirmed Mendel customer(s) running the new architecture. |
| `{{OUTCOME_SENTENCE}}` | What changes after the shift, one sentence. |

### Industry fills

#### Tech / Software

| Variable | Value |
|---|---|
| `{{vertical}}` | tech |
| `{{country}}` | México |
| `{{titlePlural}}` | CFOs |
| `{{INCUMBENT_DESIGN_LIMIT}}` | Concur + AMEX se diseñó para reportar gastos después de que pasan |
| `{{INCUMBENT_QUALIFIER}}` | Funciona bien si lo que necesitas es visibilidad post-cierre |
| `{{ARCHITECTURAL_SHIFT}}` | moviendo el control antes de la transacción: un agente de IA evalúa cada cargo contra política, recupera el CFDI y reconcilia con el ERP en tiempo real |
| `{{CUSTOMER_LOGOS}}` | Mercado Libre |
| `{{OUTCOME_SENTENCE}}` | finanzas pasa de validar tickets a aprobar reportes ya listos |

**Rendered:**
```
Hola {{firstName}},

Concur + AMEX se diseñó para reportar gastos después de que pasan. Funciona bien si lo que necesitas es visibilidad post-cierre.

Cuando hablo con {{titlePlural}} en tech en México, muchos ya están moviendo el control antes de la transacción: un agente de IA evalúa cada cargo contra política, recupera el CFDI y reconcilia con el ERP en tiempo real.

Eso es lo que corre Mercado Libre hoy, y es por eso que finanzas pasa de validar tickets a aprobar reportes ya listos.

¿Tendría sentido para {{companyName}}?
```

#### Retail & CPG

| Variable | Value |
|---|---|
| `{{vertical}}` | retail |
| `{{country}}` | México |
| `{{titlePlural}}` | CFOs |
| `{{INCUMBENT_DESIGN_LIMIT}}` | Concur + la tarjeta del banco se diseñó para reportar después del estado de cuenta |
| `{{INCUMBENT_QUALIFIER}}` | Funciona si solo necesitas el report mensual |
| `{{ARCHITECTURAL_SHIFT}}` | controlando antes de la transacción: política por tienda en el momento del cargo, recuperación automática de CFDIs y reconciliación al ERP en tiempo real |
| `{{CUSTOMER_LOGOS}}` | Walmart y OXXO |
| `{{OUTCOME_SENTENCE}}` | el mes cierra el mismo día, sin hojas paralelas |

**Rendered:**
```
Hola {{firstName}},

Concur + la tarjeta del banco se diseñó para reportar después del estado de cuenta. Funciona si solo necesitas el report mensual.

Cuando hablo con {{titlePlural}} de retail en México, muchos ya están controlando antes de la transacción: política por tienda en el momento del cargo, recuperación automática de CFDIs y reconciliación al ERP en tiempo real.

Eso es lo que corren Walmart y OXXO hoy, y es por eso que el mes cierra el mismo día, sin hojas paralelas.

¿Vale la pena revisarlo para {{companyName}}?
```

#### Logistics & Transportation

| Variable | Value |
|---|---|
| `{{vertical}}` | logística |
| `{{country}}` | México |
| `{{titlePlural}}` | CFOs |
| `{{INCUMBENT_DESIGN_LIMIT}}` | Las tarjetas de flotilla del banco se diseñaron para pagar combustible |
| `{{INCUMBENT_QUALIFIER}}` | Visibilidad por conductor y políticas por proveedor no estaban en el alcance original |
| `{{ARCHITECTURAL_SHIFT}}` | moviendo el control al momento del cargo: reglas por conductor, por proveedor y por horario, con CFDIs y per-diems auditados antes del cierre |
| `{{CUSTOMER_LOGOS}}` | Viva Aerobus |
| `{{OUTCOME_SENTENCE}}` | la conciliación pasa de manual a automática |

**Rendered:**
```
Hola {{firstName}},

Las tarjetas de flotilla del banco se diseñaron para pagar combustible. Visibilidad por conductor y políticas por proveedor no estaban en el alcance original.

Cuando hablo con {{titlePlural}} en logística en México, muchos ya están moviendo el control al momento del cargo: reglas por conductor, por proveedor y por horario, con CFDIs y per-diems auditados antes del cierre.

Eso es lo que corre Viva Aerobus hoy, y es por eso que la conciliación pasa de manual a automática.

¿Te resuena para {{companyName}}?
```

#### Manufacturing & Industrial

| Variable | Value |
|---|---|
| `{{vertical}}` | manufactura |
| `{{country}}` | México |
| `{{titlePlural}}` | CFOs |
| `{{INCUMBENT_DESIGN_LIMIT}}` | El stack típico en manufactura, Concur, tarjetas del banco y SAP, se construyó como tres sistemas separados |
| `{{INCUMBENT_QUALIFIER}}` | Cada integración entre ellos es un punto de falla |
| `{{ARCHITECTURAL_SHIFT}}` | consolidando: control de políticas multi-planta en tiempo real, recuperación automática de CFDIs entre plantas, y reconciliación nativa contra SAP S/4HANA |
| `{{CUSTOMER_LOGOS}}` | AB InBev |
| `{{OUTCOME_SENTENCE}}` | el cierre deja de depender de ajustes manuales por planta |

**Rendered:**
```
Hola {{firstName}},

El stack típico en manufactura, Concur, tarjetas del banco y SAP, se construyó como tres sistemas separados. Cada integración entre ellos es un punto de falla.

Cuando hablo con {{titlePlural}} de manufactura en México, muchos ya están consolidando: control de políticas multi-planta en tiempo real, recuperación automática de CFDIs entre plantas, y reconciliación nativa contra SAP S/4HANA.

Eso es lo que corre AB InBev hoy, y es por eso que el cierre deja de depender de ajustes manuales por planta.

¿Tendría sentido para {{companyName}}?
```

#### Pharmaceutical & Healthcare

⚠️ No confirmed pharma customer logo — verify with Alan.

| Variable | Value |
|---|---|
| `{{vertical}}` | farma |
| `{{country}}` | México |
| `{{titlePlural}}` | CFOs |
| `{{INCUMBENT_DESIGN_LIMIT}}` | Las herramientas tradicionales de expense management no se diseñaron pensando en compliance farma |
| `{{INCUMBENT_QUALIFIER}}` | Trazabilidad por HCP y reporte de transparencia terminan siendo proyectos manuales mensuales |
| `{{ARCHITECTURAL_SHIFT}}` | moviendo esa trazabilidad al momento del cargo: política por representante, auditoría en tiempo real, reporte de transparencia listo para exportar |
| `{{CUSTOMER_LOGOS}}` | operaciones farma con fuerza distribuida _(anonymous — verify with Alan)_ |
| `{{OUTCOME_SENTENCE}}` | el reporte deja de armarse a mano |

**Rendered:**
```
Hola {{firstName}},

Las herramientas tradicionales de expense management no se diseñaron pensando en compliance farma. Trazabilidad por HCP y reporte de transparencia terminan siendo proyectos manuales mensuales.

Cuando hablo con {{titlePlural}} de farma en México, muchos ya están moviendo esa trazabilidad al momento del cargo: política por representante, auditoría en tiempo real, reporte de transparencia listo para exportar.

Eso es lo que corren operaciones farma con fuerza distribuida hoy, y es por eso que el reporte deja de armarse a mano.

¿Te interesa ver cómo aplicaría a {{companyName}}?
```

#### Professional Services

| Variable | Value |
|---|---|
| `{{vertical}}` | servicios profesionales |
| `{{country}}` | LatAm |
| `{{titlePlural}}` | CFOs |
| `{{INCUMBENT_DESIGN_LIMIT}}` | Capturar gasto billable por engagement nunca fue para lo que se diseñó Concur |
| `{{INCUMBENT_QUALIFIER}}` | Tampoco soporta CFDI ni operación multi-país de forma nativa |
| `{{ARCHITECTURAL_SHIFT}}` | consolidando: gasto billable capturado en el momento del cargo, multi-país, con CFDI integrado y reconciliación directa al ERP |
| `{{CUSTOMER_LOGOS}}` | KPMG |
| `{{OUTCOME_SENTENCE}}` | los partners aprueban desde el móvil y los reembolsos manuales desaparecen |

**Rendered:**
```
Hola {{firstName}},

Capturar gasto billable por engagement nunca fue para lo que se diseñó Concur. Tampoco soporta CFDI ni operación multi-país de forma nativa.

Cuando hablo con {{titlePlural}} de servicios profesionales en LatAm, muchos ya están consolidando: gasto billable capturado en el momento del cargo, multi-país, con CFDI integrado y reconciliación directa al ERP.

Eso es lo que corre KPMG hoy, y es por eso que los partners aprueban desde el móvil y los reembolsos manuales desaparecen.

¿Vale la pena para {{companyName}}?
```

---

## VARIANT C — Ultra-short peer-pattern

### Master template

```
{Hola|Hey|Buenas} {{firstName}},

{Cuando hablo|Cuando converso} con {{titlePlural}} {de|en} {{vertical}} en {{country}}, {casi todos|la mayoría|muchos} {describen|cuentan|comparten} {el mismo patrón|lo mismo|el mismo dolor}: {{INDUSTRY_PAIN}}.

Mendel {{SOLUTION_VERB_PHRASE}}.

Es lo que {corre|corren} {{CUSTOMER_LOGOS}} hoy.

¿{Tendría sentido|Te resuena|Es algo que valga la pena} para {{companyName}}?
```

### Variable definitions

| Variable | Definition |
|---|---|
| `{{INDUSTRY_PAIN}}` | Compressed industry-specific pain (one clause, peer-observed). |
| `{{SOLUTION_VERB_PHRASE}}` | Mendel's action as verb(s) + capabilities. Starts with present-tense verb ("aplica", "consolida", "automatiza"). |
| `{{CUSTOMER_LOGOS}}` | Confirmed Mendel customer(s) relevant to the industry. |

### Industry fills

#### Tech / Software

| Variable | Value |
|---|---|
| `{{vertical}}` | tech |
| `{{country}}` | México |
| `{{titlePlural}}` | CFOs |
| `{{INDUSTRY_PAIN}}` | tech escala más rápido que finanzas, y revisar gastos termina siendo apagar fuegos |
| `{{SOLUTION_VERB_PHRASE}}` | automatiza ese control con un agente de IA antes del cargo: política en tiempo real, CFDIs recuperados y ERP reconciliado |
| `{{CUSTOMER_LOGOS}}` | Mercado Libre |

**Rendered:**
```
Hola {{firstName}},

Cuando hablo con {{titlePlural}} en tech en México, casi todos describen el mismo patrón: tech escala más rápido que finanzas, y revisar gastos termina siendo apagar fuegos.

Mendel automatiza ese control con un agente de IA antes del cargo: política en tiempo real, CFDIs recuperados y ERP reconciliado.

Es lo que corre Mercado Libre hoy.

¿Tendría sentido para {{companyName}}?
```

#### Retail & CPG

| Variable | Value |
|---|---|
| `{{vertical}}` | retail |
| `{{country}}` | México |
| `{{titlePlural}}` | CFOs |
| `{{INDUSTRY_PAIN}}` | cientos de tiendas y miles de CFDIs por mes, con un cierre que llega después del estado de cuenta |
| `{{SOLUTION_VERB_PHRASE}}` | aplica política por tienda en cada cargo, recupera los CFDIs automáticamente y reconcilia con el ERP en tiempo real |
| `{{CUSTOMER_LOGOS}}` | Walmart y OXXO |

**Rendered:**
```
Hola {{firstName}},

Cuando hablo con {{titlePlural}} de retail en México, casi todos cuentan lo mismo: cientos de tiendas y miles de CFDIs por mes, con un cierre que llega después del estado de cuenta.

Mendel aplica política por tienda en cada cargo, recupera los CFDIs automáticamente y reconcilia con el ERP en tiempo real.

Es lo que corren Walmart y OXXO hoy.

¿Es algo que valga la pena para {{companyName}}?
```

#### Logistics & Transportation

| Variable | Value |
|---|---|
| `{{vertical}}` | logística |
| `{{country}}` | México |
| `{{titlePlural}}` | CFOs |
| `{{INDUSTRY_PAIN}}` | flotilla, combustible, casetas y viáticos repartidos entre conductores, sin visibilidad hasta el cierre |
| `{{SOLUTION_VERB_PHRASE}}` | aplica reglas por conductor, proveedor y horario en el momento del cargo, con CFDIs integrados al ERP |
| `{{CUSTOMER_LOGOS}}` | Viva Aerobus |

**Rendered:**
```
Hola {{firstName}},

Cuando hablo con {{titlePlural}} en logística en México, la mayoría describe el mismo dolor: flotilla, combustible, casetas y viáticos repartidos entre conductores, sin visibilidad hasta el cierre.

Mendel aplica reglas por conductor, proveedor y horario en el momento del cargo, con CFDIs integrados al ERP.

Es lo que corre Viva Aerobus hoy.

¿Te resuena para {{companyName}}?
```

#### Manufacturing & Industrial

| Variable | Value |
|---|---|
| `{{vertical}}` | manufactura |
| `{{country}}` | México |
| `{{titlePlural}}` | CFOs |
| `{{INDUSTRY_PAIN}}` | spend operativo disperso entre plantas, reconciliación manual contra SAP, y deductibilidad perdida por CFDIs que nunca llegan |
| `{{SOLUTION_VERB_PHRASE}}` | consolida políticas multi-planta, recupera CFDIs entre plantas y se conecta nativo a SAP S/4HANA |
| `{{CUSTOMER_LOGOS}}` | AB InBev |

**Rendered:**
```
Hola {{firstName}},

Cuando hablo con {{titlePlural}} de manufactura en México, casi todos describen el mismo patrón: spend operativo disperso entre plantas, reconciliación manual contra SAP, y deductibilidad perdida por CFDIs que nunca llegan.

Mendel consolida políticas multi-planta, recupera CFDIs entre plantas y se conecta nativo a SAP S/4HANA.

Es lo que corre AB InBev hoy.

¿Tendría sentido para {{companyName}}?
```

#### Pharmaceutical & Healthcare

⚠️ no confirmed pharma customer logo — verify with Alan

| Variable | Value |
|---|---|
| `{{vertical}}` | farma |
| `{{country}}` | México |
| `{{titlePlural}}` | CFOs |
| `{{INDUSTRY_PAIN}}` | fuerza de ventas con HCPs, viáticos médicos y reembolsos que necesitan trazabilidad para reporte de transparencia |
| `{{SOLUTION_VERB_PHRASE}}` | aplica política por representante, audita en tiempo real y deja el reporte listo para exportar |
| `{{CUSTOMER_LOGOS}}` | operaciones farma con fuerza distribuida _(anonymous — verify with Alan)_ |

**Rendered:**
```
Hola {{firstName}},

Cuando hablo con {{titlePlural}} de farma en México, casi todos describen el mismo dolor: fuerza de ventas con HCPs, viáticos médicos y reembolsos que necesitan trazabilidad para reporte de transparencia.

Mendel aplica política por representante, audita en tiempo real y deja el reporte listo para exportar.

Es lo que corren operaciones farma con fuerza distribuida hoy.

¿Te interesa ver cómo aplicaría a {{companyName}}?
```

#### Professional Services

| Variable | Value |
|---|---|
| `{{vertical}}` | servicios profesionales |
| `{{country}}` | LatAm |
| `{{titlePlural}}` | CFOs |
| `{{INDUSTRY_PAIN}}` | viaje de partners, gastos billables por cliente y operación multi-país, gestionado entre tarjetas, hojas y reembolsos manuales |
| `{{SOLUTION_VERB_PHRASE}}` | captura cada gasto billable por engagement en el momento del cargo, multi-país, con CFDI y reconciliación al ERP |
| `{{CUSTOMER_LOGOS}}` | KPMG |

**Rendered:**
```
Hola {{firstName}},

Cuando hablo con {{titlePlural}} de servicios profesionales en LatAm, la mayoría cuenta lo mismo: viaje de partners, gastos billables por cliente y operación multi-país, gestionado entre tarjetas, hojas y reembolsos manuales.

Mendel captura cada gasto billable por engagement en el momento del cargo, multi-país, con CFDI y reconciliación al ERP.

Es lo que corre KPMG hoy.

¿Es algo que valga la pena para {{companyName}}?
```

---

# EMAIL 2 — Lead magnet (benchmark walkthrough)

**Goal:** trigger an engagement reply ("yes, interested") that the sender converts into a 20-min walkthrough call. The meeting booking happens in the follow-up reply, never in the cold body.

**Thread:** same thread as Email 1 (subject inherited, EmailBison auto-maintains thread via headers). No new subject line needed.

## Master template

```
{Hola|Hey|Buenas} {{firstName}},

{Armamos|Construimos|Preparamos|Hicimos} un benchmark de cómo {{titlePlural}} {de|en} {{vertical}} en {{country}} {{PEER_ACTIVITIES}}. {Datos reales|Datos crudos|Información real}, anónimos.

{Puedo mostrarte|Te puedo enseñar|Te puedo compartir} qué {hacen los otros|están haciendo los otros|hacen tus pares} y cómo se {puede aplicar|aplicaría|traduce} al setup de {{companyName}}, sin pitch.

{{CTA}}
```

## Variable definitions

| Variable | Type | Definition |
|---|---|---|
| `{{firstName}}` | merge | Lead first name |
| `{{companyName}}` | merge | Lead company |
| `{{titlePlural}}` | campaign-level | Persona plural (`CFOs`) |
| `{{vertical}}` | campaign-level | Industry word (per industry fill) |
| `{{country}}` | campaign-level | Geography (per industry fill) |
| `{{PEER_ACTIVITIES}}` | industry-specific | What peer CFOs in the benchmark are doing (3 activities in present continuous) |
| `{{CTA}}` | A/B variant | One of two CTA variants (see below) |

## CTA — two variants for A/B testing

| Variant | Spintaxed CTA | Tone | When to use |
|---|---|---|---|
| **CTA-A — Engagement probe** | `¿Te {interesaría|sería útil|haría sentido}?` | Softer, value-first, lower commitment | Default for cold first send |
| **CTA-B — Time choice** | `¿{Te funciona|Te queda|Te va} esta semana o la próxima?` | Direct, agenda-driving, binary | Default for warm leads (opened Email 1, prior signal) |

Run both in parallel. CTA-A wins on reply rate. CTA-B wins on meetings booked per reply. Pick based on which metric matters more this campaign.

## Industry fills

Only `{{PEER_ACTIVITIES}}` and the universal campaign-level vars change per industry. Body skeleton is identical.

| Industry | `{{vertical}}` | `{{country}}` | `{{PEER_ACTIVITIES}}` |
|---|---|---|---|
| Tech / Software | `tech` | `México` | están automatizando auditoría con agentes IA, recuperando CFDIs y reconciliando con ERP en tiempo real |
| Retail & CPG | `retail` | `México` | están aplicando políticas por punto de venta, recuperando CFDIs automáticamente y cerrando el mes el mismo día |
| Logistics & Transportation | `logística` | `México` | están aplicando reglas por conductor y proveedor, con CFDIs y per-diems auditados antes del cierre |
| Manufacturing & Industrial | `manufactura` | `México` | están consolidando spend multi-planta con recuperación de CFDIs y reconciliación nativa a SAP S/4HANA |
| Pharmaceutical & Healthcare ⚠️ | `farma` | `México` | están aplicando política por representante, auditando en tiempo real y dejando el reporte de transparencia listo para exportar |
| Professional Services | `servicios profesionales` | `LatAm` | están capturando gasto billable por engagement, multi-país, con CFDI integrado al ERP |

## Rendered examples

### Tech / Software — CTA-A (engagement probe)
```
Hola {{firstName}},

Armamos un benchmark de cómo {{titlePlural}} en tech en México están automatizando auditoría con agentes IA, recuperando CFDIs y reconciliando con ERP en tiempo real. Datos reales, anónimos.

Puedo mostrarte qué hacen los otros y cómo se puede aplicar al setup de {{companyName}}, sin pitch.

¿Te interesaría?
```

### Tech / Software — CTA-B (time choice)
```
Hola {{firstName}},

Armamos un benchmark de cómo {{titlePlural}} en tech en México están automatizando auditoría con agentes IA, recuperando CFDIs y reconciliando con ERP en tiempo real. Datos reales, anónimos.

Puedo mostrarte qué hacen los otros y cómo se puede aplicar al setup de {{companyName}}, sin pitch.

¿Te funciona esta semana o la próxima?
```

### Retail & CPG — CTA-A
```
Hey {{firstName}},

Armamos un benchmark de cómo {{titlePlural}} de retail en México están aplicando políticas por punto de venta, recuperando CFDIs automáticamente y cerrando el mes el mismo día. Datos reales, anónimos.

Puedo mostrarte qué hacen los otros y cómo se puede aplicar al setup de {{companyName}}, sin pitch.

¿Te sería útil?
```

### Logistics & Transportation — CTA-A
```
Buenas {{firstName}},

Armamos un benchmark de cómo {{titlePlural}} en logística en México están aplicando reglas por conductor y proveedor, con CFDIs y per-diems auditados antes del cierre. Datos reales, anónimos.

Puedo mostrarte qué hacen los otros y cómo se puede aplicar al setup de {{companyName}}, sin pitch.

¿Te haría sentido?
```

### Manufacturing & Industrial — CTA-A
```
Hola {{firstName}},

Armamos un benchmark de cómo {{titlePlural}} de manufactura en México están consolidando spend multi-planta con recuperación de CFDIs y reconciliación nativa a SAP S/4HANA. Datos reales, anónimos.

Puedo mostrarte qué hacen los otros y cómo se puede aplicar al setup de {{companyName}}, sin pitch.

¿Te interesaría?
```

### Pharmaceutical & Healthcare — CTA-A
```
Hey {{firstName}},

Armamos un benchmark de cómo {{titlePlural}} de farma en México están aplicando política por representante, auditando en tiempo real y dejando el reporte de transparencia listo para exportar. Datos reales, anónimos.

Puedo mostrarte qué hacen los otros y cómo se puede aplicar al setup de {{companyName}}, sin pitch.

¿Te sería útil?
```

### Professional Services — CTA-A
```
Hola {{firstName}},

Armamos un benchmark de cómo {{titlePlural}} de servicios profesionales en LatAm están capturando gasto billable por engagement, multi-país, con CFDI integrado al ERP. Datos reales, anónimos.

Puedo mostrarte qué hacen los otros y cómo se puede aplicar al setup de {{companyName}}, sin pitch.

¿Te haría sentido?
```

## Reply handling for Email 2

| Reply | Sender response |
|---|---|
| "Sí, me interesa" / "Sí, mándalo" | `Perfecto, lo más útil es repasarlo en 20 min. ¿Te queda jueves o viernes esta semana?` — book the meeting in the reply, never in the cold body. |
| "Mándame el PDF mejor" | `No tenemos PDF aparte porque depende del contexto. Si te queda 20 min te lo paso aplicado a {{companyName}}.` Push back to meeting once. |
| "No me interesa" | Polite acknowledgment, move to long-term nurture. No push. |
| No reply | Email 3 with a different angle (case study or direct demo offer). |

---

# Libraries

## Subject line library — Email 1

Two patterns per industry. **Pattern A** (direct question) wins on replies; **Pattern C** (peer reference) wins on opens. A/B both per campaign.

| Industry | Pattern A (direct question) | Pattern C (peer reference) |
|---|---|---|
| Tech | `{{firstName}}, ¿cómo manejan finanzas en {{companyName}}?` | `{{firstName}}, lo que hace Mercado Libre` |
| Retail | `{{firstName}}, ¿cómo cierran el mes en {{companyName}}?` | `{{firstName}}, lo que hace Walmart` |
| Logistics | `{{firstName}}, ¿cómo controlan flotilla en {{companyName}}?` | `{{firstName}}, lo que hace Viva Aerobus` |
| Manufacturing | `{{firstName}}, ¿cómo reconcilian SAP en {{companyName}}?` | `{{firstName}}, lo que hace AB InBev` |
| Pharma | `{{firstName}}, ¿cómo arman transparencia en {{companyName}}?` | `{{firstName}}, lo que cambió en farma` |
| Professional Services | `{{firstName}}, ¿cómo capturan billable en {{companyName}}?` | `{{firstName}}, lo que hace KPMG` |

## Subject line for Email 2

Same thread as Email 1 — EmailBison inherits subject. No new subject required.

## CTA library

Used in Email 1 (and as alternatives for Email 2 CTA-A).

| CTA | Tone | Use case |
|---|---|---|
| `¿Tendría sentido para {{companyName}}?` | Neutral, polite | Default |
| `¿Es algo que valga la pena revisar para {{companyName}}?` | Slightly more formal | Senior CFO targets |
| `¿Te resuena para {{companyName}}?` | Casual, conversational | Younger or modern operations |
| `¿Te interesa ver cómo aplicaría a {{companyName}}?` | Action-oriented | When ready to demo |
| `¿Vale la pena profundizar en esto?` | Open-ended | Strategic conversations |
| `¿Vale revisarlo aplicado a {{companyName}}?` | Direct, soft | Default for Variant A |
| `¿Tiene sentido verlo aplicado a {{companyName}}?` | Neutral | Variant A alternate |
| `¿Hace sentido echarle un ojo para {{companyName}}?` | Casual Mexican | Variant A alternate |

## Objection defusion library (Variant A only)

| # | Trigger | Template |
|---|---|---|
| 1 | Existing stack (Concur, AMEX, bank cards, fleet cards) | `Si ya operan con [stack], Mendel no [los/las] reemplaza: integra [things] en un solo lugar, con capacidades LatAm que [esos tools / los globales] no traen.` |
| 2 | Implementation complexity (SAP, ERP, multi-country, compliance) | `Sé que [implementing X] suena pesado. Por diseño Mendel se conecta nativo a [SAP / ERP], no se le agrega encima.` |
| 3 | Current process works well enough | `Sé que el proceso actual funciona. La pregunta es cuántas horas y cuánta deductibilidad se pierden cada mes que ya no vuelven.` |

| Industry | Default objection used in Variant A |
|---|---|
| Tech | #1 |
| Retail | #1 |
| Logistics | #1 |
| Manufacturing | #2 |
| Pharma | #2 |
| Professional Services | #3 |

---

# Spintax reference (master templates only — never in rendered examples)

Spintax in master templates lets EmailBison randomize wording per send to reduce same-text detection. Format: `{option1|option2|option3}`. Rendered examples show one resolved option per slot for human review.

**Allowed in spintax:**
- Greetings: `{Hola|Hey|Buenas}`
- Conversation verbs: `{Platicando|Hablando|Conversando}`, `{Cuando hablo|Cuando converso|En las conversaciones}`
- Quantifiers: `{todos|casi todos|la mayoría|muchos|varios}`
- Verbs of speech: `{cuentan|describen|comparten}`
- Pattern descriptors: `{el mismo patrón|el mismo cuadro|el mismo dolor|lo mismo}`
- Prepositions: `{de|en}`
- State verbs: `{están|están moviendo|están migrando hacia}`
- Operation verbs: `{corre|opera|funciona en}`, `{usan|usa}`, `{hoy|actualmente}`
- Email-2 build verbs: `{Armamos|Construimos|Preparamos|Hicimos}`
- Email-2 share verbs: `{Puedo mostrarte|Te puedo enseñar|Te puedo compartir}`, `{hacen los otros|están haciendo los otros|hacen tus pares}`, `{puede aplicar|aplicaría|traduce}`
- Email-2 data descriptors: `{Datos reales|Datos crudos|Información real}`
- CTA verbs: `{Vale|Tiene sentido|Hace sentido|Tendría sentido|Te resuena}`, `{revisarlo|verlo|echarle un ojo}`, `{interesaría|sería útil|haría sentido}`, `{Te funciona|Te queda|Te va}`

**Never spintax:**
- Merge variables (`{{firstName}}`, `{{companyName}}`, `{{titlePlural}}`, `{{vertical}}`, `{{country}}`)
- Industry-specific variable slots (`{{INDUSTRY_PAIN}}`, `{{SOLUTION_VERB_PHRASE}}`, `{{OUTCOME_SENTENCE}}`, `{{OBJECTION_DEFUSION}}`, `{{CUSTOMER_LOGOS}}`, `{{INCUMBENT_DESIGN_LIMIT}}`, `{{INCUMBENT_QUALIFIER}}`, `{{ARCHITECTURAL_SHIFT}}`, `{{PEER_ACTIVITIES}}`)
- Customer names (Mercado Libre, KPMG, AB InBev, Walmart, OXXO, Viva Aerobus)
- Product / brand references (Mendel, Concur, AMEX, SAP, S/4HANA, ERP, CFDI, SAT, HCP)
- Industry capability descriptions (CFDIs recuperados, ERP integrado, etc.)

---

# Hard rules check

All variants and rendered examples comply with:
- No em dashes
- No exclamation marks
- No currency words ($ / € / dollar / peso / cost / fee / price / pricing)
- No spam triggers (free, guaranteed, urgent, limited time, etc.)
- No signature in body (signature handled by `{SENDER_EMAIL_SIGNATURE}`)
- No bracket placeholders in final rendered copy
- No accusatory framing about the prospect's company
- One question per email (the CTA)
- Spanish for Mexico / Argentina / Chile audiences

---

# Status notes

- **No live Kinetyca campaigns yet.** Launch target: ~2026-05-26 per strategy call.
- **Database build status:** 80% complete in Clay (ClickUp `868jea2rf`).
- **Customer logo verification pending:** verify Walmart, OXXO, Viva Aerobus against `CLIENTES ACTUALES MENDEL.xlsx` (ClickUp `868jea2v0`) before launch.
- **Pharma logo gap:** no confirmed pharma customer. Either request one from Alan or keep the anonymous "operaciones farma con fuerza distribuida" framing.
- **Benchmark asset for Email 2:** the benchmark walkthrough needs to be built per vertical. Until then, the sender uses an internal Mendel deck during the call.
- **Sender:** the Mendel sender (configured per campaign in EmailBison). Sender name and tagline managed by `{SENDER_EMAIL_SIGNATURE}` system variable.

---

# Related files

- [`../CLAUDE.md`](../CLAUDE.md) — Mendel client brain
- [`outbound-campaigns.md`](outbound-campaigns.md) — operational source of truth
- [`inherited-campaign-baseline.md`](inherited-campaign-baseline.md) — agency campaign analysis
- [`../knowledge/dnc-blocklist.md`](../knowledge/dnc-blocklist.md) — DNC + competitor + bank + gov blocklist
- [`../call-summaries/2026-04-28-onboarding-mendel-kinetyca.md`](../call-summaries/2026-04-28-onboarding-mendel-kinetyca.md)
- [`../call-summaries/2026-05-05-strategy-mendel-kinetyca.md`](../call-summaries/2026-05-05-strategy-mendel-kinetyca.md)
