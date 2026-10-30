# -*- coding: utf-8 -*-
"""素材库 App：外壳（CSS / HTML / 交互）"""

import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'video-demos'))
from _lib import RESET  # noqa

APP_CSS = RESET + r"""
:root{
  --bg:#0b1219; --night:#0e151d; --card:rgba(255,255,255,.055); --card-2:rgba(255,255,255,.085);
  --txt:#e9eff7; --soft:rgba(233,239,247,.62); --dim:rgba(233,239,247,.40);
  --line:rgba(255,255,255,.13); --line-2:rgba(255,255,255,.22);
  --blue:#9dccff; --blue-c:#164a70; --mint:#5fdba8; --violet:#9d8cff; --amber:#ffd28a; --rose:#ff8fa3;
  --r:20px; --r2:14px; --pill:999px; --ease:cubic-bezier(.2,.9,.3,1.1);
}
body{
  font-family:'Segoe UI','PingFang SC','HarmonyOS Sans SC','Microsoft YaHei',system-ui,sans-serif;
  background:var(--bg); color:var(--txt); min-height:100vh; overflow-x:hidden;
  font-size:14px; line-height:1.6; -webkit-font-smoothing:antialiased;
}
body[data-palette="mint"]  {--blue:#5fdba8;--blue-c:#0b4d3a;}
body[data-palette="sunset"]{--blue:#ffb77a;--blue-c:#6c3600;}
body[data-palette="mono"]  {--blue:#a5c8dd;--blue-c:#293e4d;}
body[data-palette="coral"] {--blue:#ffb4a5;--blue-c:#7b2f25;}
body[data-palette="sakura"]{--blue:#ffb1c7;--blue-c:#723349;}
body[data-palette="galaxy"]{--blue:#b4c5ff;--blue-c:#303d8c;}
img,svg{display:block}
button,input,select,textarea{font:inherit;color:inherit;background:none;border:0;outline:none}
a{color:inherit;text-decoration:none}
::selection{background:rgba(157,204,255,.28)}

/* ---------- 极光背景 ---------- */
.aurora{position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden}
.blob{position:absolute;border-radius:50%;filter:blur(72px);opacity:.48;will-change:transform;
  animation:drift 30s linear infinite}
.blob:nth-child(1){width:58vmax;height:58vmax;top:-16vmax;left:-12vmax;
  background:radial-gradient(circle,rgba(29,74,115,.95),transparent 70%)}
.blob:nth-child(2){width:50vmax;height:50vmax;top:-8vmax;right:-16vmax;
  background:radial-gradient(circle,rgba(88,61,180,.8),transparent 70%);animation-duration:36s;animation-direction:reverse}
.blob:nth-child(3){width:60vmax;height:60vmax;bottom:-22vmax;left:-8vmax;
  background:radial-gradient(circle,rgba(23,110,88,.7),transparent 70%);animation-duration:42s}
.blob:nth-child(4){width:42vmax;height:42vmax;bottom:-12vmax;right:-8vmax;
  background:radial-gradient(circle,rgba(29,74,115,.85),transparent 70%);animation-duration:28s;animation-direction:reverse}
@keyframes drift{from{transform:translate3d(0,0,0) scale(1)}to{transform:translate3d(4vmax,-3vmax,0) scale(1.12)}}
body.reduce .blob{animation:none}
body.reduce .enter{animation:none!important}

/* ---------- 玻璃 ---------- */
.glass{position:relative;background:linear-gradient(180deg,rgba(255,255,255,.07),rgba(255,255,255,.022));
  border:1px solid rgba(255,255,255,.15);box-shadow:0 12px 32px rgba(0,0,0,.34);border-radius:var(--r)}
@supports (backdrop-filter:blur(24px)) or (-webkit-backdrop-filter:blur(24px)){
  .glass{-webkit-backdrop-filter:blur(24px) saturate(1.5) brightness(1.06);backdrop-filter:blur(24px) saturate(1.5) brightness(1.06)}
}
body.normal .glass{-webkit-backdrop-filter:none!important;backdrop-filter:none!important;background:#1a222a;
  border-color:rgba(255,255,255,.08);box-shadow:0 8px 20px rgba(0,0,0,.3)}
[hidden]{display:none!important}

/* ---------- 布局 ---------- */
.shell{position:relative;z-index:1;max-width:1080px;margin:0 auto;padding:18px 16px 132px}
.topbar{display:flex;align-items:center;gap:10px;padding:4px 2px 12px}
.brand{display:flex;align-items:center;gap:9px;font-size:15px;font-weight:700;letter-spacing:.3px}
.brand i{width:26px;height:26px;border-radius:9px;background:linear-gradient(150deg,var(--blue),var(--blue-c));
  display:grid;place-items:center;font-style:normal;font-size:12px;color:#06121c;font-weight:700;
  box-shadow:0 4px 14px rgba(0,0,0,.4)}
.brand small{display:block;font-size:10.5px;font-weight:400;color:var(--dim);letter-spacing:.02em}
.grow{flex:1}
.pal{display:flex;gap:6px;align-items:center}
.dot{width:16px;height:16px;border-radius:50%;border:2px solid transparent;cursor:pointer;transition:.2s}
.dot.on{border-color:var(--txt);transform:scale(1.15)}
.dot-aurora{background:#9dccff}.dot-mint{background:#5fdba8}.dot-sunset{background:#ffb77a}
.dot-mono{background:#a5c8dd}.dot-coral{background:#ffb4a5}.dot-sakura{background:#ffb1c7}.dot-galaxy{background:#b4c5ff}
.libbanner{display:flex;align-items:center;gap:12px;padding:14px 16px;margin:14px 0 4px;border-radius:16px;
  border:1px solid rgba(157,204,255,.34);background:linear-gradient(150deg,rgba(157,204,255,.16),rgba(95,219,168,.10));
  box-shadow:0 14px 30px rgba(0,0,0,.35)}
.libbanner .lb-t{font-size:13.5px;font-weight:800;letter-spacing:-.01em}
.libbanner .lb-d{font-size:10.5px;color:rgba(233,239,247,.55);line-height:1.7;margin-top:4px}
.libbanner .lb-r{margin-left:auto;font-size:11px;font-weight:700;color:#06121c;background:linear-gradient(180deg,#cfe3ff,#9dccff);
  padding:6px 11px;border-radius:99px;white-space:nowrap}
.tag.f{background:rgba(157,204,255,.16);color:#cfe3ff}
.mini-ico{width:34px;height:34px;border-radius:11px;display:grid;place-items:center;cursor:pointer;
  background:rgba(255,255,255,.07);border:1px solid var(--line);color:var(--soft)}
.mini-ico:hover{background:rgba(255,255,255,.12);color:#fff}

h1.title{font-size:clamp(24px,3.4vw,34px);line-height:1.28;letter-spacing:-.02em;margin:6px 0 8px;font-weight:700}
.lede{font-size:13.5px;color:var(--soft);max-width:62ch}
.lede b{color:var(--txt);font-weight:600}

/* ---------- 首页 ---------- */
.hero{padding:20px 20px 18px;border-radius:24px}
.stats{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}
.pillchip{font-size:11.5px;padding:5px 11px;border-radius:var(--pill);background:rgba(255,255,255,.07);
  border:1px solid var(--line);color:var(--soft)}
.pillchip b{color:var(--txt)}
.sec{display:flex;align-items:center;gap:8px;margin:26px 2px 12px;font-size:12px;font-weight:600;
  color:var(--soft);letter-spacing:.06em}
.sec::before{content:"";width:9px;height:9px;border-radius:3px;background:var(--blue);box-shadow:0 0 14px var(--blue)}
.coll3{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.coll{padding:16px;border-radius:18px;cursor:pointer;transition:transform .2s var(--ease),box-shadow .2s}
.coll:hover{transform:translateY(-3px);box-shadow:0 18px 40px rgba(0,0,0,.45)}
.coll .k{font-size:26px;font-weight:700;line-height:1;letter-spacing:-.02em}
.coll .n{font-size:12.5px;margin-top:7px;color:var(--txt)}
.coll .d{font-size:11px;color:var(--dim);margin-top:3px;line-height:1.55}
.pick4{display:grid;grid-template-columns:1fr 1fr;gap:12px}

/* ---------- 卡片 ---------- */
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}
.card{display:flex;flex-direction:column;border-radius:18px;padding:10px;cursor:pointer;transition:transform .2s var(--ease),box-shadow .2s;
  background:linear-gradient(180deg,rgba(255,255,255,.07),rgba(255,255,255,.022));
  border:1px solid rgba(255,255,255,.13);box-shadow:0 8px 22px rgba(0,0,0,.28)}
.card:hover{transform:translateY(-3px);box-shadow:0 18px 40px rgba(0,0,0,.45)}
body.normal .card{background:#1a222a;border-color:rgba(255,255,255,.07)}
.card-b{padding:9px 4px 3px}
.card-t{display:flex;align-items:center;gap:7px;font-size:13.5px;font-weight:600}
.num{font-size:9.5px;font-weight:700;letter-spacing:.06em;color:#06121c;background:var(--blue);
  padding:2px 6px;border-radius:5px;font-family:ui-monospace,monospace}
.card-s{font-size:11.5px;color:var(--dim);margin-top:4px;line-height:1.5;min-height:34px;
  display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.card .mini{flex:0 0 auto}
.tags{display:flex;gap:5px;margin-top:7px;flex-wrap:wrap}
.tag{font-size:10px;padding:2.5px 8px;border-radius:6px;background:rgba(157,204,255,.14);color:#a9cdf0}
.tag.g{background:rgba(95,219,168,.13);color:#8fe3c2}
.tag.v{background:rgba(157,140,255,.14);color:#c4bbff}
.tag.m{background:rgba(255,210,138,.13);color:#ffd28a}

/* ---------- 搜索 / 筛选 ---------- */
.searchrow{display:flex;gap:8px;align-items:center;margin:4px 0 10px}
.search{flex:1;display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:14px;
  background:rgba(255,255,255,.07);border:1px solid var(--line)}
.search input{flex:1;font-size:13px;color:var(--txt)}
.search input::placeholder{color:var(--dim)}
.search .cnt{font-size:11px;color:var(--dim);white-space:nowrap}
.filters{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:14px}
.fchip{font-size:11.5px;padding:5px 12px;border-radius:var(--pill);border:1px solid var(--line);
  color:var(--soft);cursor:pointer;transition:.2s}
.fchip.on{background:rgba(157,204,255,.18);border-color:rgba(157,204,255,.5);color:#d5e8ff}
.empty{padding:40px 12px;text-align:center;color:var(--dim);font-size:13px}

/* ---------- 详情面板 ---------- */
.sheet{position:fixed;inset:0;z-index:60;display:flex;align-items:flex-end;justify-content:center;
  background:rgba(4,8,12,.6);opacity:0;pointer-events:none;transition:opacity .25s}
.sheet.on{opacity:1;pointer-events:auto}
.sheet-box{width:100%;max-width:760px;max-height:92vh;overflow-y:auto;overscroll-behavior:contain;
  border-radius:24px 24px 0 0;padding:16px 16px 26px;
  background:linear-gradient(180deg,#151d25,#0f151b);border:1px solid var(--line);border-bottom:0;
  transform:translateY(24px);transition:transform .3s var(--ease);scrollbar-width:thin}
.sheet.on .sheet-box{transform:none}
.sheet-h{display:flex;align-items:flex-start;gap:10px;position:sticky;top:-16px;background:#151d25;
  padding:6px 0 10px;border-bottom:1px solid var(--line);margin-bottom:12px;z-index:2}
.sheet-h h2{display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;font-size:16px;line-height:1.35}
.sheet-h .sub{font-size:11.5px;color:var(--dim);margin-top:3px}
.x{width:32px;height:32px;border-radius:10px;display:grid;place-items:center;cursor:pointer;
  background:rgba(255,255,255,.07);border:1px solid var(--line);color:var(--soft);flex:0 0 auto}
.x:hover{color:#fff;background:rgba(255,255,255,.13)}
.kv{display:grid;gap:9px;margin:12px 0}
.kv .row{display:grid;grid-template-columns:64px 1fr;gap:10px;font-size:12.5px;line-height:1.65}
.kv .k{color:var(--dim)}
.kv .v{color:var(--soft)}
.kv .v b{color:var(--txt)}
.reqs{display:flex;gap:6px;flex-wrap:wrap;margin:10px 0}
.req{font-size:11px;padding:5px 10px;border-radius:var(--pill);border:1px solid var(--line);
  color:var(--soft);cursor:pointer;user-select:none;transition:.18s}
.req.on{background:rgba(95,219,168,.16);border-color:rgba(95,219,168,.45);color:#a8f0d2}
.custom{width:100%;min-height:52px;resize:vertical;padding:9px 12px;border-radius:11px;font-size:12px;
  background:rgba(255,255,255,.06);border:1px solid var(--line);color:var(--txt);line-height:1.6}
.custom::placeholder{color:var(--dim)}
pre.pcode{margin:10px 0;padding:12px;border-radius:12px;background:rgba(0,0,0,.32);
  border:1px solid rgba(255,255,255,.07);font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size:11px;line-height:1.75;white-space:pre-wrap;word-break:break-word;max-height:230px;overflow:auto;color:rgba(233,239,247,.8)}
.actrow{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-top:6px}
.btn{padding:9px 15px;border-radius:11px;font-size:12.5px;font-weight:600;cursor:pointer;
  background:rgba(255,255,255,.09);border:1px solid var(--line);color:var(--txt);
  transition:transform .12s var(--ease),background .18s}
.btn:active{transform:scale(.97)}
.btn.primary{background:linear-gradient(150deg,var(--blue),var(--blue-c));color:#06121c;border-color:transparent}
.btn.primary.done{background:var(--mint);color:#062b20}
.btn.ghost{background:transparent;color:var(--soft)}
.btn.sm{padding:6px 11px;font-size:11.5px}
.tip{font-size:10.5px;color:var(--dim)}

/* ---------- 对比 ---------- */
.cmp .slots{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.slot{padding:10px;border-radius:16px;background:rgba(255,255,255,.05);border:1px solid var(--line)}
.slot-h{display:flex;align-items:center;gap:8px;font-size:12.5px;font-weight:600;margin-bottom:8px}
.slot-h .badge{font-size:9.5px;padding:2px 6px;border-radius:5px;background:var(--blue);color:#06121c;font-weight:700}
.slot-h select{margin-left:auto;font-size:11px;padding:4px 8px;border-radius:8px;
  background:#1b232b;border:1px solid var(--line);color:var(--soft);max-width:52%}
.diffs{margin-top:12px;border-radius:16px;overflow:hidden;border:1px solid var(--line)}
.drow{display:grid;grid-template-columns:74px 1fr 1fr;gap:10px;padding:10px 12px;font-size:11.5px;
  border-top:1px solid rgba(255,255,255,.06);line-height:1.6}
.drow.head{border-top:0;background:rgba(255,255,255,.05);color:var(--soft);font-weight:600}
.drow .k{color:var(--dim)}

/* ---------- 设置 ---------- */
.setrow{display:flex;align-items:center;gap:12px;padding:13px 2px;border-bottom:1px solid rgba(255,255,255,.07)}
.setrow:last-child{border-bottom:0}
.setrow .lab{flex:1;font-size:13px}
.setrow .lab small{display:block;font-size:11px;color:var(--dim);margin-top:2px}
.sw{position:relative;width:46px;height:27px;border-radius:var(--pill);background:rgba(255,255,255,.14);
  cursor:pointer;transition:background .22s;flex:0 0 auto}
.sw::after{content:"";position:absolute;top:3px;left:3px;width:21px;height:21px;border-radius:50%;background:#fff;
  transition:left .24s var(--ease)}
.sw.on{background:var(--blue-c)}
.sw.on::after{left:22px}

/* ---------- 底部标签栏 ---------- */
.tabbar{position:fixed;left:50%;transform:translateX(-50%);bottom:calc(env(safe-area-inset-bottom,0px) + 14px);
  width:min(520px,calc(100% - 28px));height:64px;display:flex;align-items:center;justify-content:space-around;
  padding:0 6px;border-radius:24px;z-index:50}
.tabbar .pill{position:absolute;left:0;bottom:7px;height:34px;border-radius:var(--pill);background:rgba(255,255,255,.11);
  border:1px solid rgba(255,255,255,.18);transition:width .42s var(--ease),transform .42s var(--ease)}
.tab{position:relative;flex:1;display:flex;flex-direction:column;align-items:center;gap:3px;font-size:10.5px;
  color:var(--dim);cursor:pointer;padding:8px 0;z-index:1;transition:color .2s}
.tab .ico{font-size:17px;line-height:1}
.tab.active{color:var(--txt)}

/* ---------- 新手引导 ---------- */
.welcome{position:fixed;inset:0;z-index:70;display:grid;place-items:center;padding:20px;
  background:rgba(4,8,12,.66);opacity:0;pointer-events:none;transition:opacity .28s}
.welcome.on{opacity:1;pointer-events:auto}
.welcome-card{width:min(430px,100%);padding:24px 22px 18px;border-radius:24px;text-align:center;
  transform:translateY(14px) scale(.97);transition:transform .32s var(--ease)}
.welcome.on .welcome-card{transform:none}
.w-ico{width:54px;height:54px;border-radius:17px;margin:0 auto 14px;display:grid;place-items:center;
  font-size:22px;font-weight:700;color:#06121c;background:linear-gradient(150deg,var(--blue),var(--blue-c));
  box-shadow:0 10px 26px rgba(0,0,0,.45)}
.welcome-card h2{font-size:18px;line-height:1.4}
.w-sub{font-size:12.5px;color:var(--soft);line-height:1.75;margin-top:8px}
.w-steps{list-style:none;text-align:left;display:grid;gap:9px;margin:16px 0 4px}
.w-steps li{display:grid;grid-template-columns:22px 1fr;gap:9px;font-size:12px;color:var(--soft);line-height:1.65}
.w-steps li b{width:22px;height:22px;border-radius:7px;display:grid;place-items:center;font-size:10.5px;
  background:rgba(157,204,255,.18);color:#cfe4ff;border:1px solid rgba(157,204,255,.35)}
.w-act{display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin-top:16px}
.w-foot{font-size:10.5px;color:var(--dim);margin-top:12px}

/* ---------- 空态 / toast ---------- */
.toast{position:fixed;left:50%;bottom:96px;transform:translateX(-50%) translateY(10px);z-index:80;
  padding:9px 15px;border-radius:11px;font-size:12px;color:#eaf3ff;background:rgba(18,24,30,.96);
  border:1px solid rgba(255,255,255,.18);opacity:0;pointer-events:none;transition:.24s;white-space:nowrap}
.toast.on{opacity:1;transform:translateX(-50%) translateY(0)}
.enter{animation:rise .55s var(--ease) both}
@keyframes rise{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
.note{font-size:11px;color:var(--dim);line-height:1.75}
.note b{color:var(--soft)}
.linkrow{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}
.linkrow a{font-size:11.5px;padding:7px 12px;border-radius:10px;background:rgba(255,255,255,.07);
  border:1px solid var(--line);color:var(--soft)}
.linkrow a:hover{color:#fff;background:rgba(255,255,255,.13)}

@media (max-width:860px){
  .coll3{grid-template-columns:1fr}
  .pick4{grid-template-columns:1fr}
  .cmp .slots{grid-template-columns:1fr}
  .drow{grid-template-columns:64px 1fr;font-size:11px}
  .drow .v2{grid-column:2}
}
@media (max-width:520px){
  .shell{padding:14px 12px 124px}
  .topbar .pal{display:none}      /* 只收起顶栏那排色点，设置页里的要留着 */
}


/* ══════════════════════════════════════════════════════════════
   v3 · Dock 外壳（替换 v2 的「顶部大标题 + 底部胶囊标签栏」）
   · 近黑中性底 + 冷调极淡光团，不再用大面积蓝色极光
   · 顶栏变成一条浮动玻璃条（sticky）
   · 底部改成悬浮 Dock：图标格 + 滑动指示器
   ══════════════════════════════════════════════════════════════ */
:root{
  --bg:#08090c; --night:#0b0d11;
  --card:rgba(255,255,255,.045); --card-2:rgba(255,255,255,.075);
  --txt:#eef2f7; --soft:rgba(238,242,247,.60); --dim:rgba(238,242,247,.36);
  --line:rgba(255,255,255,.09); --line-2:rgba(255,255,255,.16);
  --r:24px; --r2:16px;
  --ease:cubic-bezier(.22,.9,.28,1);
}
body{background:var(--bg)}
/* 光团：低饱和、更小、更慢 */
.aurora{opacity:.5}
.blob{filter:blur(90px);opacity:.5}
.blob:nth-child(1){width:44vmax;height:44vmax;top:-20vmax;left:-16vmax;
  background:radial-gradient(circle,rgba(38,78,102,.55),transparent 68%)}
.blob:nth-child(2){width:38vmax;height:38vmax;top:-12vmax;right:-14vmax;
  background:radial-gradient(circle,rgba(70,58,110,.42),transparent 68%)}
.blob:nth-child(3){width:46vmax;height:46vmax;bottom:-26vmax;left:-10vmax;
  background:radial-gradient(circle,rgba(30,74,66,.36),transparent 68%)}
.blob:nth-child(4){display:none}

/* 顶栏：浮动玻璃条 */
.shell{padding:12px 14px 128px;max-width:920px}
.topbar{position:sticky;top:8px;z-index:40;margin-bottom:14px;padding:7px 9px 7px 7px;
  border-radius:18px;border:1px solid var(--line);
  background:rgba(13,15,19,.9);
  -webkit-backdrop-filter:blur(20px) saturate(1.4);backdrop-filter:blur(20px) saturate(1.4);
  box-shadow:0 10px 26px rgba(0,0,0,.42)}
.brand{gap:8px;font-size:13px}
.brand i{width:24px;height:24px;border-radius:8px;font-size:11px;
  background:linear-gradient(150deg,#e8eef6,#98a6b6);color:#07090c;
  box-shadow:0 3px 10px rgba(0,0,0,.5), inset 0 1px 0 rgba(255,255,255,.7)}
.brand small{font-size:9.5px;letter-spacing:.01em}
.mini-ico{width:30px;height:30px;border-radius:10px;background:rgba(255,255,255,.055);
  border-color:var(--line)}
.dot{width:13px;height:13px}

/* 玻璃：更干净、内高光 */
.glass{background:linear-gradient(180deg,rgba(255,255,255,.055),rgba(255,255,255,.017));
  border:1px solid rgba(255,255,255,.075);
  box-shadow:0 14px 34px rgba(0,0,0,.45), inset 0 1px 0 rgba(255,255,255,.07)}

/* ── Dock ── */
.dock{position:fixed;left:50%;transform:translateX(-50%);
  bottom:calc(env(safe-area-inset-bottom,0px) + 12px);z-index:50;
  display:flex;align-items:center;gap:2px;padding:6px;border-radius:26px;
  background:rgba(16,18,23,.72);border:1px solid rgba(255,255,255,.1);
  -webkit-backdrop-filter:blur(26px) saturate(1.7);backdrop-filter:blur(26px) saturate(1.7);
  box-shadow:0 18px 44px rgba(0,0,0,.6), inset 0 1px 0 rgba(255,255,255,.1)}
.dock .pill{position:absolute;top:6px;bottom:6px;left:0;width:0;border-radius:20px;
  background:rgba(255,255,255,.09);border:1px solid rgba(255,255,255,.1);
  transition:width .42s var(--ease),transform .42s var(--ease);pointer-events:none}
.dock .tab{flex:0 0 auto;width:62px;padding:7px 0 5px;gap:4px;border-radius:20px;
  color:var(--dim);transition:color .2s,transform .3s var(--ease)}
.dock .tab .ico{font-size:0;line-height:0}
.dock .tab svg{width:21px;height:21px;stroke:currentColor;fill:none;stroke-width:1.7;
  stroke-linecap:round;stroke-linejoin:round;transition:transform .34s var(--ease)}
.dock .tab b{font-size:9.5px;font-weight:600;letter-spacing:.02em}
.dock .tab .dotm{width:3px;height:3px;border-radius:50%;background:transparent;
  transition:background .2s,transform .2s}
.dock .tab.active{color:var(--txt)}
.dock .tab.active svg{transform:translateY(-1px) scale(1.06)}
.dock .tab.active .dotm{background:var(--txt)}
.dock .tab:hover svg{transform:translateY(-2px) scale(1.1)}
.dock .tab:active svg{transform:translateY(0) scale(.94)}
@media (max-width:360px){ .dock .tab{width:56px} }
.toast{bottom:104px}

/* ── 首页 v3 ── */
.hx-head{padding:14px 4px 4px}
.hx-hi{font-size:11px;color:var(--dim);letter-spacing:.14em}
.hx-title{font-size:clamp(26px,7.4vw,38px);line-height:1.16;letter-spacing:-.035em;
  font-weight:800;margin-top:6px}
.hx-title em{font-style:normal;color:transparent;-webkit-text-stroke:1px rgba(238,242,247,.5)}
.hx-sub{font-size:12px;color:var(--soft);line-height:1.75;margin-top:9px;max-width:40ch}
.hx-search{display:flex;align-items:center;gap:9px;margin-top:16px;padding:13px 15px;
  border-radius:18px;cursor:pointer;background:rgba(255,255,255,.05);
  border:1px solid var(--line);transition:.2s}
.hx-search:active{transform:scale(.993);background:rgba(255,255,255,.08)}
.hx-search svg{width:16px;height:16px;stroke:var(--dim);fill:none;stroke-width:1.8}
.hx-search span{font-size:12.5px;color:var(--dim)}
.hx-search i{margin-left:auto;font-style:normal;font-size:9.5px;padding:3px 7px;border-radius:7px;
  color:var(--soft);background:rgba(255,255,255,.07);border:1px solid var(--line)}
.hx-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}
.hx-card{position:relative;padding:15px 14px 13px;border-radius:20px;cursor:pointer;overflow:hidden;
  border:1px solid rgba(255,255,255,.08);
  background:linear-gradient(160deg,rgba(255,255,255,.06),rgba(255,255,255,.012));
  transition:transform .22s var(--ease),border-color .2s}
.hx-card:active{transform:scale(.985)}
.hx-card::after{content:"";position:absolute;width:120px;height:120px;right:-46px;top:-46px;
  border-radius:50%;background:radial-gradient(circle,rgba(157,204,255,.16),transparent 70%)}
.hx-card.wide{grid-column:1 / -1}
.hx-card .k{display:flex;align-items:center;gap:8px}
.hx-card .k svg{width:17px;height:17px;stroke:var(--soft);fill:none;stroke-width:1.7;
  stroke-linecap:round;stroke-linejoin:round}
.hx-card .k b{font-size:9.5px;letter-spacing:.14em;color:var(--dim);font-weight:600}
.hx-card h3{font-size:16.5px;font-weight:750;letter-spacing:-.02em;margin-top:9px}
.hx-card p{font-size:10.5px;color:var(--dim);line-height:1.65;margin-top:4px}
.hx-card .n{position:absolute;right:13px;bottom:10px;font-size:22px;font-weight:800;
  letter-spacing:-.03em;color:rgba(238,242,247,.14)}
.hx-card .chips{display:flex;gap:4px;margin-top:9px;flex-wrap:wrap}
.hx-card .chips s{text-decoration:none;font-size:8.5px;padding:2.5px 7px;border-radius:99px;
  color:var(--soft);background:rgba(255,255,255,.06);border:1px solid var(--line)}
.hx-rail{display:flex;gap:10px;overflow-x:auto;padding:2px 2px 8px;scroll-snap-type:x mandatory;
  scrollbar-width:none}
.hx-rail::-webkit-scrollbar{display:none}
.hx-rail .card{flex:0 0 232px;scroll-snap-align:start;padding:8px;border-radius:18px}
.hx-rail .card .mini{height:126px}
.hx-row{display:flex;align-items:center;gap:11px;padding:13px 14px;border-radius:18px;
  border:1px solid var(--line);background:rgba(255,255,255,.035);cursor:pointer;margin-bottom:8px}
.hx-row:active{background:rgba(255,255,255,.075)}
.hx-row .bx{width:32px;height:32px;border-radius:11px;display:grid;place-items:center;flex:0 0 auto;
  background:rgba(157,204,255,.12);border:1px solid rgba(157,204,255,.2)}
.hx-row .bx svg{width:16px;height:16px;stroke:#cfe3ff;fill:none;stroke-width:1.7}
.hx-row h4{font-size:12.5px;font-weight:650}
.hx-row p{font-size:10px;color:var(--dim);margin-top:2px}
.hx-row em{margin-left:auto;font-style:normal;font-size:10px;color:var(--soft)}
.sec{margin:24px 2px 10px;font-size:11px;letter-spacing:.1em}
.sec::before{width:6px;height:6px;border-radius:2px;opacity:.9}
"""

