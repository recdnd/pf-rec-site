/* pf-rec · pack renderer
   軟資料（簡介/強み/專案）從 data/pack.current.json 渲染；硬板塊（姓名/聯絡/學歷/語言）留在 HTML。
   換簡歷 = 換包。頁面在 <script> 前設 window.PF_PACK = { path, locale }。 */
(async function () {
  const cfg = window.PF_PACK || {};
  const path = cfg.path || "data/pack.current.json";
  const L = cfg.locale || (document.documentElement.lang === "ja" ? "ja" : "en");
  let pack;
  try {
    const res = await fetch(path);
    if (!res.ok) return;
    pack = await res.json();
  } catch (e) { return; } /* file:// 直開時無渲染；預覽請走 localhost */

  const t = (o, k) => (o && o[k + "_" + L] != null ? o[k + "_" + L] : (o ? o[k + "_en"] : ""));

  const heroTitle = document.querySelector(".hero-title");
  if (heroTitle && pack.hero) heroTitle.textContent = t(pack.hero, "title");
  const heroDesc = document.querySelector(".hero-description");
  if (heroDesc && pack.hero) heroDesc.innerHTML = t(pack.hero, "description");

  const sk = document.getElementById("pack-strengths");
  if (sk && pack.strengths) {
    let h = "";
    for (const g of pack.strengths) {
      h += "<h3>" + t(g, "heading") + "</h3><ul>" +
        (t(g, "items") || []).map(function (i) { return "<li>" + i + "</li>"; }).join("") + "</ul>";
    }
    if (pack.stack) {
      h += "<h3>" + (L === "ja" ? "技術スタック" : "Technical Exposure") + "</h3><p>" + t(pack.stack, "tech") + "</p>";
      h += "<h3>" + (L === "ja" ? "デザインツール" : "Design Tools") + "</h3><p>" + t(pack.stack, "design") + "</p>";
    }
    sk.innerHTML = h;
  }

  /* PDF 下載連結指向當前包內凍結版（L3） */
  const pdf = pack.meta && (pack.meta["pdf_" + L] || pack.meta.pdf_en);
  if (pdf) {
    const root = path.replace(/data\/pack\.current\.json$/, "");
    document.querySelectorAll(".download-link").forEach(function (a) {
      a.href = root + pdf;
      a.setAttribute("download", pdf.split("/").pop());
    });
  }

  const pj = document.getElementById("pack-projects");
  if (pj && pack.projects) {
    let h = "";
    for (const p of pack.projects) {
      if (!p.show) continue;
      const link = p.link
        ? ' <a href="' + p.link + '" target="_blank" rel="noopener noreferrer" class="project-link">→</a>'
        : "";
      h += '<div class="project-item"><div class="project-title">' + t(p, "title") + link + "</div>" +
        '<div class="project-meta">' + t(p, "meta") + "</div><p>" + t(p, "summary") + "</p>";
      const bl = t(p, "bullets") || [];
      if (bl.length) {
        h += '<div class="project-description"><ul>' +
          bl.map(function (b) { return "<li>" + b + "</li>"; }).join("") + "</ul></div>";
      }
      h += "</div>";
    }
    pj.innerHTML = h;
  }
})();
