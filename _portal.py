# -*- coding: utf-8 -*-
"""生成 工作区总入口 /home/user/index.html：两套形态互相跳转"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'app'))

from _app_data import all_items  # noqa

CSS = """
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Segoe UI', sans-serif;
    -webkit-tap-highlight-color: transparent;
}
:root{
  --bg:#0b1219;--txt:#e9eff7;--soft:rgba(233,239,247,.62);--dim:rgba(233,239,247,.40);
  --line:rgba(255,255,255,.13);--blue:#9dccff;--mint:#5fdba8;--violet:#9d8cff;--amber:#ffd28a;
  --ease:cubic-bezier(.2,.9,.3,1.1);
}
[hidden]{display:none!important}
body{background:var(--bg);color:var(--txt);min-height:100vh;overflow-x:hidden;font-size:14px;line-height:1.6;
  font-family:'Segoe UI','PingFang SC','HarmonyOS Sans SC','Microsoft YaHei',system-ui,sans-serif}
a{color:inherit;text-decoration:none}
.aurora{position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden}
.blob{position:absolute;border-radius:50%;filter:blur(72px);opacity:.46;animation:drift 30s linear infinite}
.blob:nth-child(1){width:56vmax;height:56vmax;top:-16vmax;left:-12vmax;background:radial-gradient(circle,rgba(29,74,115,.95),transparent 70%)}
.blob:nth-child(2){width:48vmax;height:48vmax;top:-8vmax;right:-16vmax;background:radial-gradient(circle,rgba(88,61,180,.8),transparent 70%);animation-duration:36s;animation-direction:reverse}
.blob:nth-child(3){width:58vmax;height:58vmax;bottom:-22vmax;left:-8vmax;background:radial-gradient(circle,rgba(23,110,88,.7),transparent 70%);animation-duration:42s}
@keyframes drift{from{transform:translate3d(0,0,0) scale(1)}to{transform:translate3d(4vmax,-3vmax,0) scale(1.12)}}
.wrap{position:relative;z-index:1;max-width:1060px;margin:0 auto;padding:26px 18px 60px}
.glass{background:linear-gradient(180deg,rgba(255,255,255,.07),rgba(255,255,255,.022));
  border:1px solid rgba(255,255,255,.15);box-shadow:0 12px 32px rgba(0,0,0,.34);border-radius:22px;
  -webkit-backdrop-filter:blur(24px) saturate(1.5) brightness(1.06);backdrop-filter:blur(24px) saturate(1.5) brightness(1.06)}
h1{font-size:clamp(24px,3.6vw,34px);line-height:1.28;letter-spacing:-.02em;font-weight:700}
.lede{font-size:13.5px;color:var(--soft);max-width:66ch;margin-top:9px}
.lede b{color:var(--txt)}
.forms{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:20px}
.form{padding:20px;display:flex;flex-direction:column;gap:8px;transition:transform .2s var(--ease),box-shadow .2s}
.form:hover{transform:translateY(-3px);box-shadow:0 20px 44px rgba(0,0,0,.5)}
.form .tag{font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--blue)}
.form h2{font-size:18px}
.form p{font-size:12.5px;color:var(--soft);line-height:1.7}
.form .go{margin-top:auto;font-size:12.5px;color:var(--blue);font-weight:600;padding-top:6px}
.sec{display:flex;align-items:center;gap:8px;margin:30px 2px 12px;font-size:12px;font-weight:600;
  color:var(--soft);letter-spacing:.06em}
.sec::before{content:"";width:9px;height:9px;border-radius:3px;background:var(--blue);box-shadow:0 0 14px var(--blue)}
table{width:100%;border-collapse:collapse;font-size:12.5px}
thead th{text-align:left;font-size:11px;font-weight:600;color:var(--dim);padding:10px 12px;border-bottom:1px solid var(--line)}
tbody tr{border-bottom:1px solid rgba(255,255,255,.06)}
tbody tr:hover{background:rgba(255,255,255,.035)}
td{padding:11px 12px;vertical-align:top;line-height:1.6}
td.num{font-family:ui-monospace,Menlo,monospace;font-size:10.5px;color:#06121c;background:var(--blue);
  border-radius:5px;padding:2px 6px;white-space:nowrap}