APP_HTML = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="color-scheme" content="dark">
<title>UI 素材库 · 素材 / 弹层 / 动效 / 结构</title>
<style>__CSS__</style>
</head>
<body data-palette="aurora">
<div class="aurora"><div class="blob"></div><div class="blob"></div><div class="blob"></div><div class="blob"></div></div>

<div class="shell">
  <header class="topbar">
    <div class="brand"><i>库</i><span>UI 素材库<small>68 素材 · 40 弹层动效 · 25 规范</small></span></div>
    <div class="grow"></div>
    <div class="pal" id="pal">
      <div class="dot dot-aurora on" data-p="aurora" title="冰蓝"></div>
      <div class="dot dot-mint" data-p="mint" title="薄荷"></div>
      <div class="dot dot-sunset" data-p="sunset" title="落日"></div>
      <div class="dot dot-mono" data-p="mono" title="素灰"></div>
      <div class="dot dot-coral" data-p="coral" title="珊瑚"></div>
      <div class="dot dot-sakura" data-p="sakura" title="樱花"></div>
      <div class="dot dot-galaxy" data-p="galaxy" title="星夜"></div>
    </div>
    <div class="mini-ico" id="glassBtn" title="液态玻璃开关">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M12 3 4 12l8 9 8-9-8-9Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
    </div>
  </header>

  <main id="main"></main>
