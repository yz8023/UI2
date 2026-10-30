# -*- coding: utf-8 -*-
"""生成全部对比演示页 + 索引页。用法：python3 _make_pages.py"""
import os, sys, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import _lib, _pages_a, _pages_c, _pages_d, _pages_e
importlib.reload(_lib)

PAGES = [_pages_a.P01, _pages_a.P02, _pages_c.P03, _pages_c.P04,
         _pages_d.P05, _pages_d.P06, _pages_e.P07, _pages_e.P08, _pages_e.P09]

def slug(p):
    return "%s-%s.html" % (p["no"], p["short"].replace(" ", "-").replace("/", "-"))

for i, p in enumerate(PAGES):
    p["title_full"] = p["title"]
    prev = PAGES[i - 1] if i > 0 else None
    nxt = PAGES[i + 1] if i < len(PAGES) - 1 else None
    pager = ""
    if prev:
        pager += '<a href="%s"><div class="k">← 上一个</div><div class="t">%s %s</div></a>' % (slug(prev), prev["no"], prev["short"])
    else:
        pager += '<a href="index.html"><div class="k">← 返回</div><div class="t">全部视频目录</div></a>'
    if nxt:
        pager += '<a class="next" href="%s"><div class="k">下一个 →</div><div class="t">%s %s</div></a>' % (slug(nxt), nxt["no"], nxt["short"])
    else:
        pager += '<a class="next" href="index.html"><div class="k">回到目录 →</div><div class="t">全部视频</div></a>'
    p["pager"] = pager
    out = _lib.render(p)
    with open(slug(p), "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote", slug(p), len(out))

# ---------------- index ----------------
cards = []
meta = {
    "01": ("浮层 / 弹窗", "弹窗 vs 抽屉 vs 页面，同一件事的三种承载", "点开四种反馈、看什么必须关不掉"),
    "02": ("浮层 / 反馈", "Bottom Sheet 三档屏高 + 撤销替代确认", "拖手柄、删条目、按 Esc 试给你看"),
    "03": ("视觉质感", "微对比分层 / 墨晕打字 / 等宽数字 / 弹簧", "四组真实可跑的动效对比"),
    "04": ("AI 界面", "输入法 Enter、滚动跟随、同心圆角、截断、分屏", "五个细节全部可交互复现"),
    "05": ("组件辨析", "Dropdown 与 Select 到底差在哪", "并排实点 + 三条选型铁律"),
    "06": ("触控体验", "热区、误触、滑动偷点击", "亲手体验一次「点不中」"),
    "07": ("国际化", "长文案溢出、变音符裁切、RTL 镜像", "切五种语言看按钮怎么炸"),
    "08": ("游戏实录", "虎先锋无伤：纯棍式 + 禁法术", "1060 上 40 帧的观感示意"),
    "09": ("游戏实录", "寅虎无伤：禁字法术流", "拖时间轴，试一次完美闪避"),
}
for p in PAGES:
    s = slug(p)
    tag, what, how = meta[p["no"]]
    cards.append("""
    <a class="vcard" href="%s">
      <div class="vtop"><span class="vno">%s</span><span class="vtags">%s</span><span class="vdur">%s</span></div>
      <h3>%s</h3>
      <p class="vwhat">%s</p>
      <p class="vhow">%s</p>
      <span class="vgo">进入演示 →</span>
    </a>""" % (s, p["no"], tag, p["dur"], p["title"], what, how))