td.nm{font-weight:600;white-space:nowrap}
td.kind{color:var(--dim);white-space:nowrap;font-size:11.5px}
td.mech{color:var(--soft);font-size:11.8px}
td.act{white-space:nowrap;text-align:right}
.apkbox{display:grid;grid-template-columns:auto 1fr;gap:18px;align-items:start;padding:18px}
.apkbox .icon{width:64px;height:64px;border-radius:16px;background:linear-gradient(150deg,#9dccff,#164a70);
  display:grid;place-items:center;font-size:26px;color:#06121c;font-weight:700}
.apkbox h3{font-size:16px;margin-bottom:4px}
.apkbox .meta{font-size:11.5px;color:var(--dim);margin-bottom:8px}
.apkbox p{font-size:12.5px;color:var(--soft);line-height:1.75}
.dl{display:inline-block;margin-top:10px;font-size:12.5px;font-weight:600;padding:9px 16px;border-radius:11px;
  background:#9dccff;color:#06121c}
.dl:hover{background:#bcdcff}
.shots{display:flex;gap:10px;margin-top:14px;flex-wrap:wrap}
.shots img{width:180px;border-radius:12px;border:1px solid var(--line);display:block}
@media (max-width:700px){.apkbox{grid-template-columns:1fr}.shots img{width:44vw}}
.btn{display:inline-block;font-size:11.5px;padding:5px 10px;border-radius:8px;border:1px solid var(--line);
  color:var(--soft);margin-left:6px;transition:.18s}
.btn:hover{color:#fff;background:rgba(157,204,255,.16);border-color:rgba(157,204,255,.45)}
.btn.p{color:#06121c;background:var(--blue);border-color:transparent;font-weight:600}
.btn.p:hover{background:#bcdcff;color:#06121c}
.foot{margin-top:34px;padding-top:18px;border-top:1px solid var(--line);font-size:11.5px;color:var(--dim);line-height:1.85}
.foot b{color:var(--soft)}
@media (max-width:820px){
  .forms{grid-template-columns:1fr}
  thead{display:none}
  tbody tr{display:grid;grid-template-columns:1fr;gap:2px;padding:12px 4px}
  td{border:0;padding:1px 2px}
  td.act{text-align:left;padding-top:8px}
  .btn{margin:0 6px 0 0}
}
"""

COLL = {'video': '视频拆解', 'motion': '动效复刻', 'glass': '液态玻璃', 'lib': '完整素材库'}


def build():
    items = [x for x in all_items() if x['coll'] != 'lib']
    rows = []
    for it in items:
        rows.append(
            '<tr>'
            '<td><span class="num">%s</span></td>'
            '<td class="nm">%s</td>'
            '<td class="kind">%s · %s</td>'
            '<td class="mech">%s</td>'
            '<td class="act">'
            '<a class="btn p" href="app/index.html#%s">在 App 里看</a>'
            '<a class="btn" href="%s" target="_blank" rel="noopener">HTML 演示页 ↗</a>'
            '</td></tr>' % (
                it['id'].upper(), it['name'], COLL[it['coll']], it['dur'],
                it['mech'][:96] + ('…' if len(it['mech']) > 96 else ''),
                it['id'], it['path'].replace('../', ''))
        )
    html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="dark">
<title>UI 素材工作区 · 两套形态</title>
<style>%s</style>
</head>
<body>
<div class="aurora"><div class="blob"></div><div class="blob"></div><div class="blob"></div></div>
<div class="wrap">
  <h1>同一个素材库，两套形态。</h1>
  <p class="lede"><b>46 条完整素材 + 22 个案例拆解</b>，从按钮一路做到登录页、设置页、个人主页，覆盖一个 App 需要的每一类界面。
  每条素材都<b>真的能跑</b>，并配齐<b>实现方案 / 参考来源 / 环境要求 / 一键复制提示词</b>四件套（文档结构移植自 yz8023/ui）。
  一套是<b>应用形态</b>：搜索、筛选、并排对比；一套是<b>HTML 形态</b>：46 个独立页 + 一张总览。</p>

  <div class="forms">
    <a class="form glass" href="app/index.html">
      <div class="tag">form 01</div>
      <h2>应用形态 · 素材库 App 3.1</h2>
      <p><b>悬浮 Dock 导航</b>（图标格 + 滑动指示器，近黑中性底，不再用大面积蓝色极光）：首页 / 素材（8 个分类页 + 全局功能搜索 + 68 张实时演示卡）/ 体验（XPopup 20 弹窗 · 20 动画 · 45 设置 · 5 手势 + motion-web 7 个 case 全屏剧场 · 20 配方 · 4 组令牌 · 25 规范）/ 结构（3 平台 × 11 功能 → 目录树 + 素材映射 + 开工提示词，勾选不跳顶）/ 更多（并排对比 + 设置）。点卡片开详情，勾变更要求即可一键复制提示词。</p>
      <div class="go">打开 App →</div>
    </a>
    <a class="form glass" href="library/index.html">
      <div class="tag">form 02</div>
      <h2>HTML 形态 · 完整素材库 2.0（46 条）</h2>
      <p>8 个分类：基础组件 · 表单输入 · 导航 · 布局 · 反馈 · 数据展示 · 动效 · 应用模板。总览页里 46 个演示同时能跑，
      点开任意一条即是「效果 / 机制 / 判据 / 代码 / 提示词 / 出处」六个面板，每页还带实现方案、参考来源、环境要求。</p>
      <div class="go">打开完整素材库 →</div>
    </a>
  </div>

    <div class="sec">源码与安装包</div>
  <div class="glass" style="padding:16px 18px">
    <div class="note">
      <b>仓库</b>：<a href="https://github.com/yz8023/UI2" style="color:var(--blue)">github.com/yz8023/UI2</a> ·
      源码、生成器、Android 壳、CI 全在里面。<br>
      <b>发布</b>：<a href="https://github.com/yz8023/UI2/releases/latest" style="color:var(--blue)">Releases · v3.1</a> —
      APK 3.1（versionCode 5、零权限、1.0 MB）+ 两个单文件 HTML。<br>
      <b>在线</b>：<a href="https://yz8023.github.io/UI2/app/index.html" style="color:var(--blue)">yz8023.github.io/UI2</a>
      —— GitHub Pages 直接跑 App。
    </div>
  </div>

<div class="sec">完整素材库 2.0 · 46 条素材 · 8 个分类</div>
  <div class="glass" style="overflow:hidden;padding:4px 6px">
    <table>
      <thead><tr><th>分类</th><th>条数</th><th>覆盖内容</th><th style="text-align:right">功能号</th></tr></thead>
      <tbody>
        <tr><td>01 基础组件</td><td>6</td><td>按钮 · 输入框 · 开关 · 滑块 · 勾选与单选 · 头像徽标</td><td style="text-align:right">F01–F06</td></tr>
        <tr><td>02 表单输入</td><td>6</td><td>校验 · 步进器 · 分段控件 · 搜索 · 上传 · 选择器</td><td style="text-align:right">F07–F12</td></tr>
        <tr><td>03 导航</td><td>6</td><td>底部标签栏 · 折叠顶栏 · 抽屉 · 面包屑 · 标签页 · 侧边栏</td><td style="text-align:right">F13–F18</td></tr>
        <tr><td>04 布局</td><td>6</td><td>Bento 网格 · 分组列表 · 瀑布流 · 响应式栅格 · 粘性堆叠 · 安全区</td><td style="text-align:right">F19–F24</td></tr>
        <tr><td>05 反馈</td><td>7</td><td>Toast · 对话框 · 底部面板 · 骨架屏 · 空状态 · 进度环 · 加载按钮</td><td style="text-align:right">F25–F31</td></tr>
        <tr><td>06 数据展示</td><td>6</td><td>折线 · 柱状 · 环形 · 数据卡 · 表格 · 时间线</td><td style="text-align:right">F32–F37</td></tr>
        <tr><td>07 动效</td><td>5</td><td>弹簧拖拽 · 错峰入场 · 手势卡片 · 页面转场 · 滚动视差</td><td style="text-align:right">F38–F42</td></tr>
        <tr><td>08 应用模板</td><td>4</td><td>引导页 · 登录页 · 设置页 · 个人主页</td><td style="text-align:right">F43–F46</td></tr>
      </tbody>
    </table>
  </div>

  <div class="sec">22 个案例拆解 · 两套形态任选</div>
  <div class="glass" style="overflow:hidden;padding:4px 6px">
    <table>
      <thead><tr><th>编号</th><th>素材</th><th>类型</th><th>机制</th><th style="text-align:right">打开方式</th></tr></thead>
      <tbody>
        %s
      </tbody>
    </table>
  </div>

  <div class="foot">
    <b>许可证</b>：完整素材库的文档结构与视觉语言移植自 <a href="https://github.com/yz8023/ui" style="color:#8fbfff">yz8023/ui</a>（MIT）；
    动效部分参考 feitangyuan/motion-web（CC BY-NC 4.0，禁止商用）；液态玻璃部分参考 iyinchao/liquid-glass-studio（MIT）；视频拆解部分为公开视频要点还原。
    所有演示均为按机制重新实现的代码，未拷贝原项目素材；玻璃背景由着色器程序化生成。<br>
    <b>离线</b>：全部单文件内联，无 CDN、无外部图片字体，拖进浏览器即可打开。
  </div>
</div>
</body>
</html>
""" % (CSS, "\n        ".join(rows))
    out = os.path.join(HERE, 'index.html')
    open(out, 'w', encoding='utf-8').write(html)
    print('wrote', out, len(html))


if __name__ == '__main__':
    build()
