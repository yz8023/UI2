# -*- coding: utf-8 -*-
"""体验馆 / 项目结构 / 搜索的样式。"""

EXP_CSS = r"""
/* ══════════ 通用小件 ══════════ */
.lede2{font-size:12px;line-height:1.95;color:rgba(233,239,247,.55);margin:6px 2px 2px;max-width:640px}
.lede2 b{color:rgba(233,239,247,.9);font-weight:600}
.empty{padding:34px 18px;text-align:center;font-size:12.5px;color:rgba(233,239,247,.45);line-height:1.9}
.sec{font-size:11px;letter-spacing:.1em;color:rgba(233,239,247,.34);margin:22px 2px 9px}

/* ══════════ 分类树（素材页） ══════════ */
.catgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px;margin-top:10px}
.catcard{position:relative;padding:11px 12px;border-radius:15px;cursor:pointer;overflow:hidden;
  border:1px solid rgba(255,255,255,.09);background:rgba(255,255,255,.035);
  transition:.2s var(--ease)}
.catcard:active{transform:scale(.985)}
.catcard.on{border-color:rgba(157,204,255,.5);background:linear-gradient(150deg,rgba(157,204,255,.16),rgba(95,219,168,.07));
  box-shadow:0 10px 26px -14px rgba(120,180,240,.7)}
.catcard .code{font-size:9.5px;font-weight:700;color:rgba(157,204,255,.85);letter-spacing:.08em;
  font-family:ui-monospace,Menlo,monospace}
.catcard h4{font-size:12.5px;font-weight:700;margin-top:3px;display:flex;align-items:center;gap:6px}
.catcard h4 em{font-style:normal;font-size:9px;color:rgba(233,239,247,.4);font-weight:400}
.catcard p{font-size:9.5px;color:rgba(233,239,247,.42);line-height:1.55;margin-top:3px;
  display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.catcard .n{position:absolute;right:9px;top:8px;font-size:14px;font-weight:800;color:rgba(255,255,255,.14)}

/* ══════════ 搜索结果 ══════════ */
.srhead{font-size:11px;color:rgba(233,239,247,.42);margin:12px 2px 4px}
.srow{display:flex;align-items:baseline;gap:9px;padding:10px 12px;border-radius:12px;cursor:pointer;
  border:1px solid rgba(255,255,255,.07);background:rgba(255,255,255,.03);margin-bottom:6px}
.srow:active{background:rgba(255,255,255,.08)}
.srow b{font-size:12.5px;font-weight:600;flex:0 0 auto;max-width:44%;overflow:hidden;text-overflow:ellipsis;
  white-space:nowrap}
.srow span{font-size:10px;color:rgba(233,239,247,.38);flex:1;min-width:0;overflow:hidden;
  text-overflow:ellipsis;white-space:nowrap}
.srow i{font-style:normal;font-size:9px;color:rgba(157,204,255,.9);border:1px solid rgba(157,204,255,.26);
  padding:1px 6px;border-radius:99px;flex:0 0 auto}

/* ══════════ 项目结构 ══════════ */
.tree{border-radius:14px;border:1px solid rgba(255,255,255,.1);background:rgba(6,11,17,.55);
  padding:10px 12px;font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;overflow:auto}
.tree .tr{display:flex;align-items:baseline;gap:7px;font-size:11px;line-height:2;white-space:nowrap}
.tree .ic{color:rgba(157,204,255,.5);font-size:9px}
.tree .nm{color:rgba(233,239,247,.88)}
.tree .nm.dir{color:rgba(157,204,255,.95);font-weight:600}
.tree .mt{font-size:8.5px;color:#06121c;background:rgba(157,204,255,.8);padding:0 5px;border-radius:4px;
  font-family:'Segoe UI',sans-serif}
.tree .nt{color:rgba(233,239,247,.32);font-size:10px;font-family:'Segoe UI',sans-serif;
  overflow:hidden;text-overflow:ellipsis}
.featwrap{display:flex;flex-direction:column;gap:7px}
.featwrap .feat{display:flex;gap:11px;padding:11px 12px;border-radius:14px;cursor:pointer;align-items:flex-start;
  border:1px solid rgba(255,255,255,.08);background:rgba(255,255,255,.03);transition:.18s}
.featwrap .feat.on{border-color:rgba(95,219,168,.45);background:rgba(95,219,168,.08)}
.featwrap .feat > b{width:22px;height:22px;flex:0 0 auto;border-radius:7px;display:grid;place-items:center;
  font-size:11px;font-weight:700;background:rgba(255,255,255,.07);color:rgba(233,239,247,.7)}
.featwrap .feat.on > b{background:rgba(95,219,168,.22);color:#8ff0c6}
.featwrap .feat h5{font-size:12.5px;font-weight:700}
.featwrap .feat p{font-size:10px;color:rgba(233,239,247,.42);margin-top:2px;line-height:1.55}
.featwrap .feat .chips2{display:flex;gap:4px;flex-wrap:wrap;margin-top:6px}
.featwrap .feat .chips2 s{text-decoration:none;font-size:8.5px;padding:1px 5px;border-radius:4px;
  color:rgba(233,239,247,.5);border:1px solid rgba(255,255,255,.1);font-family:ui-monospace,Menlo,monospace}
.featwrap .feat .chips2 s.xp{color:rgba(157,204,255,.9);border-color:rgba(157,204,255,.26)}
.feat .chips2 s.rc{color:rgba(95,219,168,.9);border-color:rgba(95,219,168,.26)}
.feat > i{font-style:normal;font-size:12px;color:#5fdba8;margin-left:auto;align-self:center}
.maprow{display:flex;gap:10px;padding:9px 2px;border-bottom:1px solid rgba(255,255,255,.06);font-size:11.5px}
.maprow .k{width:86px;flex:0 0 auto;color:rgba(233,239,247,.6)}
.maprow .v{flex:1;display:flex;gap:5px;flex-wrap:wrap}
.maprow a{font-size:9.5px;padding:1px 6px;border-radius:5px;cursor:pointer;font-family:ui-monospace,Menlo,monospace;
  color:rgba(157,204,255,.95);border:1px solid rgba(157,204,255,.26);background:rgba(157,204,255,.08)}
.maprow a.xpj{color:rgba(233,239,247,.72);border-color:rgba(255,255,255,.14);background:rgba(255,255,255,.05)}
.maprow a.rcj{color:rgba(95,219,168,.95);border-color:rgba(95,219,168,.26);background:rgba(95,219,168,.08)}

/* ══════════ 实验室 ══════════ */
.labbox .lb{box-shadow:0 6px 18px rgba(120,180,240,.35)}
"""

