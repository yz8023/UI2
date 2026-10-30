#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成素材库：46 条素材 × (在线演示 + 四件套文档) + 总览页 + 参考文献。

用法：  python3 gen_library.py
产物：  library/index.html            总览（46 个实时演示 + 详情面板）
        library/F01-button/index.html  单条：演示 + 全部文档
        library/F01-button/{实现方案,参考来源,环境要求}.md
        library/{CREDITS.md,参考来源-总表.md,AGENTS.md,README.md,index.json}
        library/prompts/全部提示词.md
"""
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from _cat_base import REG, by_cat, CAT_META, REF, DEMO_CSS   # noqa: E402
import _cat_a, _cat_b, _cat_c, _cat_d, _cat_e, _cat_f         # noqa: F401,E402
from _shell import RESET, SHELL_CSS, COMMON_JS, HUB_JS        # noqa: E402

E = lambda s: html.escape(str(s), quote=False)
EA = lambda s: html.escape(str(s), quote=True)

TAB_LABELS = ['效果', '机制', '判据', '代码', '提示词', '出处']

# 搜索用的同义词：只影响检索，不写进页面
CAT_KW = {
    '基础组件': '控件 元素 原子',
    '表单输入': '输入 表单 录入',
    '导航': '导航 跳转 菜单 页面切换',
    '布局': '排版 布局 网格 结构',
    '反馈': '提示 状态 加载 动画反馈',
    '数据展示': '图表 统计 可视化 数据',
    '动效': '动画 动效 过渡 手势',
    '应用模板': '页面 模板 整页 深色 浅色 登录 设置',
}


def scope_css(css, iid):
    """把单条素材的 CSS 限定在它自己的舞台上。

    1) keyframes 名字加条目后缀，避免同名动画互相覆盖；
    2) `.dz` 选择器换成 `[data-item="Fxx"]`，避免 46 条素材合并在同一页时互串。
    """
    for name in set(re.findall(r'@keyframes\s+([A-Za-z_][\w-]*)', css)):
        css = re.sub(r'(?<![\w-])' + re.escape(name) + r'(?![\w-])', f'{name}-{iid}', css)
    return css.replace('.dz', f'[data-item="{iid}"]')


# ───────────────────────── 公共片段 ─────────────────────────

def head(title, extra_css=''):
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#070b12">
<meta name="description" content="UI 素材库 · {EA(title)} · 46 条可运行素材，含实现方案 / 参考来源 / 环境要求">
<title>{E(title)}</title>
<style>
{RESET}
{SHELL_CSS}
{DEMO_CSS}
{extra_css}
</style>
</head>"""


def topbar(brand_href='index.html', brand_label='素材库', count=46, nav=None, right=''):
    navhtml = ''
    if nav:
        navhtml = '<nav class="catnav">' + ''.join(
            f'<a href="#cat-{k}" data-filter="{EA(c)}">{E(c)}</a>' for c, k in nav) + '</nav>'
    else:
        navhtml = '<div style="flex:1"></div>'
    return f"""<header class="topbar"><div class="topbar-in">
  <a class="brand" href="{brand_href}"><i></i>{E(brand_label)}<b>{count}</b></a>
  {navhtml}
  {right}
</div></header>"""


def search_box():
    return ('<label class="search"><span>⌕</span><input id="q" type="search" '
            'placeholder="搜索素材 / 参数" autocomplete="off"></label>')


def toast_div():
    return '<div id="toast"></div>'


# ───────────────────────── 文档面板（HTML） ─────────────────────────

