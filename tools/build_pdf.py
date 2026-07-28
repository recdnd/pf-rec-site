#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pack → resume PDF（L3 凍結匯出）。
讀 data/pack.current.json，只渲染 show:true 專案；硬事實（HEAD 派生）寫死於下方 HARD。
用法：python3 tools/build_pdf.py [輸出路徑]   預設輸出到當前包目錄 resume_en.pdf
需要：pip install reportlab
"""
import io, json, os, re, sys

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACCENT = HexColor("#dc2626")
INK = HexColor("#111111")

# 硬事實（派生自 PD+FC/HEAD.md；改動先改 HEAD）
HARD = {
    "name": "XUE JUNTAO",
    "loc": "Tokyo, Japan",
    "contact": "r@rec.ooo · pf.rec.ooo · git.rec.ooo",
    "edu": [
        ("Rikkyo University, Tokyo — B.A. in History (Expected Sep 2027)",
         "Focus: institutional systems, bureaucracy, legal structures, information organization."),
        ("University Coursework (U.S.) — Virginia Tech / Chicago",
         "Calculus I–II, Linear Algebra, Data Structures, Object-Oriented Programming."),
    ],
    "langs": "Chinese (Native) · English (Fluent) · Japanese (Fluent / JLPT N1)",
}

def strip_html(s):
    return re.sub(r"<[^>]+>", " ", s or "").replace("  ", " ").strip()

def main():
    pack = json.load(io.open(os.path.join(ROOT, "data", "pack.current.json"), encoding="utf-8"))
    ver = pack["meta"]["version"]
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "data", "packs", ver, "resume_en.pdf")

    S = {
        "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=17, leading=20, textColor=INK),
        "meta": ParagraphStyle("meta", fontName="Helvetica", fontSize=9, leading=12, textColor=INK),
        "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=ACCENT, spaceBefore=2),
        "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=ACCENT, spaceBefore=10, spaceAfter=2),
        "h3": ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=9.5, leading=12, textColor=INK, spaceBefore=4),
        "body": ParagraphStyle("body", fontName="Helvetica", fontSize=9, leading=11.8, textColor=INK),
        "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=9, leading=11.8, textColor=INK,
                                 leftIndent=8, bulletIndent=0),
        "small": ParagraphStyle("small", fontName="Helvetica", fontSize=8, leading=10, textColor=HexColor("#666666")),
    }

    story = []
    A = story.append
    A(Paragraph(HARD["name"], S["name"]))
    A(Paragraph(f'{HARD["loc"]} · {HARD["contact"]}', S["meta"]))
    A(Spacer(1, 4))
    A(Paragraph(pack["hero"]["title_en"], S["title"]))
    A(Paragraph(strip_html(pack["hero"]["description_en"]), S["body"]))

    A(Paragraph("SELECTED WORK", S["h2"]))
    for p in pack["projects"]:
        if not p.get("show"):
            continue
        t = p["title_en"] + (f'  ({p["link"].replace("https://", "")})' if p.get("link") else "")
        A(Paragraph(t, S["h3"]))
        A(Paragraph(p["meta_en"], S["small"]))
        A(Paragraph(p["summary_en"], S["body"]))
        for b in p.get("bullets_en", []):
            A(Paragraph(b, S["bullet"], bulletText="–"))

    A(Paragraph("CORE STRENGTHS", S["h2"]))
    for g in pack["strengths"]:
        A(Paragraph(g["heading_en"] + ": " + "; ".join(g["items_en"]), S["body"]))
    A(Paragraph("Stack: " + pack["stack"]["tech_en"], S["small"]))

    A(Paragraph("EDUCATION", S["h2"]))
    for head, sub in HARD["edu"]:
        A(Paragraph(head, S["h3"]))
        A(Paragraph(sub, S["body"]))

    A(Paragraph("LANGUAGES", S["h2"]))
    A(Paragraph(HARD["langs"], S["body"]))

    os.makedirs(os.path.dirname(out), exist_ok=True)
    doc = SimpleDocTemplate(out, pagesize=A4,
                            leftMargin=16 * mm, rightMargin=16 * mm,
                            topMargin=14 * mm, bottomMargin=12 * mm,
                            title=f"Xue Juntao — resume {ver}", author="Xue Juntao")
    doc.build(story)
    print("built:", out)

if __name__ == "__main__":
    main()