EXP_CSS += r"""
/* ══════════ 首页四个入口 ══════════ */
.entries{display:grid;grid-template-columns:repeat(2,1fr);gap:9px}
.entry{padding:13px 13px 12px;border-radius:16px;cursor:pointer;text-decoration:none;
  border:1px solid rgba(255,255,255,.1);background:linear-gradient(150deg,rgba(255,255,255,.06),rgba(255,255,255,.02));
  transition:.2s var(--ease);display:block}
.entry:active{transform:scale(.985)}
.entry b{display:inline-grid;place-items:center;width:26px;height:26px;border-radius:8px;font-size:13px;
  background:linear-gradient(150deg,rgba(157,204,255,.26),rgba(95,219,168,.14));
  border:1px solid rgba(157,204,255,.26);color:#cfe3ff}
.entry h4{font-size:12.5px;font-weight:700;margin-top:7px}
.entry p{font-size:9.5px;color:rgba(233,239,247,.42);line-height:1.6;margin-top:2px}
@media (max-width:520px){ .entries{grid-template-columns:1fr 1fr} }
"""

EXP_CSS += r"""
.an-t{position:relative}
.an-t em{display:block;font-style:normal;font-size:8px;line-height:1.5;color:rgba(157,204,255,.5);
  font-family:ui-monospace,Menlo,monospace;margin-top:1px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.an-card{max-width:92%;font-size:8px;padding:5px 7px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
"""

