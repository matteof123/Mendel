# Mendel — Email Sequence Library

_Language: Spanish (Mexico priority, "tú" form). Professional Services uses LatAm framing._

## Overview

Email sequence for Mendel's cold outbound. Each email has:
1. A **master template** with static phrases containing spintax `{a|b|c}` and clearly marked variable slots `{{VARIABLE_NAME}}`.
2. A **variable definition list** explaining what each slot represents.
3. **Per-industry variable fills** — each per-industry variable also contains spintax `{a|b}` so values vary per send.
4. **Per-industry rendered examples** — spintax resolved to one option per slot, variables filled.

### Strict rules

- Anything that varies per industry → variable (`{{vertical}}`, `{{country}}`, `{{INDUSTRY_PAIN}}`, etc.).
- Anything static within a variant → spintax in the master template.
- Per-industry variable values also have spintax — they hold 2+ phrasings of the same idea so each send picks one.
- Rendered examples show one resolved option per slot; merge variables stay as merge tags.

### Universal principles

- Peer-framed openers (no accusation of prospect's company).
- Value-probing CTAs (no cold "15 minutes" asks in the body).
- Customer logos as social proof.
- Topic-led subject lines personalized via `{{firstName}}` / `{{companyName}}`.
- Tone: expert, professional, straightforward, calm. Not casual, not playful.
- Mexican-CFO vernacular where natural: "perseguir tickets", "se nos van facturas", "esto lo hacemos en Excel".
- Hard rules: no em dashes, no exclamation marks, no currency words, no signature in body, no bracket placeholders, one question per email.

## Universal merge variables

| Variable | Example | Source |
|---|---|---|
| `{{firstName}}` | Carlos | Lead enrichment |
| `{{companyName}}` | Soriana | Lead enrichment |
| `{{titlePlural}}` | CFOs | Persona plural — set per campaign |
| `{{vertical}}` | operaciones tech | Industry word — set per campaign |
| `{{country}}` | México | Geography — set per campaign |

Sender name and tagline handled by EmailBison `{SENDER_EMAIL_SIGNATURE}`. Never put a sender name or sign-off in the body.

## Customer name index

| Customer | Used in |
|---|---|
| Mercado Libre | Tech-enabled operations |
| FEMSA | Tech-enabled operations, Retail & CPG |
| AB InBev | Tech-enabled operations, Manufacturing |
| Walmart | Retail & CPG |
| OXXO | Retail & CPG |
| McDonald's | Retail & CPG (QSR) |
| Tim Hortons | Retail & CPG (QSR) |
| PetCo | Retail & CPG (specialty) |
| Viva Aerobus | Logistics & Transportation |
| Grupo Bafar | Manufacturing & Industrial |
| Farmacia San Pablo | Pharmaceutical & Healthcare |
| Merck | Pharmaceutical & Healthcare |
| KPMG | Professional Services, Travel & Mobility |

## Adjacent persona library (`{{titlePlural}}` options)

| Vertical | Primary | Alternates |
|---|---|---|
| Tech-enabled operations | CFOs | Controllers, Finance Directors |
| Retail & CPG | CFOs | Controllers, Procurement Directors |
| Logistics & Transportation | CFOs | Operations Directors, Fleet Managers |
| Manufacturing & Industrial | CFOs | Controllers, Procurement Directors |
| Pharmaceutical & Healthcare | CFOs | Tax Managers, Compliance Directors |
| Professional Services | CFOs | Operations Directors |
| Travel & Mobility | Travel Managers | Event Managers, Mobility Directors |

## Sequence overview

| Email | Variants | Goal | Thread |
|---|---|---|---|
| **Email 1** | A1, A2, B, C | Plant problem + solution + soft ask for relevance | New thread |
| **Email 2** | Single template, CTA A/B/C | Trigger engagement reply → 20-min walkthrough or pilot | Same thread as Email 1 |

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
Hola {{firstName}},

{Platicando|Hablando|Conversando} con {{titlePlural}} {de|en} {{vertical}} en {{country}}, {casi todos|todos|la mayoría} {cuentan|describen|comparten} {lo mismo|el mismo patrón|el mismo cuadro|el mismo dolor}: {{INDUSTRY_PAIN}}.

Mendel resuelve eso {{SOLUTION_VERB_PHRASE}}. {{OUTCOME_SENTENCE}}.

Es la misma arquitectura que {usan|usa} {{CUSTOMER_LOGOS}} hoy.

¿{Vale|Tiene sentido|Hace sentido} {revisarlo|verlo|echarle un ojo} aplicado a {{companyName}}?
```

### Variable definitions (A1)

| Variable | Definition |
|---|---|
| `{{INDUSTRY_PAIN}}` | Industry-specific pain stated as peer observation. Spintax of 2. |
| `{{SOLUTION_VERB_PHRASE}}` | Mendel's action as gerund + capabilities. Spintax of 2. |
| `{{OUTCOME_SENTENCE}}` | What the team gets after Mendel. Spintax of 2. |
| `{{CUSTOMER_LOGOS}}` | Customer(s) for the industry. Spintax of 2. |

### Industry fills (A1)

#### Tech-enabled operations

```
vertical: operaciones tech
country: México
titlePlural: CFOs

INDUSTRY_PAIN: {operaciones tech mueven volumen alto de transacciones que finanzas no alcanza a auditar en tiempo real, y el cierre depende de revisar tickets sueltos|el área de operaciones genera transacciones a velocidad de software, y finanzas todavía persigue tickets a velocidad manual}

SOLUTION_VERB_PHRASE: {poniendo un agente de IA que audita cada transacción contra política antes del cargo|con un agente de IA que evalúa cada cargo contra política en el momento, no después}

OUTCOME_SENTENCE: {Lo que llega a finanzas son reportes ya listos, no tickets sueltos, y el ERP queda reconciliado en tiempo real|Mercado Libre subió 30% la recuperación de facturas deductibles con esta arquitectura, después de reemplazar SAP Concur}

CUSTOMER_LOGOS: {Mercado Libre y AB InBev|Mercado Libre y FEMSA}
```

**Rendered:**
```
Hola {{firstName}},

Platicando con {{titlePlural}} en operaciones tech en México, casi todos cuentan lo mismo: operaciones tech mueven volumen alto de transacciones que finanzas no alcanza a auditar en tiempo real, y el cierre depende de revisar tickets sueltos.

Mendel resuelve eso poniendo un agente de IA que audita cada transacción contra política antes del cargo. Mercado Libre subió 30% la recuperación de facturas deductibles con esta arquitectura, después de reemplazar SAP Concur.

Es la misma arquitectura que usan Mercado Libre y AB InBev hoy.

¿Vale revisarlo aplicado a {{companyName}}?
```

#### Retail & CPG

```
vertical: retail
country: México
titlePlural: CFOs

INDUSTRY_PAIN: {con cientos de tiendas y miles de CFDIs al mes, el cierre del banco llega antes que el cierre interno|cada tienda mueve volumen propio, se nos van facturas al cierre y el equipo termina perseguiendo tickets uno por uno}

SOLUTION_VERB_PHRASE: {aplicando políticas por tienda en el momento del cargo, recuperando los CFDIs automáticamente y mandándolos al ERP ya validados|con política por tienda evaluada en cada cargo, CFDIs recuperados automáticamente y reconciliación al ERP en tiempo real}

OUTCOME_SENTENCE: {El equipo cierra el mes el mismo día, sin hojas paralelas y sin perseguir tickets|El cierre mensual pasa de varios días a uno, con dashboard en tiempo real del spend por tienda}

CUSTOMER_LOGOS: {Walmart, OXXO y FEMSA|cadenas como Walmart, OXXO y McDonald's}
```

**Rendered:**
```
Hola {{firstName}},

Hablando con {{titlePlural}} de retail en México, casi todos cuentan lo mismo: cada tienda mueve volumen propio, se nos van facturas al cierre y el equipo termina perseguiendo tickets uno por uno.

Mendel resuelve eso aplicando políticas por tienda en el momento del cargo, recuperando los CFDIs automáticamente y mandándolos al ERP ya validados. El equipo cierra el mes el mismo día, sin hojas paralelas y sin perseguir tickets.

Es la misma arquitectura que usan Walmart, OXXO y FEMSA hoy.

¿Tiene sentido verlo aplicado a {{companyName}}?
```

#### Logistics & Transportation

```
vertical: logística
country: México
titlePlural: CFOs

INDUSTRY_PAIN: {tarjetas de flotilla, casetas, combustible y viáticos repartidos entre conductores, sin visibilidad hasta el cierre del mes|el spend de flota vive entre el banco, los conductores y los proveedores, sin película completa hasta fin de mes}

SOLUTION_VERB_PHRASE: {con reglas que se aplican en el momento del cargo: por conductor, por proveedor y por horario|aplicando reglas en cada cargo por conductor, proveedor y horario, antes de que el gasto cierre el ciclo}

OUTCOME_SENTENCE: {Combustible y per-diems quedan auditados antes de la conciliación, no después|La conciliación pasa de manual y posterior al cierre a automática y previa al cargo, sin perseguir tickets entre conductores}

CUSTOMER_LOGOS: {Viva Aerobus|operaciones tipo Viva Aerobus}
```

**Rendered:**
```
Hola {{firstName}},

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

INDUSTRY_PAIN: {spend operativo disperso entre plantas, reconciliación manual contra SAP, y deductibilidad que se pierde por CFDIs que nunca llegan|operaciones multi-entidad o multi-planta generan spend disperso entre subsidiarias, con reconciliación manual contra SAP o Contpaqi en cada cierre}

SOLUTION_VERB_PHRASE: {con control de políticas multi-planta en tiempo real, recuperación automática de CFDIs entre plantas y reconciliación directa contra SAP S/4HANA|aplicando políticas multi-entidad en tiempo real, recuperando CFDIs entre plantas y reconciliando nativamente contra SAP, Contpaqi u Oracle}

OUTCOME_SENTENCE: {El cierre deja de depender de ajustes manuales por planta|La conciliación entre plantas y ERP pasa de manual a automática, sin retrabajo al cierre}

CUSTOMER_LOGOS: {AB InBev y Grupo Bafar|operaciones multi-planta tipo AB InBev}
```

**Rendered:**
```
Hola {{firstName}},

Platicando con {{titlePlural}} de manufactura en México, todos describen el mismo patrón: operaciones multi-entidad o multi-planta generan spend disperso entre subsidiarias, con reconciliación manual contra SAP o Contpaqi en cada cierre.

Mendel resuelve eso aplicando políticas multi-entidad en tiempo real, recuperando CFDIs entre plantas y reconciliando nativamente contra SAP, Contpaqi u Oracle. La conciliación entre plantas y ERP pasa de manual a automática, sin retrabajo al cierre.

Es la misma arquitectura que usan AB InBev y Grupo Bafar hoy.

¿Vale revisarlo aplicado a {{companyName}}?
```

#### Pharmaceutical & Healthcare

```
vertical: farma
country: México
titlePlural: CFOs

INDUSTRY_PAIN: {las tarjetas de la fuerza de ventas, los viáticos con HCPs y los reembolsos necesitan trazabilidad completa, y armar el reporte de transparencia se vuelve un proyecto mensual|la fuerza de ventas con HCPs genera transacciones que necesitan trazabilidad para transparencia, y armar el reporte mensual consume días del equipo}

SOLUTION_VERB_PHRASE: {aplicando política por representante en cada cargo y dejando la auditoría corriendo en tiempo real|con política por representante evaluada en cada cargo y auditoría continua en tiempo real}

OUTCOME_SENTENCE: {El reporte de transparencia sale listo para exportar, sin armarlo a mano|La transparencia deja de ser un proyecto mensual y se convierte en un export listo para auditoría SAT}

CUSTOMER_LOGOS: {Farmacia San Pablo y Merck|Farmacia San Pablo}
```

**Rendered:**
```
Hola {{firstName}},

Hablando con {{titlePlural}} de farma en México, casi todos cuentan el mismo dolor: las tarjetas de la fuerza de ventas, los viáticos con HCPs y los reembolsos necesitan trazabilidad completa, y armar el reporte de transparencia se vuelve un proyecto mensual.

Mendel resuelve eso aplicando política por representante en cada cargo y dejando la auditoría corriendo en tiempo real. El reporte de transparencia sale listo para exportar, sin armarlo a mano.

Es la misma arquitectura que usan Farmacia San Pablo y Merck hoy.

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

CUSTOMER_LOGOS: {KPMG|firmas multi-país como KPMG}
```

**Rendered:**
```
Hola {{firstName}},

Conversando con {{titlePlural}} de servicios profesionales en LatAm, la mayoría cuenta el mismo dolor: viaje de partners, gastos billables por cliente y operación multi-país, gestionado entre tarjetas, hojas y reembolsos manuales.

Mendel resuelve eso capturando cada gasto billable por engagement desde el momento del cargo, con CFDI integrado y reconciliación directa al ERP. Los partners aprueban desde el móvil y los reembolsos manuales desaparecen.

Es la misma arquitectura que usa KPMG hoy.

¿Vale revisarlo aplicado a {{companyName}}?
```

#### Travel & Mobility (Corporate Travel & Events)

```
vertical: viajes corporativos
country: México
titlePlural: Travel Managers

INDUSTRY_PAIN: {viajes corporativos repartidos entre TMC, aprobaciones por mail y reembolsos manuales, sin política aplicada al momento del booking|el booking de viajes vive entre TMC, mail y Excel, y los gastos derivados llegan al cierre sin trazabilidad}

SOLUTION_VERB_PHRASE: {con Mendel Viajes: booking, política, aprobaciones y gasto integrados en una sola plataforma|consolidando booking, política, aprobaciones y reembolsos en un solo flujo, con adopción online u offline visible en tiempo real}

OUTCOME_SENTENCE: {Los viajeros reservan dentro de política sin chasear aprobaciones, y los gastos derivados llegan limpios al ERP|Travel Managers dejan de revisar bookings uno por uno y empiezan a ver el portafolio completo en tiempo real}

CUSTOMER_LOGOS: {KPMG|firmas multi-país como KPMG}
```

**Rendered:**
```
Hola {{firstName}},

Hablando con {{titlePlural}} de viajes corporativos en México, casi todos cuentan lo mismo: viajes corporativos repartidos entre TMC, aprobaciones por mail y reembolsos manuales, sin política aplicada al momento del booking.

Mendel resuelve eso con Mendel Viajes: booking, política, aprobaciones y gasto integrados en una sola plataforma. Los viajeros reservan dentro de política sin chasear aprobaciones, y los gastos derivados llegan limpios al ERP.

Es la misma arquitectura que usa KPMG hoy.

¿Tiene sentido verlo aplicado a {{companyName}}?
```

---

## VARIANT A2 — Peer-framed with objection defusion

Same as A1, plus one paragraph: `{{OBJECTION_DEFUSION}}` between the outcome and the social proof.

### Master template

```
Hola {{firstName}},

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
| `{{OBJECTION_DEFUSION}}` | Acknowledgment of likely objection + Mendel's specific counter. Spintax of 2. Industry picks #1-6 from the library. |

### Industry fills (A2) — OBJECTION_DEFUSION values

#### Tech-enabled operations (objection #1 — existing stack)

```
OBJECTION_DEFUSION: {Si ya operan con Concur + AMEX no es para reemplazarlos: Mendel los integra junto a CFDI y ERP en una sola plataforma, con las capacidades LatAm que esos tools no traen|Si la directiva global usa Concur, Mendel empuja los datos al sistema global y suma la tropicalización México que el global no cubre — recuperación de CFDI, SAT y políticas en tiempo real}
```

#### Retail & CPG (objection #4 — free bank cards)

```
OBJECTION_DEFUSION: {Sé que el banco te da tarjetas sin cargo extra. La diferencia no son las tarjetas, es la capa de software encima: política preventiva, recuperación de CFDIs y reconciliación con el ERP|Las tarjetas del banco están bien para pagar. Mendel se monta encima con la capa de software que el banco no tiene: control antes del cargo, recuperación de CFDI y reporte en tiempo real}
```

#### Logistics (objection #6 — driver/operator adoption)

```
OBJECTION_DEFUSION: {El miedo común es que los choferes no usen otra app. La acción del conductor se reduce a sacar foto al ticket — Mendel hace el resto: recuperación de CFDI, validación SAT y reconciliación con ERP|Adopción de conductores es la duda típica. Mendel reduce su parte a una foto del ticket; el resto corre en automático en el back-office}
```

#### Manufacturing (objection #2 — implementation / SAP)

```
OBJECTION_DEFUSION: {Sé que integrar con SAP suena pesado. La implementación va con acompañamiento end-to-end del equipo Mendel, no es un proyecto IT pesado del lado tuyo. Por diseño se conecta nativo a S/4HANA|Entiendo que sumar algo encima de SAP suena pesado. Por diseño Mendel se conecta nativo a S/4HANA, no se agrega como capa adicional, y el rollout va con acompañamiento white-glove}
```

#### Pharma (objection #2 — implementation / compliance)

```
OBJECTION_DEFUSION: {Entiendo que sumar un sistema con datos sensibles suena complejo. Mendel se diseñó para escenarios regulados: controles por rol, ERP nativo, audit-ready desde día uno, y la implementación corre con acompañamiento end-to-end|Sé que un sistema con datos sensibles requiere cuidado. Mendel se construyó para escenarios regulados — controles por rol, ERP nativo, audit-ready desde el inicio — y la implementación va con white-glove del equipo Mendel}
```

#### Professional Services (objection #3 — current process works)

```
OBJECTION_DEFUSION: {Sé que el proceso actual funciona. La pregunta es cuántas horas y cuánta deductibilidad se pierden cada mes que ya no vuelven|Entiendo que el flujo actual funciona. El punto es cuántas horas operativas y cuánta deductibilidad se pierden cada cierre y no regresan}
```

#### Travel & Mobility (objection #1 — existing TMC)

```
OBJECTION_DEFUSION: {Si ya usan un TMC, no es para reemplazarlo: Mendel Viajes lo conecta junto a política, aprobaciones y gasto, con la capacidad de aplicar reglas al momento del booking|Si ya tienen un TMC, Mendel Viajes no lo cambia: lo conecta con política, aprobaciones y gasto derivado en un solo flujo}
```

**Rendered example (A2 Tech-enabled operations):**
```
Hola {{firstName}},

Platicando con {{titlePlural}} en operaciones tech en México, casi todos cuentan lo mismo: operaciones tech mueven volumen alto de transacciones que finanzas no alcanza a auditar en tiempo real, y el cierre depende de revisar tickets sueltos.

Mendel resuelve eso poniendo un agente de IA que audita cada transacción contra política antes del cargo. Mercado Libre subió 30% la recuperación de facturas deductibles con esta arquitectura, después de reemplazar SAP Concur.

Si la directiva global usa Concur, Mendel empuja los datos al sistema global y suma la tropicalización México que el global no cubre — recuperación de CFDI, SAT y políticas en tiempo real.

Es la misma arquitectura que usan Mercado Libre y AB InBev hoy.

¿Vale revisarlo aplicado a {{companyName}}?
```

---

## VARIANT B — Architectural / design-limit-led

### Master template

```
Hola {{firstName}},

{{INCUMBENT_DESIGN_LIMIT}}. {{INCUMBENT_QUALIFIER}}.

{Cuando hablo|Cuando converso|En las conversaciones} con {{titlePlural}} {de|en} {{vertical}} en {{country}}, {muchos|varios|la mayoría} ya {están|están moviendo|están migrando hacia} {{ARCHITECTURAL_SHIFT}}.

Eso es lo que {corre|opera|funciona en} {{CUSTOMER_LOGOS}} hoy, y es por eso que {{OUTCOME_SENTENCE}}.

¿{Tendría sentido|Vale la pena revisarlo|Te resuena} para {{companyName}}?
```

### Variable definitions (B)

| Variable | Definition |
|---|---|
| `{{INCUMBENT_DESIGN_LIMIT}}` | Architectural fact about incumbent stack. Spintax of 2. |
| `{{INCUMBENT_QUALIFIER}}` | "Funciona si..." qualifier. Spintax of 2. |
| `{{ARCHITECTURAL_SHIFT}}` | Mendel's approach as a shift. Spintax of 2. |
| `{{CUSTOMER_LOGOS}}` | Customer(s). Spintax of 2. |
| `{{OUTCOME_SENTENCE}}` | What changes after the shift. Spintax of 2. |

### Industry fills (B)

#### Tech-enabled operations

```
vertical: operaciones tech
country: México
titlePlural: CFOs

INCUMBENT_DESIGN_LIMIT: {Concur + AMEX se diseñó para reportar gastos después de que pasan|El stack Concur + AMEX se construyó para visibilidad post-cierre, no para control en vivo}

INCUMBENT_QUALIFIER: {Funciona bien si lo que necesitas es visibilidad post-cierre|Bien si lo que se busca es ver el detalle al final del mes}

ARCHITECTURAL_SHIFT: {moviendo el control antes de la transacción: un agente de IA evalúa cada cargo contra política, recupera el CFDI y reconcilia con el ERP en tiempo real|corriendo el control antes del cargo con un agente de IA, recuperación automática de CFDIs y reconciliación al ERP en vivo}

CUSTOMER_LOGOS: {Mercado Libre|Mercado Libre y FEMSA}

OUTCOME_SENTENCE: {Mercado Libre subió 30% la recuperación de facturas deductibles después de reemplazar SAP Concur con esta arquitectura|finanzas pasa de validar tickets a aprobar reportes ya listos, con CFDI y ERP integrados al flujo}
```

**Rendered:**
```
Hola {{firstName}},

Concur + AMEX se diseñó para reportar gastos después de que pasan. Funciona bien si lo que necesitas es visibilidad post-cierre.

Cuando hablo con {{titlePlural}} en operaciones tech en México, muchos ya están moviendo el control antes de la transacción: un agente de IA evalúa cada cargo contra política, recupera el CFDI y reconcilia con el ERP en tiempo real.

Eso es lo que corre Mercado Libre hoy, y es por eso que Mercado Libre subió 30% la recuperación de facturas deductibles después de reemplazar SAP Concur con esta arquitectura.

¿Tendría sentido para {{companyName}}?
```

#### Retail & CPG

```
vertical: retail
country: México
titlePlural: CFOs

INCUMBENT_DESIGN_LIMIT: {Concur + la tarjeta del banco se diseñó para reportar después del estado de cuenta|El stack tradicional, Concur más tarjeta del banco, se construyó para reportar al cierre, no para controlar por tienda}

INCUMBENT_QUALIFIER: {Funciona si solo necesitas el report mensual|Bien si lo que se busca es el resumen mensual y nadie persigue tickets}

ARCHITECTURAL_SHIFT: {controlando antes de la transacción: política por tienda en el momento del cargo, recuperación automática de CFDIs y reconciliación al ERP en tiempo real|aplicando control antes del cargo: política por tienda, CFDIs recuperados automáticamente y reconciliación con el ERP en vivo}

CUSTOMER_LOGOS: {Walmart, OXXO y FEMSA|cadenas como Walmart, OXXO y McDonald's}

OUTCOME_SENTENCE: {el mes cierra el mismo día, sin hojas paralelas|el cierre baja de varios días a uno, sin perseguir tickets entre tiendas}
```

**Rendered:**
```
Hola {{firstName}},

Concur + la tarjeta del banco se diseñó para reportar después del estado de cuenta. Funciona si solo necesitas el report mensual.

Cuando hablo con {{titlePlural}} de retail en México, muchos ya están controlando antes de la transacción: política por tienda en el momento del cargo, recuperación automática de CFDIs y reconciliación al ERP en tiempo real.

Eso es lo que corren Walmart, OXXO y FEMSA hoy, y es por eso que el mes cierra el mismo día, sin hojas paralelas.

¿Vale la pena revisarlo para {{companyName}}?
```

#### Logistics & Transportation

```
vertical: logística
country: México
titlePlural: CFOs

INCUMBENT_DESIGN_LIMIT: {Las tarjetas de flotilla del banco y las valeras se diseñaron para pagar combustible|La tarjeta de flotilla bancaria y la valera se construyeron como medio de pago, no como sistema de control}

INCUMBENT_QUALIFIER: {Visibilidad por conductor y políticas por proveedor no estaban en el alcance original|Reglas por conductor o proveedor, y casetas o per-diems integrados, no estaban en el diseño original}

ARCHITECTURAL_SHIFT: {moviendo el control al momento del cargo: reglas por conductor, por proveedor y por horario, con CFDIs y per-diems auditados antes del cierre|corriendo el control al momento del cargo con reglas por conductor, proveedor y horario, y CFDIs y per-diems auditados antes del cierre}

CUSTOMER_LOGOS: {Viva Aerobus|operaciones como Viva Aerobus}

OUTCOME_SENTENCE: {la conciliación pasa de manual a automática|la conciliación deja de ser manual y se vuelve automática previa al cierre}
```

**Rendered:**
```
Hola {{firstName}},

Las tarjetas de flotilla del banco y las valeras se diseñaron para pagar combustible. Visibilidad por conductor y políticas por proveedor no estaban en el alcance original.

Cuando hablo con {{titlePlural}} en logística en México, muchos ya están moviendo el control al momento del cargo: reglas por conductor, por proveedor y por horario, con CFDIs y per-diems auditados antes del cierre.

Eso es lo que corre Viva Aerobus hoy, y es por eso que la conciliación pasa de manual a automática.

¿Te resuena para {{companyName}}?
```

#### Manufacturing & Industrial

```
vertical: manufactura
country: México
titlePlural: CFOs

INCUMBENT_DESIGN_LIMIT: {El stack típico en manufactura — Concur, tarjetas del banco y SAP o Contpaqi — se construyó como tres sistemas separados|La realidad típica en manufactura es operar con tres sistemas separados: Concur para reportes, tarjetas para spend, SAP o Contpaqi para ERP}

INCUMBENT_QUALIFIER: {Cada integración entre ellos es un punto de falla|Cada handoff entre esos sistemas es un punto de falla en cada cierre}

ARCHITECTURAL_SHIFT: {consolidando: control de políticas multi-planta en tiempo real, recuperación automática de CFDIs entre plantas, y reconciliación nativa contra SAP S/4HANA, Contpaqi u Oracle|unificando los tres flujos en uno: políticas multi-entidad en tiempo real, CFDIs recuperados entre plantas y reconciliación nativa con SAP, Contpaqi o el ERP de tu stack}

CUSTOMER_LOGOS: {AB InBev y Grupo Bafar|operaciones multi-planta como AB InBev}

OUTCOME_SENTENCE: {el cierre deja de depender de ajustes manuales por planta|el equipo financiero deja de armar ajustes por planta y empieza a aprobar lo que el ERP ya recibió validado}
```

**Rendered:**
```
Hola {{firstName}},

El stack típico en manufactura — Concur, tarjetas del banco y SAP o Contpaqi — se construyó como tres sistemas separados. Cada integración entre ellos es un punto de falla.

Cuando hablo con {{titlePlural}} de manufactura en México, muchos ya están consolidando: control de políticas multi-planta en tiempo real, recuperación automática de CFDIs entre plantas, y reconciliación nativa contra SAP S/4HANA, Contpaqi u Oracle.

Eso es lo que corre AB InBev hoy, y es por eso que el cierre deja de depender de ajustes manuales por planta.

¿Tendría sentido para {{companyName}}?
```

#### Pharmaceutical & Healthcare

```
vertical: farma
country: México
titlePlural: CFOs

INCUMBENT_DESIGN_LIMIT: {Las herramientas tradicionales de expense management no se diseñaron pensando en compliance farma|Los sistemas tradicionales de expense management no se construyeron con compliance farma o audit-ready en mente}

INCUMBENT_QUALIFIER: {Trazabilidad por HCP y reporte de transparencia terminan siendo proyectos manuales mensuales|La trazabilidad por HCP y el reporte de transparencia terminan armándose a mano cada mes}

ARCHITECTURAL_SHIFT: {moviendo esa trazabilidad al momento del cargo: política por representante, auditoría en tiempo real, reporte de transparencia listo para exportar|corriendo la trazabilidad al momento del cargo con política por representante, auditoría continua y reporte de transparencia listo para auditoría SAT}

CUSTOMER_LOGOS: {Farmacia San Pablo y Merck|Farmacia San Pablo}

OUTCOME_SENTENCE: {el reporte deja de armarse a mano|el equipo deja de construir el reporte de transparencia cada mes}
```

**Rendered:**
```
Hola {{firstName}},

Las herramientas tradicionales de expense management no se diseñaron pensando en compliance farma. Trazabilidad por HCP y reporte de transparencia terminan siendo proyectos manuales mensuales.

Cuando hablo con {{titlePlural}} de farma en México, muchos ya están moviendo esa trazabilidad al momento del cargo: política por representante, auditoría en tiempo real, reporte de transparencia listo para exportar.

Eso es lo que corren Farmacia San Pablo y Merck hoy, y es por eso que el reporte deja de armarse a mano.

¿Te resuena para {{companyName}}?
```

#### Professional Services

```
vertical: servicios profesionales
country: LatAm
titlePlural: CFOs

INCUMBENT_DESIGN_LIMIT: {Capturar gasto billable por engagement nunca fue para lo que se diseñó Concur|Concur no se diseñó para capturar gasto billable por engagement multi-país}

INCUMBENT_QUALIFIER: {Tampoco soporta CFDI ni operación multi-país de forma nativa|Tampoco fue construido con CFDI o operación multi-país en mente}

ARCHITECTURAL_SHIFT: {consolidando: gasto billable capturado en el momento del cargo, multi-país, con CFDI integrado y reconciliación directa al ERP|unificando: gasto billable por engagement en el momento del cargo, multi-país, con CFDI y ERP integrados}

CUSTOMER_LOGOS: {KPMG|firmas multi-país como KPMG}

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

#### Travel & Mobility

```
vertical: viajes corporativos
country: México
titlePlural: Travel Managers

INCUMBENT_DESIGN_LIMIT: {El stack típico de travel — TMC, mail, hojas de aprobación, reembolsos — se diseñó como sistemas separados|TMC, mail y reembolsos manuales se construyeron para reservar y reportar, no para controlar política al booking}

INCUMBENT_QUALIFIER: {Funciona si la prioridad es solo bookear, no controlar el gasto derivado|Bien si lo único que se necesita es la reservación}

ARCHITECTURAL_SHIFT: {consolidando booking, política, aprobaciones y gasto en una sola plataforma, con adopción online u offline visible en tiempo real|unificando booking y expense en un flujo, con política aplicada al momento de la reserva y gasto derivado integrado al ERP}

CUSTOMER_LOGOS: {KPMG|firmas multi-país como KPMG}

OUTCOME_SENTENCE: {los viajeros reservan dentro de política sin chasear aprobaciones|el cierre llega con todos los gastos de viaje ya categorizados, sin reembolsos manuales}
```

**Rendered:**
```
Hola {{firstName}},

El stack típico de travel — TMC, mail, hojas de aprobación, reembolsos — se diseñó como sistemas separados. Funciona si la prioridad es solo bookear, no controlar el gasto derivado.

Cuando hablo con {{titlePlural}} de viajes corporativos en México, muchos ya están consolidando booking, política, aprobaciones y gasto en una sola plataforma, con adopción online u offline visible en tiempo real.

Eso es lo que corre KPMG hoy, y es por eso que los viajeros reservan dentro de política sin chasear aprobaciones.

¿Tendría sentido para {{companyName}}?
```

---

## VARIANT C — Ultra-short peer-pattern

### Master template

```
Hola {{firstName}},

{Cuando hablo|Cuando converso} con {{titlePlural}} {de|en} {{vertical}} en {{country}}, {casi todos|la mayoría|muchos} {describen|cuentan|comparten} {el mismo patrón|lo mismo|el mismo dolor}: {{INDUSTRY_PAIN}}.

Mendel {{SOLUTION_VERB_PHRASE_SHORT}}.

Es lo que {corre|corren} {{CUSTOMER_LOGOS}} hoy.

¿{Tendría sentido|Te resuena|Es algo que valga la pena} para {{companyName}}?
```

### Variable definitions (C)

| Variable | Definition |
|---|---|
| `{{INDUSTRY_PAIN}}` | Same library as A1 (spintax of 2). |
| `{{SOLUTION_VERB_PHRASE_SHORT}}` | Mendel's action as present-tense verb + capabilities (compressed). Spintax of 2. |
| `{{CUSTOMER_LOGOS}}` | Same library as A1 (spintax of 2). |

### Industry fills (C) — SOLUTION_VERB_PHRASE_SHORT values

#### Tech-enabled operations

```
SOLUTION_VERB_PHRASE_SHORT: {automatiza ese control con un agente de IA antes del cargo: política en tiempo real, CFDIs recuperados y ERP reconciliado|corre auditoría IA por transacción, recupera CFDIs y reconcilia con ERP en tiempo real}
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
SOLUTION_VERB_PHRASE_SHORT: {consolida políticas multi-planta, recupera CFDIs entre plantas y se conecta nativo a SAP, Contpaqi u Oracle|unifica políticas multi-entidad con recuperación de CFDIs entre plantas y reconciliación nativa con el ERP}
```

#### Pharma

```
SOLUTION_VERB_PHRASE_SHORT: {aplica política por representante, audita en tiempo real y deja el reporte listo para exportar|corre política por representante, auditoría continua y reporte de transparencia audit-ready}
```

#### Professional Services

```
SOLUTION_VERB_PHRASE_SHORT: {captura cada gasto billable por engagement en el momento del cargo, multi-país, con CFDI y reconciliación al ERP|corre captura de gasto billable por engagement, multi-país, con CFDI integrado al ERP}
```

#### Travel & Mobility

```
SOLUTION_VERB_PHRASE_SHORT: {consolida booking, política, aprobaciones y gasto de viaje en una plataforma, con dashboard en tiempo real|unifica booking y expense con política aplicada al momento de la reserva}
```

---

# EMAIL 2 — Lead magnet (benchmark walkthrough)

**Goal:** trigger an engagement reply ("sí, me interesa") that the sender converts into a 20-min walkthrough call or a low-risk pilot. Meeting booking happens in the reply, never in the cold body.

**Thread:** same thread as Email 1 (subject inherited via EmailBison headers). No new subject line needed.

## Master template

```
Hola {{firstName}},

{Armamos|Construimos|Preparamos|Hicimos} un benchmark de cómo {{titlePlural}} {de|en} {{vertical}} en {{country}} {{PEER_ACTIVITIES}}. {Datos reales|Datos crudos|Información real}, anónimos.

{Puedo mostrarte|Te puedo enseñar|Te puedo compartir} qué {hacen|están haciendo} {{CUSTOMER_LOGOS}} y cómo se {puede aplicar|aplicaría|traduce} al setup de {{companyName}}, sin pitch.

{{CTA}}
```

## Variable definitions

| Variable | Type | Definition |
|---|---|---|
| `{{firstName}}` | merge | Lead first name |
| `{{companyName}}` | merge | Lead company |
| `{{titlePlural}}` | campaign-level | Persona plural |
| `{{vertical}}` | campaign-level | Industry word |
| `{{country}}` | campaign-level | Geography |
| `{{PEER_ACTIVITIES}}` | industry-specific | What peers do (spintax of 2) |
| `{{CUSTOMER_LOGOS}}` | industry-specific | Customer names (spintax of 2) |
| `{{CTA}}` | A/B/C variant | One of three CTA variants |

## CTA — three variants for A/B/C testing

| Variant | Spintaxed CTA | Tone | When to use |
|---|---|---|---|
| **CTA-A — Engagement probe** | `¿Te {interesaría|sería útil|haría sentido}?` | Softer, value-first | Default cold first send |
| **CTA-B — Time choice** | `¿{Te funciona|Te queda|Te va} esta semana o la próxima?` | Direct, agenda-driving | Warm leads (Email 1 opened, prior signal) |
| **CTA-C — Pilot offer** | `¿{Tendría sentido|Vale la pena armar} un piloto chico de 10 a 20 tarjetas en un equipo, con estimado de ROI antes/después?` | Concrete, low-risk | Mid-funnel touches, post-Email 1 reply with hesitation |

## Industry fills (Email 2)

#### Tech-enabled operations

```
vertical: operaciones tech
country: México
titlePlural: CFOs

PEER_ACTIVITIES: {están automatizando auditoría con agentes IA, recuperando CFDIs y reconciliando con ERP en tiempo real|están moviendo el control de gastos a tiempo real con IA: auditoría por transacción, CFDIs recuperados y ERP reconciliado}

CUSTOMER_LOGOS: {Mercado Libre y AB InBev|Mercado Libre y FEMSA}
```

**Rendered (CTA-A):**
```
Hola {{firstName}},

Armamos un benchmark de cómo {{titlePlural}} en operaciones tech en México están automatizando auditoría con agentes IA, recuperando CFDIs y reconciliando con ERP en tiempo real. Datos reales, anónimos.

Puedo mostrarte qué hacen Mercado Libre y AB InBev y cómo se puede aplicar al setup de {{companyName}}, sin pitch.

¿Te interesaría?
```

**Rendered (CTA-B):**
```
Hola {{firstName}},

Armamos un benchmark de cómo {{titlePlural}} en operaciones tech en México están automatizando auditoría con agentes IA, recuperando CFDIs y reconciliando con ERP en tiempo real. Datos reales, anónimos.

Puedo mostrarte qué hacen Mercado Libre y AB InBev y cómo se puede aplicar al setup de {{companyName}}, sin pitch.

¿Te funciona esta semana o la próxima?
```

#### Retail & CPG

```
vertical: retail
country: México
titlePlural: CFOs

PEER_ACTIVITIES: {están aplicando políticas por punto de venta, recuperando CFDIs automáticamente y cerrando el mes el mismo día|están controlando spend por tienda en cada cargo, recuperando CFDIs en vivo y cerrando el mes al instante}

CUSTOMER_LOGOS: {Walmart, OXXO y FEMSA|cadenas como Walmart, OXXO y McDonald's}
```

**Rendered (CTA-A):**
```
Hola {{firstName}},

Armamos un benchmark de cómo {{titlePlural}} de retail en México están aplicando políticas por punto de venta, recuperando CFDIs automáticamente y cerrando el mes el mismo día. Datos reales, anónimos.

Puedo mostrarte qué hacen Walmart, OXXO y FEMSA y cómo se puede aplicar al setup de {{companyName}}, sin pitch.

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
Hola {{firstName}},

Armamos un benchmark de cómo {{titlePlural}} en logística en México están aplicando reglas por conductor y proveedor, con CFDIs y per-diems auditados antes del cierre. Datos reales, anónimos.

Puedo mostrarte qué hace Viva Aerobus y cómo se puede aplicar al setup de {{companyName}}, sin pitch.

¿Te haría sentido?
```

#### Manufacturing & Industrial

```
vertical: manufactura
country: México
titlePlural: CFOs

PEER_ACTIVITIES: {están consolidando spend multi-planta con recuperación de CFDIs y reconciliación nativa a SAP, Contpaqi u Oracle|están unificando spend entre plantas con políticas en tiempo real, CFDIs recuperados y reconciliación nativa con el ERP}

CUSTOMER_LOGOS: {AB InBev y Grupo Bafar|operaciones multi-planta como AB InBev}
```

**Rendered (CTA-A):**
```
Hola {{firstName}},

Armamos un benchmark de cómo {{titlePlural}} de manufactura en México están consolidando spend multi-planta con recuperación de CFDIs y reconciliación nativa a SAP, Contpaqi u Oracle. Datos reales, anónimos.

Puedo mostrarte qué hacen AB InBev y Grupo Bafar y cómo se puede aplicar al setup de {{companyName}}, sin pitch.

¿Te interesaría?
```

#### Pharmaceutical & Healthcare

```
vertical: farma
country: México
titlePlural: CFOs

PEER_ACTIVITIES: {están aplicando política por representante, auditando en tiempo real y dejando el reporte de transparencia listo para exportar|están corriendo política por representante en cada cargo, con auditoría continua y reporte de transparencia audit-ready}

CUSTOMER_LOGOS: {Farmacia San Pablo y Merck|Farmacia San Pablo}
```

**Rendered (CTA-A):**
```
Hola {{firstName}},

Armamos un benchmark de cómo {{titlePlural}} de farma en México están aplicando política por representante, auditando en tiempo real y dejando el reporte de transparencia listo para exportar. Datos reales, anónimos.

Puedo mostrarte qué hacen Farmacia San Pablo y Merck y cómo se puede aplicar al setup de {{companyName}}, sin pitch.

¿Te sería útil?
```

#### Professional Services

```
vertical: servicios profesionales
country: LatAm
titlePlural: CFOs

PEER_ACTIVITIES: {están capturando gasto billable por engagement, multi-país, con CFDI integrado al ERP|están corriendo gasto billable por engagement en el momento del cargo, multi-país, con CFDI y ERP integrados}

CUSTOMER_LOGOS: {KPMG|firmas multi-país como KPMG}
```

**Rendered (CTA-A):**
```
Hola {{firstName}},

Armamos un benchmark de cómo {{titlePlural}} de servicios profesionales en LatAm están capturando gasto billable por engagement, multi-país, con CFDI integrado al ERP. Datos reales, anónimos.

Puedo mostrarte qué hace KPMG y cómo se puede aplicar al setup de {{companyName}}, sin pitch.

¿Te haría sentido?
```

#### Travel & Mobility

```
vertical: viajes corporativos
country: México
titlePlural: Travel Managers

PEER_ACTIVITIES: {están consolidando booking, política y gasto de viajes en una sola plataforma, con adopción online u offline trackeada en tiempo real|están unificando booking y expense con política aplicada al momento de la reserva y gasto derivado integrado al ERP}

CUSTOMER_LOGOS: {KPMG|firmas multi-país como KPMG}
```

**Rendered (CTA-A):**
```
Hola {{firstName}},

Armamos un benchmark de cómo {{titlePlural}} de viajes corporativos en México están consolidando booking, política y gasto de viajes en una sola plataforma, con adopción online u offline trackeada en tiempo real. Datos reales, anónimos.

Puedo mostrarte qué hace KPMG y cómo se puede aplicar al setup de {{companyName}}, sin pitch.

¿Te interesaría?
```

## Reply handling for Email 2

| Reply | Sender response |
|---|---|
| "Sí, me interesa" / "Sí, mándalo" | `Perfecto, lo más útil es repasarlo en 20 min. ¿Te queda jueves o viernes esta semana?` Book the meeting in the reply, never in the cold body. |
| "Mándame el PDF mejor" | `No tenemos PDF aparte porque depende del contexto. Si te queda 20 min te lo paso aplicado a {{companyName}}.` Push back to meeting once. |
| "Suena interesante pero ahora no" | Offer CTA-C pilot: `Si más adelante quieren probarlo en chico — 10 a 20 tarjetas en un equipo, sin compromiso de expansión — te armo una propuesta. Sin presión.` |
| "No me interesa" | Polite acknowledgment, move to long-term nurture. |
| No reply | Email 3 with a different angle (case study or direct demo offer). |

---

# Libraries

## Subject line library — Email 1

Three patterns per industry. **Pattern A** (direct question) wins on replies; **Pattern C** (peer reference) wins on opens; **Pattern D** (specific outcome) is the highest-impact for the Mercado Libre proof point. A/B test 2 per campaign.

| Industry | Pattern A (direct question) | Pattern C (peer reference) | Pattern D (specific outcome) |
|---|---|---|---|
| Tech-enabled operations | `{{firstName}}, ¿cómo manejan finanzas en {{companyName}}?` | `{{firstName}}, lo que hace Mercado Libre` | `{{firstName}}, cómo Mercado Libre subió 30% deducibilidad` |
| Retail | `{{firstName}}, ¿cómo cierran el mes en {{companyName}}?` | `{{firstName}}, lo que hacen Walmart y OXXO` | `{{firstName}}, cierre el mismo día como Walmart` |
| Logistics | `{{firstName}}, ¿cómo controlan flotilla en {{companyName}}?` | `{{firstName}}, lo que hace Viva Aerobus` | `{{firstName}}, control de flotilla como Viva Aerobus` |
| Manufacturing | `{{firstName}}, ¿cómo reconcilian SAP en {{companyName}}?` | `{{firstName}}, lo que hace AB InBev` | `{{firstName}}, multi-planta como AB InBev` |
| Pharma | `{{firstName}}, ¿cómo arman transparencia en {{companyName}}?` | `{{firstName}}, lo que hace Farmacia San Pablo` | `{{firstName}}, reporte audit-ready como Merck` |
| Professional Services | `{{firstName}}, ¿cómo capturan billable en {{companyName}}?` | `{{firstName}}, lo que hace KPMG` | `{{firstName}}, gasto billable como KPMG` |
| Travel & Mobility | `{{firstName}}, ¿cómo manejan viajes en {{companyName}}?` | `{{firstName}}, lo que hace KPMG en viajes` | `{{firstName}}, booking dentro de política como KPMG` |

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

## Objection defusion library

| # | Trigger | Template |
|---|---|---|
| 1 | Existing stack (Concur, AMEX, bank cards, fleet cards, TMC) | `Si ya operan con [stack], Mendel no [los/las] reemplaza: integra [things] en un solo lugar, con capacidades LatAm que [esos tools / los globales] no traen.` |
| 2 | Implementation complexity (SAP, ERP, multi-country, compliance) | `Sé que [implementing X] suena pesado. Por diseño Mendel se conecta nativo a [SAP / ERP], no se le agrega encima, y la implementación va con acompañamiento end-to-end del equipo Mendel.` |
| 3 | Current process works well enough | `Sé que el proceso actual funciona. La pregunta es cuántas horas y cuánta deductibilidad se pierden cada mes que ya no vuelven.` |
| 4 | Free bank cards / cheap credit | `Sé que el banco te da tarjetas sin cargo extra. La diferencia no son las tarjetas, es la capa de software encima: política preventiva, recuperación de CFDIs y reconciliación con el ERP.` |
| 5 | Global mandate / "the global CFO uses X" | `Sé que la directiva global usa [Concur / sistema global]. Mendel empuja los datos al sistema global y suma la tropicalización México que el global no cubre — CFDI, SAT, políticas en tiempo real.` |
| 6 | Driver / operator adoption fear | `El miedo común es que los choferes u operadores no usen otra app. La acción del usuario se reduce a sacar foto al ticket; Mendel hace el resto en automático.` |

| Industry | Default objection used in Variant A2 |
|---|---|
| Tech-enabled operations | #1 or #5 (global mandate) |
| Retail | #1 or #4 (free bank cards) |
| Logistics | #6 (driver adoption) |
| Manufacturing | #2 (SAP implementation) |
| Pharma | #2 (compliance complexity) |
| Professional Services | #3 (current process works) |
| Travel & Mobility | #1 (existing TMC) |

---

# Spintax reference

Spintax format: `{option1|option2|option3}`. Two layers:

1. **Static spintax in master templates** — connector words, verbs of speech.
2. **Industry-variable spintax in fill tables** — each per-industry variable has 2 phrasings of the same idea.

Both get resolved by EmailBison at send time. Each layer is independent.

**Allowed in spintax (Layer 1, master templates):**
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
- CTA verbs: `{Vale|Tiene sentido|Hace sentido|Tendría sentido|Te resuena}`, `{revisarlo|verlo|echarle un ojo}`, `{interesaría|sería útil|haría sentido}`, `{Te funciona|Te queda|Te va}`

**Layer 2 — variable-level spintax:** every per-industry variable value (`{{INDUSTRY_PAIN}}`, `{{SOLUTION_VERB_PHRASE}}`, `{{OUTCOME_SENTENCE}}`, `{{OBJECTION_DEFUSION}}`, `{{CUSTOMER_LOGOS}}`, `{{INCUMBENT_DESIGN_LIMIT}}`, `{{INCUMBENT_QUALIFIER}}`, `{{ARCHITECTURAL_SHIFT}}`, `{{PEER_ACTIVITIES}}`) holds 2 phrasings using the same `{a|b}` syntax. EmailBison resolves these independently per send.

**Never spintax:**
- Merge variables (`{{firstName}}`, `{{companyName}}`, `{{titlePlural}}`, `{{vertical}}`, `{{country}}`)
- Customer / brand names inside the spintax options (Mercado Libre, FEMSA, KPMG, AB InBev, Walmart, OXXO, McDonald's, Tim Hortons, PetCo, Grupo Bafar, Farmacia San Pablo, Merck, Viva Aerobus, Mendel, Concur, AMEX, SAP, S/4HANA, Contpaqi, Oracle, ERP, CFDI, SAT, HCP)
- The opening `Hola {{firstName}},`

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
- Greeting: `Hola` only (no Hey, no Buenas — preserves expert/professional tone)
