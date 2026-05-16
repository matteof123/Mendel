# Mendel — Email Sequence Library

_Last updated: 2026-05-16_
_Status: pre-launch — awaiting campaign launch (~2026-05-26)_
_Language: Spanish (Mexico priority, "tú" form). Professional Services version uses LatAm framing._
_Designed for: machine consumption (AI-driven prompt generation, EmailBison upload)._

## Overview

Email sequence for Mendel's cold outbound. Each email has:
1. A **master template** with static phrases containing spintax `{a|b|c}` and clearly marked variable slots `{{VARIABLE_NAME}}`.
2. A **variable definition list** explaining what each slot represents.
3. **Per-industry variable fills** — each per-industry variable also contains spintax `{a|b}` so values vary per send.
4. **Per-industry rendered examples** — spintax resolved to one option per slot, variables filled (these are illustrative sends).

### Strict rules

- **Anything that varies per industry → variable** (`{{vertical}}`, `{{country}}`, `{{INDUSTRY_PAIN}}`, etc.).
- **Anything static within a variant → spintax in the master template** (`{Hola|Hey|Buenas}`).
- **Per-industry variable values also have spintax** — they hold 2+ phrasings of the same idea so each send picks one.
- **Rendered examples** show one resolved option per slot; merge variables stay as merge tags.

### Universal principles

