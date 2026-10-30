# -*- coding: utf-8 -*-
"""motion-web 案例演示：共用外壳 + 提示词面板（内置同一段 CSS Reset）"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "video-demos"))
from _lib import SHARED_CSS, RESET   # noqa

MOTION_CSS = """
/* ============ motion 专用 ============ */
.casebar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-top:16px;font-size:12px;color:var(--ink-3)}
.casebar a{text-decoration:none;color:var(--ink-2);background:var(--card-2);padding:5px 10px;border-radius:7px}
.casebar a:hover{color:var(--ink);background:var(--card-3)}
.stagewrap{background:var(--card);border-radius:var(--r);box-shadow:var(--sh);padding:14px;margin-top:16px}
.stagebar{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:10px;flex-wrap:wrap}
.stagebar .lbl{font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-3);font-weight:600}
.readout{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:11px;letter-spacing:.06em;
  color:var(--ink-3);display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.readout b{color:var(--ink);font-weight:600}
.readout .sep{opacity:.45}
.canvasbox{position:relative;border-radius:14px;overflow:hidden;background:var(--paper,#fff);
  box-shadow:inset 0 0 0 1px var(--line);touch-action:none;cursor:crosshair}
.canvasbox canvas{display:block;width:100%;height:auto}
.hint{font-size:12px;color:var(--ink-3);margin-top:10px;display:flex;gap:6px;align-items:flex-start}
.hint::before{content:"↳";opacity:.7}
.ctrls{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px;align-items:center}

/* 提示词面板 */
.prompt{margin-top:34px;border-radius:var(--r);background:var(--card);box-shadow:var(--sh);overflow:hidden}
.prompt-h{display:flex;align-items:center;gap:10px;padding:15px 18px;border-bottom:1px solid var(--line);flex-wrap:wrap}
.prompt-h h2{font-size:15.5px}
.prompt-h .pill{font-size:11px;padding:4px 9px;border-radius:6px;background:var(--card-2);color:var(--ink-3)}
.prompt-body{display:grid;grid-template-columns:1fr 1fr;gap:0}
.pcol{padding:17px 18px;min-width:0}
.pcol + .pcol{border-left:1px solid var(--line)}
.pcol h3{font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-3);margin-bottom:11px;font-weight:600}
.kv{display:grid;gap:7px;font-size:12.5px;color:var(--ink-2);line-height:1.65}
.kv div{display:grid;grid-template-columns:64px 1fr;gap:9px}
.kv .k{color:var(--ink-3)}
.kv .v{color:var(--ink)}
.reqs{display:grid;gap:8px}
.req{display:flex;gap:9px;align-items:flex-start;font-size:12.5px;color:var(--ink-2);cursor:pointer;line-height:1.55}
.req input{appearance:none;-webkit-appearance:none;width:15px;height:15px;border-radius:4px;margin-top:2px;flex:0 0 auto;
  box-shadow:inset 0 0 0 1.5px var(--line-2);background:var(--card);cursor:pointer;position:relative}
.req input:checked{background:var(--teal);box-shadow:inset 0 0 0 1.5px var(--teal)}
.req input:checked::after{content:"";position:absolute;left:4px;top:1px;width:4px;height:8px;
  border:2px solid #fff;border-top:0;border-left:0;transform:rotate(42deg)}
.req b{color:var(--ink);font-weight:600}
.prompt-foot{padding:0 18px 17px}
textarea.custom{width:100%;min-height:56px;resize:vertical;padding:10px 12px;border-radius:10px;border:0;
  background:var(--card-2);font:inherit;font-size:12.5px;color:var(--ink);outline:none;line-height:1.6;
  box-shadow:inset 0 0 0 1px transparent}
textarea.custom:focus{background:var(--card);box-shadow:inset 0 0 0 1.5px var(--teal),0 0 0 4px var(--teal-2)}
textarea.custom::placeholder{color:var(--ink-3)}
.prompt-out{margin-top:14px;position:relative}
pre.pcode{margin:0;padding:15px 16px;border-radius:12px;background:var(--card-2);color:var(--ink-2);
  font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:11.8px;line-height:1.8;
  white-space:pre-wrap;word-break:break-word;max-height:300px;overflow:auto}
.copybar{display:flex;align-items:center;gap:10px;margin-top:11px;flex-wrap:wrap}
.copy-main{padding:9px 16px;border-radius:10px;background:var(--teal);color:#fff;font-size:13px;font-weight:600}
[data-theme="dark"] .copy-main{color:#06211d}
.copy-main:hover{background:color-mix(in srgb,var(--teal) 86%, #000)}
.copy-main.done{background:var(--ok,#2c7a5b)}
.copy-tip{font-size:11.5px;color:var(--ink-3)}
.notes2{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:34px}
.notes2 .card2{background:var(--card);border-radius:var(--r2);padding:16px 18px;box-shadow:var(--sh)}
.notes2 h3{font-size:13.5px;margin-bottom:10px;display:flex;align-items:center;gap:7px}
.notes2 h3 .dotm{width:7px;height:7px;border-radius:50%;display:block}
.notes2 ul{margin:0;padding:0;display:grid;gap:8px;font-size:12.8px;color:var(--ink-2);line-height:1.7}
.notes2 li{list-style:none;display:grid;grid-template-columns:13px 1fr;gap:7px}
.notes2 li::before{content:"·";color:var(--ink-3);font-weight:700}
.notes2 b{color:var(--ink);font-weight:600}
@media (max-width:900px){
  .prompt-body{grid-template-columns:1fr}
  .pcol + .pcol{border-left:0;border-top:1px solid var(--line)}
  .notes2{grid-template-columns:1fr}
}
"""

SHELL = """<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>{title} · 动效演示</title>
<style>
{css}
{motion_css}
{extra_css}
</style>
</head>
<body>
<header class="topbar">
  <div class="wrap">
    <a class="back" href="index.html">
      <svg width="13" height="13" viewBox="0 0 16 16" fill="none"><path d="M10 3 5 8l5 5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
      全部动效
    </a>
    <div class="tb-title">{no} · <b>{short}</b></div>
    <div class="tb-right">
      <span class="pill">{layer}</span>
      <a class="pill" href="{case_url}" target="_blank" rel="noopener" style="text-decoration:none">源码 ↗</a>
      <button class="iconbtn" id="themeBtn" aria-label="切换深浅色">
        <svg id="iconMoon" width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
        <svg id="iconSun" style="display:none" width="15" height="15" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.5 1.5M17.5 17.5 19 19M19 5l-1.5 1.5M6.5 17.5 5 19" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
      </button>
    </div>
  </div>
</header>

<main class="wrap">
  <section class="hero">
    <div class="kicker">motion-web · case {no} · {layer}</div>
    <h1 class="title">{title}</h1>
    <p class="lede">{lede}</p>
    <div class="quote">{quote}<small>{quote_from}</small></div>
    <div class="casebar">
      <span>参考项目</span>
      <a href="https://github.com/feitangyuan/motion-web" target="_blank" rel="noopener">feitangyuan/motion-web</a>
      <a href="{case_url}" target="_blank" rel="noopener">cases/{slug}</a>
      <span style="color:var(--ink-3)">{ref}</span>
    </div>
  </section>

{stage}

{prompt_html}

  <section class="notes2">
    <div class="card2">
      <h3><span class="dotm" style="background:var(--teal)"></span>可以照搬（机制层）</h3>
      <ul>{copyable}</ul>
    </div>
    <div class="card2">
      <h3><span class="dotm" style="background:var(--red)"></span>不许照搬（皮层）</h3>
      <ul>{uncopyable}</ul>
    </div>
  </section>

  <nav class="pager">{pager}</nav>

  <footer class="foot">
    <b>关于本页</b>：演示是按 motion-web 案例公开的机制与实测参数做的原生复现（Canvas 2D / CSS / DOM，无框架无 CDN），用于投屏讲解；视觉细节经简化，不是原案例代码。<br>
    <b>提示词</b>：勾选「变更要求」会自动拼进下方 prompt，可直接复制给任意 AI 编码工具。
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
    clearTimeout(tm); tm=setTimeout(function(){{t.classList.remove('show');}},2200);
  }};

  /* 提示词面板：勾选/输入 → 实时重写 prompt → 一键复制 */
  var base = document.getElementById('promptBase').textContent;
  var out  = document.getElementById('promptOut');
  var boxes= document.querySelectorAll('.req input');
  var custom=document.getElementById('promptCustom');
  function build(){{
    var lines=[base.trim()];
    var picked=[];
    boxes.forEach(function(b){{ if(b.checked) picked.push('- '+b.dataset.req); }});
    if(picked.length) lines.push('\\n【变更要求】\\n'+picked.join('\\n'));
    if(custom.value.trim()) lines.push('\\n【自定义要求】\\n'+custom.value.trim());
    out.textContent=lines.join('\\n');
  }}
  boxes.forEach(function(b){{ b.addEventListener('change',build); }});
  custom.addEventListener('input',build);
  build();
  document.getElementById('copyPrompt').addEventListener('click',function(){{
    var text=out.textContent, btn2=this;
    function done(){{ btn2.classList.add('done'); var o=btn2.textContent; btn2.textContent='已复制 ✓';
      setTimeout(function(){{ btn2.classList.remove('done'); btn2.textContent=o; }},1800); }}
    function fallback(){{
      var ta=document.createElement('textarea'); ta.value=text; ta.style.position='fixed'; ta.style.opacity='0';
      document.body.appendChild(ta); ta.select();
      try{{ document.execCommand('copy'); done(); }}catch(e){{ toast('请手动选择文本复制'); }}
      document.body.removeChild(ta);
    }}
    if(window.AndroidBridge&&window.AndroidBridge.copy){{ try{{ window.AndroidBridge.copy(text); done(); return; }}catch(e){{}} }}
    if(navigator.clipboard&&navigator.clipboard.writeText){{ navigator.clipboard.writeText(text).then(done).catch(fallback); }}
    else {{ fallback(); }}
  }});
}})();
</script>
<script>
{js}
</script>
</body>
</html>
"""


def prompt_panel(p, reqs):
    req_html = "".join(
        '<label class="req"><input type="checkbox" data-req="%s"><span>%s</span></label>' % (r, r)
        for r in reqs)
    return """
  <section class="prompt">
    <div class="prompt-h">
      <h2>生成提示词</h2>
      <span class="pill">参考项目 + 变更要求 → 一键复制</span>
    </div>
    <div class="prompt-body">
      <div class="pcol">
        <h3>01 · 参考项目</h3>
        <div class="kv">
          <div><span class="k">项目</span><span class="v">feitangyuan/motion-web（CC BY-NC 4.0）</span></div>
          <div><span class="k">案例</span><span class="v">cases/%s · %s</span></div>
          <div><span class="k">机制</span><span class="v">%s</span></div>
          <div><span class="k">关键参数</span><span class="v">%s</span></div>
          <div><span class="k">判据</span><span class="v">%s</span></div>
        </div>
      </div>
      <div class="pcol">
        <h3>02 · 变更要求（可勾选 / 可自写）</h3>
        <div class="reqs">%s</div>
        <div style="margin-top:12px">
          <textarea class="custom" id="promptCustom" placeholder="再补一句你的要求，例如：换成中秋主题、卡片文案改成订单数据……"></textarea>
        </div>
      </div>
    </div>
    <div class="prompt-foot">
      <div class="prompt-out">
        <pre class="pcode" id="promptBase">%s</pre>
        <pre class="pcode" id="promptOut" style="display:none"></pre>
        <div style="display:none" id="promptDummy"></div>
      </div>
      <div class="copybar">
        <button class="copy-main" id="copyPrompt">一键复制提示词</button>
        <span class="copy-tip">复制后直接贴给 AI 编码工具即可生成同款项目</span>
      </div>
    </div>
  </section>
""" % (p["slug"], p["layer_cn"], p["mech"], p["params"], p["verify"], req_html, p["prompt"].strip())


def render(p, reqs):
    def li(items):
        return "".join("<li><div>%s</div></li>" % x for x in items)
    return SHELL.format(
        title=p["title"], short=p["short"], no=p["no"], layer=p["layer"],
        case_url=p["case_url"], slug=p["slug"], ref=p["ref"],
        kicker=p["kicker"], lede=p["lede"], quote=p["quote"], quote_from=p["quote_from"],
        stage=p["stage"], prompt_html=prompt_panel(p, reqs),
        copyable=li(p["copyable"]), uncopyable=li(p["uncopyable"]),
        pager=p["pager"], css=SHARED_CSS, motion_css=MOTION_CSS,
        extra_css=p.get("extra_css", ""), js=p.get("js", ""),
    )
