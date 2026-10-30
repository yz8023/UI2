# -*- coding: utf-8 -*-
"""共用样式 / 外壳 / 组件。所有页面都原样套用用户提供的 reset。"""

RESET = """* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Segoe UI', sans-serif;
    -webkit-tap-highlight-color: transparent;
}"""

SHARED_CSS = RESET + """
:root{
  --bg:#f4f3ef; --card:#fcfcfa; --card-2:#f0efea; --card-3:#e8e7e1;
  --ink:#1a1a18; --ink-2:#58574f; --ink-3:#8b8a82;
  --line:rgba(26,26,24,.08); --line-2:rgba(26,26,24,.15);
  --violet:#5b4ed6; --violet-2:rgba(91,78,214,.10); --violet-3:rgba(91,78,214,.28);
  --teal:#0e8f80; --teal-2:rgba(14,143,128,.10); --teal-3:rgba(14,143,128,.30);
  --red:#cf463a; --red-2:rgba(207,70,58,.10); --red-3:rgba(207,70,58,.30);
  --amber:#9a6b12; --amber-2:rgba(154,107,18,.12);
  --r:18px; --r2:13px; --r3:9px;
  --sh:0 1px 2px rgba(20,20,18,.04),0 8px 24px rgba(20,20,18,.055);
  --sh2:0 18px 50px rgba(20,20,18,.16),0 2px 8px rgba(20,20,18,.07);
  --ease:cubic-bezier(.215,.61,.355,1);
  --spring:cubic-bezier(.34,1.56,.64,1);
}
[data-theme="dark"]{
  --bg:#0d0d0c; --card:#151515; --card-2:#1a1a19; --card-3:#22221f;
  --ink:#ececea; --ink-2:#a8a7a2; --ink-3:#7c7b73;
  --line:rgba(255,255,255,.075); --line-2:rgba(255,255,255,.14);
  --violet:#9d90ff; --violet-2:rgba(157,144,255,.14); --violet-3:rgba(157,144,255,.32);
  --teal:#41cbb6; --teal-2:rgba(65,203,182,.13); --teal-3:rgba(65,203,182,.30);
  --red:#f08174; --red-2:rgba(240,129,116,.13); --red-3:rgba(240,129,116,.30);
  --amber:#e2b25c; --amber-2:rgba(226,178,92,.13);
  --sh:0 1px 2px rgba(0,0,0,.3),0 10px 28px rgba(0,0,0,.3);
  --sh2:0 20px 56px rgba(0,0,0,.6),0 2px 10px rgba(0,0,0,.45);
}
body{
  background:var(--bg); color:var(--ink);
  font-family:'Segoe UI','PingFang SC','Hiragino Sans GB','Noto Sans SC','Microsoft YaHei',system-ui,sans-serif;
  font-size:15px; line-height:1.65; -webkit-font-smoothing:antialiased;
  font-variant-numeric:tabular-nums; transition:background .35s var(--ease),color .35s var(--ease);
  text-wrap:pretty;
}
::selection{background:var(--violet-2)}
button{font:inherit;color:inherit;border:0;background:none;cursor:pointer}
a{color:inherit}
h1,h2,h3,h4{line-height:1.35;letter-spacing:-.018em;font-weight:600}
p{margin:0}
svg{display:block}
[hidden]{display:none!important}
.wrap{max-width:1080px;margin:0 auto;padding:0 24px}

/* topbar */
.topbar{position:sticky;top:0;z-index:100;border-bottom:1px solid var(--line);
  background:color-mix(in srgb,var(--bg) 84%,transparent);
  backdrop-filter:saturate(180%) blur(18px);-webkit-backdrop-filter:saturate(180%) blur(18px)}
.topbar .wrap{display:flex;align-items:center;gap:14px;height:60px}
.back{display:inline-flex;align-items:center;gap:7px;font-size:13px;color:var(--ink-2);
  padding:7px 12px;border-radius:9px;background:var(--card-2);text-decoration:none;white-space:nowrap;
  transition:background .2s var(--ease),color .2s var(--ease)}
.back:hover{background:var(--card-3);color:var(--ink)}
.tb-title{font-size:13px;color:var(--ink-3);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tb-title b{color:var(--ink);font-weight:600}
.tb-right{margin-left:auto;display:flex;align-items:center;gap:8px}
.iconbtn{width:34px;height:34px;border-radius:10px;display:grid;place-items:center;
  background:var(--card-2);color:var(--ink-2);transition:background .2s var(--ease),color .2s var(--ease)}
.iconbtn:hover{background:var(--card-3);color:var(--ink)}
.pill{font-size:11.5px;padding:5px 10px;border-radius:7px;background:var(--card-2);color:var(--ink-2);white-space:nowrap}

/* hero */
main{padding:36px 0 80px}
.hero{padding-bottom:6px}
.kicker{font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3);
  font-weight:600;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.kicker::before{content:"";width:16px;height:1px;background:var(--line-2)}
h1.title{font-size:clamp(25px,3.4vw,36px);letter-spacing:-.035em;margin:12px 0 10px;font-weight:600}
.lede{color:var(--ink-2);font-size:15px;max-width:70ch}
.metas{display:flex;gap:8px;flex-wrap:wrap;margin-top:16px}
.metas .pill.v{background:var(--violet-2);color:var(--violet)}
.metas .pill.t{background:var(--teal-2);color:var(--teal)}
.quote{margin-top:20px;padding:18px 20px;border-radius:var(--r);
  background:linear-gradient(115deg,var(--violet-2),transparent 45%,var(--teal-2));
  box-shadow:inset 0 0 0 1px var(--line);font-size:15px;font-weight:500;letter-spacing:-.01em}
.quote small{display:block;margin-top:7px;font-size:12px;color:var(--ink-3);font-weight:400;letter-spacing:0}

/* demo block */
.demo{margin-top:34px}
.demo-head{display:flex;gap:13px;align-items:flex-start;margin-bottom:14px}
.dnum{font-size:11px;font-weight:600;letter-spacing:.05em;color:var(--ink-3);
  background:var(--card-2);padding:5px 8px;border-radius:7px;flex:0 0 auto;margin-top:3px}
.demo-head h2{font-size:18px;letter-spacing:-.02em}
.demo-head p{font-size:13px;color:var(--ink-2);margin-top:4px}
.split{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.pane{background:var(--card);border-radius:var(--r);padding:16px;box-shadow:var(--sh);
  display:flex;flex-direction:column;min-width:0}
.pane.bad{box-shadow:inset 0 0 0 1px var(--red-3),var(--sh)}
.pane.good{box-shadow:inset 0 0 0 1px var(--teal-3),var(--sh)}
.pane-h{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:13px}
.tag{display:inline-flex;align-items:center;gap:5px;font-size:11.5px;line-height:1;padding:5px 9px;border-radius:7px;
  background:var(--card-2);color:var(--ink-2);white-space:nowrap}
.tag.no{background:var(--red-2);color:var(--red)}
.tag.ok{background:var(--teal-2);color:var(--teal)}
.tag.v{background:var(--violet-2);color:var(--violet)}
.tag.w{background:var(--amber-2);color:var(--amber)}
.stage{background:var(--card-2);border-radius:var(--r2);padding:16px;position:relative;
  display:flex;flex-direction:column;justify-content:center;gap:12px;min-height:104px;overflow:hidden}
.stage.tall{min-height:210px}
.stage > .btn,.stage > .seg,.stage > .switch,.stage > a.btn{align-self:flex-start}
.stage > .field{align-self:stretch}
.stage.plain{background:transparent;padding:0}
.note{font-size:12px;color:var(--ink-3);margin-top:12px;line-height:1.6;display:flex;gap:6px;align-items:flex-start}
.note::before{content:"↳";opacity:.7;flex:0 0 auto}
.note b{color:var(--ink-2);font-weight:600}
.count{font-size:11.5px;color:var(--ink-3);background:var(--card-2);padding:4px 9px;border-radius:7px;white-space:nowrap}

/* controls */
.btn{padding:9px 15px;border-radius:10px;font-size:13px;background:var(--card-3);color:var(--ink);
  transition:transform .12s var(--ease),background .18s var(--ease),opacity .18s var(--ease)}
.btn:hover{background:color-mix(in srgb,var(--card-3) 72%,var(--ink) 7%)}
.btn:active{transform:scale(.97)}
.btn.primary{background:var(--teal);color:#fff}
[data-theme="dark"] .btn.primary{color:#06211d}
.btn.danger{background:var(--red-2);color:var(--red)}
.btn.sm{padding:6px 11px;font-size:12px}
.btn.ghost{background:transparent;box-shadow:inset 0 0 0 1px var(--line-2);color:var(--ink-2)}
.row{display:flex;align-items:center;gap:9px;flex-wrap:wrap}
.seg{display:inline-flex;padding:3px;border-radius:10px;background:var(--card-3);gap:2px;flex-wrap:wrap}
.seg button{padding:6px 12px;border-radius:8px;font-size:12.5px;color:var(--ink-2);transition:all .2s var(--ease)}
.seg button[aria-selected="true"]{background:var(--card);color:var(--ink);font-weight:600;box-shadow:0 1px 3px rgba(20,20,18,.12)}
input[type="range"]{-webkit-appearance:none;appearance:none;height:4px;border-radius:99px;
  background:var(--line-2);outline:none;width:100%}
input[type="range"]::-webkit-slider-thumb{-webkit-appearance:none;width:17px;height:17px;border-radius:50%;
  background:var(--card);box-shadow:0 0 0 1.5px var(--teal),0 2px 6px rgba(0,0,0,.2);cursor:pointer}
.switch{display:inline-flex;align-items:center;gap:9px;font-size:13px;color:var(--ink-2);cursor:pointer}
.switch .track{width:40px;height:23px;border-radius:99px;background:var(--card-3);position:relative;
  transition:background .25s var(--ease);flex:0 0 auto}
.switch .knob{position:absolute;top:3px;left:3px;width:17px;height:17px;border-radius:50%;background:var(--card);
  box-shadow:0 1px 3px rgba(0,0,0,.25);transition:transform .3s var(--spring)}
.switch[aria-checked="true"] .track{background:var(--teal)}
.switch[aria-checked="true"] .knob{transform:translateX(17px)}
.field{width:100%;padding:10px 12px;border-radius:11px;border:0;background:var(--card);
  font:inherit;font-size:13.5px;color:var(--ink);outline:none;
  box-shadow:inset 0 0 0 1px var(--line-2);transition:box-shadow .2s var(--ease)}
.field:focus{box-shadow:inset 0 0 0 1.5px var(--teal),0 0 0 4px var(--teal-2)}
.field::placeholder{color:var(--ink-3)}

/* notes list */
.notes{margin-top:44px;padding-top:24px;border-top:1px solid var(--line)}
.notes h2{font-size:16px;margin-bottom:14px}
.nlist{display:grid;gap:9px;font-size:13.5px;color:var(--ink-2)}
.nlist li{list-style:none;display:grid;grid-template-columns:15px 1fr;gap:8px;line-height:1.7}
.nlist li::before{content:"·";color:var(--ink-3);font-weight:700}
.nlist b{color:var(--ink);font-weight:600}
ul.nlist{margin:0;padding:0}

/* foot nav */
.pager{display:flex;gap:12px;margin-top:34px;flex-wrap:wrap}
.pager a{flex:1;min-width:200px;text-decoration:none;background:var(--card);border-radius:var(--r2);
  padding:14px 16px;box-shadow:var(--sh);transition:transform .2s var(--ease),box-shadow .2s var(--ease)}
.pager a:hover{transform:translateY(-2px);box-shadow:var(--sh2)}
.pager .k{font-size:11px;color:var(--ink-3);letter-spacing:.05em}
.pager .t{font-size:13.5px;font-weight:600;margin-top:3px;color:var(--ink)}
.pager a.next{text-align:right}
footer.foot{margin-top:40px;padding-top:18px;border-top:1px solid var(--line);
  font-size:12px;color:var(--ink-3);line-height:1.8}

/* toast */
.toast{position:fixed;left:50%;bottom:24px;transform:translate(-50%,14px);z-index:200;
  padding:10px 17px;border-radius:11px;background:var(--ink);color:var(--bg);font-size:13px;
  box-shadow:var(--sh2);opacity:0;pointer-events:none;
  transition:opacity .25s var(--ease),transform .3s var(--ease);display:flex;align-items:center;gap:8px;max-width:88vw}
.toast.show{opacity:1;transform:translate(-50%,0)}

@media (max-width:880px){
  .split{grid-template-columns:1fr}
  .tb-title{display:none}
}
@media (max-width:520px){
  .wrap{padding:0 16px}
  main{padding:24px 0 56px}
  .stage{padding:13px}
  .pane{padding:13px}
}
"""