INDEX = """<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>KD一对A · 9 个视频的对比演示</title>
<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Segoe UI', sans-serif;
    -webkit-tap-highlight-color: transparent;
}
:root{
  --bg:#f4f3ef; --card:#fcfcfa; --card-2:#f0efea; --card-3:#e8e7e1;
  --ink:#1a1a18; --ink-2:#58574f; --ink-3:#8b8a82;
  --line:rgba(26,26,24,.08); --line-2:rgba(26,26,24,.15);
  --violet:#5b4ed6; --violet-2:rgba(91,78,214,.10);
  --teal:#0e8f80; --teal-2:rgba(14,143,128,.10);
  --sh:0 1px 2px rgba(20,20,18,.04),0 8px 24px rgba(20,20,18,.055);
  --sh2:0 18px 50px rgba(20,20,18,.16);
  --ease:cubic-bezier(.215,.61,.355,1);
}
[data-theme="dark"]{
  --bg:#0d0d0c; --card:#151515; --card-2:#1a1a19; --card-3:#22221f;
  --ink:#ececea; --ink-2:#a8a7a2; --ink-3:#7c7b73;
  --line:rgba(255,255,255,.075); --line-2:rgba(255,255,255,.14);
  --violet:#9d90ff; --violet-2:rgba(157,144,255,.14);
  --teal:#41cbb6; --teal-2:rgba(65,203,182,.13);
  --sh:0 1px 2px rgba(0,0,0,.3),0 10px 28px rgba(0,0,0,.3);
  --sh2:0 20px 56px rgba(0,0,0,.6);
}
body{background:var(--bg);color:var(--ink);
  font-family:'Segoe UI','PingFang SC','Hiragino Sans GB','Noto Sans SC','Microsoft YaHei',system-ui,sans-serif;
  font-size:15px;line-height:1.65;-webkit-font-smoothing:antialiased;font-variant-numeric:tabular-nums;
  transition:background .35s var(--ease),color .35s var(--ease);text-wrap:pretty}
::selection{background:var(--violet-2)}
a{color:inherit;text-decoration:none}
button{font:inherit;color:inherit;border:0;background:none;cursor:pointer}
h1,h2,h3{line-height:1.35;letter-spacing:-.02em;font-weight:600}
svg{display:block}
.wrap{max-width:1080px;margin:0 auto;padding:0 24px}
.topbar{position:sticky;top:0;z-index:50;border-bottom:1px solid var(--line);
  background:color-mix(in srgb,var(--bg) 84%,transparent);backdrop-filter:saturate(180%) blur(18px)}
.topbar .wrap{display:flex;align-items:center;gap:12px;height:60px}
.brand{display:flex;align-items:center;gap:9px;font-size:13.5px;font-weight:600;letter-spacing:-.02em}
.brand i{width:26px;height:26px;border-radius:8px;background:linear-gradient(140deg,var(--violet),var(--teal));display:grid;place-items:center;color:#fff;font-style:normal;font-size:12px}
.spacer{flex:1}
.iconbtn{width:34px;height:34px;border-radius:10px;display:grid;place-items:center;background:var(--card-2);color:var(--ink-2)}
.iconbtn:hover{background:var(--card-3);color:var(--ink)}
main{padding:38px 0 80px}
.kicker{font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3);font-weight:600;display:flex;align-items:center;gap:8px}
.kicker::before{content:"";width:16px;height:1px;background:var(--line-2)}
h1{font-size:clamp(26px,3.6vw,38px);letter-spacing:-.035em;margin:12px 0 10px}
.lede{color:var(--ink-2);font-size:15px;max-width:72ch}
.stats{display:flex;gap:10px;flex-wrap:wrap;margin-top:18px}
.pill{font-size:11.5px;padding:5px 10px;border-radius:7px;background:var(--card-2);color:var(--ink-2)}
.pill.v{background:var(--violet-2);color:var(--violet)}
.pill.t{background:var(--teal-2);color:var(--teal)}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:26px}
.vcard{background:var(--card);border-radius:18px;padding:18px;box-shadow:var(--sh);display:flex;flex-direction:column;gap:9px;
  transition:transform .22s var(--ease),box-shadow .22s var(--ease)}
.vcard:hover{transform:translateY(-3px);box-shadow:var(--sh2)}
.vtop{display:flex;align-items:center;gap:9px;flex-wrap:wrap}
.vno{font-size:11.5px;font-weight:600;padding:4px 8px;border-radius:6px;background:var(--ink);color:var(--bg)}
[data-theme="dark"] .vno{background:var(--card-3);color:var(--ink)}
.vtags{font-size:11.5px;color:var(--ink-3)}
.vdur{margin-left:auto;font-size:11.5px;color:var(--ink-3);background:var(--card-2);padding:3px 8px;border-radius:6px}
.vcard h3{font-size:15px;letter-spacing:-.02em;margin-top:2px}
.vwhat{font-size:13px;color:var(--ink-2);line-height:1.7}
.vhow{font-size:12px;color:var(--ink-3);line-height:1.7}
.vgo{margin-top:auto;font-size:12.5px;color:var(--teal);font-weight:600;padding-top:6px}
.foot{margin-top:40px;padding-top:20px;border-top:1px solid var(--line);font-size:12px;color:var(--ink-3);line-height:1.85}
.foot b{color:var(--ink-2)}
@media (max-width:820px){.grid{grid-template-columns:1fr}}
@media (max-width:520px){.wrap{padding:0 16px}main{padding:24px 0 56px}.vcard{padding:15px}}
</style>
</head>
<body>
<header class="topbar">
  <div class="wrap">
    <div class="brand"><i>下</i>KD一对A · 对比演示合集</div>
    <div class="spacer"></div>
    <a class="pill" href="https://space.bilibili.com/2044980/video" target="_blank" rel="noopener">UP 主主页 ↗</a>
    <button class="iconbtn" id="themeBtn" aria-label="切换深浅色">
      <svg id="iconMoon" width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
      <svg id="iconSun" style="display:none" width="15" height="15" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.5 1.5M17.5 17.5 19 19M19 5l-1.5 1.5M6.5 17.5 5 19" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    </button>
  </div>
</header>
<main class="wrap">
  <div class="kicker">9 个投稿 · 9 个对比演示页</div>
  <h1>每个视频，一套可以点着讲的对比演示</h1>
  <p class="lede">这个账号一共 9 个视频：7 个 UI / 交互设计科普 + 2 个《黑神话：悟空》无伤实录。每个视频各做一页，共 9 个单文件页面，点进去都是能直接投屏演示的交互页面。</p>
  <div class="stats">
    <span class="pill v">9 个单文件 HTML</span>
    <span class="pill t">零外部依赖 · 可离线</span>
    <span class="pill">统一套用同一段 CSS Reset</span>
    <span class="pill">深浅色切换</span>
  </div>
  <div class="grid">__CARDS__</div>
  <div class="crosslink" style="display:flex;gap:12px;flex-wrap:wrap;margin-top:26px">
    <a href="../index.html" style="background:var(--card);border-radius:12px;padding:12px 16px;box-shadow:var(--sh);font-size:12.8px;color:var(--ink-2);text-decoration:none"><b style="display:block;color:var(--ink);font-size:13.5px;margin-bottom:2px">工作区总入口：两套形态对照表</b>22 个素材 · App 与 HTML 两种打开方式</a>
    <a href="../app/index.html" style="background:var(--card);border-radius:12px;padding:12px 16px;box-shadow:var(--sh);font-size:12.8px;color:var(--ink-2);text-decoration:none"><b style="display:block;color:var(--ink);font-size:13.5px;margin-bottom:2px">应用形态：22 个素材的「素材库」App</b>一个应用里 22 条素材 · 搜索 / 对比 / 一键复制提示词</a>
    <a href="../motion-demos/index.html" style="background:var(--card);border-radius:12px;padding:12px 16px;box-shadow:var(--sh);font-size:12.8px;color:var(--ink-2);text-decoration:none"><b style="display:block;color:var(--ink);font-size:13.5px;margin-bottom:2px">另一套：motion-web 的 7 个动效案例</b>每个案例一套可交互演示 + 一键复制提示词</a>
    <a href="../glass-demos/index.html" style="background:var(--card);border-radius:12px;padding:12px 16px;box-shadow:var(--sh);font-size:12.8px;color:var(--ink-2);text-decoration:none"><b style="display:block;color:var(--ink);font-size:13.5px;margin-bottom:2px">再一套：liquid-glass-studio 的 6 个液态玻璃案例</b>WebGL2 真实 4-pass · 折射 / 色散 / 菲涅尔 / SDF</a>
  </div>
  <div class="foot">
    <b>说明</b>：演示内容按各视频公开的要点还原，组件形态与视频一致，但画面不是视频原片截图；两条游戏视频为非 UI 主题，只做信息归档、帧率观感与闪避窗口示意。<br>
    <b>用法</b>：每个页面都是独立 HTML，可直接拖进浏览器、投屏或用微信/飞书发出去；改主题按钮在右上角。
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
""".replace("__CARDS__", "".join(cards))

with open("index.html", "w", encoding="utf-8") as f:
    f.write(INDEX)
print("wrote index.html", len(INDEX))
