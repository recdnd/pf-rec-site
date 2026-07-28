# pf-rec · data model（版本包）

version: 0.1
last-updated: 2026-07-28

## 硬 / 軟 切分

- **硬板塊（HTML 靜態，改動走 HEAD 派生）**：姓名、聯絡、外鏈、學歷、語言、PDF 連結。
- **軟資料（版本包 JSON，會成長會變動）**：hero 定位語＋簡介、強み、技術/設計 stack、專案區。

## 檔案

| 檔 | 角色 |
|---|---|
| `data/packs/<YYYY-MM>.json` | 版本包，只增不改（append-only；要改就出新版本） |
| `data/pack.current.json` | 當前使用包（= 某版本的拷貝；換包 = 覆蓋這個檔） |
| `data/render.js` | 渲染器，四頁共用（en/ja × desktop/mobile，`window.PF_PACK` 定 path/locale） |

## Pack schema

```
meta      { version, positioning, derived_from, note }
hero      { title_en/ja, description_en/ja(html) }
strengths [ { heading_en/ja, items_en/ja[] } ]
stack     { tech_en/ja, design_en/ja }
projects  [ { id, show, status: active|maintained|archived,
              tier: flagship|product|tool|content, draft,
              title_en/ja, link, meta_en/ja, summary_en/ja, bullets_en/ja[] } ]
```

- **show** = T2 策展開關，Rec 專屬；AI 只能提案、加進池子（show:false）。
- **draft:true** = AI 依 repo 現況起草、Rec 尚未校核的條目；校核後改 false。
- **status** 誠實標注；archived 專案照樣可展示（履歷計績效不計心跳）。
- 一包雙語：en 為母本欄位，ja 為其翻譯欄位；缺 ja 時 renderer 回退 en。

## 換包一條龍（不用絞腦版）

1. `python3 tools/derive_check.py` → 得「未展示候補」清單。
2. 叫 AI session：「依 <專案>/cyc/ 起草 pack 條目」→ 追加進新版本包（show:false, draft:true）。
3. Rec 只做兩件事：翻 show 開關、掃一眼 draft 條目改順眼。
4. `cp data/packs/<新版>.json data/pack.current.json` → push（GH Pages 即上線）。
5. 要出 PDF 時另行凍結到 `resume/`（L3）。

## 禁止回歸項

- 軟資料寫回 HTML（違反 08 data/view 契約）。
- 修改舊版本包（append-only；歷史包 = 各時期簡歷的原樣存檔）。
- AI 自行翻動 show 或刪池內條目。