def panels_html(it):
    """详情里 6 个面板：效果 / 机制 / 判据 / 代码 / 提示词 / 出处"""
    effect = f"""<div class="prose" data-p="0">
  <h4>看到什么</h4><p>{E(it['mech'])}</p>
  <h4>参数</h4><div class="kv">{''.join(f'<b>{E(k)}</b><span>{E(v)}</span>' for k, v in [('参数组', it['params'])])}</div>
  <h4>操作提示</h4><p>{E(it['demo_hint'])}</p>
</div>"""
    steps = ''.join(f'<li>{E(s)}</li>' for s in it['steps'])
    mech = f"""<div class="prose" data-p="1" hidden>
  <h4>实现原理</h4><p>{E(it['mech'])}</p>
  <h4>详细步骤</h4><ol>{steps}</ol>
</div>"""
    checks = ''.join(f'<li>{E(v)}</li>' for v in it['verify'].split('；'))
    reds = ''.join(f'<li>{E(r)}</li>' for r in it['redline'])
    rows = ''.join(f'<tr><td class="bad">{E(a)}</td><td>{E(b)}</td><td>{E(c)}</td></tr>' for a, b, c in it['fails'])
    judge = f"""<div class="prose" data-p="2" hidden>
  <h4>验收判据（逐条可测）</h4><ul class="checks">{checks}</ul>
  <h4>红线（违反即返工）</h4><ul class="reds">{reds}</ul>
  <h4>失败指纹</h4>
  <table class="tbl"><thead><tr><th>现象</th><th>根因</th><th>修正</th></tr></thead><tbody>{rows}</tbody></table>
</div>"""
    code = f"""<div class="prose" data-p="3" hidden>
  <h4>HTML</h4><pre class="prompt">{E(it['html'])}</pre>
  <h4>CSS</h4><pre class="prompt">{E(it['css'])}</pre>
  <h4>JS</h4><pre class="prompt">{E(it['js'])}</pre>
</div>"""
    prompt = f"""<div class="prose" data-p="4" hidden>
  <h4>一键复制提示词</h4>
  <pre class="prompt" id="p-{it['id']}">{E(it['prompt'])}</pre>
  <div class="copybar"><button class="btnp" data-copy="#p-{it['id']}">复制提示词</button>
  <span class="hint">含参考项目 · 变更要求 · 产出约束</span></div>
</div>"""
    refcards = ''.join(
        f"""<div class="refcard"><div class="t">{E(n)} <em>{E(l)}</em></div>
        <div class="u">{E(u)}</div><div class="d">{E(use)}</div></div>"""
        for n, u, l, use in it['refs'])
    refp = f"""<div class="prose" data-p="5" hidden>
  <h4>参考来源（独立实现，不含上游源码 / 图片）</h4>{refcards}
  <h4>借鉴边界</h4><p>只借鉴结构、参数与交互语义；所有演示代码为本库按上述思路重新绘制，
  不复制任何上游项目的源码、贴图或字体。许可证与署名见 <code>CREDITS.md</code>。</p>
</div>"""
    return {'effect': effect, 'mech': mech, 'judge': judge, 'code': code,
            'prompt': prompt, 'refs': refp}


# ───────────────────────── 单条页面 ─────────────────────────

