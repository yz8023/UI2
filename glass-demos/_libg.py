# -*- coding: utf-8 -*-
"""liquid-glass-studio 演示页外壳（复用 motion-demos 的样式与提示词面板）"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'motion-demos'))
from _libm import SHARED_CSS, MOTION_CSS, prompt_panel  # noqa

GLASS_CSS = """
.pair{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.cell{background:var(--card);border-radius:var(--r2);padding:10px;box-shadow:var(--sh);min-width:0}
.cell-h{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:8px;font-size:11.5px;color:var(--ink-3)}
.cell-h b{color:var(--ink);font-size:12px;font-weight:600}
.gcanvas{position:relative;border-radius:11px;overflow:hidden;background:#0a0c14;box-shadow:inset 0 0 0 1px var(--line)}
.gcanvas canvas{display:block;width:100%;height:320px;touch-action:none;cursor:crosshair}
.gcanvas.short canvas{height:210px}
.gcanvas.tall canvas{height:420px}
.ctl{margin-top:14px;background:var(--card);border-radius:var(--r2);padding:14px 16px;box-shadow:var(--sh)}
.ctl-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:13px 20px}
.sl{display:grid;gap:5px}
.sl .lab{display:flex;align-items:baseline;justify-content:space-between;font-size:12px;color:var(--ink-2)}
.sl .lab b{font-family:ui-monospace,Menlo,monospace;font-size:11.5px;color:var(--ink);font-weight:600}
.sl input[type="range"]{width:100%}
.togrow{display:flex;gap:14px;flex-wrap:wrap;align-items:center;margin-top:12px}
@media (max-width:760px){
  .pair{grid-template-columns:1fr}
  .gcanvas canvas{height:260px}
  .ctl-grid{grid-template-columns:1fr 1fr}
}
@media (max-width:460px){.ctl-grid{grid-template-columns:1fr}}
.gcanvas.nowebgl::after{content:"此浏览器不支持 WebGL2";position:absolute;inset:0;display:grid;place-items:center;
  font-size:12.5px;color:#fff;background:rgba(0,0,0,.6)}
"""

SHELL = """<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>{title} · 液态玻璃演示</title>
<style>
{css}
{motion_css}
{glass_css}
{extra_css}
</style>
</head>
<body>
<header class="topbar">
  <div class="wrap">
    <a class="back" href="index.html">
      <svg width="13" height="13" viewBox="0 0 16 16" fill="none"><path d="M10 3 5 8l5 5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
      全部演示
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
    <div class="kicker">liquid-glass-studio · {no} · {layer}</div>
    <h1 class="title">{title}</h1>
    <p class="lede">{lede}</p>
    <div class="quote">{quote}<small>{quote_from}</small></div>
    <div class="casebar">
      <span>参考项目</span>
      <a href="https://github.com/iyinchao/liquid-glass-studio" target="_blank" rel="noopener">iyinchao/liquid-glass-studio</a>
      <a href="{case_url}" target="_blank" rel="noopener">{path}</a>
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
    <b>关于本页</b>：这是按 liquid-glass-studio 实际使用的着色器结构与默认参数做的复现（WebGL2 · 4 pass：背景 → 纵向模糊 → 横向模糊 → 主合成），代码为重新实现；原项目的参数范围与默认值取自其 <code>src/Controls.tsx</code>，判据取自其 <code>openspec/specs</code>。<br>
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
  var base = document.getElementById('promptBase').textContent;
  var out  = document.getElementById('promptOut');
  var boxes= document.querySelectorAll('.req input');
  var custom=document.getElementById('promptCustom');
  function build(){{
    var lines=[base.trim()], picked=[];
    boxes.forEach(function(b){{ if(b.checked) picked.push('- '+b.dataset.req); }});
    if(picked.length) lines.push('\\n【变更要求】\\n'+picked.join('\\n'));
    if(custom.value.trim()) lines.push('\\n【自定义要求】\\n'+custom.value.trim());
    out.textContent=lines.join('\\n');
  }}
  boxes.forEach(function(b){{ b.addEventListener('change',build); }});
  custom.addEventListener('input',build);
  build();
  document.getElementById('copyPrompt').addEventListener('click',function(){{
    var text=out.textContent, b2=this;
    function done(){{ b2.classList.add('done'); var o=b2.textContent; b2.textContent='已复制 ✓';
      setTimeout(function(){{ b2.classList.remove('done'); b2.textContent=o; }},1800); }}
    function fb(){{
      var ta=document.createElement('textarea'); ta.value=text; ta.style.position='fixed'; ta.style.opacity='0';
      document.body.appendChild(ta); ta.select();
      try{{ document.execCommand('copy'); done(); }}catch(e){{ toast('请手动选择文本复制'); }}
      document.body.removeChild(ta);
    }}
    if(window.AndroidBridge&&window.AndroidBridge.copy){{ try{{ window.AndroidBridge.copy(text); done(); return; }}catch(e){{}} }}
    if(navigator.clipboard&&navigator.clipboard.writeText){{ navigator.clipboard.writeText(text).then(done).catch(fb); }}
    else {{ fb(); }}
  }});
}})();
</script>
<script>
{glass_js}
</script>
<script>
{js}
</script>
</body>
</html>
"""


def render(p, reqs, glass_js):
    def li(items):
        return "".join("<li><div>%s</div></li>" % x for x in items)
    return SHELL.format(
        title=p["title"], short=p["short"], no=p["no"], layer=p["layer"],
        case_url=p["case_url"], path=p["path"], ref=p["ref"],
        lede=p["lede"], quote=p["quote"], quote_from=p["quote_from"],
        stage=p["stage"], prompt_html=prompt_panel(p, reqs),
        copyable=li(p["copyable"]), uncopyable=li(p["uncopyable"]),
        pager=p["pager"],
        css=SHARED_CSS, motion_css=MOTION_CSS, glass_css=GLASS_CSS,
        extra_css=p.get("extra_css", ""),
        glass_js=glass_js, js=p.get("js", ""),
    )


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
          <div><span class="k">项目</span><span class="v">iyinchao/liquid-glass-studio（MIT）</span></div>
          <div><span class="k">案例</span><span class="v">%s · %s</span></div>
          <div><span class="k">机制</span><span class="v">%s</span></div>
          <div><span class="k">关键参数</span><span class="v">%s</span></div>
          <div><span class="k">判据</span><span class="v">%s</span></div>
        </div>
      </div>
      <div class="pcol">
        <h3>02 · 变更要求（可勾选 / 可自写）</h3>
        <div class="reqs">%s</div>
        <div style="margin-top:12px">
          <textarea class="custom" id="promptCustom" placeholder="再补一句你的要求，例如：做成 iOS 深色导航栏、玻璃上放 3 个图标按钮……"></textarea>
        </div>
      </div>
    </div>
    <div class="prompt-foot">
      <div class="prompt-out">
        <pre class="pcode" id="promptBase">%s</pre>
        <pre class="pcode" id="promptOut" style="display:none"></pre>
      </div>
      <div class="copybar">
        <button class="copy-main" id="copyPrompt">一键复制提示词</button>
        <span class="copy-tip">复制后直接贴给 AI 编码工具即可生成同款页面</span>
      </div>
    </div>
  </section>
""" % (p["path"].split("/")[-1], p["short"], p["mech"], p["params"], p["verify"], req_html, p["prompt"].strip())


