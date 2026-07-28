# pf-rec · derivation（真相源層級與派生契約）

version: 0.1
last-updated: 2026-07-28
ruled-by: Rec（2026-07-28 裁定：pf-rec 永遠不是真相源）

## 層級

```
L0  PD+FC/Personal-Directory/HEAD.md          個人 T0/T1 唯一活真值
L1  PD+FC/Personal-Directory/source/corpus/    專案/技能/經歷原子（T2/T3 素材）
    DungeonsRoot/<project>/cyc/                各專案自述真相（what it is / journal）
L2  rec-pf（本 repo）                          挑選＋包裝＋定位轉譯後給企業看的視圖
                                               ＝簡歷母本，derived，永非真相
L3  resume/*.pdf                               L2 的凍結匯出（投遞用終態）
```

## 鐵律

1. **pf-rec 上的任何個人事實必須可回溯到 HEAD**；任何專案陳述必須可回溯到該專案 cyc/（或 corpus 原子）。
2. **衝突時上游贏**：發現 pf-rec 與 HEAD/cyc 不一致 → 先修上游、再派生下來；禁止只改 pf-rec。
3. **選什麼展示（T2 策展）與怎麼說（T3 轉譯）是 Rec 的判斷**；AI 只能提案清單，不得自行增刪專案。
4. 定位語（product-builder 框架、AI-assisted under my direction 等）依 `resume/resume_strategy_summary.txt`；改策略先改該檔。
5. EN 為母本，ja/ 為其翻譯視圖；內容改動 EN → ja 需同步（`tools/derive_check.py` 會抓漂移）。

## 同步儀式

新專案落地或半年一巡：

```bash
python3 tools/derive_check.py   # 對帳 HEAD 事實 + 盤點未展示專案
```

輸出兩份清單：①頁面與 HEAD 不一致的事實（必修）；②DungeonsRoot 有而 pf-rec 未展示的專案（Rec 挑選）。
選定後：改 EN index.html → 跑 ja 同步（見 journal 2026-07-28 的翻譯管線）→ 匯出新 PDF 進 resume/。

## 語言分流

無顯性切換鈕。`index.html`/`mobile/index.html` head 偵測 `navigator.language` 以 ja 開頭
→ `ja/`／`ja/mobile/`。每個 runtime 單語（machine 00-shared-foundations §7）。
