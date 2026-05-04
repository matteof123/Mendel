#!/usr/bin/env python3
"""
Mendel GTM Playbook Generator
Generated: May 4, 2026
Sources: BD Assessment 3-tab sheet (Apr 28), UVP doc (Apr 28),
         Onboarding/Strategy call w/ Alan Karpovsky (Apr 28),
         Mendel sales decks + Concur/Edenred/T&E benchmarks
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfgen import canvas as pdfcanvas

# ── Color Palette ──────────────────────────────────────────────────────────
ACCENT      = colors.HexColor('#0A2540')   # Mendel-style deep navy
ACCENT2     = colors.HexColor('#1F4E8C')
LIGHT_BG    = colors.HexColor('#EEF3FB')
DIVIDER     = colors.HexColor('#BCD0EA')
TEXT_DARK   = colors.HexColor('#15181D')
MUTED       = colors.HexColor('#5A6A80')
WHITE       = colors.white
RED_FLAG    = colors.HexColor('#B0341E')
GREEN_GO    = colors.HexColor('#1E7B4B')
AMBER       = colors.HexColor('#B07300')
ROW_ALT     = colors.HexColor('#F5F8FC')

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), 'Mendel_GTM_Playbook_May2026.pdf')

PAGE_W, PAGE_H = letter
MARGIN = 0.75 * inch
CONTENT_W = PAGE_W - 2 * MARGIN

def S(name, **kw): return ParagraphStyle(name, **kw)

TITLE_STYLE   = S('Title',  fontName='Helvetica-Bold', fontSize=30, textColor=WHITE,
                  alignment=TA_CENTER, spaceAfter=8, leading=36)
SUBTITLE_STYLE= S('Sub',    fontName='Helvetica',      fontSize=13, textColor=DIVIDER,
                  alignment=TA_CENTER, spaceAfter=4, leading=18)
COVER_META    = S('Meta',   fontName='Helvetica',      fontSize=10, textColor=DIVIDER,
                  alignment=TA_CENTER, spaceAfter=2, leading=14)
H1 = S('H1', fontName='Helvetica-Bold', fontSize=16, textColor=ACCENT,
       spaceBefore=14, spaceAfter=6, leading=20)
H2 = S('H2', fontName='Helvetica-Bold', fontSize=12, textColor=ACCENT2,
       spaceBefore=10, spaceAfter=4, leading=16)
H3 = S('H3', fontName='Helvetica-Bold', fontSize=10, textColor=ACCENT,
       spaceBefore=8, spaceAfter=3, leading=13)
BODY = S('Body', fontName='Helvetica', fontSize=9.5, textColor=TEXT_DARK,
         spaceBefore=2, spaceAfter=4, leading=14, alignment=TA_JUSTIFY)
BODY_SM = S('BodySm', fontName='Helvetica', fontSize=8.5, textColor=TEXT_DARK,
            spaceBefore=2, spaceAfter=2, leading=12)
BULLET = S('Bullet', fontName='Helvetica', fontSize=9.5, textColor=TEXT_DARK,
           spaceBefore=1, spaceAfter=3, leading=13, leftIndent=14, bulletIndent=4)
LABEL = S('Label', fontName='Helvetica-Bold', fontSize=8, textColor=ACCENT2,
          spaceBefore=0, spaceAfter=1, leading=10)
SECTION_NUM = S('SecNum', fontName='Helvetica-Bold', fontSize=8.5, textColor=ACCENT2,
                spaceBefore=0, spaceAfter=2, leading=12)
PAIN_LABEL = S('PainLabel', fontName='Helvetica-Bold', fontSize=8, textColor=RED_FLAG, leading=11)
VALUE_LABEL = S('ValLabel', fontName='Helvetica-Bold', fontSize=8, textColor=GREEN_GO, leading=11)
OUTCOME_LABEL = S('OutLabel', fontName='Helvetica-Bold', fontSize=8, textColor=ACCENT, leading=11)
AI_NOTE = S('AiNote', fontName='Helvetica-Oblique', fontSize=8.5, textColor=AMBER,
            spaceBefore=2, spaceAfter=2, leading=12, leftIndent=8)

def hr(width=CONTENT_W, color=DIVIDER, thickness=0.5):
    return HRFlowable(width=width, thickness=thickness, color=color, spaceAfter=6, spaceBefore=4)

def section_header(num, title):
    return [Spacer(1, 0.15*inch),
            Paragraph(f'SECTION {num}', SECTION_NUM),
            Paragraph(title, H1),
            hr(color=ACCENT, thickness=1.5),
            Spacer(1, 0.05*inch)]

def bullet(text):
    return Paragraph(f'•  {text}', BULLET)

def kv_table(rows, label_w=1.6*inch):
    data = [[Paragraph(k, LABEL), Paragraph(v, BODY_SM)] for k,v in rows]
    t = Table(data, colWidths=[label_w, CONTENT_W - label_w])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('ROWBACKGROUNDS', (0,0), (-1,-1), [LIGHT_BG, WHITE]),
        ('GRID', (0,0), (-1,-1), 0.3, DIVIDER),
        ('TEXTCOLOR', (0,0), (0,-1), ACCENT),
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
    ]))
    return t

def pain_value_block(pain, value, outcome):
    rows = [
        [Paragraph('PAIN', PAIN_LABEL),     Paragraph(pain,    BODY_SM)],
        [Paragraph('VALUE', VALUE_LABEL),   Paragraph(value,   BODY_SM)],
        [Paragraph('OUTCOME', OUTCOME_LABEL), Paragraph(outcome, BODY_SM)],
    ]
    t = Table(rows, colWidths=[0.85*inch, CONTENT_W - 0.85*inch])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('BACKGROUND', (0,0), (0,0), colors.HexColor('#FDECEA')),
        ('BACKGROUND', (0,1), (0,1), colors.HexColor('#E8F5EE')),
        ('BACKGROUND', (0,2), (0,2), colors.HexColor('#EBF3FC')),
        ('GRID', (0,0), (-1,-1), 0.3, DIVIDER),
    ]))
    return t

def messaging_angle_block(vertical, hook, value_lead, proof, problem_solved, subject):
    h = Table([[Paragraph(vertical, H3)]], colWidths=[CONTENT_W])
    h.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
    ]))
    rows = [['Hook', hook], ['Value Lead', value_lead], ['Proof Point', proof],
            ['Problem Solved', problem_solved], ['Subject Direction', subject]]
    data = [[Paragraph(k, LABEL), Paragraph(v, BODY_SM)] for k,v in rows]
    bt = Table(data, colWidths=[1.3*inch, CONTENT_W - 1.3*inch])
    bt.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('ROWBACKGROUNDS', (0,0), (-1,-1), [WHITE, ROW_ALT]),
        ('GRID', (0,0), (-1,-1), 0.3, DIVIDER),
        ('TEXTCOLOR', (0,0), (0,-1), ACCENT2),
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
    ]))
    return [h, bt, Spacer(1, 0.08*inch)]

# ── Page Numbering Canvas ───────────────────────────────────────────────────
class NumberedCanvas(pdfcanvas.Canvas):
    def __init__(self, *args, **kwargs):
        pdfcanvas.Canvas.__init__(self, *args, **kwargs)
        self._saved = []
    def showPage(self):
        self._saved.append(dict(self.__dict__))
        self._startPage()
    def save(self):
        n = len(self._saved)
        for s in self._saved:
            self.__dict__.update(s)
            if self._pageNumber > 1:
                self.setFont('Helvetica', 8)
                self.setFillColor(MUTED)
                self.drawCentredString(PAGE_W/2, 0.45*inch,
                    f"Mendel GTM Playbook  –  May 2026  –  Page {self._pageNumber} of {n}")
            pdfcanvas.Canvas.showPage(self)
        pdfcanvas.Canvas.save(self)

# ── Cover Page ──────────────────────────────────────────────────────────────
def cover_page():
    flow = []
    cover = Table([
        [Paragraph('', BODY)],
        [Paragraph('GO‑TO‑MARKET', SUBTITLE_STYLE)],
        [Paragraph('PLAYBOOK', TITLE_STYLE)],
        [Paragraph('', BODY)],
        [Paragraph('Mendel', S('m', fontName='Helvetica-Bold', fontSize=44,
                               textColor=WHITE, alignment=TA_CENTER, leading=50))],
        [Paragraph('Enterprise Spend Management for Latin America', SUBTITLE_STYLE)],
        [Paragraph('', BODY)],
        [Paragraph('Generated: May 4, 2026', COVER_META)],
        [Paragraph('Prepared by Outreach Magic / Kinetyca', COVER_META)],
        [Paragraph('CONFIDENTIAL  –  Internal Use Only', COVER_META)],
    ], colWidths=[CONTENT_W])
    cover.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), ACCENT),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 18),
        ('BOTTOMPADDING', (0,0), (-1,-1), 18),
    ]))
    flow.append(Spacer(1, 0.6*inch))
    flow.append(cover)
    flow.append(PageBreak())
    return flow

# ── Table of Contents ───────────────────────────────────────────────────────
def toc_page():
    items = [
        ('1', 'Client Overview',                          '3'),
        ('2', 'Unique Value Proposition & Positioning',   '4'),
        ('3', 'Social Proof & Case Studies',              '6'),
        ('4', 'Target Verticals',                         '7'),
        ('5', 'Ideal Customer Profiles & Personas',       '10'),
        ('6', 'Pain‑to‑Value Mapping',          '14'),
        ('7', 'Signals, Triggers & Timing',               '18'),
        ('8', 'Cold Email Messaging Angles',              '20'),
        ('9', 'AI‑Identified Opportunities',         '22'),
        ('A', 'Appendix – Sources & Gaps',           '23'),
    ]
    flow = [Paragraph('Table of Contents', H1), hr(color=ACCENT, thickness=1.5)]
    data = [[Paragraph(f'<b>{n}</b>', BODY),
             Paragraph(t, BODY),
             Paragraph(f'<para align=right>{p}</para>', BODY)] for n,t,p in items]
    tbl = Table(data, colWidths=[0.5*inch, CONTENT_W - 1.3*inch, 0.8*inch])
    tbl.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,-2), 0.3, DIVIDER),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    flow.append(tbl)
    flow.append(PageBreak())
    return flow

# ── SECTION 1: CLIENT OVERVIEW ──────────────────────────────────────────────
def section_1():
    flow = section_header(1, 'Client Overview')
    flow.append(Paragraph(
        "Mendel is the all-in-one corporate spend management platform built for enterprise companies "
        "in Latin America. Mendel combines corporate cards, expense reports, reimbursements, invoice "
        "payments, business travel, real-time policy controls, ERP integrations, and an AI layer into "
        "one platform for CFOs and finance teams. The product is sold as enterprise SaaS, customised by "
        "modules, scale, geography, and implementation complexity.", BODY))
    flow.append(Spacer(1, 0.08*inch))
    flow.append(kv_table([
        ('Company',         'Mendel'),
        ('Website',         'mendel.com'),
        ('Category',        'Enterprise spend management platform (LatAm)'),
        ('Core markets',    'Mexico (90% growth focus), Argentina, Chile  –  expansion across Spanish‑speaking LatAm'),
        ('Customer base',   '1,000+ large enterprises (KPMG, OXXO/FEMSA, Walmart, Suzuki, Viva Aerobus, +others)'),
        ('Avg. ACV',        'USD $15K – $20K per year ($700 – $1,800 / month)'),
        ('Sales cycle',     '3 – 6 months (some enterprise deals 12+ months)'),
        ('LTV',             'Effectively infinite – near‑zero churn'),
        ('Conversion',      'Inbound 18%, Outbound 12%, SDR prospecting 7%, WhatsApp chat 8%, Global 17%'),
        ('CRM',             'HubSpot'),
        ('Outbound stack',  'Currently: agency (black‑box) + freelancer on SmartLead. New: Outreach Magic + EmailBison + Heyreach + Zapmail infra'),
        ('Q2-2026 goal',    '100+ qualified sales meetings per quarter with target ICPs'),
    ]))
    flow.append(Spacer(1, 0.1*inch))
    flow.append(Paragraph('Product Modules', H2))
    flow.append(hr())
    products = [
        ('1. Corporate Cards + Smart Spend Controls',
         'Issues physical and virtual corporate cards for any employee, team, or BU. The differentiator is a real‑time policy engine: rules by employee, role, business unit, merchant category, country, amount, channel, day/time, expense type, budget owner, cost centre, or project. Finance approves, blocks, or flags transactions BEFORE they happen – not at month‑end.'),
        ('2. Expense Management',
         'Full expense‑report workflow automation. Employees submit receipts, invoices, and reports inside the platform. The system classifies expenses, matches receipts to card transactions, applies policy, and prepares everything for accounting. Replaces SAP Concur + Excel + email + AMEX.'),
        ('3. Mendel Viajes (Corporate Travel)',
         'Built‑in OBT certified with Sabre and Amadeus. Partnered with BCD Travel, Altour, Cocha, Travel Services, and Furlong. Flights, hotels, cars, policy enforcement, multi‑level approvals, virtual‑card payments, and expense reconciliation – all inside the same platform.'),
        ('4. ERP Integrations & Finance Automation',
         'Direct posting of card transactions, expense reports, invoices, reimbursements, and travel data into the customer’s ERP. Automates classification, cost‑centre allocation, tax docs, approvals, month‑end reconciliation, ERP posting, and audit trails. Critical for SAP S/4HANA, Oracle, and Netsuite shops.'),
        ('5. Invoice Retrieval / Recupero de Facturas (Mexico‑only)',
         'Detects card transactions missing a CFDI, automates retrieval from merchants, validates against the SAT, and matches the invoice back to the original card transaction. Documented +30% lift in deductibility. This is Mendel’s most defensible module against global competitors.'),
        ('6. AI Layer',
         'Embedded across the platform: anomaly and fraud detection, receipt/invoice intelligence (OCR + classification), WhatsApp receipt capture with auto‑matching, AI‑assisted travel booking inside policy, automated cost‑centre suggestions, and policy‑enforcement copilots for finance.'),
    ]
    for h, t in products:
        flow.append(Paragraph(h, H3))
        flow.append(Paragraph(t, BODY))
    flow.append(PageBreak())
    return flow

# ── SECTION 2: UVP & POSITIONING ───────────────────────────────────────────
def section_2():
    flow = section_header(2, 'Unique Value Proposition & Positioning')
    flow.append(Paragraph('UVP – As Stated by Mendel', H2))
    flow.append(hr())
    flow.append(Paragraph(
        "<i>“Mendel is the all‑in‑one spend management platform for enterprise companies in Latin "
        "America – combining corporate cards, expense reports, reimbursements, invoice payments, travel, "
        "real‑time policy controls, ERP integrations, and AI into one platform. We help CFOs control "
        "company spend in real time, close the month faster, reduce fraud and leakage, and recover more "
        "deductible invoices.”</i>", BODY))
    flow.append(Spacer(1, 0.08*inch))
    flow.append(Paragraph('UVP – Refined for Cold Outbound', H2))
    flow.append(hr())
    flow.append(Paragraph(
        "<b>The one platform LatAm CFOs use to control every peso in real time</b> – cards, expenses, "
        "reimbursements, invoice payments, and travel in one system, integrated with the ERP, with "
        "automatic CFDI recovery in Mexico.", BODY))
    flow.append(Spacer(1, 0.1*inch))

    flow.append(Paragraph('Three Specific Differentiators', H2))
    flow.append(hr())
    diffs = [
        ('1. One platform across all six spend modules',
         'Cards + Expenses + Reimbursements + Invoice Payments + Travel + ERP, plus an AI layer. SAP Concur + AMEX is fragmented into two systems and a card brand. Clara stops at cards + expenses for SMB / mid‑market. Edenred is prepaid HR‑benefits, not enterprise spend. No competitor in LatAm currently offers all six modules in one platform with an enterprise feature set.'),
        ('2. A real‑time policy engine that fires BEFORE the transaction',
         'Mendel does not just record what was spent – it can approve, block, or flag a transaction the moment it is attempted, based on employee, role, BU, merchant, amount, category, day/time, country, or channel. SAP Concur is post‑hoc reconciliation. Bank corporate cards expose only credit limits, not policy. Mendel turns the corporate card into a programmable enforcement layer.'),
        ('3. CFDI invoice recovery built for Mexican tax law',
         'Automated retrieval of missing CFDIs from merchants, SAT validation, and reconciliation to the original card charge. Documented +30% lift in deductibility for Mexican customers. SAP Concur and AMEX do not solve this; Clara and Edenred do not match the depth. This single module is often the #1 ROI driver for Mexican CFOs.'),
    ]
    for h, t in diffs:
        flow.append(Paragraph(h, H3))
        flow.append(Paragraph(t, BODY))
    flow.append(Spacer(1, 0.1*inch))

    flow.append(Paragraph('Lead Magnets / Content Assets Available for Outreach', H2))
    flow.append(hr())
    for b in [
        '<b>Mendel vs Concur</b> benchmark deck (PDF) – head‑to‑head on cards, expenses, travel, pricing.',
        '<b>Mendel vs Edenred</b> one‑pager (PDF) – full module / functionality comparison.',
        '<b>Mendel vs T&amp;E</b> one‑pager (PDF) – generic T&E vendors compared to Mendel.',
        '<b>Invoice Recovery one‑pager</b> – step‑by‑step CFDI retrieval flow with documented +30% deductibility uplift.',
        '<b>Mendel Viajes pitch deck</b> – corporate travel module standalone.',
        '<b>Mendel Expenses + Viajes 2026 full deck</b> – master sales deck.',
        'Customer success videos and case studies (mendel.com/blog).',
        'Prior podcast archive (CForward, paused 2023) – reusable for thought leadership clips.',
    ]:
        flow.append(bullet(b))
    flow.append(Spacer(1, 0.1*inch))

    flow.append(Paragraph('Positioning Statement', H2))
    flow.append(hr())
    flow.append(Paragraph(
        "For LatAm CFOs and finance leaders managing complex, multi‑entity, multi‑country spend, "
        "Mendel is the all‑in‑one spend management platform that replaces the fragmented stack of "
        "SAP Concur + AMEX + Excel + local invoice tools – giving them a real‑time policy engine "
        "across cards, expenses, travel, reimbursements, and invoice payments, fully integrated with their "
        "ERP and tuned for Mexican CFDI compliance.", BODY))
    flow.append(PageBreak())
    return flow

# ── SECTION 3: SOCIAL PROOF ─────────────────────────────────────────────────
def section_3():
    flow = section_header(3, 'Social Proof & Case Studies')
    flow.append(Paragraph(
        "Mendel has built a strong reference base in LatAm enterprise. The combination of household‑name "
        "logos, quantified ROI metrics, and enterprise‑grade certifications gives outbound campaigns a "
        "high‑trust footing with CFOs from day one.", BODY))
    flow.append(Spacer(1, 0.05*inch))

    flow.append(Paragraph('Customer Footprint', H2))
    flow.append(hr())
    flow.append(kv_table([
        ('Logos to cite',         'KPMG, OXXO, FEMSA, Walmart, Suzuki, Viva Aerobus, +1,000 large enterprises'),
        ('Geo coverage',          'Mexico (primary), Argentina, Colombia, Chile'),
        ('Card issuance',         'Live in Argentina and Mexico'),
        ('Industry breadth',      'Retail, CPG, professional services, energy, telecom, media, logistics, manufacturing, large tech‑enabled enterprises'),
    ]))
    flow.append(Spacer(1, 0.08*inch))

    flow.append(Paragraph('Quantified Outcomes (Mendel One‑Pager Metrics)', H2))
    flow.append(hr())
    flow.append(kv_table([
        ('Admin hours saved',     '150+ hours of administrative tasks saved per month'),
        ('Non‑deductible reduction', '+20% reduction in non‑deductible expenses'),
        ('Invoice reconciliation', '30+ hours of invoice reconciliation saved per month'),
        ('Admin cost savings',    '+US$20K saved in administrative expenses'),
        ('Deductibility lift',    '+30% increase in deductibility (CFDI recovery)'),
        ('Real‑time audit',  '100% of expenses audited in real time'),
        ('Per‑employee uplift',  '6+ hours of productivity per employee per month'),
        ('Month‑end close',  'Same‑day close (vs. prior 5+ days)'),
    ]))
    flow.append(Spacer(1, 0.08*inch))

    flow.append(Paragraph('Trust & Compliance', H2))
    flow.append(hr())
    for b in [
        'SOC 2 Type II',
        'ISO 27001',
        'PCI DSS',
        'CNBV operational security standards (Mexico)',
        'AWS hosting, end‑to‑end encryption, public Trust Center',
    ]:
        flow.append(bullet(b))
    flow.append(Spacer(1, 0.08*inch))

    flow.append(Paragraph('Travel Infrastructure Partners (Mendel Viajes)', H2))
    flow.append(hr())
    for b in [
        'Sabre + Amadeus GDS certification',
        'BCD Travel, Altour, Cocha, Travel Services, Furlong (TMC partners)',
    ]:
        flow.append(bullet(b))
    flow.append(Spacer(1, 0.08*inch))

    flow.append(Paragraph('Case‑Study Gap to Address', H2))
    flow.append(hr())
    flow.append(Paragraph(
        "Mendel has Success Story videos and named logos but few public, vertical‑specific case studies "
        "with named buyer + named outcome metrics. <b>Recommendation:</b> for the four priority verticals "
        "below, request from Alan one anonymised mini‑case (Challenge → Solution → Result with "
        "numbers) so cold copy can lead with concrete proof per industry, not just logos.", BODY))
    flow.append(PageBreak())
    return flow

# ── SECTION 4: TARGET VERTICALS ────────────────────────────────────────────
def section_4():
    flow = section_header(4, 'Target Verticals')
    flow.append(Paragraph(
        "Mendel positions itself as sector‑agnostic, but the data points to five verticals where the "
        "combination of distributed teams, complex spend, ERP density, and Mexican CFDI exposure makes "
        "the value proposition strongest. Verticals are ranked below by current evidence (logos, "
        "client‑confirmed use cases, conversion data) rather than market size alone.", BODY))
    flow.append(Spacer(1, 0.05*inch))

    verticals = [
        {
            'rank': '1', 'name': 'Retail & Consumer Goods (Mexico‑centric)',
            'why': 'Highest evidence vertical. Mendel already serves OXXO/FEMSA and Walmart – two of the largest retail/CPG operations in Mexico. The combination of distributed store networks, regional managers, supplier ecosystems, and very high CFDI volume makes this the densest value pocket Mendel can mine.',
            'size': '500+ employees, 50+ store/distribution points, USD $50M+ annual operational spend',
            'pain': 'Tracking spend across hundreds of locations and store managers; recovering CFDIs from a long tail of suppliers; petty‑cash chaos at store level; reconciling supplier payments with multi‑entity ERP; T&E for regional managers covering large territories.',
            'value': 'A single platform that gives the CFO real‑time visibility into every store’s spend, enforces policy at the merchant‑category level, automates CFDI capture from each ticket via WhatsApp, and posts everything cleanly into SAP/Oracle.',
            'signals': 'Hiring Controller / Finance Director / "Gerente de Tesoreria"; new store openings or DC launches; SAP/Oracle ERP migration; references to SAT CFDI 4.0 compliance pain; agreements with new suppliers/distributors.',
            'confidence': 'Client‑confirmed (active customers, named logos)',
        },
        {
            'rank': '2', 'name': 'Logistics & Transportation',
            'why': 'Client surfaced this vertical specifically: "a large logistics operator can use our card controls to manage their fleets (fuel, repairs, etc)." Viva Aerobus is an existing logo. The fleet/per‑diem use case gives Mendel a sharper angle than generic spend management.',
            'size': '200+ vehicles in road logistics, OR 10+ aircraft in aviation, OR 50+ drivers',
            'pain': 'Reconciling fuel and repair spend across hundreds of vehicles; controlling driver per‑diems and tolls; route‑by‑route cost allocation; fraud risk on fleet cards; CFDI recovery from gas stations and repair shops.',
            'value': 'Granular per‑vehicle / per‑driver / per‑route policy rules, real‑time fraud blocks, automatic CFDI retrieval from fuel and repair merchants, and ERP‑ready cost‑centre allocation by route.',
            'signals': 'Fleet expansion announcements; new route launches; hiring Fleet Manager / Operations Director; switching off legacy fuel‑card programs (Edenred Fleet, e.g.); nearshoring‑driven trucking buildouts.',
            'confidence': 'Client‑confirmed use case + Viva Aerobus logo',
        },
        {
            'rank': '3', 'name': 'Manufacturing & Industrial',
            'why': 'High vendor invoicing density, multi‑plant operations, complex ERP environments, and Mexico’s nearshoring boom make manufacturing a structural fit. Vendor invoice payments + ERP integration are core Mendel modules and the natural buying centre for a finance VP in a multi‑plant operation.',
            'size': '1,000+ employees, 2+ plants in Mexico/LatAm, multi‑entity finance structure',
            'pain': 'Vendor invoice payment cycles; cost‑centre allocation across plants; multi‑plant T&E governance; long ERP reconciliation cycles in SAP S/4HANA; CFDI compliance across hundreds of suppliers.',
            'value': 'A single posting layer into the ERP that classifies, allocates, and reconciles spend by plant and cost centre, with real‑time invoice approval workflows.',
            'signals': 'ERP migration projects (SAP S/4HANA, Oracle Cloud, Netsuite); nearshoring announcements; new plant openings; hiring "Procure‑to‑Pay Manager" or "Cost Controller"; M&A with a target in MX/LatAm.',
            'confidence': 'Client‑confirmed sector fit',
        },
        {
            'rank': '4', 'name': 'Pharmaceutical & Healthcare',
            'why': 'Client surfaced this specifically: "a pharmaceutical company can give their sales team a Mendel card for when they travel to congresses, conferences, inviting doctors to dine out". Compliance‑sensitive T&E and HCP‑entertainment policy is a sharply differentiated angle for the policy engine.',
            'size': '100+ medical reps in MX/LatAm, OR 500+ employees in healthcare services',
            'pain': 'Compliance‑sensitive T&E (anti‑bribery, HCP transparency); rep dining and gift policy enforcement; congress/conference travel approvals; reimbursing reps weeks after the fact creating cash‑flow friction; CFDI capture from dozens of restaurants and hotels per rep per month.',
            'value': 'Pre‑transaction policy enforcement on HCP‑entertainment limits, automatic itemised reporting for compliance, and CFDI recovery for every dinner and hotel night.',
            'signals': 'Hiring Compliance Officer or Medical Affairs Director; congress sponsorships; medical liaison hires; product launches in MX/LatAm; transparency‑reporting season.',
            'confidence': 'Client‑confirmed use case',
        },
        {
            'rank': '5', 'name': 'Professional Services (Consulting / Audit / Legal)',
            'why': 'KPMG is an existing logo. Heavy partner/manager travel, billable client expenses, and multi‑country engagements make Mendel an obvious fit. Travel Manager persona becomes an additional buying centre via Mendel Viajes.',
            'size': '500+ consultants/auditors/lawyers, regional client travel base',
            'pain': 'Capturing billable expenses for client invoicing; partner–manager–staff approval chains; currency complexity in multi‑country engagements; distinguishing reimbursable vs. non‑reimbursable expenses; lost CFDIs that erode the firm’s own deductibility.',
            'value': 'Tag‑by‑engagement expense capture, multi‑currency, multi‑country approval flows, virtual cards per engagement, and ERP‑ready data for billing.',
            'signals': 'New office openings; large engagement announcements; hiring Engagement Operations Manager / Travel Manager; partner promotions; nearshoring‑advisory boom in MX.',
            'confidence': 'Client‑confirmed (KPMG logo)',
        },
    ]
    for v in verticals:
        flow.append(Spacer(1, 0.06*inch))
        flow.append(Paragraph(f"#{v['rank']}  {v['name']}", H2))
        flow.append(hr())
        flow.append(kv_table([
            ('Why this vertical', v['why']),
            ('Size sweet spot',   v['size']),
            ('Vertical pain',     v['pain']),
            ('Value angle',       v['value']),
            ('Buying signals',    v['signals']),
            ('Confidence',        v['confidence']),
        ]))
    flow.append(PageBreak())
    return flow

# ── SECTION 5: PERSONAS ────────────────────────────────────────────────────
def section_5():
    flow = section_header(5, 'Ideal Customer Profiles & Personas')
    flow.append(Paragraph(
        "The CFO is the consistent primary buyer across every vertical. The Controller is the operational "
        "co‑decider in nearly every deal. Beyond those two, each vertical surfaces a third persona "
        "who sponsors specific modules – Shared Services for retail, Fleet Operations for logistics, "
        "Procurement for manufacturing, Compliance for pharma, Travel Manager for professional services. "
        "All targeting filters should require a Mexican (or LatAm) entity for relevance.", BODY))
    flow.append(Spacer(1, 0.05*inch))

    personas = [
        # Cross-vertical
        {
            'name': 'CFO / Director de Finanzas',
            'titles': '"Chief Financial Officer", "CFO", "Director de Finanzas", "Director Financiero", "VP Finance LatAm", "Finance Director Mexico"',
            'where': 'All verticals; companies 500+ employees in Mexico / LatAm',
            'reality': 'Owns month‑end close, cash management, board reporting, and audit. Spends days reconciling spend that lives across AMEX statements, Concur, ERP, supplier portals, and Excel. Carries the blame for fraud or audit findings.',
            'metrics': 'Days to close, audit findings, deductible expense %, EBITDA, days payable outstanding, fraud incidents',
            'frustration': 'Detecting policy violations and fraud only at month‑end; chasing CFDIs after the fact; explaining variances to the board for spend they have no real‑time view of.',
            'budget': 'Owns budget. Final yes/no on enterprise SaaS. Often signs alongside CEO/Audit Committee for >$50K ACV.',
            'go':  'Recently appointed (90‑day window); LatAm regional CFO with multi‑country scope; quoted in press about "controls" or "modernisation"; company in audit/compliance review.',
            'skip': 'Pure US/EU CFO with no LatAm responsibility; CFO at &lt;100‑employee company; CFO at existing Mendel customer.',
        },
        {
            'name': 'Controller / Contralor',
            'titles': '"Controller", "Contralor", "Corporate Controller", "Group Controller", "Finance Operations Director"',
            'where': 'All verticals; usually one per legal entity in companies 500+ employees',
            'reality': 'Operational owner of the close cycle and policy enforcement. Manages the Concur/AMEX/Excel stack day‑to‑day. Coordinates with auditors, tax, and ERP teams.',
            'metrics': 'Close cycle days, % expenses with valid CFDI, exception count, ERP posting accuracy, audit prep hours',
            'frustration': 'Manually chasing receipts and invoices from employees; reconciling card statements line‑by‑line; building the same exception report every month.',
            'budget': 'Heavy influence; rarely the sole approver. Champions the procurement evaluation.',
            'go':  'Posting jobs for "AP analyst", "expense analyst", "month‑end close associate"; new ERP module rollouts; hiring around year‑end audit.',
            'skip': 'Controller at company already on Mendel; Controller in pure‑services single‑country firm with <100 employees.',
        },
        {
            'name': 'Procurement / Purchasing Director',
            'titles': '"Director of Procurement", "Director de Compras", "Procurement Manager", "Procure‑to‑Pay Manager", "Sourcing Director"',
            'where': 'Manufacturing, Retail/CPG, Logistics, Healthcare; 500+ employees with structured P2P',
            'reality': 'Owns vendor onboarding, PO issuance, and the AP‑side workflow. Sits between Finance and the business units. Often leads RFPs for tools like Mendel.',
            'metrics': 'Cycle time PO‑to‑payment, vendor compliance %, contract savings, supplier disputes',
            'frustration': 'Vendor invoices in 8 different formats; mismatch between PO, GR, and invoice; manual three‑way matching; supplier complaints about late payments.',
            'budget': 'Co‑approver on procurement‑led RFPs; champions the integration requirements.',
            'go':  'Active P2P RFP; new ERP rollout; supplier portal complaints; hiring AP/sourcing roles.',
            'skip': 'Procurement role with no link to expense or invoice payments; indirect‑only purchasing.',
        },
        # Vertical-specific
        {
            'name': 'Shared Services / Finance Operations Manager (Retail/CPG)',
            'titles': '"Shared Services Manager", "Finance Operations Manager", "Gerente de Servicios Compartidos", "Head of Finance Shared Services LatAm"',
            'where': 'Retail / CPG companies running shared‑service centres in MX/LatAm',
            'reality': 'Runs the AP/AR/Expense factory for hundreds or thousands of stores. Daily user of Concur or Excel. Owns the volume – thousands of expense lines per month.',
            'metrics': 'Lines processed per FTE, exception rate, CFDI capture rate per region, on‑time payment %',
            'frustration': 'Processing 10K+ low‑value retail tickets per month, most without a CFDI; chasing store managers for receipts; manual classification by cost centre.',
            'budget': 'Heavy operational influence; champions automation cases.',
            'go':  'New shared‑service centre opening; automation initiatives announced; hiring "RPA / automation lead".',
            'skip': 'Shared services at a non‑retail company.',
        },
        {
            'name': 'Fleet / Operations Director (Logistics)',
            'titles': '"Fleet Manager", "Director de Operaciones", "Operations Director", "Logistics Operations Manager", "Director de Flota"',
            'where': 'Trucking, courier, last‑mile, aviation; 200+ vehicles or 10+ aircraft',
            'reality': 'Manages fuel cards, repair vendors, driver per‑diems, tolls, and route economics. Owns the cost line that the CFO sees as the biggest variable expense.',
            'metrics': 'Cost per km, fuel‑card fraud rate, vehicle uptime, driver per‑diem variance',
            'frustration': 'Drivers using fuel cards off‑route; repair invoices without CFDI; manual reconciliation of fuel cards against route plans.',
            'budget': 'Sponsors the operational case; co‑decides with CFO.',
            'go':  'Fleet expansion; new route launches; switching from legacy fuel‑card programs; nearshoring trucking buildouts.',
            'skip': 'Fleet roles in companies with <50 vehicles.',
        },
        {
            'name': 'Compliance / Medical Affairs Director (Pharma)',
            'titles': '"Compliance Officer", "Medical Affairs Director", "Director de Cumplimiento", "Ethics & Compliance Lead LatAm"',
            'where': 'Pharma, medical devices, healthcare services in MX/LatAm',
            'reality': 'Owns transparency reporting on HCP interactions, gift/dining limits, and audit response. Often blocked from real‑time data by the rep‑expense reimbursement workflow.',
            'metrics': 'Transparency report completeness, policy‑breach incidents, audit findings, time‑to‑report',
            'frustration': 'No real‑time view of what reps are spending on HCPs; reimbursements arriving 30+ days after the dinner; impossible to enforce limits before the spend happens.',
            'budget': 'Strong influence on policy module + pre‑transaction enforcement features.',
            'go':  'Transparency‑reporting season; recent audit; new product launch with field‑force expansion; HCP‑incident press.',
            'skip': 'Compliance roles in industries with no HCP‑equivalent risk.',
        },
        {
            'name': 'Travel Manager / Procurement Travel Lead (Professional Services + Pharma)',
            'titles': '"Travel Manager", "Corporate Travel Manager", "Director de Viajes", "Procurement Travel Lead", "Travel & Expense Manager"',
            'where': 'Professional services (consulting, audit, legal), pharma, large enterprises with 500+ travellers',
            'reality': 'Owns the OBT/TMC relationship, travel policy, and traveller experience. Caught between cost pressure from Finance and convenience pressure from partners/reps.',
            'metrics': 'Policy compliance %, average ticket cost, leakage rate (out‑of‑tool bookings), traveller NPS',
            'frustration': 'Travellers booking outside the tool because the legacy OBT is slow; payment via personal card and reimbursement; no visibility on travel‑tied expenses (Uber, dinners, hotels) until weeks later.',
            'budget': 'Sole or co‑decider on Mendel Viajes; brings Finance into the deal.',
            'go':  'OBT contract renewals (typically 12–24 months); TMC rebid; complaints in employee surveys about travel tooling; new office or engagement openings.',
            'skip': 'Travel managers at companies with <100 travellers; agencies acting as TMCs.',
        },
        {
            'name': 'Sales Operations / Field‑Force Operations Director (Pharma)',
            'titles': '"Sales Operations Director", "Director de Ventas Field", "Field‑Force Operations Lead", "Commercial Excellence Director"',
            'where': 'Pharma, medical devices with 100+ field reps',
            'reality': 'Equips and supports the rep force. Owns the rep‑expense workflow operationally even when Finance owns the policy. Blamed when reps complain or compliance breaks.',
            'metrics': 'Rep productivity, days‑to‑reimburse, compliance incident rate, rep churn',
            'frustration': 'Reps fronting cash for HCP dinners and waiting weeks for reimbursement; expense reports eating selling time; compliance team blocking spend mid‑cycle.',
            'budget': 'Strong influence; co‑sponsor with Finance / Compliance.',
            'go':  'Field‑force expansion; new product launch; rep retention initiatives; complaints in Glassdoor about expense reimbursements.',
            'skip': 'Sales ops at companies with no field reimbursement workflow.',
        },
        {
            'name': 'Engagement Operations Manager (Professional Services)',
            'titles': '"Engagement Operations Manager", "Engagement Manager Operations", "Practice Operations Director", "Resource & Operations Manager"',
            'where': 'Big 4, top‑tier consulting, large law firms; 500+ billable staff',
            'reality': 'Owns engagement P&L hygiene. Cares about billable expense capture, write‑offs, and clean cost‑by‑engagement reporting.',
            'metrics': 'Realisation rate, billable expense capture %, write‑off rate, days from spend‑to‑client‑invoice',
            'frustration': 'Billable expenses not tagged correctly; write‑offs because the receipt is lost; engagement P&L incomplete at month‑end.',
            'budget': 'Strong influence on engagement‑centric features (per‑engagement virtual cards, tagging, billable export).',
            'go':  'New large engagements announced; partner promotions; engagement‑management software RFP; growth in advisory practice.',
            'skip': 'Operations roles at firms with <500 billable staff.',
        },
        {
            'name': 'Cost Controller / Plant Finance Manager (Manufacturing)',
            'titles': '"Cost Controller", "Plant Finance Manager", "Controller de Planta", "Finance Manager – Plant", "Manufacturing Finance Director"',
            'where': 'Multi‑plant manufacturing in MX/LatAm; 1,000+ employees',
            'reality': 'Controls cost per plant; tracks variances against budget; owns vendor invoice flow at plant level. ERP‑heavy day.',
            'metrics': 'Cost variance vs. budget, vendor on‑time payment %, plant close days, CFDI capture by supplier',
            'frustration': 'Vendor invoices arriving in fragmented formats; plant‑level CFDI gaps; differences between SAP postings and AMEX statements; T&E for plant managers untracked.',
            'budget': 'Strong influence; champions the ERP‑integration story.',
            'go':  'New plant openings; ERP module rollouts; cost‑saving initiatives; nearshoring growth at the plant level.',
            'skip': 'Plant roles in single‑plant operations or non‑LatAm only.',
        },
    ]
    for p in personas:
        flow.append(Spacer(1, 0.06*inch))
        flow.append(Paragraph(p['name'], H2))
        flow.append(hr())
        flow.append(kv_table([
            ('Job titles',           p['titles']),
            ('Where they exist',     p['where']),
            ('Daily reality',        p['reality']),
            ('Metrics they own',     p['metrics']),
            ('Biggest frustration',  p['frustration']),
            ('Budget authority',     p['budget']),
            ('✅ Target when',   p['go']),
            ('❌ Skip when',     p['skip']),
        ]))
    flow.append(PageBreak())
    return flow

# ── SECTION 6: PAIN-TO-VALUE MAPPING ───────────────────────────────────────
def section_6():
    flow = section_header(6, 'Pain‑to‑Value Mapping')
    flow.append(Paragraph(
        "Each pain below references a specific role, activity, or metric and maps to a Mendel module that "
        "delivers a quantifiable outcome – the foundation for every cold email hook.", BODY))
    flow.append(Spacer(1, 0.05*inch))

    blocks = [
        # CFO
        ('CFO / Director de Finanzas',
         [('Detecting policy violations and fraud only at month‑end, after the money is gone, because Concur posts after the fact and AMEX shows only a credit limit.',
           'Real‑time policy engine on the corporate card that approves, blocks, or flags transactions before they post, with rules per role, BU, merchant, amount, and country.',
           'From "find fraud at close" to "block fraud at swipe"  –  +20% reduction in non‑deductible/out‑of‑policy spend reported by Mendel customers.'),
          ('Month‑end close runs 5+ days because card transactions, Concur expenses, AMEX statements, and supplier invoices live in disconnected systems and none post cleanly to SAP/Oracle.',
           'A single platform that consolidates cards, expenses, reimbursements, invoice payments, and travel and posts directly to the ERP with pre‑classified cost centres.',
           'Same‑day month‑end close (vs. prior 5 days) with audit‑ready data already in the ERP.'),
          ('Mexican operations losing 20–30% of corporate spend to non‑deductibility because employees never recover CFDIs from Uber, OXXO, gas stations, restaurants, and small suppliers.',
           'Automated CFDI retrieval module that detects missing invoices, pulls them from merchant portals, validates against the SAT, and matches them to the original card transaction.',
           '+30% lift in deductible expenses, directly improving EBITDA and reducing audit risk.'),
         ]),
        # Controller
        ('Controller / Contralor',
         [('Manually building the same exception report every month – transactions without CFDI, transactions out of policy, missing receipts, missing categorisation – across 4+ tools.',
           'Single dashboard with all exceptions auto‑classified, plus AI‑assisted receipt and invoice intelligence that flags missing/non‑compliant items as they happen.',
           '30+ hours of invoice reconciliation saved per month and 100% of expenses audited in real time.'),
          ('Chasing employees on Slack/email for receipts and invoices weeks after the fact, then cross‑matching them to AMEX statement lines.',
           'WhatsApp receipt capture: employees send a photo, AI extracts and matches automatically to the corresponding card transaction; finance gets a clean record without chasing.',
           '6+ hours of admin saved per employee per month and a measurable lift in receipt capture rate.'),
          ('Approval queues blocking the close because cost‑centre allocation is manual and ambiguous between business units.',
           'Mapping engine for cost centre + GL account + business unit, applied automatically by Mendel from the moment of the transaction.',
           'Approvals shifted from "manual triage at month‑end" to "exception‑only review during the month".'),
         ]),
        # Shared Services Retail
        ('Shared Services / Finance Ops Manager (Retail/CPG)',
         [('Processing 10,000+ low‑value tickets per month from hundreds of stores, most missing CFDIs and improperly categorised by store managers using personal cards.',
           'Issue Mendel cards to every store manager with merchant‑category limits and automatic CFDI recovery for every ticket.',
           '150+ admin hours saved per month and a measurable rise in CFDI capture across the store network.'),
          ('Reconciling supplier payments with multi‑entity ERP across 5+ legal entities and 3 countries.',
           'Multi‑entity, multi‑currency platform with native ERP posting per entity.',
           'A single supplier payment workflow replacing the entity‑by‑entity manual loops.'),
          ('Petty cash chaos at store level – cash boxes, ad‑hoc reimbursements, and missing receipts.',
           'Eliminating petty cash by issuing virtual or physical Mendel cards to store managers with policy controls.',
           'Petty‑cash leakage eliminated and visibility on every peso spent in real time.'),
         ]),
        # Fleet
        ('Fleet / Operations Director (Logistics)',
         [('Drivers using fuel cards off‑route or for repairs at non‑approved vendors with no real‑time block.',
           'Per‑vehicle / per‑driver / per‑route policy rules that block off‑policy fuel spend at the moment of swipe.',
           'Drop in fleet‑card fraud incidents and a clean cost‑per‑km figure at the route level.'),
          ('Repair invoices arriving without CFDI, eroding deductibility on a major variable cost line.',
           'Automatic CFDI retrieval from repair vendors and gas stations with SAT validation.',
           '+30% deductibility lift on repair and fuel categories.'),
          ('Manual reconciliation of 100+ fuel‑card lines per week against route plans, done in Excel by an analyst.',
           'Native cost‑centre allocation by route, with ERP‑ready data and AI categorisation.',
           'Analyst time freed up; reconciliation goes from days to minutes.'),
         ]),
        # Compliance Pharma
        ('Compliance / Medical Affairs Director (Pharma)',
         [('Reps reimbursed weeks after dining HCPs, with no real‑time visibility on whether the spend respects HCP‑interaction limits.',
           'Pre‑transaction policy enforcement on HCP‑entertainment categories, by rep, by region, by amount, with itemised reporting for transparency disclosures.',
           'Compliance breaches caught before they happen, transparency report assembled from clean source data.'),
          ('Transparency reports built manually from receipts and Excel, with gaps and disputes from rep memory.',
           'A single source of truth for every HCP‑tied transaction, with structured data and CFDI documentation.',
           'Transparency report compilation reduced from weeks to days, audit‑ready output.'),
          ('Reps using personal cards because corporate cards are reserved for senior leadership, creating cash‑flow friction and reimbursement disputes.',
           'Issuing Mendel cards to every rep with built‑in policy enforcement and automated reimbursement workflows.',
           'Eliminated personal‑card friction and improved rep retention via better expense experience.'),
         ]),
        # Travel Manager
        ('Travel Manager (Pro Services / Pharma)',
         [('Travellers booking outside the legacy OBT because it is slow and bureaucratic, creating leakage on negotiated rates.',
           'Mendel Viajes built‑in OBT (Sabre + Amadeus certified, BCD/Altour/Cocha/TS/Furlong partnered) with policy enforcement and AI‑assisted search.',
           'Higher in‑tool booking rate and cleaner negotiated‑rate utilisation.'),
          ('Travellers paying with personal cards and waiting weeks for reimbursement, generating complaints in employee surveys.',
           'Virtual‑card payment for every booking, with reconciliation back to the engagement / cost centre automatically.',
           'Reimbursement friction eliminated and traveller NPS lifted.'),
          ('No visibility on travel‑tied expenses (Uber, dinners, hotels) until weeks after the trip, breaking budget tracking.',
           'Real‑time spend on travel‑associated expenses tied to the original trip ID, with policy enforcement.',
           'Trip‑level P&L available the day the trip ends.'),
         ]),
        # Engagement Ops
        ('Engagement Operations Manager (Pro Services)',
         [('Billable expenses lost to write‑offs because receipts disappear, miscategorised expenses, or missing CFDI.',
           'Per‑engagement virtual cards, automatic tagging by engagement, and CFDI capture at swipe.',
           'Lower write‑off rate and faster spend‑to‑client‑invoice cycle.'),
          ('Engagement P&L incomplete at month‑end because expenses post late and unallocated.',
           'Real‑time engagement‑tagged spend with ERP posting cleanly mapped to the engagement code.',
           'Same‑day engagement P&L; partners can run pricing decisions on live data.'),
          ('Multi‑country engagements with currency conversion ambiguity and reconciliation pain.',
           'Native multi‑currency, multi‑country platform with consistent reporting standards.',
           'Multi‑country engagements run as cleanly as single‑country ones.'),
         ]),
        # Cost Controller Manufacturing
        ('Cost Controller / Plant Finance Manager (Manufacturing)',
         [('Vendor invoices arriving in 8 different formats with no automated three‑way match against PO and goods receipt.',
           'Mendel’s invoice payments + ERP integration combined with AI invoice intelligence to extract, classify, and three‑way match automatically.',
           'Vendor invoice cycle compressed and supplier dispute volume reduced.'),
          ('Plant‑level CFDI gaps eroding deductibility on indirect spend (MRO, services, T&E).',
           'CFDI retrieval module covering plant‑level merchants and services.',
           '+30% deductibility lift on indirect plant spend.'),
          ('SAP postings inconsistent with AMEX statements forcing manual reconciliation each close.',
           'Direct posting from Mendel into SAP S/4HANA with cost‑centre and GL pre‑classified.',
           'Reconciliation eliminated; single source of truth between transaction and ERP.'),
         ]),
    ]
    for persona, items in blocks:
        flow.append(Spacer(1, 0.05*inch))
        flow.append(Paragraph(persona, H2))
        flow.append(hr())
        for pain, val, out in items:
            flow.append(pain_value_block(pain, val, out))
            flow.append(Spacer(1, 0.03*inch))
    flow.append(PageBreak())
    return flow

# ── SECTION 7: SIGNALS, TRIGGERS, TIMING ──────────────────────────────────
def section_7():
    flow = section_header(7, 'Signals, Triggers & Timing')
    flow.append(Paragraph(
        "Buying signals below are ranked from most to least actionable for outbound list‑building. "
        "Wherever possible, criteria are written as Apollo, LinkedIn Sales Navigator, or job‑board "
        "filters that the targeting engine can apply at scale.", BODY))
    flow.append(Spacer(1, 0.05*inch))

    flow.append(Paragraph('Hiring Signals (Highest Actionability)', H2))
    flow.append(hr())
    for b in [
        'New CFO / Controller / Finance Director appointed in the last 90 days with Mexico / LatAm responsibility.',
        'Active job posts with titles "Procure‑to‑Pay Manager", "AP Manager", "Expense Analyst", "Month‑End Close Lead", "Cost Controller", "Compliance Officer", "Travel Manager".',
        'Job descriptions mentioning "CFDI", "Concur", "AMEX corporate", "expense reconciliation", "month‑end close", "policy enforcement", "vendor invoice management".',
        'Field‑force expansion in pharma (medical reps, KAMs).',
        'Fleet manager / operations director hires in logistics.',
        'Engagement operations / travel manager hires in professional services.',
    ]:
        flow.append(bullet(b))
    flow.append(Spacer(1, 0.06*inch))

    flow.append(Paragraph('Tech Stack & Vendor Signals', H2))
    flow.append(hr())
    for b in [
        '<b>Replacement targets:</b> SAP Concur + AMEX corporate cards → Mendel positions as one‑platform consolidation with LatAm depth.',
        '<b>Upgrade target:</b> Clara on file → Mendel positions as the enterprise tier (deeper controls, ERP, travel, multi‑country).',
        '<b>Modernisation target:</b> Edenred (prepaid) → Mendel positions as credit‑based with full spend management.',
        '<b>Fit signal:</b> ERP = SAP S/4HANA, Oracle Cloud, Netsuite, Microsoft Dynamics F&O – native integration story.',
        'Visible CFDI 4.0 compliance pain on LinkedIn / blog / job descriptions.',
    ]:
        flow.append(bullet(b))
    flow.append(Spacer(1, 0.06*inch))

    flow.append(Paragraph('Company Event Triggers', H2))
    flow.append(hr())
    for b in [
        'Funding rounds in Mexico / LatAm (Series B+).',
        'Multi‑country expansion or new market entry into Mexico, Argentina, Chile.',
        'New plant, store, distribution centre, or office openings.',
        'M&A activity with a target in Mexico / LatAm.',
        'IPO announcements driving control / audit modernisation.',
        'ERP migration or upgrade projects (SAP S/4HANA migrations are top‑tier).',
        'Press coverage of fraud incidents, audit findings, or compliance failures.',
    ]:
        flow.append(bullet(b))
    flow.append(Spacer(1, 0.06*inch))

    flow.append(Paragraph('Industry & Regulatory Triggers', H2))
    flow.append(hr())
    for b in [
        'New SAT regulations or CFDI version updates in Mexico.',
        'Tax reform announcements affecting deductibility rules.',
        'Anti‑bribery / transparency reporting cycles in pharma.',
        'Nearshoring announcements driving manufacturing buildouts in Mexico.',
    ]:
        flow.append(bullet(b))
    flow.append(Spacer(1, 0.06*inch))

    flow.append(Paragraph('Stop Signals (Do NOT Contact)', H2))
    flow.append(hr())
    for b in [
        '<b>Already a Mendel customer</b> – cross‑check HubSpot before adding to outbound list.',
        '<b>Recently churned or cancelled</b> from any Mendel partner / agency outbound effort – use the agency "do‑not‑contact" list once shared.',
        '<b>Headquartered outside LatAm with no LatAm subsidiary</b> – even if logo is iconic.',
        '<b>Under 100 employees</b> – below ICP for enterprise spend.',
        '<b>Family‑owned micro‑businesses</b> with no finance team beyond the owner.',
        '<b>Existing Concur+AMEX bundle just renewed (within 6 months)</b> – timing wrong; recycle in 6–9 months.',
    ]:
        flow.append(bullet(b))
    flow.append(PageBreak())
    return flow

# ── SECTION 8: MESSAGING ANGLES ───────────────────────────────────────────
def section_8():
    flow = section_header(8, 'Cold Email Messaging Angles')
    flow.append(Paragraph(
        "Two to three messaging angles per priority vertical. Each angle is a self‑contained "
        "hook → value lead → proof → problem solved → subject‑line direction. Subject "
        "lines respect Outreach Magic rules: max three words, lowercase except company / person names. "
        "Body length 50–80 words. Lead magnet = one of the public benchmark PDFs; offer = a 30‑day "
        "spend‑leakage assessment for the prospect.", BODY))
    flow.append(Spacer(1, 0.06*inch))

    angles = [
        ('Retail / CPG – angle 1: store‑network spend visibility',
         'reconciling 10,000+ store tickets per month with most missing a CFDI',
         'one card per store manager with merchant‑category limits and automatic CFDI capture',
         'OXXO/FEMSA and Walmart run their store networks on Mendel; +30% deductibility lift typical.',
         'manual reconciliation across hundreds of stores and a long supplier tail',
         'store ctrl'),
        ('Retail / CPG – angle 2: same‑day close',
         'closing the books in 5+ days because card transactions, Concur, and AMEX statements never agree',
         'a single platform that posts cards, expenses, invoices, reimbursements, and travel directly to your ERP',
         '150+ admin hours saved per month, same‑day month‑end close.',
         'multi‑system reconciliation chaos at close',
         'close cycle'),
        ('Logistics – angle 1: fleet‑card fraud at swipe',
         'fuel‑card fraud and off‑route swipes detected only at month‑end',
         'per‑driver / per‑route real‑time policy rules that block fraud at the moment of swipe',
         'Viva Aerobus runs fleet‑class card controls on Mendel.',
         'fuel and repair leakage on the largest variable cost line',
         'fleet swipe'),
        ('Logistics – angle 2: deductibility on fuel and repairs',
         'losing 20–30% of fleet spend to non‑deductibility because gas stations and repair shops never deliver CFDIs',
         'automated CFDI retrieval from fuel + repair merchants with SAT validation',
         '+30% deductibility lift on repair and fuel categories.',
         'invisible deductibility leakage hitting EBITDA',
         'fleet CFDI'),
        ('Manufacturing – angle 1: ERP‑clean spend',
         'SAP postings inconsistent with AMEX statements every close',
         'direct posting from Mendel into SAP S/4HANA with cost‑centre and GL already classified',
         'plants closing same‑day with audit‑ready data in ERP.',
         'multi‑plant reconciliation pain',
         'SAP posting'),
        ('Manufacturing – angle 2: vendor invoice cycle',
         'vendor invoices in eight different formats and three‑way matching by hand',
         'AI invoice intelligence + ERP integration handling extraction, classification, and matching',
         '30+ hours of invoice reconciliation saved per month.',
         'AP backlog and supplier disputes',
         'vendor cycle'),
        ('Pharma – angle 1: HCP entertainment policy at swipe',
         'reps dining HCPs without a real‑time check on policy limits',
         'pre‑transaction enforcement of HCP‑entertainment limits, by rep, region, and amount',
         'transparency reports built from clean source data, audit‑ready in days.',
         'compliance breaches found weeks after the dinner',
         'HCP policy'),
        ('Pharma – angle 2: rep cash‑flow friction',
         'reps fronting cash for HCP dinners and waiting weeks to be reimbursed',
         'a Mendel card per rep with embedded policy and automatic reimbursement workflows',
         '6+ hours saved per rep per month, complaints about reimbursement gone.',
         'rep retention pain and lost selling time',
         'rep cards'),
        ('Pro Services – angle 1: billable expense capture',
         'billable expenses written off because receipts disappear',
         'per‑engagement virtual cards with automatic tagging and CFDI capture at swipe',
         'engagement P&L same‑day, less write‑off; KPMG already on Mendel.',
         'realisation rate eroded by lost expenses',
         'billable capture'),
        ('Pro Services – angle 2: travel + expense in one',
         'travellers booking outside the OBT and paying on personal cards',
         'Mendel Viajes (Sabre + Amadeus certified, BCD/Altour partnered) plus Mendel cards in one platform',
         'higher in‑tool booking, traveller NPS lifted, trip‑level P&L same‑day.',
         'OBT leakage and traveller reimbursement friction',
         'travel ops'),
    ]
    for v, h, vl, p, ps, s in angles:
        for f in messaging_angle_block(v, h, vl, p, ps, s):
            flow.append(f)
    flow.append(PageBreak())
    return flow

# ── SECTION 9: AI-IDENTIFIED OPPORTUNITIES ─────────────────────────────────
def section_9():
    flow = section_header(9, 'AI‑Identified Opportunities')
    flow.append(Paragraph(
        "Hypotheses surfaced by the model that the client has not explicitly validated. Treat as starting "
        "points for the next strategy call, not committed strategy.", BODY))
    flow.append(Spacer(1, 0.05*inch))

    flow.append(Paragraph('Telecom (Mexican Carriers + Subsidiaries)', H2))
    flow.append(hr())
    flow.append(Paragraph(
        "Mendel’s assessment lists telecom as a fit sector but no anchor logo has been confirmed. "
        "Mexican carriers have very high T&E (technician fleets), heavy supplier ecosystems, and SAT "
        "exposure – the same density that makes retail strong. Telmex / AT&T / Megacable spinoffs and "
        "regional ISPs are likely high‑fit accounts to test in a focused vertical campaign.", BODY))
    flow.append(Paragraph('Status: <i>Unvalidated by client</i>', AI_NOTE))
    flow.append(Spacer(1, 0.05*inch))

    flow.append(Paragraph('Energy & Utilities (Distributed Field Operations)', H2))
    flow.append(hr())
    flow.append(Paragraph(
        "Solar/wind project developers, oil & gas service providers, and regional utilities have the "
        "logistics + manufacturing pattern doubled: distributed field crews, fleet cards, vendor invoicing "
        "in remote regions, and high CFDI exposure. Worth a vertical experiment after Q2.", BODY))
    flow.append(Paragraph('Status: <i>Unvalidated by client</i>', AI_NOTE))
    flow.append(Spacer(1, 0.05*inch))

    flow.append(Paragraph('Tech‑Enabled Enterprises (LatAm Scaleups)', H2))
    flow.append(hr())
    flow.append(Paragraph(
        "Series B/C LatAm scaleups (Kavak, Cornershop alumni, fintech, healthtech) hire LatAm CFOs early, "
        "are SAP‑less or migrating to Netsuite, and bleed cash on disconnected stacks of Mexican fintech "
        "cards + Excel. The pitch shifts to "
        "“we scale with you” rather than “replace your stack.”", BODY))
    flow.append(Paragraph('Status: <i>Unvalidated by client</i>', AI_NOTE))
    flow.append(Spacer(1, 0.05*inch))

    flow.append(Paragraph('Family Offices & Multi‑Entity Holdings', H2))
    flow.append(hr())
    flow.append(Paragraph(
        "Large Mexican family‑owned holdings (5–20 operating companies) face cross‑entity spend "
        "pain that Mendel’s multi‑entity architecture handles natively. Approach via the holding’s "
        "Group CFO or Head of Family Office Operations.", BODY))
    flow.append(Paragraph('Status: <i>Unvalidated by client</i>', AI_NOTE))
    flow.append(Spacer(1, 0.05*inch))

    flow.append(Paragraph('Re‑Engagement of Old Clay Tables + HubSpot Inbound', H2))
    flow.append(hr())
    flow.append(Paragraph(
        "On the onboarding call Alan flagged "
        "“old Clay tables we are not using anymore” and “lots of info in HubSpot.” "
        "Before sourcing brand‑new lists, the targeting engine should ingest those tables, dedupe "
        "against current HubSpot, exclude churned/won/in‑sequence, and prioritise the cleanest "
        "high‑value remainder for the first re‑engagement campaign.", BODY))
    flow.append(Paragraph('Status: <i>Confirmed in onboarding call – ready to action</i>', AI_NOTE))
    flow.append(Spacer(1, 0.05*inch))

    flow.append(Paragraph('LinkedIn Outbound (Heyreach) Layered with Email', H2))
    flow.append(hr())
    flow.append(Paragraph(
        "Mendel’s current outbound is email‑only (agency black‑box + freelancer SmartLead). "
        "CFOs, Controllers, Compliance, and Travel Managers all live actively on LinkedIn in LatAm. "
        "Adding Heyreach LinkedIn touches as the second channel – connection request → message "
        "→ email re‑engage – should lift positive reply rate and SQL volume materially.", BODY))
    flow.append(Paragraph('Status: <i>Recommended addition – not yet in scope</i>', AI_NOTE))
    flow.append(PageBreak())
    return flow

# ── APPENDIX ───────────────────────────────────────────────────────────────
def appendix():
    flow = section_header('A', 'Appendix – Sources & Gaps')
    flow.append(Paragraph('Sources Used', H2))
    flow.append(hr())
    flow.append(kv_table([
        ('BD Assessment 3‑tab sheet',  'Drive: clients/Mendel/1. Analysis/Business Dev Assessment - [Mendel].xlsx (modified Apr 27, 2026)'),
        ('UVP & Offer document',            'Drive: clients/Mendel/1. Analysis/UVP and Offer - [Mendel].docx (modified Apr 28, 2026)'),
        ('Onboarding / Strategy Call #1',   'Fireflies: "Onboarding / Mendel – Kinetyca", Apr 28, 2026 (Alan Karpovsky + Matteo Fois + David)'),
        ('Mendel One‑Pager (MX)',      'Drive: clients/Mendel/6. Additional Elements/Mendel MX - One Pager.pdf'),
        ('Mendel Expenses + Viajes 2026 deck', 'Drive: clients/Mendel/6. Additional Elements/Mendel Expenses + Viajes 2026 - Full Deck.pdf'),
        ('Mendel Viajes pitch deck',        'Drive: clients/Mendel/6. Additional Elements/Mendel Viajes - Travel Pitch Deck.pdf'),
        ('Mendel vs Concur benchmark',      'Drive: clients/Mendel/6. Additional Elements/BenchMark_Mendel_VS_Concur.pdf'),
        ('Mendel vs Edenred / vs T&E',      'Drive: clients/Mendel/6. Additional Elements/OnePager_Mendel_VS_Edenred.jpg + OnePager_Mendel_VS_T&E.jpg'),
        ('Invoice Recovery one‑pager', 'Drive: clients/Mendel/6. Additional Elements/OnePager_Recupero_Facturas.jpg'),
    ]))
    flow.append(Spacer(1, 0.08*inch))

    flow.append(Paragraph('Gaps to Close in Strategy Call #2', H2))
    flow.append(hr())
    for b in [
        'Vertical‑specific named case studies with quantified outcomes (one per priority vertical).',
        'Detailed pricing per module (currently only ACV ranges – needed to write tighter ROI cold copy).',
        'Definition of "qualified meeting" – what passes Mendel’s SQL bar today vs. what they want.',
        'Formal "do‑not‑contact" list from existing agency + freelancer (action item from Apr 28 call).',
        'SmartLead access for review of past outbound performance and copy.',
        'Old Clay tables export for re‑engagement campaign sourcing.',
        'Decision: include Argentina + Chile in V1 outbound or save for V2 (90% Mexico signal points to V2).',
        'Confirm outbound SLA – 100+ qualified meetings / Q goal split by vertical.',
    ]:
        flow.append(bullet(b))
    flow.append(Spacer(1, 0.08*inch))

    flow.append(Paragraph('Conflict Notes', H2))
    flow.append(hr())
    flow.append(Paragraph(
        "<b>Geo focus:</b> the BD Assessment lists Mexico, Chile, Argentina as "
        "core. The same document explicitly states <i>“90% of the focus should be in generating more "
        "revenue for Mexico”</i>. The playbook follows that priority – Argentina and Chile are "
        "in‑scope only for the cross‑vertical pharma and pro‑services angles where the ICP is "
        "regional by definition.", BODY))
    flow.append(Spacer(1, 0.04*inch))
    flow.append(Paragraph(
        "<b>Sector breadth:</b> the BD Assessment positions Mendel as sector‑agnostic. The playbook "
        "ranks five verticals based on existing logo evidence and conversion signals; the AI‑identified "
        "opportunities section preserves the broader sector list (telecom, energy, tech‑enabled) for "
        "future validation.", BODY))
    flow.append(PageBreak())
    return flow

# ── BUILD ─────────────────────────────────────────────────────────────────
def build():
    doc = SimpleDocTemplate(
        OUTPUT_PATH, pagesize=letter,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN, bottomMargin=MARGIN,
        title='Mendel GTM Playbook', author='Outreach Magic / Kinetyca',
    )
    flow = []
    flow += cover_page()
    flow += toc_page()
    flow += section_1()
    flow += section_2()
    flow += section_3()
    flow += section_4()
    flow += section_5()
    flow += section_6()
    flow += section_7()
    flow += section_8()
    flow += section_9()
    flow += appendix()
    doc.build(flow, canvasmaker=NumberedCanvas)
    print(f'Wrote {OUTPUT_PATH}')

if __name__ == '__main__':
    build()