INDEX_HEAD = """<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>liquid-glass-studio · 6 个液态玻璃演示</title>
<style>
{css}
{extra}
</style>
</head>
<body>
<header class="topbar">
  <div class="wrap">
    <div class="brand"><i>玻</i>liquid-glass · 玻璃演示</div>
    <div class="spacer"></div>
    <a class="pill" href="https://github.com/iyinchao/liquid-glass-studio" target="_blank" rel="noopener">原项目 ↗</a>
    <button class="iconbtn" id="themeBtn" aria-label="切换深浅色">
      <svg id="iconMoon" width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
      <svg id="iconSun" style="display:none" width="15" height="15" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.5 1.5M17.5 17.5 19 19M19 5l-1.5 1.5M6.5 17.5 5 19" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    </button>
  </div>
</header>
<main class="wrap">
  <div class="kicker">iyinchao/liquid-glass-studio · MIT · 6 个案例 · 全部可交互</div>
  <h1>玻璃不是一个滤镜，是一串 pass。</h1>
  <p class="lede">原项目用 4 个 WebGL2 pass 把一块玻璃拆成：背景 → 纵向模糊 → 横向模糊 → 主合成（SDF / 折射 / 色散 / 菲涅尔 / 眩光）。这里把它拆成 6 个可单独调节的演示页：每页左边是机制，右边是成品，下方滑杆直接改真实 uniform；页内附<b>参考项目 + 变更要求 + 一键复制提示词</b>。</p>
  <div class="stats">
    <span class="pill v">6 个单文件 HTML</span>
    <span class="pill t">WebGL2 · 真实 4-pass</span>
    <span class="pill">参数取自 src/Controls.tsx</span>
    <span class="pill">无 CDN / 无外部图片</span>
  </div>
  <div class="grid">{cards}</div>

  <div class="crosslink">
    <a href="../index.html"><b>工作区总入口：两套形态对照表</b>点击进入 · 22 个素材 × App / HTML 两种打开方式</a>
    <a href="../app/index.html"><b>应用形态：22 个素材的「素材库」App</b>点击进入 · 搜索 / 筛选 / 并排对比 / 复制提示词</a>
    <a href="../motion-demos/index.html"><b>另一套：motion-web 的 7 个动效案例</b>点击进入 · 绳幕 / 乌鸦 / 绳钟 / 叠压 / 滚轮 / 翻页 / 手绘</a>
    <a href="../video-demos/index.html"><b>再一套：9 个 UI 设计视频的对比演示</b>点击进入 · 组件选型 / 浮层 / 热区 / 国际化</a>
    <a href="https://github.com/iyinchao/liquid-glass-studio" target="_blank" rel="noopener"><b>原始仓库（MIT）</b>shader 数学、参数范围与 openspec 判据都在里面</a>
  </div>

  <div class="foot">
    <b>说明</b>：本套演示按 liquid-glass-studio 的着色器结构与 <code>src/Controls.tsx</code> 的默认参数重新实现（代码全部重写，未拷贝其资产）；背景是程序化生成的，因为原项目的图片/视频素材不随演示分发。<br>
    <b>提示词用法</b>：进入任意案例页 → 勾选变更要求或补一句自定义要求 → 「一键复制提示词」→ 贴给 AI 编码工具。
  </div>
</main>
<script>
(function(){
  var root=document.documentElement, btn=document.getElementById('themeBtn');
  var moon=document.getElementById('iconMoon'), sun=document.getElementById('iconSun');
  btn.addEventListener('click',function(){
    var dark=root.dataset.theme==='dark';
    root.dataset.theme=dark?'light':'dark';
    moon.style.display=dark?'':'none'; sun.style.display=dark?'none':'';
  });
})();
</script>
</body>
</html>
"""