SHELL = """<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>{title} · 对比演示</title>
<style>
{css}
{extra_css}
</style>
</head>
<body>
<header class="topbar">
  <div class="wrap">
    <a class="back" href="index.html">
      <svg width="13" height="13" viewBox="0 0 16 16" fill="none"><path d="M10 3 5 8l5 5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
      全部视频
    </a>
    <div class="tb-title">{no} · <b>{short}</b></div>
    <div class="tb-right">
      <span class="pill">{dur}</span>
      <a class="pill" href="https://www.bilibili.com/video/{bvid}" target="_blank" rel="noopener" style="text-decoration:none">原视频 ↗</a>
      <button class="iconbtn" id="themeBtn" aria-label="切换深浅色">
        <svg id="iconMoon" width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
        <svg id="iconSun" style="display:none" width="15" height="15" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.5 1.5M17.5 17.5 19 19M19 5l-1.5 1.5M6.5 17.5 5 19" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
      </button>
    </div>
  </div>
</header>

<main class="wrap">
  <section class="hero">
    <div class="kicker">{kicker}</div>
    <h1 class="title">{title}</h1>
    <p class="lede">{lede}</p>
    <div class="metas">
      <span class="pill v">{tag1}</span>
      <span class="pill t">{tag2}</span>
      <span class="pill">{date}</span>
    </div>
    <div class="quote">{quote}</div>
  </section>

{demos}

  <section class="notes">
    <h2>这期视频的要点</h2>
    <ul class="nlist">{notes}</ul>
  </section>

  <nav class="pager">{pager}</nav>

  <footer class="foot">
    <b>关于本页</b>：对比演示是按视频公开的要点做的交互还原，用于投屏讲解；组件形态与视频中演示的一致，但画面不是视频原片截图。<br>
    <b>技术</b>：单文件 HTML，零外部依赖，可离线打开；所有页面统一套用同一段 CSS Reset。
  </footer>
</main>

<div class="toast" id="toast">
  <svg width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="m3 8.5 3.5 3.5L13 4.5" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>
  <span id="toastText"></span>
</div>

<script>
(function(){{
  var root=document.documentElement, btn=document.getElementById('themeBtn');
  var moon=document.getElementById('iconMoon'), sun=document.getElementById('iconSun');
  btn.addEventListener('click',function(){{
    var dark=root.dataset.theme==='dark';
    root.dataset.theme=dark?'light':'dark';
    moon.style.display=dark?'':'none'; sun.style.display=dark?'none':'';
  }});
  var t=document.getElementById('toast'), tx=document.getElementById('toastText'), tm;
  window.toast=function(msg){{
    tx.textContent=msg; t.classList.add('show');
    clearTimeout(tm); tm=setTimeout(function(){{t.classList.remove('show');}},2400);
  }};
}})();
</script>
<script>
{js}
</script>
</body>
</html>
"""


def render(page):
    notes = "".join("<li><div>%s</div></li>" % n for n in page["notes"])
    return SHELL.format(
        title=page["title"],
        short=page["short"],
        no=page["no"],
        dur=page["dur"],
        bvid=page["bvid"],
        kicker=page["kicker"],
        lede=page["lede"],
        tag1=page["tag1"],
        tag2=page["tag2"],
        date=page["date"],
        quote=page["quote"],
        demos=page["demos"],
        notes=notes,
        pager=page["pager"],
        css=SHARED_CSS,
        extra_css=page.get("extra_css", ""),
        js=page.get("js", ""),
    )
