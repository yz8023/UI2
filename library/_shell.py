# -*- coding: utf-8 -*-
"""素材库 · 页面皮肤（CSS / JS 常量）。所有页面共用同一套视觉语言。"""

RESET = ("* { margin:0; padding:0; box-sizing:border-box; font-family:'Segoe UI',sans-serif; "
         "-webkit-tap-highlight-color:transparent; }")

SHELL_CSS = r"""
:root{
  --ink:#eaf1fb; --soft:rgba(234,241,251,.64); --dim:rgba(234,241,251,.36);
  --line:rgba(255,255,255,.10); --line2:rgba(255,255,255,.18);
  --acc:#a8cbff; --mint:#6fe0c0; --violet:#b6a3ff; --danger:#ff9aa9; --warn:#ffd28a;
  --card:rgba(255,255,255,.045);
  --spring:cubic-bezier(.2,.9,.3,1.15); --ease:cubic-bezier(.2,.8,.3,1);
}
[hidden]{display:none!important}
html{scroll-behavior:smooth}
body{
  min-height:100vh;color:var(--ink);background:#070b12;overflow-x:hidden;
  font-family:'Segoe UI','PingFang SC','Hiragino Sans GB','Microsoft YaHei',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;
}
body::before{
  content:"";position:fixed;inset:0;z-index:-2;
  background:
    radial-gradient(90% 62% at 10% -8%, #1d3f6e 0%, rgba(29,63,110,0) 62%),
    radial-gradient(76% 58% at 98% 4%, #1b3166 0%, rgba(27,49,102,0) 58%),
    radial-gradient(88% 68% at 74% 104%, #0d4a45 0%, rgba(13,74,69,0) 62%),
    radial-gradient(62% 52% at -6% 102%, #2b2050 0%, rgba(43,32,80,0) 62%),
    #070b12;
}
body::after{
  content:"";position:fixed;inset:0;z-index:-1;pointer-events:none;opacity:.4;
  background-image:radial-gradient(rgba(255,255,255,.06) 1px, transparent 1px);
  background-size:3px 3px;
  -webkit-mask-image:radial-gradient(120% 88% at 50% 0%, #000 26%, transparent 84%);
  mask-image:radial-gradient(120% 88% at 50% 0%, #000 26%, transparent 84%);
}
a{color:inherit;text-decoration:none}
img,svg{display:block}
button,input,textarea,select{font:inherit;color:inherit}
button{background:none;border:0;cursor:pointer}
::selection{background:rgba(168,203,255,.3)}
::-webkit-scrollbar{width:9px;height:9px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:rgba(255,255,255,.14);border-radius:99px;border:2px solid transparent;background-clip:padding-box}
::-webkit-scrollbar-thumb:hover{background:rgba(255,255,255,.24);background-clip:padding-box}

/* ── 顶栏 ───────────────────────────────────────────── */
.topbar{position:sticky;top:0;z-index:50;border-bottom:1px solid rgba(255,255,255,.07);
  background:linear-gradient(180deg,rgba(7,11,18,.9),rgba(7,11,18,.55));
  -webkit-backdrop-filter:blur(20px) saturate(1.5);backdrop-filter:blur(20px) saturate(1.5)}
.topbar-in{max-width:1240px;margin:0 auto;display:flex;align-items:center;gap:14px;padding:12px 22px;width:100%}
.brand{display:flex;align-items:center;gap:9px;font-size:14.5px;font-weight:800;letter-spacing:-.01em;white-space:nowrap}
.brand i{width:9px;height:9px;border-radius:50%;background:linear-gradient(150deg,#cfe3ff,#6fe0c0);
  box-shadow:0 0 14px rgba(168,203,255,.85);animation:brandPulse 3.6s ease-in-out infinite}
@keyframes brandPulse{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(1.22);opacity:.7}}
.brand b{font-size:10.5px;font-weight:600;color:var(--dim);padding:2px 7px;border-radius:99px;border:1px solid var(--line)}
.catnav{display:flex;gap:2px;flex:1;overflow:auto;scrollbar-width:none;margin:0 4px}
.catnav::-webkit-scrollbar{display:none}
.catnav a{font-size:11.5px;color:var(--soft);padding:6px 10px;border-radius:99px;white-space:nowrap;transition:.2s}
.catnav a:hover{color:var(--ink);background:rgba(255,255,255,.07)}
.catnav a.on{color:#06121c;font-weight:700;background:linear-gradient(180deg,#cfe3ff,#9dccff);
  box-shadow:0 6px 16px rgba(140,190,245,.28)}
.search{display:flex;align-items:center;gap:7px;height:33px;padding:0 12px;border-radius:99px;
  background:rgba(255,255,255,.05);border:1px solid var(--line);transition:.2s}
.search:focus-within{border-color:rgba(168,203,255,.5);background:rgba(168,203,255,.08)}
.search span{font-size:11px;color:var(--dim)}
.search input{width:118px;background:none;border:0;outline:none;color:var(--ink);font-size:12px;
  font-family:inherit}
.search input::placeholder{color:var(--dim)}
.btnp{display:inline-flex;align-items:center;gap:6px;height:33px;padding:0 13px;border-radius:99px;font-size:11.5px;
  color:#06121c;font-weight:700;background:linear-gradient(180deg,#cfe3ff,#9dccff);white-space:nowrap;
  transition:transform .16s var(--spring),box-shadow .2s;box-shadow:0 8px 18px rgba(140,190,245,.24)}
.btnp:hover{transform:translateY(-1px);box-shadow:0 12px 24px rgba(140,190,245,.34)}
.btnp:active{transform:scale(.97)}
.btn-ghost{display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 12px;border-radius:99px;
  font-size:11.5px;color:var(--soft);border:1px solid var(--line);background:rgba(255,255,255,.04);transition:.2s}
.btn-ghost:hover{color:var(--ink);border-color:var(--line2);background:rgba(255,255,255,.08)}

/* ── 首屏 ───────────────────────────────────────────── */
.hero{max-width:1240px;margin:0 auto;padding:52px 22px 26px;position:relative}
.hero .eyebrow{display:inline-flex;align-items:center;gap:7px;font-size:10.5px;letter-spacing:.14em;color:var(--acc);
  padding:5px 11px;border-radius:99px;border:1px solid rgba(168,203,255,.28);background:rgba(168,203,255,.08);
  text-transform:uppercase}
.hero h1{font-size:clamp(27px,4.6vw,48px);line-height:1.1;letter-spacing:-.035em;font-weight:800;margin-top:16px}
.hero h1 em{font-style:normal;background:linear-gradient(100deg,#e3efff,#93c8ff 42%,#6fe0c0);
  -webkit-background-clip:text;background-clip:text;color:transparent}
.hero p{margin-top:14px;max-width:660px;color:var(--soft);font-size:13px;line-height:1.95}
.hero .pills{display:flex;gap:7px;flex-wrap:wrap;margin-top:20px}
.pill{padding:7px 13px;border-radius:99px;border:1px solid var(--line);background:rgba(255,255,255,.04);
  font-size:11.5px;color:var(--soft);backdrop-filter:blur(8px)}
.pill b{color:var(--ink);font-weight:700}
.pill.acc{border-color:rgba(168,203,255,.3);background:rgba(168,203,255,.09);color:#d6e7ff}

/* ── 分类段 ─────────────────────────────────────────── */
.cat{max-width:1240px;margin:0 auto;padding:26px 22px 2px;scroll-margin-top:74px}
.cat-h{display:flex;align-items:flex-end;gap:12px;margin-bottom:14px;flex-wrap:wrap}
.cat-h .num{font-size:32px;font-weight:800;line-height:.78;color:transparent;
  -webkit-text-stroke:1px rgba(255,255,255,.18);letter-spacing:-.02em}
.cat-h h2{font-size:17px;letter-spacing:-.01em}
.cat-h p{font-size:11.5px;color:var(--dim);padding-bottom:2px;flex:1;min-width:180px}
.cat-h .cnt{font-size:10.5px;color:var(--dim);padding:3px 9px;border-radius:99px;border:1px solid var(--line);
  padding-bottom:4px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(272px,1fr));gap:16px}

/* ── 卡片 ───────────────────────────────────────────── */
.card{position:relative;border-radius:22px;overflow:hidden;cursor:pointer;text-align:left;width:100%;
  border:1px solid rgba(255,255,255,.1);
  background:linear-gradient(180deg,rgba(255,255,255,.062),rgba(255,255,255,.018));
  box-shadow:0 18px 42px -22px rgba(0,0,0,.85), inset 0 1px 0 rgba(255,255,255,.08);
  transition:transform .3s var(--spring),border-color .3s,box-shadow .3s}
.card:hover{transform:translateY(-4px);border-color:rgba(168,203,255,.36);
  box-shadow:0 28px 54px -20px rgba(0,0,0,.9),0 0 0 1px rgba(168,203,255,.14),inset 0 1px 0 rgba(255,255,255,.14)}
.card:focus-visible{outline:2px solid var(--acc);outline-offset:3px}
.card .stage{position:relative;height:196px;background:#0d141b;overflow:hidden;border-bottom:1px solid rgba(255,255,255,.07);
  display:grid;place-items:center}
.card .stage .cap{display:none}
.card .stage .fit{box-shadow:0 0 0 1px rgba(255,255,255,.07),0 18px 40px -24px #000}
.card .stage::after{content:"";position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(180deg,rgba(7,11,18,.28),transparent 32%,transparent 68%,rgba(7,11,18,.42))}
.card .meta{padding:12px 14px 14px}
.card .r1{display:flex;align-items:center;gap:7px}
.card .fid{font-size:9.5px;font-weight:700;letter-spacing:.06em;color:var(--acc);
  padding:2px 6px;border-radius:5px;background:rgba(168,203,255,.13);border:1px solid rgba(168,203,255,.22)}
.card h3{font-size:13px;font-weight:700;letter-spacing:-.01em;flex:1}
.card .diff{font-size:9px;color:var(--warn);letter-spacing:.06em}
.card .desc{font-size:10.5px;color:var(--dim);line-height:1.65;margin-top:6px;
  display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.card .tags{display:flex;gap:5px;margin-top:9px;flex-wrap:wrap}
.card .tag{font-size:9px;color:var(--soft);padding:2px 7px;border-radius:99px;border:1px solid var(--line)}
.card .tag.hot{color:var(--mint);border-color:rgba(111,224,192,.32);background:rgba(111,224,192,.08)}

/* ── 底部玻璃坞 ─────────────────────────────────────── */
.dock{position:fixed;left:50%;bottom:16px;transform:translateX(-50%);z-index:60;display:flex;align-items:center;gap:3px;
  max-width:calc(100% - 18px);overflow-x:auto;scrollbar-width:none;
  padding:6px;border-radius:99px;border:1px solid rgba(255,255,255,.16);
  background:rgba(13,20,29,.66);-webkit-backdrop-filter:blur(24px) saturate(1.6);backdrop-filter:blur(24px) saturate(1.6);
  box-shadow:0 20px 44px rgba(0,0,0,.6),inset 0 1px 0 rgba(255,255,255,.14)}
.dock::-webkit-scrollbar{display:none}
.dock button{flex:0 0 auto;white-space:nowrap;height:29px;padding:0 12px;border-radius:99px;font-size:11px;color:var(--soft);transition:.2s;font-family:inherit}
.dock button:hover{color:var(--ink);background:rgba(255,255,255,.08)}
.dock button.on{color:#06121c;font-weight:700;background:linear-gradient(180deg,#cfe3ff,#9dccff);
  box-shadow:0 4px 12px rgba(140,190,245,.35)}
.dock .sep{width:1px;height:16px;background:rgba(255,255,255,.16);margin:0 3px}

/* ── 详情面板 ───────────────────────────────────────── */
.mask{position:fixed;inset:0;z-index:80;background:rgba(3,6,11,.6);opacity:0;pointer-events:none;
  -webkit-backdrop-filter:blur(7px);backdrop-filter:blur(7px);transition:opacity .3s}
.mask.on{opacity:1;pointer-events:auto}
.sheet{position:fixed;top:0;right:0;bottom:0;z-index:90;width:min(800px,100%);display:flex;flex-direction:column;
  transform:translateX(101%);transition:transform .4s cubic-bezier(.2,.86,.25,1);
  background:linear-gradient(180deg,#0e1721,#080c12 60%);border-left:1px solid rgba(255,255,255,.1);
  box-shadow:-30px 0 80px rgba(0,0,0,.6)}
.sheet.on{transform:none}
.sheet-top{display:flex;align-items:center;gap:10px;padding:13px 18px;border-bottom:1px solid rgba(255,255,255,.07);
  background:rgba(10,16,23,.72);-webkit-backdrop-filter:blur(16px);backdrop-filter:blur(16px)}
.sheet-top .fid{font-size:10px;font-weight:700;color:var(--acc);padding:2px 7px;border-radius:5px;
  background:rgba(168,203,255,.13);border:1px solid rgba(168,203,255,.22)}
.sheet-top h2{font-size:14px;flex:1;letter-spacing:-.01em}
.sheet-top .cat{font-size:10px;color:var(--dim);padding:2px 8px;border-radius:99px;border:1px solid var(--line)}
.sheet-top .x{width:30px;height:30px;border-radius:50%;display:grid;place-items:center;font-size:15px;
  color:var(--soft);border:1px solid var(--line);background:rgba(255,255,255,.04);transition:.2s;font-family:inherit}
.sheet-top .x:hover{color:var(--ink);background:rgba(255,255,255,.1);transform:rotate(90deg)}
.sheet-body{flex:1;overflow:auto;padding:16px 18px 96px;overscroll-behavior:contain}
.stage-lg{position:relative;height:330px;border-radius:18px;overflow:hidden;border:1px solid rgba(255,255,255,.1);
  background:radial-gradient(120% 120% at 50% 0%,#111b26,#0a1016);box-shadow:inset 0 1px 0 rgba(255,255,255,.07);
  display:grid;place-items:center}
.fit{position:relative;width:300px;height:210px;flex:0 0 auto;overflow:hidden;border-radius:14px;
  transform:scale(var(--s,1));transform-origin:center center;will-change:transform;background:#0d141b;
  box-shadow:0 0 0 1px rgba(255,255,255,.08),0 24px 50px -26px #000}
.fit > .dz{width:100%;height:100%;min-height:0}
.tabs{display:flex;gap:3px;padding:4px;border-radius:13px;margin:15px 0 13px;overflow:auto;scrollbar-width:none;
  background:rgba(255,255,255,.05);border:1px solid var(--line)}
.tabs::-webkit-scrollbar{display:none}
.tabs button{flex:1;height:29px;border-radius:9px;font-size:11px;color:var(--soft);white-space:nowrap;
  transition:.2s;font-family:inherit;padding:0 10px}
.tabs button.on{color:var(--ink);font-weight:700;background:rgba(255,255,255,.1);
  box-shadow:0 2px 10px rgba(0,0,0,.4)}
.panel{animation:panelIn .26s var(--ease)}
@keyframes panelIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}

/* ── 排版 ───────────────────────────────────────────── */
.prose h4{font-size:10.5px;letter-spacing:.1em;color:var(--dim);margin:20px 0 8px;text-transform:uppercase}
.prose h4:first-child{margin-top:4px}
.prose p{font-size:12.5px;line-height:1.95;color:var(--soft)}
.prose ol,.prose ul{padding-left:19px;font-size:12.5px;line-height:1.9;color:var(--soft)}
.prose li{margin:4px 0}
.prose li::marker{color:var(--dim)}
.prose code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:11.5px;
  background:rgba(255,255,255,.07);padding:1px 5px;border-radius:5px;color:#cfe3ff}
.kv{display:grid;grid-template-columns:78px 1fr;gap:8px 14px;font-size:12px;line-height:1.8}
.kv b{color:var(--acc);font-weight:600;white-space:nowrap}
.kv span{color:var(--soft)}
.checks,.reds{list-style:none;padding:0}
.checks li,.reds li{position:relative;padding-left:21px;font-size:12.5px;line-height:1.9;color:var(--soft)}
.checks li::before{content:"✓";position:absolute;left:0;top:0;color:var(--mint);font-size:11px}
.reds li::before{content:"✕";position:absolute;left:0;top:0;color:var(--danger);font-size:11px}
table.tbl{width:100%;border-collapse:collapse;font-size:11.5px;margin-top:6px}
.tbl th{text-align:left;color:var(--dim);font-weight:500;border-bottom:1px solid var(--line);padding:6px 8px}
.tbl td{border-bottom:1px solid rgba(255,255,255,.06);padding:7px 8px;color:var(--soft);vertical-align:top;line-height:1.7}
.tbl tr:last-child td{border-bottom:0}
.tbl td.bad{color:#ffb3bf}
pre.prompt{white-space:pre-wrap;font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  font-size:11.5px;line-height:1.9;color:#d9e8fb;padding:15px;border-radius:14px;max-height:430px;overflow:auto;
  background:linear-gradient(180deg,rgba(168,203,255,.09),rgba(255,255,255,.015));
  border:1px solid rgba(168,203,255,.22)}
.copybar{display:flex;align-items:center;gap:8px;margin:14px 0 0;flex-wrap:wrap}
.copybar .hint{font-size:10.5px;color:var(--dim)}
.refcard{display:flex;flex-direction:column;gap:5px;padding:11px 13px;border-radius:12px;margin-bottom:8px;
  border:1px solid var(--line);background:rgba(255,255,255,.035)}
.refcard .t{display:flex;align-items:center;gap:7px;font-size:12px;font-weight:700}
.refcard .t em{font-style:normal;font-size:9px;font-weight:600;color:var(--mint);padding:1px 6px;border-radius:99px;
  background:rgba(111,224,192,.1);border:1px solid rgba(111,224,192,.28)}
.refcard .u{font-size:10.5px;color:var(--acc);word-break:break-all}
.refcard .d{font-size:11px;color:var(--dim);line-height:1.7}

/* ── 页脚 ───────────────────────────────────────────── */
.foot{max-width:1240px;margin:52px auto 0;padding:26px 22px 96px;border-top:1px solid rgba(255,255,255,.07)}
.foot .row{display:flex;gap:20px;flex-wrap:wrap;justify-content:space-between;align-items:flex-start}
.foot h5{font-size:11px;letter-spacing:.1em;color:var(--dim);margin-bottom:8px;text-transform:uppercase}
.foot a{font-size:11.5px;color:var(--soft);display:block;padding:3px 0}
.foot a:hover{color:var(--acc)}
.foot .note{font-size:10.5px;color:var(--dim);line-height:1.9;max-width:520px}

/* ── 单条文档页 ─────────────────────────────────────── */
.doc{max-width:900px;margin:0 auto;padding:26px 22px 110px}
.doc .eyebrow{display:inline-flex;align-items:center;gap:7px;font-size:10px;letter-spacing:.12em;color:var(--acc);
  padding:4px 10px;border-radius:99px;border:1px solid rgba(168,203,255,.26);background:rgba(168,203,255,.08)}
.doc h1{font-size:clamp(22px,3.4vw,32px);letter-spacing:-.03em;margin:13px 0 8px}
.doc .lede{font-size:12.5px;color:var(--soft);line-height:1.9;max-width:680px}
.doc .stage-lg{height:300px;margin:20px 0 6px}
.sec{margin-top:26px;padding-top:22px;border-top:1px solid rgba(255,255,255,.07)}
.sec > h3{font-size:13.5px;letter-spacing:-.01em;margin-bottom:11px;display:flex;align-items:center;gap:8px}
.sec > h3 i{width:5px;height:5px;border-radius:50%;background:var(--acc);box-shadow:0 0 10px rgba(168,203,255,.9)}
.pager{display:flex;gap:10px;margin-top:32px}
.pager a{flex:1;padding:12px 14px;border-radius:14px;border:1px solid var(--line);
  background:rgba(255,255,255,.035);transition:.2s;min-width:0}
.pager a:hover{border-color:rgba(168,203,255,.34);background:rgba(168,203,255,.08)}
.pager span{display:block;font-size:9.5px;color:var(--dim);letter-spacing:.08em;margin-bottom:4px}
.pager b{font-size:12px;font-weight:600;display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.pager a.next{text-align:right}

/* ── toast ──────────────────────────────────────────── */
#toast{position:fixed;left:50%;bottom:76px;transform:translate(-50%,14px);z-index:120;padding:9px 15px;
  border-radius:99px;font-size:11.5px;color:var(--ink);background:rgba(22,32,43,.95);
  border:1px solid rgba(255,255,255,.16);box-shadow:0 16px 40px rgba(0,0,0,.6);
  opacity:0;pointer-events:none;transition:.26s var(--spring)}
#toast.on{opacity:1;transform:translate(-50%,0)}

@media (max-width:720px){
  .topbar-in{padding:10px 14px;gap:9px}
  .catnav{display:none}
  .hero{padding:34px 16px 16px}
  .hero p{font-size:12.5px}
  .cat{padding:20px 16px 0}
  .grid{grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:12px}
  .card .stage{height:172px}
  .sheet{width:100%}
  .stage-lg{height:260px}
  .doc{padding:20px 16px 110px}
  .dock{bottom:10px;gap:1px}
  .dock button{padding:0 9px;font-size:10.5px}
  .dock [data-copy-all],.dock .sep{display:none}
}
@media (prefers-reduced-motion: reduce){
  *{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}
  html{scroll-behavior:auto}
}
"""

