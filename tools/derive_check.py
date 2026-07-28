#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pf-rec 派生對帳器（read-only，絕不改檔）。
①HEAD(L0) 事實 vs 頁面；②EN↔ja 結構漂移；③DungeonsRoot 專案 vs 展示清單。
用法：在 rec-pf 根目錄 python3 tools/derive_check.py
"""
import io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DROOT = os.path.dirname(ROOT)
HEAD = os.path.join(DROOT, "PD+FC", "Personal-Directory", "HEAD.md")

def read(p):
    try:
        return io.open(p, encoding="utf-8").read()
    except OSError:
        return ""

def head_value(head_text, key):
    m = re.search(r"^" + re.escape(key) + r":\n(?:.*\n)*?\s+value:\s*\"?([^\"\n]+)\"?", head_text, re.M)
    return m.group(1).strip() if m else None

def main():
    ok = True
    head = read(HEAD)
    en = read(os.path.join(ROOT, "index.html"))
    ja = read(os.path.join(ROOT, "ja", "index.html"))
    if not head:
        print("!! HEAD.md 讀不到：", HEAD); sys.exit(1)

    print("== ① HEAD(L0) 事實對帳 ==")
    checks = [
        ("email_alt",  lambda v: v in en and v in ja, "頁面聯絡信箱"),
        ("rikkyo_expected_graduation", lambda v: ("Expected Sep 2027" in en) and ("2027年9月卒業見込み" in ja), "卒業予定"),
        ("rikkyo_school", lambda v: ("Rikkyo University" in en) and (v in ja), "学校名"),
        ("virginia_tech_ja_canonical", lambda v: True if not ja else (v in ja), "VT 日文 canonical（バ）"),
    ]
    for key, test, label in checks:
        v = head_value(head, key)
        if v is None:
            print(f"  ?  {label}: HEAD 無 {key}"); ok = False; continue
        good = test(v)
        print(f"  {'✓' if good else '✗'}  {label}: HEAD={v}")
        if not good: ok = False

    print("\n== ② EN ↔ ja 結構漂移 ==")
    for pat, name in [(r'class="project-item"', "project-item 數"),
                      (r"<h2>", "h2 節數"), (r"<h3>", "h3 節數")]:
        a, b = len(re.findall(pat, en)), len(re.findall(pat, ja))
        print(f"  {'✓' if a == b else '✗'}  {name}: EN={a} ja={b}")
        if a != b: ok = False

    print("\n== ③ 專案盤點（DungeonsRoot vs 展示） ==")
    shown_src = en
    SKIP = {"rec-pf", "sov", "derivatives", "CommonLibrary", "prompt", "scripts-booba",
            "util-misc", "mom-pack", "baobao", "artifact-suschurch", "replit-remains",
            "e-mail", "_bin_preview"}
    rows = []
    for name in sorted(os.listdir(DROOT)):
        p = os.path.join(DROOT, name)
        if not os.path.isdir(p) or name.startswith(".") or name in SKIP:
            continue
        has_cyc = os.path.isdir(os.path.join(p, "cyc"))
        needle = name.lower().replace("-rec", "").replace("rec-", "")
        shown = (len(needle) >= 3 and needle in shown_src.lower()) or name.lower() in shown_src.lower()
        rows.append((name, has_cyc, shown))
    for name, has_cyc, shown in rows:
        mark = "展示中" if shown else "未展示"
        print(f"  {'●' if shown else '○'} {name:<18} cyc{'✓' if has_cyc else '—'}  {mark}")
    print("\n  ○＝候補；要不要進簡歷是 T2 策展，Rec 裁定。")

    print("\n==", "PASS" if ok else "有不一致，先修上游再派生", "==")
    sys.exit(0 if ok else 2)

if __name__ == "__main__":
    main()