EXP_CSS += r"""
/* ── 动画网格：小舞台 + 两行说明 ── */
.an-grid{grid-template-columns:repeat(2,1fr) !important;gap:9px !important}
.an-t{height:104px !important;overflow:hidden;background:rgba(255,255,255,.028);
  border:1px solid rgba(255,255,255,.08);border-radius:13px}
.an-t:active{background:rgba(157,204,255,.1)}
.an-t .an-stage{position:absolute;inset:26px 8px 30px;display:grid;place-items:center;
  border-radius:9px;background:rgba(6,11,17,.5);border:1px solid rgba(255,255,255,.05);overflow:hidden}
.an-t .an-card{width:44px;height:26px;border-radius:8px;display:grid;place-items:center;
  background:linear-gradient(150deg,#3a6a97,#1a2a3a);border:1px solid rgba(157,204,255,.34);
  box-shadow:0 8px 18px rgba(0,0,0,.4);font-size:0}
.an-t span{position:absolute;left:8px;right:8px;bottom:13px;font-size:9px;line-height:1.2;
  color:rgba(233,239,247,.66);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.an-t em{position:absolute;left:8px;right:8px;bottom:4px;font-family:ui-monospace,Menlo,monospace;
  font-size:7px;line-height:1.2;color:rgba(157,204,255,.45);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
"""

EXP_CSS += r"""
/* ── 分类详情 / 相关入口 ── */
.backrow{display:inline-flex;align-items:center;gap:5px;font-size:12px;color:rgba(157,204,255,.9);
  padding:6px 11px;border-radius:99px;border:1px solid rgba(157,204,255,.22);
  background:rgba(157,204,255,.08);margin-bottom:12px;cursor:pointer}
.rlinks{display:grid;gap:8px}
.rlink{display:flex;align-items:center;gap:10px;padding:12px 14px;border-radius:13px;cursor:pointer;
  border:1px solid rgba(255,255,255,.1);background:rgba(255,255,255,.035)}
.rlink b{font-size:12.5px;font-weight:600}
.rlink span{margin-left:auto;font-size:10px;color:rgba(157,204,255,.75)}
.rlink:active{background:rgba(157,204,255,.1)}
.catmeta{display:flex;gap:6px;flex-wrap:wrap;margin:10px 0 4px}
.catmeta s{text-decoration:none;font-size:9.5px;padding:4px 9px;border-radius:99px;
  color:rgba(233,239,247,.55);background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.08)}
#qClear{cursor:pointer}
"""

EXP_CSS += r"""
.cpbtn{position:absolute;right:8px;top:8px;z-index:4;height:24px;padding:0 9px;border-radius:8px;
  font:inherit;font-size:9.5px;font-weight:600;color:#cfe3ff;cursor:pointer;
  background:rgba(10,17,25,.72);border:1px solid rgba(157,204,255,.3);
  -webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px)}
.cpbtn:active{transform:scale(.96)}
.cpbtn.done{color:#bff0d5;border-color:rgba(95,219,168,.42);background:rgba(20,60,44,.8)}
.recuse{font-size:9.5px;color:rgba(233,239,247,.4);line-height:1.6;margin-top:6px}
"""

EXP_CSS += r"""
/* 首页「先看这四个」：两列紧凑卡 */
.pick4{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.pick4 .card{padding:8px;border-radius:15px}
.pick4 .card .mini{height:118px !important}
.pick4 .card-b{padding:7px 2px 1px}
.pick4 .card-t{font-size:11px;gap:5px}
.pick4 .card-t .num{font-size:8px;padding:1px 4px}
.pick4 .card-s{font-size:10px;min-height:0;margin-top:3px;-webkit-line-clamp:2}
.pick4 .tags{margin-top:5px;gap:4px}
.pick4 .tags .tag{font-size:8.5px;padding:1.5px 6px}
.pick4 .tags .tag:nth-child(3){display:none}
"""

