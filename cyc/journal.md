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