</div>

<nav class="dock" id="tabs">
  <div class="pill" id="pill"></div>
  <div class="tab active" data-v="home"><span class="ico"><svg viewBox="0 0 24 24"><path d="M4 10.5 12 4l8 6.5"/><path d="M6.5 9.5V19h11V9.5"/><path d="M10 19v-4.5h4V19"/></svg></span><b>首页</b><i class="dotm"></i></div>
  <div class="tab" data-v="lib"><span class="ico"><svg viewBox="0 0 24 24"><rect x="4" y="4" width="6.6" height="6.6" rx="2"/><rect x="13.4" y="4" width="6.6" height="6.6" rx="2"/><rect x="4" y="13.4" width="6.6" height="6.6" rx="2"/><rect x="13.4" y="13.4" width="6.6" height="6.6" rx="2"/></svg></span><b>素材</b><i class="dotm"></i></div>
  <div class="tab" data-v="exp"><span class="ico"><svg viewBox="0 0 24 24"><path d="M12 3.5 13.9 9l5.6 1.9L13.9 13 12 18.5 10.1 13 4.5 10.9 10.1 9Z"/><path d="M18.5 16.5 19.3 19l2.2.8-2.2.8-.8 2.4-.8-2.4-2.2-.8 2.2-.8Z"/></svg></span><b>体验</b><i class="dotm"></i></div>
  <div class="tab" data-v="proj"><span class="ico"><svg viewBox="0 0 24 24"><path d="M12 3.5v5"/><rect x="8.5" y="8.5" width="7" height="5" rx="1.6"/><path d="M12 13.5v3M6.5 20v-3.5h11V20"/><path d="M6.5 16.5H4v3.5M17.5 16.5H20v3.5"/></svg></span><b>结构</b><i class="dotm"></i></div>
  <div class="tab" data-v="more"><span class="ico"><svg viewBox="0 0 24 24"><circle cx="6" cy="12" r="1.4"/><circle cx="12" cy="12" r="1.4"/><circle cx="18" cy="12" r="1.4"/></svg></span><b>更多</b><i class="dotm"></i></div>
