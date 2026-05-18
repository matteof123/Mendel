#!/usr/bin/env python3
"""
Generate a client-ready PDF of the Mendel email library from the markdown source.

Reads campaigns/email-library.md and produces campaigns/Mendel_Email_Library.pdf
using reportlab, with proper handling of headings, tables, code blocks, and lists.
"""

import re
from pathlib import Path
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak,
    Table, TableStyle, KeepTogether, Preformatted
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

HERE = Path(__file__).parent
SRC = HERE / "campaigns" / "Mendel_Rendered_Emails.md"
OUT = HERE / "campaigns" / "Mendel_Email_Library.pdf"

# Colors — match Mendel's brand neutrals
BRAND_PRIMARY = colors.HexColor("#1A1A2E")
BRAND_ACCENT = colors.HexColor("#0F3460")
BRAND_MUTED = colors.HexColor("#6B7280")
CODE_BG = colors.HexColor("#F4F4F8")
TABLE_HEADER_BG = colors.HexColor("#1A1A2E")
TABLE_HEADER_FG = colors.white
TABLE_ALT_BG = colors.HexColor("#FAFAFA")
BORDER = colors.HexColor("#E5E7EB")


def build_styles():
    base = getSampleStyleSheet()
    s = {}

    s["title"] = ParagraphStyle(
        "Title",
        parent=base["Title"],
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=26,
        textColor=BRAND_PRIMARY,
        spaceAfter=8,
        alignment=TA_LEFT,
    )
    s["subtitle"] = ParagraphStyle(
        "Subtitle",
        parent=base["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=11,
        textColor=BRAND_MUTED,
        spaceAfter=18,
    )
    s["h1"] = ParagraphStyle(
        "H1",
        parent=base["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=22,
        textColor=BRAND_PRIMARY,
        spaceBefore=22,
        spaceAfter=10,
        borderPadding=(0, 0, 4, 0),
        borderColor=BRAND_ACCENT,
    )
    s["h2"] = ParagraphStyle(
        "H2",
        parent=base["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=18,
        textColor=BRAND_ACCENT,
        spaceBefore=16,
        spaceAfter=8,
    )
    s["h3"] = ParagraphStyle(
        "H3",
        parent=base["Heading3"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=15,
        textColor=BRAND_PRIMARY,
        spaceBefore=12,
        spaceAfter=6,
    )
    s["h4"] = ParagraphStyle(
        "H4",
        parent=base["Heading4"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=14,
        textColor=BRAND_ACCENT,
        spaceBefore=10,
        spaceAfter=4,
    )
    s["body"] = ParagraphStyle(
        "Body",
        parent=base["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=BRAND_PRIMARY,
        spaceAfter=6,
    )
    s["bullet"] = ParagraphStyle(
        "Bullet",
        parent=base["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=BRAND_PRIMARY,
        leftIndent=14,
        bulletIndent=2,
        spaceAfter=3,
    )
    s["code"] = ParagraphStyle(
        "Code",
        parent=base["Code"],
        fontName="Courier",
        fontSize=8.5,
        leading=11,
        textColor=BRAND_PRIMARY,
        backColor=CODE_BG,
        leftIndent=8,
        rightIndent=8,
        borderPadding=8,
        spaceAfter=8,
        spaceBefore=4,
    )
    s["table_cell"] = ParagraphStyle(
        "TableCell",
        parent=base["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=11,
        textColor=BRAND_PRIMARY,
    )
    s["table_header"] = ParagraphStyle(
        "TableHeader",
        parent=base["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9,
        leading=11,
        textColor=TABLE_HEADER_FG,
    )
    s["table_code"] = ParagraphStyle(
        "TableCode",
        parent=base["Normal"],
        fontName="Courier",
        fontSize=8,
        leading=10,
        textColor=BRAND_PRIMARY,
    )
    return s


def inline_md_to_html(text):
    """Convert inline markdown (bold, italic, code) to ReportLab-compatible HTML."""
    # Escape XML
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # Bold
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    # Italic
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)
    # Inline code
    text = re.sub(r"`([^`]+)`", r'<font name="Courier" size="9" backColor="#F4F4F8">\1</font>', text)
    # Links - just keep the text
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text


def parse_table(lines, i):
    """Parse a markdown table starting at lines[i]. Returns (rows, next_i)."""
    rows = []
    while i < len(lines) and lines[i].lstrip().startswith("|"):
        line = lines[i].strip()
        # Skip alignment row like |---|---|
        if re.match(r"^\|[\s\-:|]+\|$", line):
            i += 1
            continue
        # Split cells
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append(cells)
        i += 1
    return rows, i


def build_story(md_text):
    styles = build_styles()
    story = []

    lines = md_text.split("\n")
    i = 0

    # Title block (manual, override any first H1)
    story.append(Paragraph("Mendel — Rendered Email Copy", styles["title"]))
    story.append(Paragraph(
        "All 35 rendered emails. Spanish (Mexico priority). Industry · target persona · subject · body.",
        styles["subtitle"]
    ))

    in_code_block = False
    code_buffer = []

    while i < len(lines):
        line = lines[i]

        # Code block fence
        if line.strip().startswith("```"):
            if in_code_block:
                # Close it — render the buffer
                code_text = "\n".join(code_buffer)
                if code_text.strip():
                    pre = Preformatted(code_text, styles["code"])
                    story.append(pre)
                code_buffer = []
                in_code_block = False
            else:
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            code_buffer.append(line)
            i += 1
            continue

        # Horizontal rule
        if line.strip() == "---":
            story.append(Spacer(1, 0.15 * inch))
            i += 1
            continue

        # Headings — skip the first H1 (title done above)
        if line.startswith("# "):
            text = line[2:].strip()
            if text in ("Mendel — Email Sequence Library", "Mendel — Rendered Email Copy"):
                i += 1
                continue
            story.append(Paragraph(inline_md_to_html(text), styles["h1"]))
            i += 1
            continue
        if line.startswith("## "):
            story.append(Paragraph(inline_md_to_html(line[3:].strip()), styles["h2"]))
            i += 1
            continue
        if line.startswith("### "):
            story.append(Paragraph(inline_md_to_html(line[4:].strip()), styles["h3"]))
            i += 1
            continue
        if line.startswith("#### "):
            story.append(Paragraph(inline_md_to_html(line[5:].strip()), styles["h4"]))
            i += 1
            continue

        # Table
        if line.lstrip().startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s\-:|]+\|$", lines[i + 1].strip()):
            rows, i = parse_table(lines, i)
            if not rows:
                continue
            # Build table data with Paragraphs for wrapping
            header = rows[0]
            body = rows[1:]

            # Decide per-column style: detect code cells (start with backtick)
            def cell_para(text):
                # If the cell is mostly inline code (starts/ends with `), use code style
                if text.startswith("`") and text.endswith("`"):
                    inner = text.strip("`")
                    return Paragraph(inner.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"), styles["table_code"])
                return Paragraph(inline_md_to_html(text), styles["table_cell"])

            data = [[Paragraph(inline_md_to_html(c), styles["table_header"]) for c in header]]
            for row in body:
                data.append([cell_para(c) for c in row])

            ncols = len(header)
            # Distribute width
            usable_width = 6.7 * inch
            # Heuristic: if 2-column, give more to second; otherwise even
            if ncols == 2:
                col_widths = [usable_width * 0.32, usable_width * 0.68]
            elif ncols == 3:
                col_widths = [usable_width * 0.25, usable_width * 0.45, usable_width * 0.30]
            elif ncols == 4:
                col_widths = [usable_width * 0.22] * 4
            else:
                col_widths = [usable_width / ncols] * ncols

            table = Table(data, colWidths=col_widths, repeatRows=1)
            style_cmds = [
                ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
                ("TEXTCOLOR", (0, 0), (-1, 0), TABLE_HEADER_FG),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("GRID", (0, 0), (-1, -1), 0.5, BORDER),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
            for r in range(1, len(data)):
                if r % 2 == 0:
                    style_cmds.append(("BACKGROUND", (0, r), (-1, r), TABLE_ALT_BG))
            table.setStyle(TableStyle(style_cmds))
            story.append(table)
            story.append(Spacer(1, 0.1 * inch))
            continue

        # Bullet
        if re.match(r"^\s*[-*]\s", line):
            text = re.sub(r"^\s*[-*]\s", "", line)
            story.append(Paragraph(inline_md_to_html(text), styles["bullet"], bulletText="•"))
            i += 1
            continue

        # Numbered
        m = re.match(r"^\s*\d+\.\s(.+)$", line)
        if m:
            text = m.group(1)
            story.append(Paragraph(inline_md_to_html(text), styles["bullet"], bulletText="•"))
            i += 1
            continue

        # Blank line
        if not line.strip():
            i += 1
            continue

        # Italic note (lines wrapped in single underscores)
        if line.startswith("_") and line.endswith("_") and "_" not in line[1:-1]:
            text = line.strip("_")
            story.append(Paragraph(f"<i>{inline_md_to_html(text)}</i>", styles["body"]))
            i += 1
            continue

        # Plain paragraph
        story.append(Paragraph(inline_md_to_html(line), styles["body"]))
        i += 1

    return story


def header_footer(canvas, doc):
    canvas.saveState()
    # Header bar
    canvas.setFillColor(BRAND_PRIMARY)
    canvas.rect(0, LETTER[1] - 0.5 * inch, LETTER[0], 0.5 * inch, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 10)
    canvas.drawString(0.7 * inch, LETTER[1] - 0.3 * inch, "Mendel — Rendered Email Copy")
    canvas.setFont("Helvetica", 8)
    canvas.drawRightString(LETTER[0] - 0.7 * inch, LETTER[1] - 0.3 * inch, "Cold outbound")

    # Footer
    canvas.setFillColor(BRAND_MUTED)
    canvas.setFont("Helvetica", 8)
    canvas.drawString(0.7 * inch, 0.4 * inch, "Confidential — for Mendel internal use")
    canvas.drawRightString(LETTER[0] - 0.7 * inch, 0.4 * inch, f"Page {doc.page}")
    canvas.restoreState()


def build_pdf():
    md_text = SRC.read_text(encoding="utf-8")
    story = build_story(md_text)

    doc = BaseDocTemplate(
        str(OUT),
        pagesize=LETTER,
        leftMargin=0.7 * inch,
        rightMargin=0.7 * inch,
        topMargin=0.9 * inch,
        bottomMargin=0.7 * inch,
        title="Mendel — Email Sequence Library",
        author="Outreach Magic / Kinetyca",
    )
    frame = Frame(
        doc.leftMargin,
        doc.bottomMargin,
        doc.width,
        doc.height,
        id="normal",
    )
    template = PageTemplate(id="main", frames=[frame], onPage=header_footer)
    doc.addPageTemplates([template])
    doc.build(story)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build_pdf()