def build_item(it, idx, prev_it, next_it):
    p = panels_html(it)
    pid = it['id']
    cat_code = CAT_META[it['catname']][0]
    body = f"""<body>
{topbar('../index.html', '素材库', 46)}
<main class="doc">
  <a class="btn-ghost" href="../index.html">← 返回素材库</a>
  <div style="margin-top:16px"><span class="eyebrow">{pid} · {cat_code} {E(it['catname'])} · {E(it['tag'])}</span></div>
  <h1>{E(it['name'])}</h1>
  <p class="lede">{E(it['mech'])}</p>
  <div class="pills" style="display:flex;gap:7px;flex-wrap:wrap;margin-top:14px">
    <span class="pill">难度 <b>{E(it['diff'])}</b></span>
    <span class="pill">参数 <b>{E(it['params'].split(' · ')[0])}</b></span>
    <span class="pill acc">可离线运行</span>
  </div>

  <div class="stage-lg"><div class="fit"><div class="dz" id="stage" data-item="{pid}"></div></div></div>
  <div class="copybar">
    <button class="btnp" data-copy="#p-{pid}">复制提示词</button>
    <button class="btn-ghost" data-replay>重播演示</button>
    <span class="hint">{E(it['demo_hint'])}</span>
  </div>

  <div class="tabs">{''.join(f'<button class="{"on" if i == 0 else ""}">{E(t)}</button>' for i, t in enumerate(TAB_LABELS))}</div>
  <div id="doc">
    {p['effect']}{p['mech']}{p['judge']}{p['code']}{p['prompt']}{p['refs']}
  </div>

  <div class="pager">
    <a class="prev" href="../{prev_it['id']}-{prev_it['slug']}/index.html"><span>← 上一条</span><b>{prev_it['id']} {E(prev_it['name'])}</b></a>
    <a class="next" href="../{next_it['id']}-{next_it['slug']}/index.html"><span>下一条 →</span><b>{next_it['id']} {E(next_it['name'])}</b></a>
  </div>
</main>
{toast_div()}
<template id="tpl-demo">{it['html']}</template>
<script>
{COMMON_JS}
(function(){{
  var stage = document.getElementById('stage');
  function run(){{
    stage.innerHTML = document.getElementById('tpl-demo').innerHTML;
    window.__fit(stage.closest('.fit'));
    try{{ ({it['js']})(stage); }}catch(e){{ console.error(e); }}
  }}
  run();
  document.querySelector('[data-replay]').addEventListener('click', run);
  var tabs = [].slice.call(document.querySelectorAll('.tabs button'));
  var ps = [].slice.call(document.querySelectorAll('#doc [data-p]'));
  tabs.forEach(function(b, i){{
    b.addEventListener('click', function(){{
      tabs.forEach(function(x, k){{ x.classList.toggle('on', k === i); }});
      ps.forEach(function(x, k){{ x.hidden = k !== i; }});
    }});
  }});
}})();
</script>
</body>
</html>
"""
    return head(f"{pid} {it['name']} · 素材库", scope_css(it['css'], pid)) + body


# ───────────────────────── 总览页 ─────────────────────────