</nav>

<div class="sheet" id="sheet" aria-hidden="true"></div>

<div class="welcome" id="welcome" aria-hidden="true">
  <div class="welcome-card glass">
    <div class="w-ico">库</div>
    <h2>把界面拆成能抄的零件</h2>
    <p class="w-sub">68 条素材分 8 类；XPopup 的 20 种弹窗 / 20 种动画 / 45 个设置 / 5 组手势，motion-web 的 7 个 case / 20 条配方 / 4 组令牌 / 25 篇规范，全部能点能拖。</p>
    <ul class="w-steps">
      <li><b>1</b><span>「素材」按分类浏览，或直接搜功能词。</span></li>
      <li><b>2</b><span>「体验」里真弹弹窗、真跑配方，7 个 case 全屏可切。</span></li>
      <li><b>3</b><span>「结构」勾功能出目录树，一键复制开工提示词。</span></li>
    </ul>
    <div class="w-act">
      <button class="btn primary" data-w-go>逛素材库</button>
      <button class="btn" data-w-demo>玩弹层</button>
      <button class="btn ghost" data-w-close>知道了</button>
    </div>
    <div class="w-foot">全部离线 · 单文件 · 无外部请求</div>
  </div>
</div>
<div class="toast" id="toast"></div>
<script>__GLASS__</script>
__PAYLOAD__
__RECJS__
<script>__MINIS__</script>
<script>__GLASSMINIS__</script>
<script>__XPJS__</script>
<script>__EXPJS__</script>
<script>__APPJS__</script>
</body>
</html>
"""

APP_CSS += r"""
/* 欢迎卡对齐 v3 */
.welcome{background:rgba(4,5,8,.7);-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px)}
.welcome-card{background:linear-gradient(180deg,rgba(24,27,33,.96),rgba(12,14,18,.98)) !important;
  border-color:rgba(255,255,255,.1) !important}
.w-ico{background:linear-gradient(150deg,#e8eef6,#98a6b6) !important;color:#07090c !important;
  border-radius:18px;box-shadow:0 8px 22px rgba(0,0,0,.55), inset 0 1px 0 rgba(255,255,255,.75)}
.welcome-card h2{font-size:18.5px;letter-spacing:-.02em}
.w-steps li b{background:rgba(255,255,255,.08) !important;color:var(--soft) !important;
  border-color:rgba(255,255,255,.14) !important}
.btn.primary{background:linear-gradient(180deg,#f2f6fb,#c9d6e4) !important;color:#0a0d12 !important;
  border:0 !important;box-shadow:0 6px 18px rgba(0,0,0,.4)}
"""

APP_CSS += r"""
/* 顶栏吸顶时左右有点浮空，补一点外扩阴影 */
.topbar::after{content:"";position:absolute;inset:-10px -14px -14px;z-index:-1;pointer-events:none;
  background:linear-gradient(180deg,rgba(8,9,12,.92),rgba(8,9,12,0) 88%)}
"""