COMMON_JS = r"""
/* 把 300×210 的设计画布等比塞进容器 */
window.__fit = function(fitEl){
  if(!fitEl) return;
  var host = fitEl.parentElement;
  function calc(){
    var w = host.clientWidth, h = host.clientHeight;
    if(!w || !h) return;
    var s = Math.min((w - 10) / 300, (h - 10) / 210);
    s = Math.max(.28, Math.min(1.55, s));
    fitEl.style.setProperty('--s', s.toFixed(4));
  }
  calc();
  if(window.ResizeObserver){ try{ new ResizeObserver(calc).observe(host); }catch(e){} }
  window.addEventListener('resize', calc);
};
window.__copy = async function(t){
  try{
    if(window.AndroidBridge && typeof AndroidBridge.copy === 'function'){ AndroidBridge.copy(t); return true; }
    if(navigator.clipboard && navigator.clipboard.writeText){ await navigator.clipboard.writeText(t); return true; }
  }catch(e){}
  try{
    var ta = document.createElement('textarea');
    ta.value = t; ta.style.position = 'fixed'; ta.style.top = '-1000px'; ta.style.opacity = '0';
    document.body.appendChild(ta); ta.focus(); ta.select();
    var ok = document.execCommand('copy'); ta.remove(); return ok;
  }catch(e){ return false; }
};
window.__toast = function(msg){
  var el = document.getElementById('toast');
  if(!el){ el = document.createElement('div'); el.id = 'toast'; document.body.appendChild(el); }
  el.textContent = msg; el.classList.add('on');
  clearTimeout(window.__tt); window.__tt = setTimeout(function(){ el.classList.remove('on'); }, 1600);
};
document.addEventListener('click', function(e){
  var b = e.target.closest('[data-copy]');
  if(!b) return;
  var sel = b.getAttribute('data-copy') || '';
  var node = sel ? document.querySelector(sel) : null;
  var text = node ? (node.dataset.raw ? decodeURIComponent(node.dataset.raw) : node.textContent) : '';
  window.__copy(text).then(function(ok){
    window.__toast(ok ? '已复制到剪贴板' : '复制失败，请长按选择文本');
  });
});
"""