def build_hub():
    cats = by_cat()
    cards, templates, doc_templates, mount, items_json = [], [], [], [], []
    item_css = []

    def catkey(c):
        return 'c' + CAT_META[c][0]

    for cname, its in cats:
        code, desc, rng = CAT_META[cname]
        inner = []
        for it in its:
            i = next(k for k, x in enumerate(REG) if x['id'] == it['id'])
            kw = ' '.join([it['catname'], CAT_KW.get(it['catname'], ''), it['tag'],
                           it['params'], it['diff'], it['mech']])
            inner.append(f"""<button class="card" data-i="{i}" data-id="{it['id']}" data-cat="{EA(cname)}"
        data-name="{EA(it['name'])}" data-kw="{EA(kw)}" aria-label="打开 {EA(it['name'])} 详情">
      <div class="stage"><div class="fit"><div class="dz" data-item="{it['id']}" data-demo="{i}"></div></div></div>
      <div class="meta">
        <div class="r1"><span class="fid">{it['id']}</span><h3>{E(it['name'])}</h3><span class="diff">{E(it['diff'])}</span></div>
        <div class="desc">{E(it['mech'])}</div>
        <div class="tags"><span class="tag">{E(cname)}</span><span class="tag">{E(it['tag'])}</span>
          <span class="tag hot">点击看详情</span></div>
      </div>
    </button>""")
            item_css.append(scope_css(it['css'], it['id']))
            templates.append(f'<template id="tpl-{i}">{it["html"]}</template>')
            p = panels_html(it)
            doc_templates.append(
                f'<template id="doc-{i}">{p["effect"]}{p["mech"]}{p["judge"]}{p["code"]}{p["prompt"]}{p["refs"]}</template>')
            mount.append(f"function(root){{ try{{ ({it['js']})(root); }}catch(e){{ console.error('{it['id']}', e); }} }}")
            items_json.append({'i': i, 'id': it['id'], 'name': it['name'], 'cat': cname,
                               'slug': it['slug'], 'mech': it['mech'], 'params': it['params'],
                               'diff': it['diff']})
        cards.append(f"""<section class="cat" id="cat-{catkey(cname)}" data-cat="{EA(cname)}">
  <div class="cat-h"><span class="num">{code}</span><h2>{E(cname)}</h2>
    <p>{E(desc)}</p><span class="cnt">{rng} · {len(its)} 条</span></div>
  <div class="grid">{''.join(inner)}</div>
</section>""")

    nav = [(CAT_META[c][0].lstrip('0') or '0', c) for c, _ in cats]
    navlinks = ''.join(f'<a href="#cat-c{CAT_META[c][0]}" data-filter="{EA(c)}">{E(c)}</a>' for c, _ in cats)

    refs_html = ''.join(
        f"""<div class="refcard"><div class="t">{E(n)} <em>{E(l)}</em></div>
        <div class="u">{E(u)}</div><div class="d">{E(use)}</div></div>"""
        for n, u, l, use in REF.values())

    total = len(REG)
    body = f"""<body>
<header class="topbar"><div class="topbar-in">
  <a class="brand" href="index.html"><i></i>UI 素材库<b>{total}</b></a>
  <nav class="catnav">{navlinks}</nav>
  {search_box()}
  <button class="btnp" data-copy-all>复制全部提示词</button>
</div></header>

<header class="hero">
  <span class="eyebrow">素材 + 文档 · 四件套</span>
  <h1>一个 App 需要的每个界面，<br><em>从组件到页面全部到位</em></h1>
  <p>46 条素材，8 个分类：组件 → 布局 → 反馈 → 数据 → 动效 → 页面模板。
  每条素材都是可直接运行的实时演示，配 <b>实现方案 · 参考来源 · 环境要求 · 一键复制提示词</b>。
  全部离线可用，不依赖任何 CDN、字体或图片。</p>
  <div class="pills">
    <span class="pill"><b>46</b> 条素材</span>
    <span class="pill"><b>8</b> 个分类</span>
    <span class="pill"><b>0</b> 外部依赖</span>
    <span class="pill acc">点击任意卡片看实现与提示词</span>
  </div>
</header>

<main>{''.join(cards)}</main>

<footer class="foot" id="refs">
  <div class="row">
    <div style="min-width:260px">
      <h5>参考文献 · CREDITS</h5>
      <div class="note">本素材库的文档结构（实现方案 / 参考来源 / 环境要求 / 红线 / 失败指纹）与深色极光 + 液态玻璃的视觉语言，
      移植自 <a href="https://github.com/yz8023/ui" target="_blank" rel="noopener">yz8023/ui</a>（MIT）。
      全部演示代码为独立实现，未复制任何上游项目的源码、贴图或字体。</div>
    </div>
    <div style="min-width:240px">
      <h5>全部来源</h5>
      {refs_html}
    </div>
  </div>
</footer>

<div class="dock">
  <button data-filter="all" class="on">全部</button>
  <button data-filter="基础组件">组件</button>
  <button data-filter="布局">布局</button>
  <button data-filter="反馈">反馈</button>
  <button data-filter="应用模板">模板</button>
  <span class="sep"></span>
  <button data-copy-all>复制提示词</button>
</div>

<div class="mask" id="mask"></div>
<aside class="sheet" id="sheet" role="dialog" aria-modal="true" aria-label="素材详情">
  <div class="sheet-top">
    <span class="fid" id="dId">F01</span>
    <h2 id="dName">素材</h2>
    <span class="cat" id="dCat">分类</span>
    <button class="x" id="dClose" aria-label="关闭">✕</button>
  </div>
  <div class="sheet-body" id="dBody">
    <div class="stage-lg"><div class="fit"><div class="dz" id="dStage"></div></div></div>
    <div class="tabs" id="dTabs">{''.join(f'<button class="{"on" if i == 0 else ""}">{E(t)}</button>' for i, t in enumerate(TAB_LABELS))}</div>
    <div id="dDoc"></div>
    <div class="pager" style="margin-top:22px">
      <a class="prev" href="#" id="dPrev"><span>← 上一条</span><b>键盘 ←</b></a>
      <a class="next" href="#" id="dNext"><span>下一条 →</span><b>键盘 →</b></a>
    </div>
  </div>
</aside>

{toast_div()}
{''.join(templates)}
{''.join(doc_templates)}
<script>
window.__ITEMS = {json.dumps(items_json, ensure_ascii=False)};
window.__MOUNT = [{','.join(mount)}];
{COMMON_JS}
document.querySelectorAll('[data-copy-all]').forEach(function(b){{
  b.addEventListener('click', function(){{
    var all = window.__ITEMS.map(function(x){{ return document.getElementById('p-' + x.id); }})
      .filter(Boolean).map(function(n){{ return n.textContent; }}).join('\\n\\n' + '─'.repeat(40) + '\\n\\n');
    window.__copy(all).then(function(ok){{ window.__toast(ok ? '已复制 46 条提示词' : '复制失败，请手动选择'); }});
  }});
}});
{HUB_JS}
</script>
</body>
</html>
"""
    extra = '\n/* ── 46 条素材样式（按 data-item 作用域隔离）── */\n' + '\n'.join(item_css)
    return head(f"UI 素材库 · {total} 条素材（演示 + 实现方案 + 参考来源）", extra) + body