EXP_CSS += r"""
/* ── 案例剧场 ── */
.th-title{font-size:clamp(24px,6.6vw,32px);font-weight:800;letter-spacing:-.03em;line-height:1.2;margin-top:2px}
.th-sub{font-size:12px;color:var(--soft);line-height:1.7;margin-top:6px}
.th-meta{display:flex;gap:5px;flex-wrap:wrap;margin-top:10px}
.th-meta s{text-decoration:none;font-size:9px;padding:3px 8px;border-radius:99px;color:var(--soft);
  background:rgba(255,255,255,.055);border:1px solid var(--line);font-family:ui-monospace,Menlo,monospace}
.th-stage{margin-top:13px;border-radius:22px;overflow:hidden;border:1px solid rgba(255,255,255,.1);
  background:radial-gradient(120% 90% at 50% 0%,rgba(157,204,255,.08),rgba(6,8,12,.9) 62%),#080a0e;
  box-shadow:0 24px 50px rgba(0,0,0,.5), inset 0 1px 0 rgba(255,255,255,.07);position:relative}
.th-mini{height:auto !important;margin:0 !important;border:0 !important;border-radius:0 !important;
  background:transparent !important}
.th-mini canvas{height:380px}
.th-hint{position:absolute;left:50%;bottom:10px;transform:translateX(-50%);font-size:9.5px;
  color:rgba(238,242,247,.42);background:rgba(0,0,0,.34);padding:3px 10px;border-radius:99px;
  border:1px solid rgba(255,255,255,.07);pointer-events:none;white-space:nowrap}
.th-info{display:grid;gap:8px;margin-top:12px}
.th-k{padding:11px 13px;border-radius:15px;border:1px solid var(--line);background:rgba(255,255,255,.032)}
.th-k em{font-style:normal;font-size:9px;letter-spacing:.14em;color:rgba(157,204,255,.85);font-weight:700}
.th-k p{font-size:11px;line-height:1.72;color:rgba(238,242,247,.7);margin-top:4px}
.th-tabs{display:grid;grid-template-columns:repeat(2,1fr);gap:7px}
.th-tab{display:flex;align-items:center;gap:8px;padding:9px 11px;border-radius:13px;cursor:pointer;
  border:1px solid var(--line);background:rgba(255,255,255,.03)}
.th-tab b{width:17px;height:17px;border-radius:6px;display:grid;place-items:center;font-size:8.5px;
  background:rgba(255,255,255,.06);color:var(--dim);flex:0 0 auto}
.th-tab span{font-size:10.5px;color:var(--soft);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.th-tab.on{border-color:rgba(157,204,255,.42);background:rgba(157,204,255,.12)}
.th-tab.on b{background:rgba(157,204,255,.3);color:#0b1015}
.th-tab.on span{color:#e8f2ff;font-weight:650}
.th-pn{display:flex;gap:8px;margin-top:10px}
.th-p{flex:1;padding:11px 13px;border-radius:14px;font-size:11px;color:var(--soft);cursor:pointer;
  border:1px solid var(--line);background:rgba(255,255,255,.03);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.th-p:last-child{text-align:right}
.th-p:active{background:rgba(255,255,255,.07)}
@media (min-width:640px){ .th-mini canvas{height:440px} }
"""

EXP_CSS += r"""
/* 剧场里的 DOM 型演示要撑满 */
.th-mini{height:380px !important;overflow:hidden;border-radius:0}
.th-mini .m4scroll{height:100% !important}
.th-mini .m4screen{height:236px}
.th-mini .mini-chip{top:8px;right:8px;left:auto}
@media (min-width:640px){
  .th-mini{height:440px !important}
  .th-mini canvas{height:440px}
  .th-mini .m4screen{height:272px}
}
"""