INDEX_EXTRA = """
.brand{display:flex;align-items:center;gap:9px;font-size:13.5px;font-weight:600;color:var(--ink)}
.brand i{width:22px;height:22px;border-radius:7px;background:var(--ink);color:var(--bg);display:grid;place-items:center;
  font-style:normal;font-size:11.5px}
[data-theme="dark"] .brand i{background:var(--card-3);color:var(--ink)}
.spacer{flex:1}
.stats{display:flex;gap:8px;flex-wrap:wrap;margin-top:16px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:26px}
.vcard{background:var(--card);border-radius:18px;padding:18px;box-shadow:var(--sh);display:flex;flex-direction:column;gap:9px;
  transition:transform .22s var(--ease),box-shadow .22s var(--ease);text-decoration:none}
.vcard:hover{transform:translateY(-3px);box-shadow:var(--sh2)}
.vtop{display:flex;align-items:center;gap:9px;flex-wrap:wrap}
.vno{font-size:11.5px;font-weight:600;padding:4px 8px;border-radius:6px;background:var(--ink);color:var(--bg)}
[data-theme="dark"] .vno{background:var(--card-3);color:var(--ink)}
.vtags{font-size:11.5px;color:var(--ink-3)}
.vdur{margin-left:auto;font-size:11.5px;color:var(--ink-3);background:var(--card-2);padding:3px 8px;border-radius:6px}
.vcard h3{font-size:15px;margin-top:2px}
.vwhat{font-size:13px;color:var(--ink-2);line-height:1.7}
.vhow{font-size:12px;color:var(--ink-3);line-height:1.7}
.vgo{margin-top:auto;font-size:12.5px;color:var(--teal);font-weight:600;padding-top:6px}
.crosslink{display:flex;gap:12px;flex-wrap:wrap;margin-top:26px}
.crosslink a{background:var(--card);border-radius:12px;padding:12px 16px;box-shadow:var(--sh);
  font-size:12.8px;color:var(--ink-2);transition:transform .2s var(--ease);text-decoration:none}
.crosslink a:hover{transform:translateY(-2px)}
.crosslink b{color:var(--ink);display:block;font-size:13.5px;margin-bottom:2px}
.foot{margin-top:36px;padding-top:20px;border-top:1px solid var(--line);font-size:12px;color:var(--ink-3);line-height:1.85}
.foot b{color:var(--ink-2)}
@media (max-width:820px){.grid{grid-template-columns:1fr}}
@media (max-width:520px){.wrap{padding:0 16px}main{padding:24px 0 56px}}
"""