# ───────────────────────── Markdown 四件套 ─────────────────────────

def md_plan(it):
    cat_code = CAT_META[it['catname']][0]
    steps = '\n'.join(f'{i+1}. {s}' for i, s in enumerate(it['steps']))
    checks = '\n'.join(f'- [ ] {v}' for v in it['verify'].split('；'))
    reds = '\n'.join(f'- ✕ {r}' for r in it['redline'])
    fails = '\n'.join(f'| {a} | {b} | {c} |' for a, b, c in it['fails'])
    return f"""# {it['id']} · {it['name']} — 实现方案

> 分类：{cat_code} {it['catname']}　｜　难度：{it['diff']}　｜　主题：{it['tag']}
>
> 一句话：{it['mech']}

## 一、效果（用户看到什么）

{it['mech']}

演示入口：本目录 `index.html`（自包含，双击即可运行）。

## 二、实现原理

{it['mech']}

关键点：

{chr(10).join('- ' + s for s in it['steps'])}

## 三、参数表

| 参数 | 值 | 说明 |
| --- | --- | --- |
| 参数组 | {it['params']} | 改动这里就能整体换手感 |

## 四、详细步骤

{steps}

## 五、验收判据（逐条可测）

{checks}

## 六、红线（违反即返工）

{reds}

## 七、失败指纹（改坏了长什么样）

| 现象 | 根因 | 修正 |
| --- | --- | --- |
{fails}

## 八、可直接复制的提示词

```text
{it['prompt']}
```

## 九、依赖与环境

见同目录 `环境要求.md`：{it['env_deps']}
"""


def md_refs(it):
    rows = '\n'.join(f"| {n} | {u} | {l} | {use} |" for n, u, l, use in it['refs'])
    return f"""# {it['id']} · {it['name']} — 参考来源

本条目为**独立实现**：只借鉴下表中的结构、参数与交互语义，不含任何上游项目的源码、图片、字体或贴图。
许可证与全局署名见仓库根目录 `CREDITS.md`。

## 直接参考

| 项目 | 链接 | 许可 | 本项目借鉴了什么 |
| --- | --- | --- | --- |
{rows}

## 文档方法论来源

| 项目 | 链接 | 许可 | 借鉴了什么 |
| --- | --- | --- | --- |
| yz8023/ui | https://github.com/yz8023/ui | MIT | 「实现方案 / 参考来源 / 环境要求」四件套写法、红线与失败指纹的表达方式、深色极光 + 液态玻璃的视觉语言 |

## 借鉴边界

- ✅ 借鉴：组件语义、尺寸与动效参数、无障碍与手势约定、文档结构。
- ❌ 不借鉴：源码片段、UI 截图、图标与字体资源、商标与品牌名。
- 若下游项目需要商用，请单独核对表中每个上游仓库的许可证（尤其 CC BY-NC 4.0 的 motion-web：
  仅可用于非商业场景，本库未复制其任何素材，仅参考其动效 token 的思路）。
"""