HUB_JS = r"""
(function(){
  var IO = window.IntersectionObserver ? new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(e.isIntersecting && !e.target.dataset.mounted){
        e.target.dataset.mounted = '1'; mount(e.target);
      }
    });
  }, {rootMargin:'260px 0px'}) : null;

  function mount(el){
    var i = el.dataset.demo;
    var tpl = document.getElementById('tpl-' + i);
    if(!tpl) return;
    el.innerHTML = tpl.innerHTML;
    window.__fit(el.closest('.fit'));
    var fn = window.__MOUNT && window.__MOUNT[+i];
    if(typeof fn === 'function'){
      try{ fn(el); }catch(err){ console.error('demo ' + i, err); }
    }
  }

  document.querySelectorAll('[data-demo]').forEach(function(el){
    if(IO) IO.observe(el); else mount(el);
  });

  /* ── 分类筛选 / 搜索 ── */
  var cards = [].slice.call(document.querySelectorAll('.card'));
  var secs  = [].slice.call(document.querySelectorAll('.cat'));
  var q = document.getElementById('q');
  var dockBtns = [].slice.call(document.querySelectorAll('.dock [data-filter]'));
  var navLinks = [].slice.call(document.querySelectorAll('.catnav a'));
  var active = 'all';

  function apply(){
    var s = (q && q.value || '').trim().toLowerCase();
    cards.forEach(function(c){
      var okCat = active === 'all' || c.dataset.cat === active;
      var hay = (c.dataset.name + ' ' + c.dataset.id + ' ' + c.dataset.cat + ' ' + c.dataset.kw).toLowerCase();
      var okQ = !s || hay.indexOf(s) >= 0;
      c.hidden = !(okCat && okQ);
    });
    secs.forEach(function(sec){
      var any = sec.querySelector('.card:not([hidden])');
      sec.hidden = !any;
    });
    dockBtns.forEach(function(b){ b.classList.toggle('on', b.dataset.filter === active); });
    navLinks.forEach(function(a){ a.classList.toggle('on', a.dataset.filter === active); });
  }
  if(q) q.addEventListener('input', apply);
  dockBtns.forEach(function(b){
    b.addEventListener('click', function(){
      active = b.dataset.filter;
      apply();
      if(active !== 'all'){
        var s = document.querySelector('.cat[data-cat="' + active + '"]');
        if(s) s.scrollIntoView({behavior:'smooth', block:'start'});
      } else { window.scrollTo({top:0, behavior:'smooth'}); }
    });
  });
  navLinks.forEach(function(a){
    a.addEventListener('click', function(e){
      e.preventDefault();
      active = a.dataset.filter; apply();
      var s = document.querySelector('.cat[data-cat="' + active + '"]');
      if(s) s.scrollIntoView({behavior:'smooth', block:'start'});
    });
  });

  /* ── 详情面板 ── */
  var sheet = document.getElementById('sheet'), mask = document.getElementById('mask');
  var dStage = document.getElementById('dStage');
  var dId = document.getElementById('dId'), dName = document.getElementById('dName'), dCat = document.getElementById('dCat');
  var tabBtns = [].slice.call(document.querySelectorAll('.tabs button'));
  var cur = 0, order = cards.map(function(c){ return +c.dataset.i; });

  function showTab(k){
    tabBtns.forEach(function(b, i){ b.classList.toggle('on', i === k); });
    var ps = [].slice.call(document.querySelectorAll('#dDoc [data-p]'));
    ps.forEach(function(x, i){ x.hidden = i !== k; });
  }
  tabBtns.forEach(function(b, i){ b.addEventListener('click', function(){ showTab(i); }); });

  function open(i){
    cur = i;
    var it = window.__ITEMS[i];
    dId.textContent = it.id; dName.textContent = it.name; dCat.textContent = it.cat;
    var fit = dStage.closest('.fit');
    dStage.dataset.item = it.id;
    dStage.innerHTML = '';
    var tpl = document.getElementById('tpl-' + i);
    if(tpl){ dStage.innerHTML = tpl.innerHTML; }
    var dTpl = document.getElementById('doc-' + i);
    document.getElementById('dDoc').innerHTML = dTpl ? dTpl.innerHTML : '';
    var fn = window.__MOUNT && window.__MOUNT[i];
    if(typeof fn === 'function'){ try{ fn(dStage); }catch(e){ console.error('detail ' + i, e); } }
    var n = window.__ITEMS.length;
    var pv = window.__ITEMS[(i - 1 + n) % n], nx = window.__ITEMS[(i + 1) % n];
    document.querySelector('#dPrev b').textContent = pv.id + ' ' + pv.name;
    document.querySelector('#dNext b').textContent = nx.id + ' ' + nx.name;
    document.getElementById('dBody').scrollTop = 0;
    showTab(0);
    sheet.classList.add('on'); mask.classList.add('on');
    fit.style.setProperty('--s', '1');
    setTimeout(function(){ window.__fit(fit); }, 20);
    if(location.hash !== '#' + it.id) history.replaceState(null, '', '#' + it.id);
    document.body.style.overflow = 'hidden';
  }
  function close(){
    sheet.classList.remove('on'); mask.classList.remove('on');
    document.body.style.overflow = '';
    if(location.hash) history.replaceState(null, '', location.pathname);
  }
  cards.forEach(function(c){
    c.addEventListener('click', function(){ open(+c.dataset.i); });
  });
  mask.addEventListener('click', close);
  document.getElementById('dClose').addEventListener('click', close);
  document.addEventListener('keydown', function(e){
    if(sheet.classList.contains('on')){
      if(e.key === 'Escape') close();
      if(e.key === 'ArrowRight') open((cur + 1) % order.length);
      if(e.key === 'ArrowLeft')  open((cur - 1 + order.length) % order.length);
    }
  });
  document.getElementById('dPrev').addEventListener('click', function(){ open((cur - 1 + order.length) % order.length); });
  document.getElementById('dNext').addEventListener('click', function(){ open((cur + 1) % order.length); });

  var h = location.hash.replace('#', '');
  if(h){
    var i = window.__ITEMS.findIndex(function(x){ return x.id === h; });
    if(i >= 0) setTimeout(function(){ open(i); }, 60);
  }
  apply();
})();
"""
