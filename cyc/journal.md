# pf-rec · journal

## 2026-07-28 · ja 版 + 派生契約

- 新增 `ja/index.html`、`ja/mobile/index.html`：EN 母本經替換表全文翻譯（管線＝python 精確字串替換，
  表在 session 記錄；下次 EN 改動後重跑或手動同步）。無切換鈕，head 偵測 navigator.language 分流。
- 確立層級：HEAD(L0) → corpus/各專案cyc(L1) → pf-rec(L2, derived) → PDF(L3)。見 `cyc/specs/derivation.md`。
- 新增 `tools/derive_check.py` 對帳器。
- 待 Rec 裁定：①「Virginia Tech / Chicago」的 Chicago（=IIT online）在 HEAD 衝突清單中被裁定不入正式學歷，
  簡歷上以「University Coursework」名義呈現是否維持；②ja 版語学欄要不要補 TOEIC 960 / TOEFL 110（HEAD 有、EN 版無）；
  ③PDF 目前僅英語版，ja 版連結沿用之，日語 PDF 另案。

## （既往）

- 2026-04-15 以前：EN 版內容定稿（resume_strategy_summary 終態宣言）、BraintankAI 下架。

## 2026-07-28 · 版本包化（分包管理）

- 軟資料（hero/強み/stack/專案）抽離 HTML → `data/packs/2026-07.json`（en+ja 一包雙語），
  四頁共用 `data/render.js` 渲染；硬板塊留 HTML。schema 與換包流程見 `cyc/specs/data-model.md`。
- 2026-07 包為全新重寫（不參照 2026-04 舊文案）：定位語改 Product Builder / Systems Designer，
  新增 PD+FC、Fleet Governance、Kiln、Ruvia 條目；Spiral 誠實標 archived；池內另有 qf/exe/zenn（show:false）。
- draft:true 待 Rec 校核：machine / kiln / ruvia / exe / zenn。
- 注意：file:// 直開軟區塊為空（fetch 限制），預覽走 localhost（port 2200）。

## 2026-07-29 · 標準版包 + PDF 進包 + legacy 歸檔

- 包改目錄制：`data/packs/<版本>/` = pack.json ＋ 該版凍結 PDF，只增不改。手動維護期最後版
  凍結進 `packs/2026-04-legacy/`（PDF＋策略檔；歷次頁面文案在 git 歷史裡）。
- 2026-07 標準版（Rec 裁定）：只展示 **Kiln（主打 live product，kiln.ooo）＋ 總合システム設計**；
  其餘全部蹲池 show:false。Kiln 條目依 kiln/cyc（axioms／presets／8-locale SEO）重寫，draft 解除。
- `tools/build_pdf.py`：pack → resume_en.pdf 一鍵匯出（reportlab、A4 一頁、ATS 友好）；
  renderer 令頁面下載鈕自動指向當前包內 PDF。