def md_env(it):
    return f"""# {it['id']} · {it['name']} — 环境要求

## 运行时

| 项目 | 要求 |
| --- | --- |
| 浏览器 | 支持 CSS 自定义属性、`position: sticky`、`pointer events` 的现代浏览器（Chrome 88+ / Safari 15+ / WebView 88+） |
| 依赖 | {it['env_deps']} |
| 网络 | 不需要。全部样式与脚本内联，不引用 CDN、字体或图片 |
| 构建 | 不需要。`index.html` 双击即运行 |

## 文件清单

| 文件 | 作用 |
| --- | --- |
| `index.html` | 演示 + 全部文档 + 一键复制提示词（自包含单文件） |
| `实现方案.md` | 效果 / 原理 / 参数 / 步骤 / 判据 / 红线 / 失败指纹 |
| `参考来源.md` | 直接参考与借鉴边界 |
| `环境要求.md` | 本文件 |

## 本条的额外说明

{it['env_notes'] or '无。'}

## 接入到真实项目

1. 复制 `index.html` 里 `<template id="tpl-demo">` 的内容（结构）与对应 CSS 段（全部以 `.dz` 前缀隔离，把 `.dz` 换成你的作用域即可）。
2. 复制 `<script>` 里的函数体，传入你的根元素：`fn(rootEl)`。
3. 把硬编码的演示数据换成你的数据源；不要改动参数表里的数值，除非你同时接受判据里对应条目的变化。

## 自检命令（可选）

```bash
python3 -m http.server 8080   # 打开 http://localhost:8080/ 逐条点开
```
"""


# ───────────────────────── 全局文档 ─────────────────────────

def build_credits():
    rows = '\n'.join(f"| **{n}** | {u} | {l} | {use} |" for n, u, l, use in REF.values())
    return f"""# 致谢 · 参考文献

本素材库的**代码与视觉语言**建立在以下开源项目与公开文档之上。谢谢所有作者的无私分享。

## 一、方法论与视觉总来源

| 项目 | 链接 | 许可 | 借鉴了什么 |
| --- | --- | --- | --- |
| **yz8023/ui** | https://github.com/yz8023/ui | MIT | 素材库的「四件套」文档结构（实现方案 / 参考来源 / 环境要求）、
AGENTS 红线写法、验收清单与失败指纹的表达、深色极光 + 液态玻璃的界面语言 |

> 移植的是**方法与观感**，不是代码：上游是 Android Compose 工程，本库是 HTML/CSS/JS，
> 两者共享同一套文档骨架与视觉规则。

## 二、每个条目的直接参考

| 项目 | 链接 | 许可 | 借鉴了什么 |
| --- | --- | --- | --- |
{rows}

## 三、许可证与使用边界

- 本库全部演示代码为**独立实现**（procedural），未复制任何上游项目的源码、截图、图标、字体。
- **feitangyuan/motion-web** 为 **CC BY-NC 4.0**：仅可用于非商业用途。本库只参考其动效 token 的数值思路
  （时长、缓动、错峰节奏），未复制其任何素材；如需商用请自行评估。
- **iyinchao/liquid-glass-studio** 为 **MIT**：本库的玻璃参数体系（厚度 / 折射率 / 色散 / 菲涅尔）参考其公开参数表，
  渲染实现为 CSS + SVG 的简化版本。
- **yz8023/ui** 为 **MIT**：可自由借鉴与再分发，保留本致谢即可。
- Material Design 3、Apple HIG 为文档，非代码，按其公开条款引用。

## 四、如何引用本库

```text
UI 素材库 2.0（46 条素材），文档结构参考 yz8023/ui（MIT），
动效 token 参考 feitangyuan/motion-web（CC BY-NC 4.0），玻璃参数参考 iyinchao/liquid-glass-studio（MIT）。
```
"""


def build_ref_index():
    use = {}
    for it in REG:
        for n, u, l, _ in it['refs']:
            use.setdefault((n, u, l), []).append(it['id'])
    lines = ['# 参考来源 · 总表', '',
             '按上游项目聚合：左边是来源，右边是引用了它的素材编号。每条素材的详细借鉴说明见各自的 `参考来源.md`。', '',
             '| 来源 | 链接 | 许可 | 被引用于 | 条目数 |', '| --- | --- | --- | --- | --- |']
    for (n, u, l), ids in sorted(use.items(), key=lambda kv: -len(kv[1])):
        lines.append(f'| **{n}** | {u} | {l} | {"、".join(ids)} | {len(ids)} |')
    lines += ['', '---', '',
              '## 文档方法论', '',
              '全部 46 条素材的「实现方案 / 参考来源 / 环境要求」结构、红线与失败指纹的写法，',
              '移植自 [yz8023/ui](https://github.com/yz8023/ui)（MIT）。', '',
              f'合计：{len(REG)} 条素材 / {len(use)} 个上游来源。', '']
    return '\n'.join(lines)


