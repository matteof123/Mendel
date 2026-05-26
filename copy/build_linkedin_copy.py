#!/usr/bin/env python3
"""
Mendel - LinkedIn Copy v1 (Spanish, Mexico-first, LatAm)
Modeled on Framework Consulting v5 structure:
 - 3 angles × 2 persona variants each
 - 3 messages per sequence (connection note, personalised follow-up, lead magnet)
 - Amber [PERSONALISATION] slot in Message 2 with examples
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.colors import HexColor

# Mendel-aligned palette (dark navy + accent blue, matches email library PDF)
NAVY    = HexColor('#1A1A2E')
BLUE    = HexColor('#0F3460')
LGREY   = HexColor('#F3F4F6')
MGREY   = HexColor('#6B7280')
WHITE   = colors.white
LBLUE   = HexColor('#EFF6FF')
BORDER  = HexColor('#BFDBFE')
GREEN   = HexColor('#16A34A')
LGREEN  = HexColor('#F0FDF4')
GBORDER = HexColor('#86EFAC')
AMBER   = HexColor('#D97706')
LAMBER  = HexColor('#FFFBEB')
ABORDER = HexColor('#FCD34D')

OUTPUT = "/Users/matteofois/Documents/Claude/Claude Folder/clients/mendel/copy/Mendel_LinkedIn_Copy.pdf"

PAGE_W, PAGE_H = letter
LM = RM = 0.9 * inch
USABLE = PAGE_W - LM - RM

PERSONALISATION_SLOT = (
    '<font color="#D97706"><b>[PERSONALIZACIÓN]</b></font>'
)


def add_footer(canvas, doc):
    if doc.page > 1:
        canvas.saveState()
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(MGREY)
        canvas.drawString(LM, 0.45 * inch, "Mendel - LinkedIn Copy")
        canvas.drawRightString(PAGE_W - RM, 0.45 * inch, f"Página {doc.page}")
        canvas.restoreState()


def S(name, **kw):
    return ParagraphStyle(name, **kw)


def txt(text, fn='Helvetica', fs=10, color=HexColor('#1F2937'),
        leading=None, align=TA_LEFT, spaceAfter=0):
    if leading is None:
        leading = fs + 5
    return Paragraph(str(text), S(f'a{id(text)}',
        fontName=fn, fontSize=fs, textColor=color,
        leading=leading, spaceAfter=spaceAfter, alignment=align))


def wrap(data):
    out = []
    for r, row in enumerate(data):
        fn = 'Helvetica-Bold' if r == 0 else 'Helvetica'
        tc = WHITE if r == 0 else HexColor('#1F2937')
        out.append([Paragraph(str(c), S(f'w{r}{i}', fontName=fn,
            fontSize=9, textColor=tc, leading=14)) for i, c in enumerate(row)])
    return out


def divider(s, title, subtitle=None):
    s.append(Spacer(1, 0.2 * inch))
    s.append(HRFlowable(width=USABLE, thickness=2, color=BLUE, spaceAfter=8))
    s.append(txt(title, fn='Helvetica-Bold', fs=17, color=NAVY, leading=24, spaceAfter=3))
    if subtitle:
        s.append(txt(subtitle, fn='Helvetica-Oblique', fs=9.5, color=MGREY, leading=14, spaceAfter=0))
    s.append(HRFlowable(width=USABLE, thickness=0.4, color=HexColor('#D1D5DB'), spaceBefore=8, spaceAfter=14))


def card(s, label, label_color, text, bg, border, mixed=False):
    """mixed=True means text already contains XML/color markup."""
    lbl = Paragraph(label, S('lbl', fontName='Helvetica-Bold', fontSize=8,
        textColor=label_color, leading=12))
    if mixed:
        body = Paragraph(text, S('bdm', fontName='Helvetica',
            fontSize=10.5, textColor=HexColor('#111827'), leading=17))
    else:
        body = Paragraph(text.replace('\n', '<br/>'), S(f'bd{id(text)}', fontName='Helvetica',
            fontSize=10.5, textColor=HexColor('#111827'), leading=17))
    t = Table([[lbl], [body]], colWidths=[USABLE - 0.2 * inch],
        style=TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), bg),
            ('BOX', (0, 0), (-1, -1), 1, border),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 0), (0, 0), 8),
            ('BOTTOMPADDING', (0, 0), (0, 0), 3),
            ('TOPPADDING', (0, 1), (0, 1), 3),
            ('BOTTOMPADDING', (0, 1), (0, 1), 12),
        ]))
    s.append(t)
    s.append(Spacer(1, 0.06 * inch))


def examples_card(s, examples):
    rows = []
    lbl = Paragraph(
        '<b>EJEMPLOS DE PERSONALIZACIÓN</b>  '
        '<font color="#6B7280">— escribe una línea y reemplaza [PERSONALIZACIÓN]</font>',
        S('exlbl', fontName='Helvetica-Bold', fontSize=8, textColor=AMBER, leading=12))
    rows.append([lbl])

    for ex in examples:
        bullet = Paragraph(
            f'<font color="#D97706">&#9656;</font>  <i>{ex}</i>',
            S(f'ex{id(ex)}', fontName='Helvetica-Oblique', fontSize=9.5,
              textColor=HexColor('#92400E'), leading=15))
        rows.append([bullet])

    t = Table(rows, colWidths=[USABLE - 0.2 * inch],
        style=TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), LAMBER),
            ('BOX', (0, 0), (-1, -1), 1, ABORDER),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 0), (0, 0), 8),
            ('BOTTOMPADDING', (0, 0), (0, 0), 4),
            ('TOPPADDING', (0, 1), (-1, -1), 3),
            ('BOTTOMPADDING', (0, -1), (-1, -1), 10),
        ]))
    s.append(t)
    s.append(Spacer(1, 0.12 * inch))


def build_followup(opening, personalisation_line, body):
    return (
        f"{opening}<br/><br/>"
        f"{personalisation_line}<br/><br/>"
        f"{body.replace(chr(10), '<br/>')}"
    )


def angle(s, title, for_whom, note, followup_open, followup_body,
          personalisation_examples, leadmagnet):

    s.append(KeepTogether([
        txt(title, fn='Helvetica-Bold', fs=13, color=NAVY, leading=18, spaceAfter=3),
        txt(f"Para: {for_whom}", fn='Helvetica-Oblique', fs=9, color=MGREY, leading=13, spaceAfter=10),
    ]))

    card(s, "MENSAJE 1 - NOTA DE CONEXIÓN  (con la solicitud, máx ~300 chars)",
         MGREY, note, bg=LBLUE, border=BORDER)

    followup_markup = build_followup(followup_open, PERSONALISATION_SLOT, followup_body)
    card(s, "MENSAJE 2 - PRIMER SEGUIMIENTO  (1-2 días después de aceptar)",
         MGREY, followup_markup, bg=LGREY, border=HexColor('#D1D5DB'), mixed=True)

    examples_card(s, personalisation_examples)

    card(s, "MENSAJE 3 - LEAD MAGNET  (Día 5-7 — enviar respondan o no al M2)",
         GREEN, leadmagnet, bg=LGREEN, border=GBORDER)

    s.append(Spacer(1, 0.05 * inch))


# ─────────────────────────────────────────────────────────────────────────────
def build():
    doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
        leftMargin=LM, rightMargin=RM,
        topMargin=0.9 * inch, bottomMargin=0.9 * inch)
    s = []

    # COVER
    s.append(Spacer(1, 1.2 * inch))
    cover = Table([
        [txt("Mendel", fn='Helvetica-Bold', fs=12,
             color=HexColor('#BFD3F7'), align=TA_CENTER)],
        [txt("LinkedIn Copy", fn='Helvetica-Bold', fs=38,
             color=WHITE, leading=48, align=TA_CENTER)],
        [Spacer(1, 0.08 * inch)],
        [txt("3 ángulos por pain  ·  3 mensajes por ángulo  ·  cierre con lead magnet",
             fn='Helvetica', fs=11, color=HexColor('#90AAD4'), align=TA_CENTER)],
        [Spacer(1, 0.12 * inch)],
        [txt("Mayo 2026 — Español (México prioridad, LatAm)",
             fn='Helvetica-Oblique', fs=10,
             color=HexColor('#90AAD4'), align=TA_CENTER)],
    ], colWidths=[USABLE], style=TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), NAVY),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('LEFTPADDING', (0, 0), (-1, -1), 32),
        ('RIGHTPADDING', (0, 0), (-1, -1), 32),
    ]))
    s.append(cover)
    s.append(PageBreak())

    # HOW IT WORKS
    s.append(txt("Cómo funciona la secuencia", fn='Helvetica-Bold', fs=18, color=NAVY, leading=24, spaceAfter=6))
    s.append(HRFlowable(width=USABLE, thickness=1, color=BLUE, spaceAfter=12))
    flow = [
        ["Paso", "Mensaje", "Objetivo"],
        ["Conectar", "Mensaje 1 — Nota de conexión",
         "Conseguir la aceptación. Sin pitch. Solo relevancia."],
        ["Día 1-2", "Mensaje 2 — Primer seguimiento",
         "Abrir con una línea personalizada (resaltada en ámbar), luego nombrar el dolor. Una pregunta suave."],
        ["Día 5-7", "Mensaje 3 — Lead magnet",
         "Ofrecer algo concreto: benchmark privado anónimo, sin compromiso. "
         "Enviar hayan o no respondido al M2."],
    ]
    tw = [0.7 * inch, 2.0 * inch, USABLE - 0.7 * inch - 2.0 * inch]
    t = Table(wrap(flow), colWidths=tw)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LGREY]),
        ('BOX', (0, 0), (-1, -1), 0.5, MGREY),
        ('INNERGRID', (0, 0), (-1, -1), 0.3, HexColor('#E5E7EB')),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.15 * inch))
    s.append(txt(
        "El espacio ámbar [PERSONALIZACIÓN] en el Mensaje 2 queda en blanco a propósito. "
        "Antes de enviar, escribe una línea específica de esa persona: un post que compartió, "
        "una novedad de su empresa, algo de su perfil. "
        "Debajo de cada mensaje hay ejemplos que sirven como referencia.",
        fn='Helvetica', fs=10, color=MGREY, leading=15, spaceAfter=0))
    s.append(PageBreak())

    # ── ANGLE 1 ───────────────────────────────────────────────────────────────
    divider(s,
        "Ángulo 1 — Recuperación de CFDIs y deducibilidad (+30%)",
        "Para: Tax Manager · Head of Accounting · CFO · Director Administración y Finanzas")
    s.append(txt(
        "Tensión central: en México, la deducibilidad fiscal se pierde por CFDIs que nunca llegan "
        "o llegan tarde. Eso se traduce directo al P&L y no se recupera al cierre.",
        fn='Helvetica', fs=10, color=MGREY, leading=15, spaceAfter=14))

    angle(s,
        title="1A — Tax Manager / Head of Accounting",
        for_whom="Tax Manager, Head of Accounting, Director de Impuestos, Contralor Fiscal",
        note=(
            "{{firstName}} - ayudamos a equipos de tax en México a recuperar CFDIs automáticamente "
            "y validar contra SAT desde el momento del cargo. Trabajamos solo con operaciones en LatAm. "
            "Quería conectar."
        ),
        followup_open="Hola {{firstName}}, gracias por conectar.",
        followup_body=(
            "Lo que escucho seguido de Tax Managers en México: el equipo termina persiguiendo facturas "
            "y armando el reporte de transparencia a mano cada cierre. La deducibilidad que se pierde no regresa.\n\n"
            "Mendel automatiza la recuperación de CFDIs y validación SAT desde el cargo, no después. "
            "Mercado Libre subió 30% la recuperación de facturas deductibles después de implementarlo.\n\n"
            "¿Tendría sentido revisarlo para {{companyName}}?"
        ),
        personalisation_examples=[
            "Vi tu post sobre [tema fiscal / SAT / CFDI] — resonó exacto con lo que escucho de Tax Managers en operaciones similares.",
            "Noté que {{companyName}} tiene operación multi-entidad — el flujo de CFDIs entre subsidiarias suele ser donde más deducibilidad se pierde.",
            "Vi que {{companyName}} expandió a [nuevo mercado / país] — esos movimientos suelen complicar el cierre fiscal del trimestre.",
            "Leí tu comentario sobre [auditoría / cierre / SAT] en LinkedIn — es el dolor más común que escucho del equipo de tax.",
        ],
        leadmagnet=(
            "Hola {{firstName}}, armé un benchmark de cómo equipos de tax en operaciones tipo {{companyName}} "
            "están recuperando 30% más deducibilidad sin sumar headcount.\n\n"
            "Tres páginas, datos reales y anónimos. Sin pitch.\n\n"
            "¿Te lo paso?\n\n"
            "PS: Mendel se conecta nativo a SAP, Contpaqi y Oracle, con SAT integrado al core."
        )
    )

    angle(s,
        title="1B — CFO / Director de Finanzas",
        for_whom="CFO, VP / Director de Finanzas, Director de Administración y Finanzas",
        note=(
            "{{firstName}} - ayudamos a CFOs en LatAm a recuperar deducibilidad fiscal y controlar gastos "
            "antes del cargo. Mercado Libre subió 30% recuperación con esta arquitectura. Quería conectar."
        ),
        followup_open="Hola {{firstName}}, gracias por conectar.",
        followup_body=(
            "El patrón que veo en CFOs en México: 20-30% de la deducibilidad fiscal se pierde por CFDIs "
            "que nunca llegan o llegan tarde. Eso se traduce directo al P&L y no se recupera al cierre.\n\n"
            "Mendel automatiza la recuperación y validación SAT desde el cargo. Mercado Libre subió 30% "
            "recuperación de facturas deductibles después de reemplazar SAP Concur.\n\n"
            "¿Te resuena para {{companyName}}?"
        ),
        personalisation_examples=[
            "Vi {{companyName}} acaba de [cerrar ronda / hito / contrato grande] — en ese momento el control de spend suele entrar al radar del board.",
            "Noté que recientemente entraste como CFO a {{companyName}} — los primeros 90 días suelen revelar dónde se está perdiendo deducibilidad.",
            "Vi tu post sobre [finanzas / cierre / cash management] — el punto sobre [X] resonó con lo que escucho de CFOs en operaciones similares.",
            "Leí que {{companyName}} expandió a [nuevo mercado / país] — los flujos fiscales multi-país son donde más deducibilidad se filtra.",
        ],
        leadmagnet=(
            "Hola {{firstName}}, armé un benchmark de cómo CFOs en operaciones tipo {{companyName}} "
            "están recuperando deducibilidad y cerrando el mes el mismo día.\n\n"
            "Tres páginas, datos reales y anónimos. Sin pitch.\n\n"
            "¿Te lo paso?\n\n"
            "PS: Operaciones como Mercado Libre, AB InBev y KPMG corren sobre esta arquitectura hoy."
        )
    )
    s.append(PageBreak())

    # ── ANGLE 2 ───────────────────────────────────────────────────────────────
    divider(s,
        "Ángulo 2 — Control en tiempo real (no reporting post-cierre)",
        "Para: CFO · Controller · Director de Finanzas")
    s.append(txt(
        "Tensión central: Concur + AMEX se diseñaron para reportar gastos después de que pasan. "
        "El control en el momento del cargo simplemente no estaba en el alcance original.",
        fn='Helvetica', fs=10, color=MGREY, leading=15, spaceAfter=14))

    angle(s,
        title="2A — CFO (frame arquitectónico)",
        for_whom="CFO, VP Finanzas, Director de Administración y Finanzas",
        note=(
            "{{firstName}} - ayudamos a CFOs en LatAm a mover el control de gastos antes del cargo, "
            "no después como Concur. Mercado Libre reemplazó SAP Concur con esto. Quería conectar."
        ),
        followup_open="Hola {{firstName}}, gracias por conectar.",
        followup_body=(
            "Lo que cuentan los CFOs: Concur + AMEX se diseñó para reportar gastos después de que pasan. "
            "Funciona si lo que necesitas es visibilidad post-cierre, pero no controla nada en el momento del cargo.\n\n"
            "Mendel evalúa cada cargo contra política antes de que pase: por empleado, proveedor, monto "
            "y horario. Si viola política, no pasa.\n\n"
            "¿Tendría sentido revisarlo para {{companyName}}?"
        ),
        personalisation_examples=[
            "Vi tu post sobre [cierre mensual / control / spend] — el punto sobre [X] es exactamente lo que escucho de CFOs en operaciones similares.",
            "Noté que {{companyName}} está creciendo rápido el equipo operativo — el desfase entre velocidad de spend y velocidad de control suele aparecer ahí.",
            "Vi {{companyName}} acaba de [cerrar deal / firmar contrato / partnership] — los movimientos grandes revelan gaps de control que no estaban en el radar.",
            "Leí que migraste de [tool A] a [tool B] — curioso si el control en tiempo real estaba en el alcance del cambio.",
        ],
        leadmagnet=(
            "Hola {{firstName}}, armé un benchmark de cómo CFOs en operaciones tipo {{companyName}} "
            "mueven el control antes del cargo, no después.\n\n"
            "Tres páginas, datos reales y anónimos. Sin pitch.\n\n"
            "¿Te lo paso?\n\n"
            "PS: Mercado Libre reemplazó SAP Concur con esta arquitectura."
        )
    )

    angle(s,
        title="2B — Controller / Finance Director (frame operativo)",
        for_whom="Controller, Finance Director, Contralor, Director Contable",
        note=(
            "{{firstName}} - ayudamos a Controllers en México a cerrar el mes el mismo día, sin perseguir "
            "tickets ni armar hojas paralelas. Walmart y OXXO corren así. Quería conectar."
        ),
        followup_open="Hola {{firstName}}, gracias por conectar.",
        followup_body=(
            "El patrón que escucho de Controllers en México: el equipo termina perseguiendo tickets "
            "y armando el cierre en Excel mientras Concur reporta lo que ya pasó. Eso suma días al cierre mensual.\n\n"
            "Mendel aplica política en el momento del cargo, recupera CFDIs automáticamente y reconcilia "
            "con el ERP en tiempo real. El equipo cierra el mes el mismo día.\n\n"
            "¿Hace sentido revisarlo para {{companyName}}?"
        ),
        personalisation_examples=[
            "Vi tu post sobre [cierre / conciliación / ERP] — el dolor que describes es exactamente lo que escucho de Controllers en operaciones similares.",
            "Noté que {{companyName}} es operación multi-planta — el cierre multi-entidad suele ser donde más se pierde tiempo manual.",
            "Vi que {{companyName}} migró a SAP S/4HANA — el control de spend conectado nativo al ERP suele ser un gap visible en esos rollouts.",
            "Leí tu comentario sobre [equipo / scaling / hiring] — los controllers que conozco sienten el desfase entre velocidad operativa y de cierre.",
        ],
        leadmagnet=(
            "Hola {{firstName}}, armé un benchmark de cómo Controllers en operaciones tipo {{companyName}} "
            "están cerrando el mes el mismo día.\n\n"
            "Tres páginas, datos reales y anónimos. Sin pitch.\n\n"
            "¿Te lo paso?\n\n"
            "PS: Walmart y OXXO corren sobre esta arquitectura para sus cadenas multi-tienda."
        )
    )
    s.append(PageBreak())

    # ── ANGLE 3 ───────────────────────────────────────────────────────────────
    divider(s,
        "Ángulo 3 — Una plataforma vs stack fragmentado",
        "Para: CFO · Travel Manager · Director de Operaciones")
    s.append(txt(
        "Tensión central: el stack típico es Concur para reportes + tarjetas del banco para spend "
        "+ TMC para viajes + SAP para ERP. Cada integración entre ellos es un punto de falla.",
        fn='Helvetica', fs=10, color=MGREY, leading=15, spaceAfter=14))

    angle(s,
        title="3A — CFO (consolidación de stack)",
        for_whom="CFO, VP Finanzas, Director Administración y Finanzas",
        note=(
            "{{firstName}} - ayudamos a CFOs en LatAm a consolidar tarjetas, gastos, viajes y ERP en una "
            "sola plataforma, no en cuatro herramientas separadas. KPMG y Mercado Libre corren así. "
            "Quería conectar."
        ),
        followup_open="Hola {{firstName}}, gracias por conectar.",
        followup_body=(
            "El stack típico que veo: Concur para reportes, tarjetas del banco para spend, TMC para "
            "viajes, SAP para ERP. Cada integración entre ellos es un punto de falla, y cada cierre "
            "depende de que los cuatro hagan handoff sin errores.\n\n"
            "Mendel unifica cards, expenses, viajes, CFDI y ERP en una sola plataforma. KPMG y "
            "Mercado Libre corren así hoy.\n\n"
            "¿Te resuena para {{companyName}}?"
        ),
        personalisation_examples=[
            "Vi {{companyName}} expandió a [nuevo mercado / país] — los flujos multi-país suelen revelar dónde el stack está atado con cinta.",
            "Noté que {{companyName}} usa SAP — la conexión nativa entre spend y ERP suele ser el punto donde más se rompe la reconciliación.",
            "Vi tu post sobre [operación / cierre / scaling] — el punto sobre [X] resonó con lo que escucho de CFOs consolidando stack.",
            "Leí que {{companyName}} cerró [contrato grande / partnership] — esos eventos exponen gaps entre sistemas que no se veían a menor escala.",
        ],
        leadmagnet=(
            "Hola {{firstName}}, armé un benchmark de cómo CFOs en operaciones tipo {{companyName}} "
            "están consolidando cards + expenses + travel + ERP en una sola plataforma.\n\n"
            "Tres páginas, datos reales y anónimos. Sin pitch.\n\n"
            "¿Te lo paso?\n\n"
            "PS: Operaciones como KPMG, AB InBev y Mercado Libre corren así hoy."
        )
    )

    angle(s,
        title="3B — Travel Manager (Mendel Viajes)",
        for_whom="Travel Manager, Event Manager, Mobility Director",
        note=(
            "{{firstName}} - ayudamos a Travel Managers en LatAm a consolidar booking, política y gasto "
            "de viajes en una sola plataforma, no en TMC + mail + reembolsos. Quería conectar."
        ),
        followup_open="Hola {{firstName}}, gracias por conectar.",
        followup_body=(
            "Lo que escucho de Travel Managers: el stack típico — TMC + mail + hojas de aprobación + "
            "reembolsos — se diseñó para reservar y reportar, no para aplicar política al momento del "
            "booking. Los viajeros reservan fuera de política y los reembolsos se aprueban a mano.\n\n"
            "Mendel Viajes integra booking, política, aprobaciones y gasto en un solo flujo. Los viajeros "
            "reservan dentro de política sin chasear aprobaciones.\n\n"
            "¿Tiene sentido revisarlo para {{companyName}}?"
        ),
        personalisation_examples=[
            "Vi tu post sobre [travel / booking / política] — el punto sobre [X] resonó con lo que escucho de Travel Managers en operaciones similares.",
            "Noté que {{companyName}} es operación multi-país — los flujos de aprobación multi-país son donde más se nos van los reembolsos manuales.",
            "Vi {{companyName}} acaba de [expandirse / contratar / mover oficinas] — esos eventos suelen disparar volumen de viajes que el sistema actual no maneja bien.",
            "Leí que migraste a [TMC X] — curioso si la política aplicada al booking estaba en el alcance del cambio.",
        ],
        leadmagnet=(
            "Hola {{firstName}}, armé un benchmark de cómo Travel Managers en operaciones tipo "
            "{{companyName}} están consolidando booking + política + gasto en una sola plataforma.\n\n"
            "Tres páginas, datos reales y anónimos. Sin pitch.\n\n"
            "¿Te lo paso?\n\n"
            "PS: Firmas multi-país como KPMG corren sobre esta arquitectura."
        )
    )
    s.append(PageBreak())

    # ── QUICK REF ─────────────────────────────────────────────────────────────
    divider(s, "Referencia rápida")
    ref = [
        ["Ángulo", "Dolor central", "Persona ideal"],
        ["1A — Recuperación CFDIs",
         "Equipo persigue facturas; deducibilidad se pierde al cierre",
         "Tax Manager, Head of Accounting"],
        ["1B — Deducibilidad CFO",
         "20-30% de deducibilidad se pierde al P&L por CFDIs faltantes",
         "CFO, Director de Finanzas"],
        ["2A — Control real-time",
         "Concur reporta después; sin control en el momento del cargo",
         "CFO, VP Finanzas"],
        ["2B — Cierre el mismo día",
         "Equipo persigue tickets y arma Excel; cierre toma varios días",
         "Controller, Finance Director"],
        ["3A — Consolidación stack",
         "Stack fragmentado entre 4 herramientas; integraciones se rompen",
         "CFO, Director de Operaciones"],
        ["3B — Mendel Viajes",
         "TMC + mail + reembolsos no aplican política al booking",
         "Travel Manager, Event Manager"],
    ]
    tw = [1.5 * inch, 2.7 * inch, USABLE - 1.5 * inch - 2.7 * inch]
    t = Table(wrap(ref), colWidths=tw)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LGREY]),
        ('BOX', (0, 0), (-1, -1), 0.5, MGREY),
        ('INNERGRID', (0, 0), (-1, -1), 0.3, HexColor('#E5E7EB')),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    s.append(t)

    doc.build(s, onFirstPage=add_footer, onLaterPages=add_footer)
    print(f"Built: {OUTPUT}")


if __name__ == "__main__":
    build()