- Peer-framed openers (no accusation of prospect's company).
- Value-probing CTAs (no cold "15 minutes" asks in the body).
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

| Email | Variants | Goal | Thread |
|---|---|---|---|
| **Email 1** | A1, A2, B, C | Plant problem + solution + soft ask for relevance | New thread |
| **Email 2** | Single template with CTA A/B test | Trigger engagement reply → 20-min walkthrough call | Same thread as Email 1 |

---

# EMAIL 1

## Email 1 — Variant overview

| Variant | Voice | Word count | Best for |
|---|---|---:|---|
| **A1** — Peer-framed, no objection | Peer-CFO insight, 4-paragraph | ~75-80 | Default Email 1, fastest read |
| **A2** — Peer-framed, with objection | Adds objection defusion paragraph | ~95-100 | Segments where the common objection is well known |
| **B** — Architectural | Direct, founder-confident, contrasts incumbent stack | ~95-100 | CFOs who pattern-match on architecture |
| **C** — Ultra-short | Compressed peer-pattern, mobile-first | ~55-70 | Time-poor buyers, follow-up touches |

---

## VARIANT A1 — Peer-framed (no objection defusion)

### Master template

```
{Hola|Hey|Buenas} {{firstName}},

{Platicando|Hablando|Conversando} con {{titlePlural}} {de|en} {{vertical}} en {{country}}, {casi todos|todos|la mayoría} {cuentan|describen|comparten} {lo mismo|el mismo patrón|el mismo cuadro|el mismo dolor}: {{INDUSTRY_PAIN}}.

Mendel resuelve eso {{SOLUTION_VERB_PHRASE}}. {{OUTCOME_SENTENCE}}.

Es la misma arquitectura que {usan|usa} {{CUSTOMER_LOGOS}} hoy.

¿{Vale|Tiene sentido|Hace sentido} {revisarlo|verlo|echarle un ojo} aplicado a {{companyName}}?
```

### Variable definitions (A1)

| Variable | Definition |
|---|---|
| `{{INDUSTRY_PAIN}}` | Industry-specific pain stated as peer observation. Spintax of 2 phrasings. |
| `{{SOLUTION_VERB_PHRASE}}` | Mendel's action as gerund + capabilities. Spintax of 2 phrasings. |
| `{{OUTCOME_SENTENCE}}` | What the team gets after Mendel. Spintax of 2 phrasings. |
| `{{CUSTOMER_LOGOS}}` | Confirmed customer(s) for the industry. Spintax of 2 phrasings. |

### Industry fills (A1)

#### Tech / Software

```
vertical: tech
country: México
titlePlural: CFOs

INDUSTRY_PAIN: {el área de tech crece más rápido que finanzas, y el equipo termina validando tickets en vez de cerrar el mes|tech escala antes que finanzas, y los gastos terminan revisándose semanas después}

SOLUTION_VERB_PHRASE: {poniendo un agente de IA que audita cada transacción contra política antes del cargo|con un agente de IA que evalúa cada cargo contra política en el momento, no después}

OUTCOME_SENTENCE: {Lo que llega a finanzas son reportes ya listos, no tickets sueltos, y el ERP queda reconciliado en tiempo real|Finanzas deja de validar tickets y empieza a aprobar reportes ya armados, con ERP reconciliado al instante}

CUSTOMER_LOGOS: {Mercado Libre y AB InBev|operaciones como Mercado Libre y AB InBev}
```

**Rendered:**
```
Hola {{firstName}},

Platicando con {{titlePlural}} en tech en México, casi todos cuentan lo mismo: el área de tech crece más rápido que finanzas, y el equipo termina validando tickets en vez de cerrar el mes.

Mendel resuelve eso poniendo un agente de IA que audita cada transacción contra política antes del cargo. Lo que llega a finanzas son reportes ya listos, no tickets sueltos, y el ERP queda reconciliado en tiempo real.

Es la misma arquitectura que usan Mercado Libre y AB InBev hoy.

¿Vale revisarlo aplicado a {{companyName}}?
```

#### Retail & CPG

```
vertical: retail
country: México
titlePlural: CFOs

INDUSTRY_PAIN: {con cientos de tiendas y miles de CFDIs al mes, el cierre del banco llega antes que el cierre interno|cada tienda mueve volumen propio, y el cierre interno depende de cuándo termine finanzas de procesar todos los CFDIs}

SOLUTION_VERB_PHRASE: {aplicando políticas por tienda en el momento del cargo, recuperando los CFDIs automáticamente y mandándolos al ERP ya validados|con política por tienda evaluada en cada cargo, CFDIs recuperados automáticamente y reconciliación al ERP en tiempo real}

OUTCOME_SENTENCE: {El equipo cierra el mes el mismo día, sin hojas paralelas|El cierre mensual pasa de varios días a uno, sin hojas paralelas}

CUSTOMER_LOGOS: {Walmart y OXXO|cadenas como Walmart y OXXO}
```

**Rendered:**
```
Hey {{firstName}},

Hablando con {{titlePlural}} de retail en México, casi todos cuentan lo mismo: con cientos de tiendas y miles de CFDIs al mes, el cierre del banco llega antes que el cierre interno.

Mendel resuelve eso aplicando políticas por tienda en el momento del cargo, recuperando los CFDIs automáticamente y mandándolos al ERP ya validados. El equipo cierra el mes el mismo día, sin hojas paralelas.

Es la misma arquitectura que usan Walmart y OXXO hoy.

¿Tiene sentido verlo aplicado a {{companyName}}?
```

#### Logistics & Transportation

```
vertical: logística
country: México
titlePlural: CFOs

INDUSTRY_PAIN: {tarjetas de flotilla, casetas, combustible y viáticos repartidos entre conductores, sin visibilidad hasta el cierre del mes|el spend de flota vive entre el banco, los conductores y los proveedores, sin película completa hasta fin de mes}

SOLUTION_VERB_PHRASE: {con reglas que se aplican en el momento del cargo: por conductor, por proveedor y por horario|aplicando reglas en cada cargo por conductor, proveedor y horario, antes de que el gasto cierre el ciclo}

OUTCOME_SENTENCE: {Combustible y per-diems quedan auditados antes de la conciliación, no después|La conciliación pasa de manual y posterior al cierre a automática y previa al cargo}

CUSTOMER_LOGOS: {Viva Aerobus|operaciones como Viva Aerobus}
```

**Rendered:**
```
Buenas {{firstName}},

Conversando con {{titlePlural}} en logística en México, la mayoría cuenta lo mismo: tarjetas de flotilla, casetas, combustible y viáticos repartidos entre conductores, sin visibilidad hasta el cierre del mes.

Mendel resuelve eso con reglas que se aplican en el momento del cargo: por conductor, por proveedor y por horario. Combustible y per-diems quedan auditados antes de la conciliación, no después.

Es la misma arquitectura que usa Viva Aerobus hoy.

¿Hace sentido echarle un ojo para {{companyName}}?
```

#### Manufacturing & Industrial

```
vertical: manufactura
country: México
titlePlural: CFOs

INDUSTRY_PAIN: {spend operativo disperso entre plantas, reconciliación manual contra SAP, y deductibilidad que se pierde por CFDIs que nunca llegan|cada planta opera con su propio flujo de spend, el cierre depende de reconciliar todo a mano contra SAP, y la deductibilidad se pierde entre CFDIs traspapelados}

SOLUTION_VERB_PHRASE: {con control de políticas multi-planta en tiempo real, recuperación automática de CFDIs entre plantas y reconciliación directa contra SAP S/4HANA|aplicando políticas multi-planta en tiempo real, recuperando CFDIs entre plantas y reconciliando nativamente contra SAP S/4HANA}

OUTCOME_SENTENCE: {El cierre deja de depender de ajustes manuales por planta|La conciliación entre plantas y SAP pasa de manual a automática, sin retrabajo al cierre}

CUSTOMER_LOGOS: {AB InBev|operaciones como AB InBev}
```

**Rendered:**
```
Hola {{firstName}},

Platicando con {{titlePlural}} de manufactura en México, todos describen el mismo patrón: spend operativo disperso entre plantas, reconciliación manual contra SAP, y deductibilidad que se pierde por CFDIs que nunca llegan.

Mendel resuelve eso con control de políticas multi-planta en tiempo real, recuperación automática de CFDIs entre plantas y reconciliación directa contra SAP S/4HANA. El cierre deja de depender de ajustes manuales por planta.

Es la misma arquitectura que usa AB InBev hoy.

¿Vale revisarlo aplicado a {{companyName}}?
```

#### Pharmaceutical & Healthcare

⚠️ No confirmed pharma customer logo — verify with Alan.

```
vertical: farma
country: México
titlePlural: CFOs

INDUSTRY_PAIN: {las tarjetas de la fuerza de ventas, los viáticos con HCPs y los reembolsos necesitan trazabilidad completa, y armar el reporte de transparencia se vuelve un proyecto mensual|la fuerza de ventas con HCPs genera transacciones que necesitan trazabilidad para transparencia, y armar el reporte mensual consume días del equipo}

SOLUTION_VERB_PHRASE: {aplicando política por representante en cada cargo y dejando la auditoría corriendo en tiempo real|con política por representante evaluada en cada cargo y auditoría continua en tiempo real}

OUTCOME_SENTENCE: {El reporte de transparencia sale listo para exportar, sin armarlo a mano|La transparencia deja de ser un proyecto mensual y se convierte en un export}

CUSTOMER_LOGOS: {operaciones farma con fuerza distribuida|equipos farma con fuerza de ventas activa}
```

**Rendered:**
```
Hey {{firstName}},

Hablando con {{titlePlural}} de farma en México, casi todos cuentan el mismo dolor: las tarjetas de la fuerza de ventas, los viáticos con HCPs y los reembolsos necesitan trazabilidad completa, y armar el reporte de transparencia se vuelve un proyecto mensual.

Mendel resuelve eso aplicando política por representante en cada cargo y dejando la auditoría corriendo en tiempo real. El reporte de transparencia sale listo para exportar, sin armarlo a mano.

Es la misma arquitectura que usan operaciones farma con fuerza distribuida hoy.

¿Tiene sentido verlo aplicado a {{companyName}}?
```

#### Professional Services

```
vertical: servicios profesionales
country: LatAm
titlePlural: CFOs

INDUSTRY_PAIN: {viaje de partners, gastos billables por cliente y operación multi-país, gestionado entre tarjetas, hojas y reembolsos manuales|el gasto billable se reparte entre tarjetas, hojas y reembolsos, sin un solo lugar donde quede capturado por engagement}

SOLUTION_VERB_PHRASE: {capturando cada gasto billable por engagement desde el momento del cargo, con CFDI integrado y reconciliación directa al ERP|con captura de gasto billable por engagement en el momento del cargo, CFDI integrado y reconciliación al ERP}

OUTCOME_SENTENCE: {Los partners aprueban desde el móvil y los reembolsos manuales desaparecen|Los partners firman desde el móvil y la cola de reembolsos manuales se acaba}

CUSTOMER_LOGOS: {KPMG|firmas como KPMG}
```

**Rendered:**
```
Hola {{firstName}},

Conversando con {{titlePlural}} de servicios profesionales en LatAm, la mayoría cuenta el mismo dolor: viaje de partners, gastos billables por cliente y operación multi-país, gestionado entre tarjetas, hojas y reembolsos manuales.

Mendel resuelve eso capturando cada gasto billable por engagement desde el momento del cargo, con CFDI integrado y reconciliación directa al ERP. Los partners aprueban desde el móvil y los reembolsos manuales desaparecen.

Es la misma arquitectura que usa KPMG hoy.

¿Vale revisarlo aplicado a {{companyName}}?
```

---

## VARIANT A2 — Peer-framed with objection defusion

Same as A1, plus one paragraph: `{{OBJECTION_DEFUSION}}` between the outcome and the social proof.

### Master template

```
{Hola|Hey|Buenas} {{firstName}},

{Platicando|Hablando|Conversando} con {{titlePlural}} {de|en} {{vertical}} en {{country}}, {casi todos|todos|la mayoría} {cuentan|describen|comparten} {lo mismo|el mismo patrón|el mismo cuadro|el mismo dolor}: {{INDUSTRY_PAIN}}.

Mendel resuelve eso {{SOLUTION_VERB_PHRASE}}. {{OUTCOME_SENTENCE}}.

{{OBJECTION_DEFUSION}}.

Es la misma arquitectura que {usan|usa} {{CUSTOMER_LOGOS}} hoy.

¿{Vale|Tiene sentido|Hace sentido} {revisarlo|verlo|echarle un ojo} aplicado a {{companyName}}?
```

### Variable definitions (A2)

Same as A1, plus:

| Variable | Definition |
|---|---|
| `{{OBJECTION_DEFUSION}}` | Acknowledgment of likely objection + Mendel's specific counter. Spintax of 2 phrasings. Industry picks objection #1, #2, or #3 from the library. |

### Industry fills — OBJECTION_DEFUSION only (rest same as A1)

#### Tech / Software (objection #1)

```
OBJECTION_DEFUSION: {Si ya operan con Concur + AMEX no es para reemplazarlos: Mendel los integra junto a CFDI y ERP en una sola plataforma, con las capacidades LatAm que esos tools no traen|Si ya tienen Concur + AMEX, no se trata de cambiarlos: Mendel se conecta con ambos y suma CFDI, ERP y políticas en tiempo real en un solo lugar}
```

**Rendered (A2 Tech):**
```
Hola {{firstName}},

Platicando con {{titlePlural}} en tech en México, casi todos cuentan lo mismo: el área de tech crece más rápido que finanzas, y el equipo termina validando tickets en vez de cerrar el mes.

Mendel resuelve eso poniendo un agente de IA que audita cada transacción contra política antes del cargo. Lo que llega a finanzas son reportes ya listos, no tickets sueltos, y el ERP queda reconciliado en tiempo real.

Si ya operan con Concur + AMEX no es para reemplazarlos: Mendel los integra junto a CFDI y ERP en una sola plataforma, con las capacidades LatAm que esos tools no traen.

Es la misma arquitectura que usan Mercado Libre y AB InBev hoy.

¿Vale revisarlo aplicado a {{companyName}}?
```

#### Retail & CPG (objection #1)

```
OBJECTION_DEFUSION: {Si ya operan con Concur o la tarjeta del banco, no es para reemplazarlos: Mendel los integra junto a CFDI y ERP en una sola plataforma, con las capacidades LatAm que los globales no traen|Si ya tienen Concur o la tarjeta del banco, Mendel no los cambia: los conecta junto a CFDI y ERP en un solo lugar, con las capacidades LatAm que los globales no cubren}
```

#### Logistics (objection #1)

```
OBJECTION_DEFUSION: {Si ya usan tarjetas de flotilla del banco, no es para reemplazarlas: Mendel las integra junto a viáticos, CFDIs y ERP, con políticas que las tarjetas tradicionales no aplican|Si ya tienen tarjetas de flotilla del banco, Mendel no las cambia: las conecta junto a viáticos, CFDIs y ERP, con políticas que las tradicionales no soportan}
```

#### Manufacturing (objection #2)

```
OBJECTION_DEFUSION: {Sé que integrar con SAP suena pesado. Por diseño Mendel se conecta nativo a S/4HANA, no se le monta encima|Entiendo que sumar algo encima de SAP suena pesado. Por diseño Mendel se conecta nativo a S/4HANA, no se agrega como capa adicional}
```

#### Pharma (objection #2)

```
OBJECTION_DEFUSION: {Entiendo que sumar un sistema con datos sensibles suena complejo. Mendel se diseñó para escenarios regulados: controles por rol, ERP nativo, audit-ready desde día uno|Sé que un sistema con datos sensibles requiere cuidado. Mendel se construyó para escenarios regulados: controles por rol, ERP nativo y audit-ready desde el inicio}
```

#### Professional Services (objection #3)

```
OBJECTION_DEFUSION: {Sé que el proceso actual funciona. La pregunta es cuántas horas y cuánta deductibilidad se pierden cada mes que ya no vuelven|Entiendo que el flujo actual funciona. El punto es cuántas horas operativas y cuánta deductibilidad se pierden cada cierre y no regresan}
```

(Other A2 industry rendered examples follow the same shape as the Tech example above: same A1 body + the objection paragraph inserted before the social proof line.)

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

### Variable definitions (B)

| Variable | Definition |
|---|---|
| `{{INCUMBENT_DESIGN_LIMIT}}` | Architectural fact about the incumbent stack. Spintax of 2 phrasings. |
| `{{INCUMBENT_QUALIFIER}}` | "Funciona si..." qualifier. Spintax of 2 phrasings. |
| `{{ARCHITECTURAL_SHIFT}}` | Mendel's approach as a shift. Spintax of 2 phrasings. |
| `{{CUSTOMER_LOGOS}}` | Confirmed customer(s). Spintax of 2 phrasings. |
| `{{OUTCOME_SENTENCE}}` | What changes after the shift. Spintax of 2 phrasings. |

### Industry fills (B)

#### Tech / Software

```
vertical: tech
country: México
titlePlural: CFOs

INCUMBENT_DESIGN_LIMIT: {Concur + AMEX se diseñó para reportar gastos después de que pasan|El stack Concur + AMEX se construyó para visibilidad post-cierre, no para control en vivo}

INCUMBENT_QUALIFIER: {Funciona bien si lo que necesitas es visibilidad post-cierre|Bien si lo que se busca es ver el detalle al final del mes}

ARCHITECTURAL_SHIFT: {moviendo el control antes de la transacción: un agente de IA evalúa cada cargo contra política, recupera el CFDI y reconcilia con el ERP en tiempo real|corriendo el control antes del cargo con un agente de IA, recuperación automática de CFDIs y reconciliación al ERP en vivo}

CUSTOMER_LOGOS: {Mercado Libre|operaciones como Mercado Libre}

OUTCOME_SENTENCE: {finanzas pasa de validar tickets a aprobar reportes ya listos|el equipo financiero deja de revisar tickets sueltos y empieza a aprobar reportes armados}
```

**Rendered:**
```
Hola {{firstName}},

Concur + AMEX se diseñó para reportar gastos después de que pasan. Funciona bien si lo que necesitas es visibilidad post-cierre.

Cuando hablo con {{titlePlural}} en tech en México, muchos ya están moviendo el control antes de la transacción: un agente de IA evalúa cada cargo contra política, recupera el CFDI y reconcilia con el ERP en tiempo real.

Eso es lo que corre Mercado Libre hoy, y es por eso que finanzas pasa de validar tickets a aprobar reportes ya listos.

¿Tendría sentido para {{companyName}}?
```

#### Retail & CPG

```
vertical: retail
country: México
titlePlural: CFOs

INCUMBENT_DESIGN_LIMIT: {Concur + la tarjeta del banco se diseñó para reportar después del estado de cuenta|El stack tradicional, Concur más tarjeta del banco, se construyó para reportar al cierre, no para controlar por tienda}

INCUMBENT_QUALIFIER: {Funciona si solo necesitas el report mensual|Bien si lo que se busca es el resumen mensual}

ARCHITECTURAL_SHIFT: {controlando antes de la transacción: política por tienda en el momento del cargo, recuperación automática de CFDIs y reconciliación al ERP en tiempo real|aplicando control antes del cargo: política por tienda, CFDIs recuperados automáticamente y reconciliación con el ERP en vivo}

CUSTOMER_LOGOS: {Walmart y OXXO|cadenas como Walmart y OXXO}

OUTCOME_SENTENCE: {el mes cierra el mismo día, sin hojas paralelas|el cierre baja de varios días a uno, sin trabajo manual paralelo}
```

**Rendered:**
```
Hola {{firstName}},

Concur + la tarjeta del banco se diseñó para reportar después del estado de cuenta. Funciona si solo necesitas el report mensual.

Cuando hablo con {{titlePlural}} de retail en México, muchos ya están controlando antes de la transacción: política por tienda en el momento del cargo, recuperación automática de CFDIs y reconciliación al ERP en tiempo real.

Eso es lo que corren Walmart y OXXO hoy, y es por eso que el mes cierra el mismo día, sin hojas paralelas.

¿Vale la pena revisarlo para {{companyName}}?
```

#### Logistics & Transportation

```
vertical: logística
country: México
titlePlural: CFOs

INCUMBENT_DESIGN_LIMIT: {Las tarjetas de flotilla del banco se diseñaron para pagar combustible|La tarjeta de flotilla bancaria se construyó como medio de pago, no como sistema de control}

INCUMBENT_QUALIFIER: {Visibilidad por conductor y políticas por proveedor no estaban en el alcance original|Reglas por conductor o proveedor no estaban en el diseño original}

ARCHITECTURAL_SHIFT: {moviendo el control al momento del cargo: reglas por conductor, por proveedor y por horario, con CFDIs y per-diems auditados antes del cierre|corriendo el control al momento del cargo con reglas por conductor, proveedor y horario, y CFDIs y per-diems auditados antes del cierre}

CUSTOMER_LOGOS: {Viva Aerobus|operaciones como Viva Aerobus}

OUTCOME_SENTENCE: {la conciliación pasa de manual a automática|la conciliación deja de ser manual y se vuelve automática previa al cierre}
```

**Rendered:**
```
Hola {{firstName}},

Las tarjetas de flotilla del banco se diseñaron para pagar combustible. Visibilidad por conductor y políticas por proveedor no estaban en el alcance original.

Cuando hablo con {{titlePlural}} en logística en México, muchos ya están moviendo el control al momento del cargo: reglas por conductor, por proveedor y por horario, con CFDIs y per-diems auditados antes del cierre.

Eso es lo que corre Viva Aerobus hoy, y es por eso que la conciliación pasa de manual a automática.

¿Te resuena para {{companyName}}?
```

#### Manufacturing & Industrial

```
vertical: manufactura
country: México
titlePlural: CFOs

INCUMBENT_DESIGN_LIMIT: {El stack típico en manufactura, Concur, tarjetas del banco y SAP, se construyó como tres sistemas separados|La realidad típica en manufactura es operar con tres sistemas separados: Concur para reportes, tarjetas para spend, SAP para ERP}

INCUMBENT_QUALIFIER: {Cada integración entre ellos es un punto de falla|Cada handoff entre esos sistemas es un punto de falla}

ARCHITECTURAL_SHIFT: {consolidando: control de políticas multi-planta en tiempo real, recuperación automática de CFDIs entre plantas, y reconciliación nativa contra SAP S/4HANA|unificando los tres flujos en uno: políticas multi-planta en tiempo real, CFDIs recuperados entre plantas y reconciliación nativa con SAP S/4HANA}

CUSTOMER_LOGOS: {AB InBev|operaciones como AB InBev}

OUTCOME_SENTENCE: {el cierre deja de depender de ajustes manuales por planta|el equipo financiero deja de armar ajustes por planta y empieza a aprobar lo que SAP ya recibió validado}
```

**Rendered:**
```
Hola {{firstName}},

El stack típico en manufactura, Concur, tarjetas del banco y SAP, se construyó como tres sistemas separados. Cada integración entre ellos es un punto de falla.

Cuando hablo con {{titlePlural}} de manufactura en México, muchos ya están consolidando: control de políticas multi-planta en tiempo real, recuperación automática de CFDIs entre plantas, y reconciliación nativa contra SAP S/4HANA.

Eso es lo que corre AB InBev hoy, y es por eso que el cierre deja de depender de ajustes manuales por planta.

¿Tendría sentido para {{companyName}}?
```

#### Pharmaceutical & Healthcare

⚠️ no confirmed pharma logo — verify with Alan

```
vertical: farma
country: México
titlePlural: CFOs

INCUMBENT_DESIGN_LIMIT: {Las herramientas tradicionales de expense management no se diseñaron pensando en compliance farma|Los sistemas tradicionales de expense management no se construyeron con compliance farma en mente}

INCUMBENT_QUALIFIER: {Trazabilidad por HCP y reporte de transparencia terminan siendo proyectos manuales mensuales|La trazabilidad por HCP y el reporte de transparencia terminan armándose a mano cada mes}

ARCHITECTURAL_SHIFT: {moviendo esa trazabilidad al momento del cargo: política por representante, auditoría en tiempo real, reporte de transparencia listo para exportar|corriendo la trazabilidad al momento del cargo con política por representante, auditoría continua y reporte de transparencia listo para exportar}

CUSTOMER_LOGOS: {operaciones farma con fuerza distribuida|equipos farma con fuerza de ventas activa}

OUTCOME_SENTENCE: {el reporte deja de armarse a mano|el equipo deja de construir el reporte de transparencia cada mes}
```

**Rendered:**
```
Hola {{firstName}},

Las herramientas tradicionales de expense management no se diseñaron pensando en compliance farma. Trazabilidad por HCP y reporte de transparencia terminan siendo proyectos manuales mensuales.

Cuando hablo con {{titlePlural}} de farma en México, muchos ya están moviendo esa trazabilidad al momento del cargo: política por representante, auditoría en tiempo real, reporte de transparencia listo para exportar.

Eso es lo que corren operaciones farma con fuerza distribuida hoy, y es por eso que el reporte deja de armarse a mano.

¿Te resuena para {{companyName}}?
```

#### Professional Services

```
vertical: servicios profesionales
country: LatAm
titlePlural: CFOs

INCUMBENT_DESIGN_LIMIT: {Capturar gasto billable por engagement nunca fue para lo que se diseñó Concur|Concur no se diseñó para capturar gasto billable por engagement}

INCUMBENT_QUALIFIER: {Tampoco soporta CFDI ni operación multi-país de forma nativa|Tampoco fue construido con CFDI o operación multi-país en mente}

ARCHITECTURAL_SHIFT: {consolidando: gasto billable capturado en el momento del cargo, multi-país, con CFDI integrado y reconciliación directa al ERP|unificando: gasto billable por engagement en el momento del cargo, multi-país, con CFDI y ERP integrados}

CUSTOMER_LOGOS: {KPMG|firmas como KPMG}

OUTCOME_SENTENCE: {los partners aprueban desde el móvil y los reembolsos manuales desaparecen|los partners firman desde el móvil y la cola de reembolsos manuales se acaba}
```

**Rendered:**
```
Hola {{firstName}},

Capturar gasto billable por engagement nunca fue para lo que se diseñó Concur. Tampoco soporta CFDI ni operación multi-país de forma nativa.

Cuando hablo con {{titlePlural}} de servicios profesionales en LatAm, muchos ya están consolidando: gasto billable capturado en el momento del cargo, multi-país, con CFDI integrado y reconciliación directa al ERP.

Eso es lo que corre KPMG hoy, y es por eso que los partners aprueban desde el móvil y los reembolsos manuales desaparecen.

¿Vale la pena revisarlo para {{companyName}}?
```

---

## VARIANT C — Ultra-short peer-pattern

### Master template

```
{Hola|Hey|Buenas} {{firstName}},

{Cuando hablo|Cuando converso} con {{titlePlural}} {de|en} {{vertical}} en {{country}}, {casi todos|la mayoría|muchos} {describen|cuentan|comparten} {el mismo patrón|lo mismo|el mismo dolor}: {{INDUSTRY_PAIN}}.

Mendel {{SOLUTION_VERB_PHRASE_SHORT}}.

Es lo que {corre|corren} {{CUSTOMER_LOGOS}} hoy.

¿{Tendría sentido|Te resuena|Es algo que valga la pena} para {{companyName}}?
```

### Variable definitions (C)

| Variable | Definition |
|---|---|
| `{{INDUSTRY_PAIN}}` | Same library as A1 (spintax of 2). |
| `{{SOLUTION_VERB_PHRASE_SHORT}}` | Mendel's action as present-tense verb + capabilities (compressed for C). Spintax of 2. |
| `{{CUSTOMER_LOGOS}}` | Same library as A1 (spintax of 2). |

### Industry fills (C) — SOLUTION_VERB_PHRASE_SHORT only

INDUSTRY_PAIN and CUSTOMER_LOGOS reuse Variant A1's spintax libraries.

#### Tech

```
SOLUTION_VERB_PHRASE_SHORT: {automatiza ese control con un agente de IA antes del cargo: política en tiempo real, CFDIs recuperados y ERP reconciliado|corre auditoría IA por transacción, recupera CFDIs y reconcilia con ERP en tiempo real}
```

**Rendered:**
```
Hola {{firstName}},

Cuando hablo con {{titlePlural}} en tech en México, casi todos describen el mismo patrón: tech escala antes que finanzas, y los gastos terminan revisándose semanas después.

Mendel automatiza ese control con un agente de IA antes del cargo: política en tiempo real, CFDIs recuperados y ERP reconciliado.

Es lo que corre Mercado Libre hoy.

¿Tendría sentido para {{companyName}}?
```

#### Retail

```
SOLUTION_VERB_PHRASE_SHORT: {aplica política por tienda en cada cargo, recupera los CFDIs automáticamente y reconcilia con el ERP en tiempo real|corre política por tienda en cada cargo, con CFDIs recuperados y ERP reconciliado al instante}
```

#### Logistics

```
SOLUTION_VERB_PHRASE_SHORT: {aplica reglas por conductor, proveedor y horario en el momento del cargo, con CFDIs integrados al ERP|corre reglas por conductor, proveedor y horario en cada cargo, con CFDIs y per-diems auditados antes del cierre}
```

#### Manufacturing

```
SOLUTION_VERB_PHRASE_SHORT: {consolida políticas multi-planta, recupera CFDIs entre plantas y se conecta nativo a SAP S/4HANA|unifica políticas multi-planta con recuperación de CFDIs entre plantas y reconciliación nativa con SAP S/4HANA}
```

#### Pharma

```
SOLUTION_VERB_PHRASE_SHORT: {aplica política por representante, audita en tiempo real y deja el reporte listo para exportar|corre política por representante, auditoría continua y reporte de transparencia listo para exportar}
```

#### Professional Services

```
SOLUTION_VERB_PHRASE_SHORT: {captura cada gasto billable por engagement en el momento del cargo, multi-país, con CFDI y reconciliación al ERP|corre captura de gasto billable por engagement, multi-país, con CFDI integrado al ERP}
```

(Other industries' rendered examples follow the Tech shape: greeting + peer-framed opener + 3-beat capability sentence + customer line + soft CTA. Combine the SOLUTION_VERB_PHRASE_SHORT here with A1's INDUSTRY_PAIN and CUSTOMER_LOGOS to render.)

---

# EMAIL 2 — Lead magnet (benchmark walkthrough)

**Goal:** trigger an engagement reply ("sí, me interesa") that the sender converts into a 20-min walkthrough call. Meeting booking happens in the reply, never in the cold body.

**Thread:** same thread as Email 1 (subject inherited via EmailBison headers). No new subject line needed.

## Master template

```
{Hola|Hey|Buenas} {{firstName}},

{Armamos|Construimos|Preparamos|Hicimos} un benchmark de cómo {{titlePlural}} {de|en} {{vertical}} en {{country}} {{PEER_ACTIVITIES}}. {Datos reales|Datos crudos|Información real}, anónimos.

{Puedo mostrarte|Te puedo enseñar|Te puedo compartir} qué {hacen|están haciendo} {{CUSTOMER_LOGOS}} y cómo se {puede aplicar|aplicaría|traduce} al setup de {{companyName}}, sin pitch.

{{CTA}}
```

## Variable definitions

| Variable | Type | Definition |
|---|---|---|
| `{{firstName}}` | merge | Lead first name |
| `{{companyName}}` | merge | Lead company |
| `{{titlePlural}}` | campaign-level | Persona plural (`CFOs`) |
| `{{vertical}}` | campaign-level | Industry word |
| `{{country}}` | campaign-level | Geography |
| `{{PEER_ACTIVITIES}}` | industry-specific | What peers do (spintax of 2) |
| `{{CUSTOMER_LOGOS}}` | industry-specific | Named Mendel customers (spintax of 2) |
| `{{CTA}}` | A/B variant | One of two CTA variants |

## CTA — two variants for A/B testing

| Variant | Spintaxed CTA | Tone |
|---|---|---|
| **CTA-A — Engagement probe** | `¿Te {interesaría|sería útil|haría sentido}?` | Softer, value-first |
| **CTA-B — Time choice** | `¿{Te funciona|Te queda|Te va} esta semana o la próxima?` | Direct, agenda-driving |

## Industry fills (Email 2)

#### Tech / Software

```
vertical: tech
country: México
titlePlural: CFOs

PEER_ACTIVITIES: {están automatizando auditoría con agentes IA, recuperando CFDIs y reconciliando con ERP en tiempo real|están moviendo el control de gastos a tiempo real con IA: auditoría por transacción, CFDIs recuperados y ERP reconciliado}

CUSTOMER_LOGOS: {Mercado Libre y AB InBev|operaciones como Mercado Libre y AB InBev}
```

**Rendered (CTA-A):**
```
Hola {{firstName}},

Armamos un benchmark de cómo {{titlePlural}} en tech en México están automatizando auditoría con agentes IA, recuperando CFDIs y reconciliando con ERP en tiempo real. Datos reales, anónimos.

Puedo mostrarte qué hacen Mercado Libre y AB InBev y cómo se puede aplicar al setup de {{companyName}}, sin pitch.

¿Te interesaría?
```

**Rendered (CTA-B):**
```
Hola {{firstName}},

Armamos un benchmark de cómo {{titlePlural}} en tech en México están automatizando auditoría con agentes IA, recuperando CFDIs y reconciliando con ERP en tiempo real. Datos reales, anónimos.

Puedo mostrarte qué hacen Mercado Libre y AB InBev y cómo se puede aplicar al setup de {{companyName}}, sin pitch.

¿Te funciona esta semana o la próxima?
```

#### Retail & CPG

```
vertical: retail
country: México
titlePlural: CFOs

PEER_ACTIVITIES: {están aplicando políticas por punto de venta, recuperando CFDIs automáticamente y cerrando el mes el mismo día|están controlando spend por tienda en cada cargo, recuperando CFDIs en vivo y cerrando el mes al instante}

CUSTOMER_LOGOS: {Walmart y OXXO|cadenas como Walmart y OXXO}
```

**Rendered (CTA-A):**
```
Hey {{firstName}},

Armamos un benchmark de cómo {{titlePlural}} de retail en México están aplicando políticas por punto de venta, recuperando CFDIs automáticamente y cerrando el mes el mismo día. Datos reales, anónimos.

Puedo mostrarte qué hacen Walmart y OXXO y cómo se puede aplicar al setup de {{companyName}}, sin pitch.

¿Te sería útil?
```

#### Logistics & Transportation

```
vertical: logística
country: México
titlePlural: CFOs

PEER_ACTIVITIES: {están aplicando reglas por conductor y proveedor, con CFDIs y per-diems auditados antes del cierre|están corriendo control en cada cargo de flotilla por conductor, proveedor y horario, con CFDIs y per-diems auditados antes del cierre}

CUSTOMER_LOGOS: {Viva Aerobus|operaciones como Viva Aerobus}
```

**Rendered (CTA-A):**
```
Buenas {{firstName}},

Armamos un benchmark de cómo {{titlePlural}} en logística en México están aplicando reglas por conductor y proveedor, con CFDIs y per-diems auditados antes del cierre. Datos reales, anónimos.

Puedo mostrarte qué hace Viva Aerobus y cómo se puede aplicar al setup de {{companyName}}, sin pitch.

¿Te haría sentido?
```

#### Manufacturing & Industrial

```
vertical: manufactura
country: México
titlePlural: CFOs

PEER_ACTIVITIES: {están consolidando spend multi-planta con recuperación de CFDIs y reconciliación nativa a SAP S/4HANA|están unificando spend entre plantas con políticas en tiempo real, CFDIs recuperados y reconciliación nativa con SAP S/4HANA}

CUSTOMER_LOGOS: {AB InBev|operaciones como AB InBev}
```

**Rendered (CTA-A):**
```
Hola {{firstName}},

Armamos un benchmark de cómo {{titlePlural}} de manufactura en México están consolidando spend multi-planta con recuperación de CFDIs y reconciliación nativa a SAP S/4HANA. Datos reales, anónimos.

Puedo mostrarte qué hace AB InBev y cómo se puede aplicar al setup de {{companyName}}, sin pitch.

¿Te interesaría?
```

#### Pharmaceutical & Healthcare

⚠️ no confirmed pharma logo — verify with Alan

```
vertical: farma
country: México
titlePlural: CFOs

PEER_ACTIVITIES: {están aplicando política por representante, auditando en tiempo real y dejando el reporte de transparencia listo para exportar|están corriendo política por representante en cada cargo, con auditoría continua y reporte de transparencia listo para exportar}

CUSTOMER_LOGOS: {operaciones farma con fuerza distribuida|equipos farma con fuerza de ventas activa}
```

**Rendered (CTA-A):**
```
Hey {{firstName}},

Armamos un benchmark de cómo {{titlePlural}} de farma en México están aplicando política por representante, auditando en tiempo real y dejando el reporte de transparencia listo para exportar. Datos reales, anónimos.

Puedo mostrarte qué hacen operaciones farma con fuerza distribuida y cómo se puede aplicar al setup de {{companyName}}, sin pitch.

¿Te sería útil?
```

#### Professional Services

```
vertical: servicios profesionales
country: LatAm
titlePlural: CFOs

PEER_ACTIVITIES: {están capturando gasto billable por engagement, multi-país, con CFDI integrado al ERP|están corriendo gasto billable por engagement en el momento del cargo, multi-país, con CFDI y ERP integrados}

CUSTOMER_LOGOS: {KPMG|firmas como KPMG}
```

**Rendered (CTA-A):**
```
Hola {{firstName}},

Armamos un benchmark de cómo {{titlePlural}} de servicios profesionales en LatAm están capturando gasto billable por engagement, multi-país, con CFDI integrado al ERP. Datos reales, anónimos.

Puedo mostrarte qué hace KPMG y cómo se puede aplicar al setup de {{companyName}}, sin pitch.

¿Te haría sentido?
```

## Reply handling for Email 2

| Reply | Sender response |
|---|---|
| "Sí, me interesa" / "Sí, mándalo" | `Perfecto, lo más útil es repasarlo en 20 min. ¿Te queda jueves o viernes esta semana?` — book the meeting in the reply, never in the cold body. |
| "Mándame el PDF mejor" | `No tenemos PDF aparte porque depende del contexto. Si te queda 20 min te lo paso aplicado a {{companyName}}.` Push back to meeting once. |
| "No me interesa" | Polite acknowledgment, move to long-term nurture. |
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

Used in Email 1 (any variant) and as alternatives for Email 2 CTA-A.

| CTA | Tone | Use case |
|---|---|---|
| `¿Tendría sentido para {{companyName}}?` | Neutral, polite | Default |
| `¿Es algo que valga la pena revisar para {{companyName}}?` | Slightly more formal | Senior CFO targets |
| `¿Te resuena para {{companyName}}?` | Casual, conversational | Younger or modern operations |
| `¿Te interesa ver cómo aplicaría a {{companyName}}?` | Action-oriented | When ready to demo |
| `¿Vale la pena profundizar en esto?` | Open-ended | Strategic conversations |
| `¿Vale revisarlo aplicado a {{companyName}}?` | Direct, soft | Default for Variant A1/A2 |
| `¿Tiene sentido verlo aplicado a {{companyName}}?` | Neutral | Variant A1/A2 alternate |
| `¿Hace sentido echarle un ojo para {{companyName}}?` | Casual Mexican | Variant A1/A2 alternate |

## Objection defusion library (Variant A2 only)

| # | Trigger | Template |
|---|---|---|
| 1 | Existing stack (Concur, AMEX, bank cards, fleet cards) | `Si ya operan con [stack], Mendel no [los/las] reemplaza: integra [things] en un solo lugar, con capacidades LatAm que [esos tools / los globales] no traen.` |
| 2 | Implementation complexity (SAP, ERP, multi-country, compliance) | `Sé que [implementing X] suena pesado. Por diseño Mendel se conecta nativo a [SAP / ERP], no se le agrega encima.` |
| 3 | Current process works well enough | `Sé que el proceso actual funciona. La pregunta es cuántas horas y cuánta deductibilidad se pierden cada mes que ya no vuelven.` |

| Industry | Default objection used in Variant A2 |
|---|---|
| Tech | #1 |
| Retail | #1 |
| Logistics | #1 |
| Manufacturing | #2 |
| Pharma | #2 |
| Professional Services | #3 |

---

# Spintax reference

Spintax format: `{option1|option2|option3}`. Two layers exist in this library:

1. **Static spintax in master templates** — connector words, greetings, verbs of speech.
2. **Industry-variable spintax in fill tables** — each per-industry variable has 2 phrasings of the same idea.

Both get resolved by EmailBison at send time. Each layer is independent.

**Allowed in spintax (Layer 1, master templates):**
- Greetings: `{Hola|Hey|Buenas}`
- Conversation verbs: `{Platicando|Hablando|Conversando}`, `{Cuando hablo|Cuando converso|En las conversaciones}`
- Quantifiers: `{todos|casi todos|la mayoría|muchos|varios}`
- Verbs of speech: `{cuentan|describen|comparten}`
- Pattern descriptors: `{el mismo patrón|el mismo cuadro|el mismo dolor|lo mismo}`
- Prepositions: `{de|en}`
- State verbs: `{están|están moviendo|están migrando hacia}`
- Operation verbs: `{corre|opera|funciona en}`, `{usan|usa}`, `{hoy|actualmente}`
- Email-2 build verbs: `{Armamos|Construimos|Preparamos|Hicimos}`
- Email-2 share verbs: `{Puedo mostrarte|Te puedo enseñar|Te puedo compartir}`, `{hacen|están haciendo}`, `{puede aplicar|aplicaría|traduce}`
- Email-2 data descriptors: `{Datos reales|Datos crudos|Información real}`
- CTA verbs: `{Vale|Tiene sentido|Hace sentido|Tendría sentido|Te resuena}`, `{revisarlo|verlo|echalle un ojo}`, `{interesaría|sería útil|haría sentido}`, `{Te funciona|Te queda|Te va}`

**Layer 2 — variable-level spintax:** every per-industry variable value (`{{INDUSTRY_PAIN}}`, `{{SOLUTION_VERB_PHRASE}}`, `{{OUTCOME_SENTENCE}}`, `{{OBJECTION_DEFUSION}}`, `{{CUSTOMER_LOGOS}}`, `{{INCUMBENT_DESIGN_LIMIT}}`, `{{INCUMBENT_QUALIFIER}}`, `{{ARCHITECTURAL_SHIFT}}`, `{{PEER_ACTIVITIES}}`) holds 2 phrasings using the same `{a|b}` syntax. EmailBison resolves these independently per send.

**Never spintax:**
- Merge variables (`{{firstName}}`, `{{companyName}}`, `{{titlePlural}}`, `{{vertical}}`, `{{country}}`)
- Customer / brand names inside the spintax options (Mercado Libre, KPMG, AB InBev, Walmart, OXXO, Viva Aerobus, Mendel, Concur, AMEX, SAP, S/4HANA, ERP, CFDI, SAT, HCP)

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