def build_agents():
    return """# AGENTS.md · 本素材库的协作红线

> 移植自 [yz8023/ui](https://github.com/yz8023/ui) 的 AGENTS 规范，按 HTML 素材库的实际情况改写。
> 任何 AI / 协作者改动本库前，先读这一页。

## 一、红线（违反即返工）

1. **不改名**：`Fxx-slug` 的编号与目录名是稳定标识，引用关系都靠它。要改必须全库同步。
2. **不换机制**：每条素材的动效机制写死在「实现方案 · 实现原理」里。
   要把 CSS 过渡换成弹簧、把 sticky 换成 JS 模拟滚动——属于换实现，必须同时更新参数表与判据。
3. **不混搭**：一条素材只解决一件事。把 Toast 塞进对话框、把主题色散落各处，都会被判为混搭。
4. **不跳前置**：先跑通演示，再改文档；不要文档写了效果没做。
5. **不静默降级**：不支持 `backdrop-filter`、`IntersectionObserver`、`ResizeObserver` 时要有可见兜底，
   不许悄悄变成一块静止的方块。
6. **不动无关文件**：一次改动只碰目标素材目录 + 必要的索引（`index.html` / `index.json`）。
7. **不引外链**：任何 CDN、字体、图片、`fetch` 一律禁止——预览在沙箱 iframe 里没有网络。
8. **不覆盖 CSS reset**：每个页面的第一段样式必须是约定的 reset 块。

## 二、工作流（照抄 yz8023/ui 的六步）

1. **体检**：打开目标条目，先看演示是否流畅、判据是否全部通过。
2. **开工表**：写清「改哪一条 / 改什么 / 影响哪些判据 / 是否动参数表」。
3. **整文件改写**：不要用零散 patch 拼，宁可整段替换，避免半截动画。
4. **本地编译**：`python3 gen_library.py`，确认 46 条全部生成、0 报错。
5. **验收**：逐条跑判据；用「失败指纹」表反查有没有引入新毛病。
6. **汇报**：一句话说清改了什么、哪条判据受影响、参数表是否变化。

## 三、引用规范

- 新增素材必须在 `参考来源.md` 里写明：借鉴了哪个项目的哪个机制、许可证、借鉴边界。
- 新增上游来源时，同时写进 `CREDITS.md` 与 `参考来源-总表.md`，并在 `_cat_base.py` 的 `REF` 里登记。
- 不复制上游源码；只写「思路来源」。

## 四、验收清单模板

```text
[ ] 演示在 60fps 下无掉帧（Chrome Performance 面板）
[ ] 判据全部通过（逐条打勾）
[ ] 红线无违反
[ ] 失败指纹表里的现象没有出现
[ ] 窄屏 360px / 宽屏 1440px 都不溢出
[ ] prefers-reduced-motion 下有降级
[ ] 提示词可直接复制并复现同样效果
```
"""


def build_readme():
    cats = by_cat()
    rows = '\n'.join(f'| {CAT_META[c][0]} | {c} | {len(i)} | {CAT_META[c][1]} | {CAT_META[c][2]} |' for c, i in cats)
    return f"""# UI 素材库 2.0 · 46 条素材

一个 App 从组件到页面所需的全部界面素材：**每条素材 = 可运行演示 + 实现方案 + 参考来源 + 环境要求 + 一键复制提示词**。

## 打开方式

- 直接双击 `index.html`（不需要服务器；离线可用，无任何 CDN / 字体 / 图片依赖）。
- 卡片可点，右侧滑出详情：效果 / 机制 / 判据 / 代码 / 提示词 / 出处，六个面板。
- 键盘：`Esc` 关闭，`←` `→` 切换上一条 / 下一条。

## 分类总表

| 编号 | 分类 | 条目 | 覆盖内容 | 功能号 |
| --- | --- | --- | --- | --- |
{rows}

## 目录结构

```text
library/
├── index.html              总览：46 个实时演示 + 详情面板 + 参考文献
├── index.json              机器可读索引
├── CREDITS.md              致谢与许可证
├── 参考来源-总表.md          按上游项目聚合的引用表
├── AGENTS.md               协作红线与工作流
├── prompts/全部提示词.md     46 条提示词的合集
├── _cat_base.py            设计 token / item 工厂 / REF 表
├── _cat_a.py … _cat_f.py   46 条素材的数据（HTML/CSS/JS/文档字段）
├── _shell.py               页面皮肤（CSS/JS）
├── gen_library.py          生成器（`python3 gen_library.py`）
└── F01-button/
    ├── index.html          演示 + 全部文档（自包含）
    ├── 实现方案.md
    ├── 参考来源.md
    └── 环境要求.md
```

## 文档方法论

「四件套」结构与红线 / 失败指纹的写法移植自 [yz8023/ui](https://github.com/yz8023/ui)（MIT），
见 `CREDITS.md` 与 `AGENTS.md`。

## 重新生成

```bash
cd library && python3 gen_library.py
```
"""


def build_prompts():
    out = ['# 全部提示词 · 46 条', '',
           '每条提示词都包含：参考项目（机制 + 关键参数）、变更要求、产出约束、自检标准。',
           '直接整段复制给 AI，即可复现同样的效果。', '']
    for it in REG:
        out += [f"## {it['id']} · {it['name']}（{it['catname']} · {it['diff']}）", '',
                f"> {it['mech']}", '', '```text', it['prompt'], '```', '']
    return '\n'.join(out)


# ───────────────────────── 主流程 ─────────────────────────

def main():
    n = len(REG)
    for idx, it in enumerate(REG):
        prev_it = REG[(idx - 1) % n]
        next_it = REG[(idx + 1) % n]
        d = os.path.join(HERE, f"{it['id']}-{it['slug']}")
        os.makedirs(d, exist_ok=True)
        files = {
            'index.html': build_item(it, idx, prev_it, next_it),
            '实现方案.md': md_plan(it),
            '参考来源.md': md_refs(it),
            '环境要求.md': md_env(it),
        }
        for name, content in files.items():
            with open(os.path.join(d, name), 'w', encoding='utf-8') as f:
                f.write(content)

    with open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(build_hub())

    docs = {
        'CREDITS.md': build_credits(),
        '参考来源-总表.md': build_ref_index(),
        'AGENTS.md': build_agents(),
        'README.md': build_readme(),
        '参考来源.md': build_credits(),          # 兼容上游命名
    }
    for name, content in docs.items():
        with open(os.path.join(HERE, name), 'w', encoding='utf-8') as f:
            f.write(content)

    os.makedirs(os.path.join(HERE, 'prompts'), exist_ok=True)
    with open(os.path.join(HERE, 'prompts', '全部提示词.md'), 'w', encoding='utf-8') as f:
        f.write(build_prompts())

    index = [{
        'id': it['id'], 'slug': it['slug'], 'name': it['name'],
        'cat': it['catname'], 'catCode': CAT_META[it['catname']][0],
        'diff': it['diff'], 'tag': it['tag'], 'params': it['params'],
        'mech': it['mech'], 'path': f"{it['id']}-{it['slug']}/index.html",
        'refs': [r[0] for r in it['refs']],
    } for it in REG]
    with open(os.path.join(HERE, 'index.json'), 'w', encoding='utf-8') as f:
        json.dump({'version': '2.0', 'total': n, 'categories': CAT_META,
                   'items': index}, f, ensure_ascii=False, indent=1)

    hub = os.path.getsize(os.path.join(HERE, 'index.html'))
    print(f'✓ {n} 条素材 / {len(by_cat())} 个分类')
    print(f'✓ 总览页 {hub/1024:.1f} KB')
    for c, its in by_cat():
        print(f'  {CAT_META[c][0]} {c:<6} {len(its):>2} 条  {CAT_META[c][2]}')


if __name__ == '__main__':
    main()
