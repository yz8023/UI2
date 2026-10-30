# -*- coding: utf-8 -*-
"""F13–F24：导航 + 布局"""
from _cat_base import item, add, refs

# ───────────────────────── 导航 ─────────────────────────

F13 = item(
    id='F13', slug='tabbar', name='底部标签栏', cat='03-导航', catname='导航', diff='★★☆', tag='导航',
    mech='液态玻璃底栏 + 胶囊指示器：指示器宽度由文字宽度算、位置用 transform 平移 420ms 弹簧；点击时图标上浮 1px 并回弹。',
    params='高 64 · 圆角 24 · 指示器高 34 · 位移 420ms cubic-bezier(.3,.9,.3,1.12)',
    verify='切换时指示器只平移；连续点击不堆积动画；安全区底部留白 env(safe-area-inset-bottom)。',
    steps=['指示器用 getBoundingClientRect 相对底栏计算，避免 offsetParent 变化导致错位。',
           '底栏滚动时保持固定，正文加 padding-bottom 等于底栏高度 + 安全区。'],
    redline=['不许把底栏做成 4 个等分色块（没有指示器就没有空间感）。'],
    fails=[('指示器偏左', '用了 offsetLeft（受定位上下文影响）', '统一用 getBoundingClientRect 差值')],
    prompt='''做液态玻璃底部标签栏（4 个 tab）。
【结构】固定底部、宽 min(520px, 100%-28px)、高 64、圆角 24、backdrop-filter: blur(24px) saturate(1.5)；
内部一个绝对定位胶囊指示器（高 34），当前项图标 + 文字。
【动效】指示器宽 = 选中项宽 - 16，位移用 transform，420ms cubic-bezier(.3,.9,.3,1.12)；
点击时图标 translateY(-1px) 回弹；切页时内容淡入 180ms。
【自检】切换 10 次指示器不错位；安全区留白正确；毛玻璃在深色背景上有可见的高光边缘。''',
    html='''<div class="tb">
  <div class="tb-pill"></div>
  <button class="tb-i on"><b>⌂</b>首页</button>
  <button class="tb-i"><b>▤</b>素材</button>
  <button class="tb-i"><b>⇄</b>对比</button>
  <button class="tb-i"><b>⚙</b>设置</button>
</div>
<div class="cap" style="bottom:auto;top:9px">指示器 420ms 弹簧位移</div>''',
    css='''.dz .tb{position:absolute;left:14px;right:14px;bottom:12px;height:56px;border-radius:22px;
  display:flex;align-items:center;justify-content:space-around;padding:0 6px;
  background:linear-gradient(180deg,rgba(255,255,255,.10),rgba(255,255,255,.03));
  border:1px solid rgba(255,255,255,.18);box-shadow:0 12px 30px rgba(0,0,0,.45);
  -webkit-backdrop-filter:blur(18px) saturate(1.5);backdrop-filter:blur(18px) saturate(1.5)}
.dz .tb-pill{position:absolute;left:0;bottom:6px;height:32px;border-radius:16px;background:rgba(255,255,255,.14);
  border:1px solid rgba(255,255,255,.20);transition:transform .42s cubic-bezier(.3,.9,.3,1.12),width .42s cubic-bezier(.3,.9,.3,1.12)}
.dz .tb-i{position:relative;z-index:1;flex:1;display:flex;flex-direction:column;align-items:center;gap:1px;
  font-size:9.5px;color:var(--dim);padding:5px 0;transition:color .22s}
.dz .tb-i b{font-size:15px;line-height:1;font-weight:400;transition:transform .24s var(--spring)}
.dz .tb-i.on{color:var(--ink)}
.dz .tb-i.on b{transform:translateY(-1px)}''',
    js='''function(root){
  var bar = root.querySelector('.tb'), pill = bar.querySelector('.tb-pill');
  var its = [...bar.querySelectorAll('.tb-i')];
  function sel(i){
    its.forEach(function(b, k){ b.classList.toggle('on', k === i); });
    var b = its[i], br = bar.getBoundingClientRect(), r = b.getBoundingClientRect();
    pill.style.width = Math.max(30, r.width - 16) + 'px';
    pill.style.transform = 'translateX(' + (r.left - br.left + 8) + 'px)';
  }
  its.forEach(function(b, i){ b.addEventListener('click', function(){ sel(i); }); });
  requestAnimationFrame(function(){ sel(0); });
}''',
    refs=refs('miuix', 'hig', 'glass'),
    env_notes='无依赖；放到真实项目里请把 inset 换成 safe-area-inset-bottom 的计算。',
    demo_hint='点四个 tab 看胶囊滑动',
)

F14 = item(
    id='F14', slug='navbar', name='顶栏（大标题折叠）', cat='03-导航', catname='导航', diff='★★☆', tag='导航',
    mech='滚动时大标题缩小并淡出、小标题淡入、底部分割线出现：三件事用同一个滚动进度 p 驱动，避免各写一套。',
    params='折叠区间 0–64px · 大标题 20px→0 · 小标题 0→13px · 透明度线性映射',
    verify='滚动到 64px 时大标题完全消失、小标题完全出现；反向滚动对称；空闲无抖动。',
    steps=['用一个可滚动容器 + scroll 事件算 p，再用 CSS 变量喂给所有属性。'],
    redline=['不许用两个 DOM 切换（会出现一帧双标题）。'],
    fails=[('标题跳变', '两个标题各自 transition', '统一由 --p 连续驱动')],
    prompt='''做可折叠顶栏：滚动容器内的内容把大标题顶出去。
【效果】滚动 0→64px 期间：大标题 font-size 20→0、opacity 1→0；小标题 opacity 0→1、font-size 0→13px；
分割线在 p>0.7 时出现。全部由同一个 --p 驱动。
【自检】缓慢滚动来回无跳变；p 到 1 时只剩小标题；滚动停止 3 秒仍稳定。''',
    html='''<div class="nb">
  <div class="nb-bar"><span class="nb-mini">素材库</span><span class="nb-act">＋</span></div>
  <div class="nb-scroll">
    <div class="nb-big">素材库</div>
    <div class="nb-body"></div>
  </div>
</div>
<div class="cap">在框里向下滚</div>''',
    css='''.dz .nb{position:absolute;inset:0;display:flex;flex-direction:column}
.dz .nb-bar{position:relative;height:38px;display:flex;align-items:center;justify-content:center;flex:0 0 auto;
  border-bottom:1px solid transparent;transition:border-color .2s;z-index:2;background:linear-gradient(180deg,#0d141b,rgba(13,20,27,.82))}
.dz .nb-mini{font-size:0px;opacity:0;font-weight:600;color:var(--ink)}
.dz .nb-act{position:absolute;right:12px;color:var(--acc);font-size:16px}
.dz .nb-scroll{flex:1;overflow:auto;padding:0 14px;scrollbar-width:none}
.dz .nb-scroll::-webkit-scrollbar{display:none}
.dz .nb-big{font-size:20px;font-weight:700;letter-spacing:-.02em;padding:2px 0 8px}
.dz .nb-body{height:260px;border-radius:12px;
  background:repeating-linear-gradient(180deg,rgba(255,255,255,.07) 0 34px,transparent 34px 42px)}''',
    js='''function(root){
  var sc = root.querySelector('.nb-scroll'), big = root.querySelector('.nb-big'),
      mini = root.querySelector('.nb-mini'), bar = root.querySelector('.nb-bar');
  sc.addEventListener('scroll', function(){
    var p = Math.min(1, sc.scrollTop / 64);
    big.style.fontSize = (20 - 20*p).toFixed(2) + 'px';
    big.style.opacity = (1 - p).toFixed(2);
    mini.style.fontSize = (13*p).toFixed(2) + 'px';
    mini.style.opacity = p.toFixed(2);
    bar.style.borderBottomColor = p > .7 ? 'rgba(255,255,255,.14)' : 'transparent';
  }, {passive:true});
}''',
    refs=refs('hig', 'miuix', 'm3'),
    env_notes='无依赖；接到真实页面时把 scroll 容器换成 window 并节流到 rAF。',
    demo_hint='在框里滚动',
)

F15 = item(
    id='F15', slug='drawer', name='抽屉导航', cat='03-导航', catname='导航', diff='★★☆', tag='导航',
    mech='左侧抽屉 + 遮罩 + 手势：拖拽超过 30% 或速度 >0.4 才关闭，否则弹簧回位；抽屉内容错峰入场。',
    params='宽度 62% · 打开 300ms · 关闭阈值位移 30% / 速度 0.4px·ms⁻¹',
    verify='小幅拖拽松手回弹；快速轻扫也能关闭；遮罩透明度随拖拽距离联动。',
    steps=['拖拽中直接改 translateX，松手按阈值二选一，都用同一套弹簧曲线。'],
    redline=['不许只有点击关闭（移动端必须支持边缘滑动）。'],
    fails=[('拖拽后卡住', '松手没有重置 transition', '松手时显式设置 transition 再改 transform')],
    prompt='''做左侧抽屉导航：宽 62%，遮罩 40% 黑，内容项错峰入场（每项延迟 40ms）。
【手势】从任意位置向右拖拽关闭；位移 >30% 宽 或 速度 >0.4px/ms 判定关闭，否则 300ms 弹簧回位；
拖拽过程中遮罩透明度跟随位移线性变化。
【自检】小幅拖拽回弹、快速轻扫关闭；打开时按 Esc 关闭；遮罩点击关闭；错峰入场不抖动。''',
    html='''<div class="dr-wrap">
  <button class="dr-open">≡ 打开抽屉</button>
  <div class="dr-mask"></div>
  <aside class="dr on">
    <div class="dr-h">素材库</div>
    <a class="dr-i">⌂ 首页</a><a class="dr-i">▤ 组件</a><a class="dr-i">⇄ 对比</a><a class="dr-i">⚙ 设置</a>
  </aside>
</div>
<div class="cap">向右拖关闭 · 小幅回弹</div>''',
    css='''.dz .dr-wrap{position:absolute;inset:0;overflow:hidden}
.dz .dr-open{position:absolute;left:14px;top:12px;height:32px;padding:0 12px;border-radius:10px;
  background:rgba(255,255,255,.08);border:1px solid var(--line);font-size:11.5px;color:var(--ink)}
.dz .dr-mask{position:absolute;inset:0;background:#000;opacity:0;pointer-events:none;transition:opacity .3s}
.dz .dr{position:absolute;left:0;top:0;bottom:0;width:62%;background:#121b23;border-right:1px solid var(--line);
  transform:translateX(-100%);transition:transform .3s var(--spring);padding:12px 10px;z-index:2}
.dz .dr.on{transform:none}
.dz .dr.on + .dr-mask,.dz .dr-wrap.move .dr-mask{opacity:.45;pointer-events:auto}
.dz .dr-h{font-size:11px;color:var(--dim);padding:2px 6px 8px}
.dz .dr-i{display:block;padding:8px 10px;border-radius:9px;font-size:12px;color:var(--soft)}
.dz .dr.on .dr-i{animation:drIn .34s var(--ease) both}
.dz .dr.on .dr-i:nth-child(2){animation-delay:.04s}
.dz .dr.on .dr-i:nth-child(3){animation-delay:.08s}
.dz .dr.on .dr-i:nth-child(4){animation-delay:.12s}
.dz .dr.on .dr-i:nth-child(5){animation-delay:.16s}
@keyframes drIn{from{opacity:0;transform:translateX(-10px)}to{opacity:1;transform:none}}''',
    js='''function(root){
  var dr = root.querySelector('.dr'), mask = root.querySelector('.dr-mask'), wrap = root.querySelector('.dr-wrap');
  function open(){ dr.classList.add('on'); }
  function close(){ dr.classList.remove('on'); dr.style.transform=''; }
  root.querySelector('.dr-open').addEventListener('click', open);
  mask.addEventListener('click', close);
  var sx = 0, dx = 0, t0 = 0, dragging = false;
  dr.addEventListener('pointerdown', function(e){ dragging = true; sx = e.clientX; t0 = performance.now(); dr.style.transition='none'; });
  window.addEventListener('pointermove', function(e){
    if(!dragging) return;
    dx = Math.min(0, e.clientX - sx);
    dr.style.transform = 'translateX(' + dx + 'px)';
  });
  window.addEventListener('pointerup', function(){
    if(!dragging) return;
    dragging = false;
    dr.style.transition = '';
    var dist = Math.abs(dx) / dr.offsetWidth, v = Math.abs(dx) / Math.max(1, performance.now() - t0);
    if(dist > .3 || v > .4) close();
    else dr.style.transform = '';
    dx = 0;
  });
}''',
    refs=refs('ionic', 'hig', 'miuix'),
    env_notes='无依赖；真实项目里建议加边缘触发区（左侧 20px 起手）。',
    demo_hint='打开后向右拖',
)

F16 = item(
    id='F16', slug='breadcrumb', name='面包屑', cat='03-导航', catname='导航', diff='★☆☆', tag='导航',
    mech='空间不足时折叠中间层级（首层 + … + 末层），hover 省略号弹出被折叠的部分；分隔符用伪元素，不占 DOM。',
    params='最多显示 3 段 · 折叠后 首/…/末 · 分隔符 10px 透明度 40%',
    verify='窄容器下自动折叠；展开列表可点；当前页不可点且颜色更深。',
    steps=['用容器宽度与每段宽度累加判断是否折叠，ResizeObserver 监听变化。'],
    redline=['不许在移动端横向滚动面包屑（会顶破布局）。'],
    fails=[('省略号点了没反应', '省略号只是文本', '省略号做成按钮 + 浮层')],
    prompt='''做自适应面包屑：层级为 首页 / 素材库 / 组件 / 表单 / 输入框。
【折叠】容器不够宽时保留首层与末层，中间折叠成「…」，点击省略号弹出被折叠的层级列表。
【样式】分隔符用 ::after（10px、透明度 40%），当前页加粗且不可点，其余 hover 变亮。
【自检】320px 宽时折叠正确；省略号浮层可点；当前页无 hover 反馈。''',
    html='''<div class="bc" id="bc">
  <a>首页</a><span class="bc-mid"><a>素材库</a><a>组件</a><a>表单</a></span><a class="cur">输入框</a>
</div>
<div class="bc-pop">素材库<br>组件<br>表单</div>
<div class="cap">窄屏自动折叠中间层级</div>''',
    css='''.dz .bc{display:flex;align-items:center;gap:6px;font-size:11.5px;color:var(--soft);max-width:100%;
  white-space:nowrap;overflow:hidden}
.dz .bc a{color:var(--soft);cursor:pointer}
.dz .bc a:hover{color:var(--ink)}
.dz .bc a.cur{color:var(--ink);font-weight:700;cursor:default}
.dz .bc a + a::before,.dz .bc-mid + a::before{content:"/";margin-right:6px;color:var(--dim)}
.dz .bc-mid{display:flex;gap:6px}
.dz .bc-mid.collapsed a{display:none}
.dz .bc-mid.collapsed::before{content:"…";color:var(--acc);cursor:pointer;margin-right:6px}
.dz .bc-pop{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) scale(.94);opacity:0;pointer-events:none;
  background:#1b242d;border:1px solid var(--line);border-radius:10px;padding:8px 12px;font-size:11px;
  color:var(--soft);line-height:1.8;transition:.2s;box-shadow:0 12px 30px rgba(0,0,0,.5)}
.dz .bc-pop.on{opacity:1;transform:translate(-50%,-50%);pointer-events:auto}''',
    js='''function(root){
  var bc = root.querySelector('.bc'), mid = bc.querySelector('.bc-mid'), pop = root.querySelector('.bc-pop');
  function fit(){
    var w = bc.clientWidth, need = 0;
    [...bc.children].forEach(function(c){ need += c.scrollWidth + 8; });
    mid.classList.toggle('collapsed', need > w);
  }
  fit();
  if(window.ResizeObserver) new ResizeObserver(fit).observe(bc);
  mid.addEventListener('click', function(e){
    if(!mid.classList.contains('collapsed')) return;
    e.stopPropagation(); pop.classList.toggle('on');
  });
  document.addEventListener('click', function(){ pop.classList.remove('on'); });
}''',
    refs=refs('antd', 'm3'),
    env_notes='无依赖。',
    demo_hint='把窗口拉窄看折叠',
)

F17 = item(
    id='F17', slug='tabs', name='标签页', cat='03-导航', catname='导航', diff='★★☆', tag='导航',
    mech='墨条跟随 + 面板横向滑动：墨条宽度等于标签文字宽，切换时平移 300ms；面板用 translateX 整排滑动，'
         '支持左右滑动切换。',
    params='墨条高 2px · 位移 300ms · 面板滑动 320ms · 滑动阈值 60px',
    verify='墨条与文字对齐；滑动切换与点击切换状态一致；面板内容不重排。',
    steps=['面板容器宽度 = n×100%，内部每页 100%，用 translateX 百分比切换。'],
    redline=['不许每个面板各自淡入（会出现两层同时可见）。'],
    fails=[('墨条错位', '给墨条写了 padding', '墨条宽度取文字宽度，left 取文字左侧')],
    prompt='''做标签页（3 个）：墨条指示器 + 横向滑动的面板。
【墨条】宽 = 标签文字宽，高 2，圆角，切换 300ms；初始位置在第一个标签下。
【面板】容器宽 300%，内部每页 100%，用 translateX(-i*100%) 切换（320ms）；
支持在内容区左右拖动超过 60px 切换（松手回弹）。
【自检】点击与滑动结果一致；墨条不错位；切换时只有 transform 变化。''',
    html='''<div class="tp">
  <div class="tp-h"><button class="on">概览</button><button>参数</button><button>代码</button><i class="tp-ink"></i></div>
  <div class="tp-vp"><div class="tp-track">
    <div class="tp-p">机制说明：SDF + 折射 + 色散</div>
    <div class="tp-p">参数：厚度 20 / 距离 0.05 / 折射率 1.4</div>
    <div class="tp-p">代码：4-pass WebGL2 渲染器</div>
  </div></div>
</div>
<div class="cap">点击或左右拖拽切换</div>''',
    css='''.dz .tp{width:250px}
.dz .tp-h{position:relative;display:flex;gap:16px;border-bottom:1px solid var(--line);padding-bottom:7px}
.dz .tp-h button{font-size:12px;color:var(--dim);transition:color .2s}
.dz .tp-h button.on{color:var(--ink);font-weight:700}
.dz .tp-ink{position:absolute;bottom:-1px;left:0;height:2px;border-radius:2px;background:var(--acc);
  transition:transform .3s var(--ease),width .3s var(--ease)}
.dz .tp-vp{overflow:hidden;margin-top:10px}
.dz .tp-track{display:flex;width:300%;transition:transform .32s var(--ease)}
.dz .tp-p{width:33.333%;font-size:11.5px;color:var(--soft);padding-right:10px;line-height:1.7}''',
    js='''function(root){
  var btns = [...root.querySelectorAll('.tp-h button')], ink = root.querySelector('.tp-ink'),
      track = root.querySelector('.tp-track'), vp = root.querySelector('.tp-vp');
  var i = 0;
  function sel(n){
    i = Math.max(0, Math.min(btns.length-1, n));
    btns.forEach(function(b,k){ b.classList.toggle('on', k===i); });
    var b = btns[i];
    ink.style.width = b.offsetWidth + 'px';
    ink.style.transform = 'translateX(' + b.offsetLeft + 'px)';
    track.style.transform = 'translateX(' + (-i * (100/btns.length)) + '%)';
  }
  btns.forEach(function(b,k){ b.addEventListener('click', function(){ sel(k); }); });
  var sx = 0, dx = 0, drag = false;
  vp.addEventListener('pointerdown', function(e){ drag = true; sx = e.clientX; track.style.transition='none'; });
  window.addEventListener('pointermove', function(e){
    if(!drag) return;
    dx = e.clientX - sx;
    track.style.transform = 'translateX(calc(' + (-i * 100/btns.length) + '% + ' + dx + 'px))';
  });
  window.addEventListener('pointerup', function(){
    if(!drag) return;
    drag = false; track.style.transition = '';
    if(dx < -60) sel(i+1); else if(dx > 60) sel(i-1); else sel(i);
    dx = 0;
  });
  requestAnimationFrame(function(){ sel(0); });
}''',
    refs=refs('m3', 'ionic', 'antd'),
    env_notes='无依赖；页数可变，改 .tp-track 的宽度即可。',
    demo_hint='点击标签，或在内容区拖动',
)

F18 = item(
    id='F18', slug='sidebar', name='侧边栏', cat='03-导航', catname='导航', diff='★★☆', tag='导航',
    mech='图标轨（rail）与展开态互切：宽度 56 ↔ 200，文字用 opacity + 位移错峰出现，展开状态记忆在 localStorage。',
    params='宽度 56/200 · 过渡 260ms · 文字延迟 60ms · 激活项有左侧 3px 高亮条',
    verify='切换时图标不移动位置；文字不换行不抖动；刷新后保持上次状态。',
    steps=['图标位置固定：用固定 56px 的内层容器，外层面板只改宽度。'],
    redline=['不许让图标随着展开一起平移（会显得在"跳"）。'],
    fails=[('文字挤出抖动', '宽度过渡 + 文本撑开', '文本设 white-space:nowrap + overflow:hidden')],
    prompt='''做可折叠侧边栏：收起 56px 只显示图标，展开 200px 显示图标 + 文字。
【动效】宽度 260ms；文字 opacity 0→1 并右移 6px，逐项延迟 60ms；图标位置始终不变。
【状态】当前项左侧 3px 主题色高亮条 + 背景 tint；折叠按钮在底部；状态写入 localStorage。
【自检】展开/收起 10 次不抖动；刷新保持状态；图标 x 坐标全程不变（用 JS 打印验证）。''',
    html='''<div class="sb-wrap">
  <aside class="sb">
    <div class="sb-logo">库</div>
    <a class="sb-i on"><b>⌂</b><span>首页</span></a>
    <a class="sb-i"><b>▤</b><span>素材库</span></a>
    <a class="sb-i"><b>⇄</b><span>对比</span></a>
    <a class="sb-i"><b>⚙</b><span>设置</span></a>
    <button class="sb-t">‹</button>
  </aside>
  <div class="sb-body"><div class="sb-ph"></div><div class="sb-ph"></div><div class="sb-ph"></div></div>
</div>
<div class="cap">点底部 ‹ 折叠 / 展开</div>''',
    css='''.dz .sb-wrap{display:flex;width:100%;height:100%;gap:10px;align-items:stretch;padding:8px}
.dz .sb{width:56px;border-radius:14px;background:rgba(255,255,255,.06);border:1px solid var(--line);
  padding:8px 6px;display:flex;flex-direction:column;gap:3px;overflow:hidden;
  transition:width .26s var(--ease)}
.dz .sb.open{width:132px}
.dz .sb-logo{height:26px;display:flex;align-items:center;justify-content:center;font-weight:800;color:var(--acc);
  font-size:12px;margin-bottom:6px}
.dz .sb-i{position:relative;display:flex;align-items:center;gap:9px;height:30px;padding:0 7px;border-radius:8px;
  color:var(--dim);font-size:11.5px;white-space:nowrap;overflow:hidden;flex:0 0 auto}
.dz .sb-i b{width:16px;text-align:center;font-weight:400;font-size:14px;flex:0 0 auto}
.dz .sb-i span{opacity:0;transform:translateX(4px);transition:opacity .2s .04s,transform .2s .04s}
.dz .sb.open .sb-i span{opacity:1;transform:none}
.dz .sb-i.on{color:var(--ink);background:rgba(157,204,255,.14)}
.dz .sb-i.on::before{content:"";position:absolute;left:0;top:7px;bottom:7px;width:3px;border-radius:2px;background:var(--acc)}
.dz .sb-t{margin-top:auto;height:26px;border-radius:8px;background:rgba(255,255,255,.07);color:var(--soft);
  font-size:12px;transition:transform .2s}
.dz .sb.open .sb-t{transform:rotate(180deg)}
.dz .sb-body{flex:1;display:flex;flex-direction:column;gap:8px}
.dz .sb-ph{flex:1;border-radius:12px;background:repeating-linear-gradient(90deg,rgba(255,255,255,.06) 0 40px,transparent 40px 48px);
  border:1px solid var(--line)}''',
    js='''function(root){
  var sb = root.querySelector('.sb'), btn = root.querySelector('.sb-t');
  function apply(open){ sb.classList.toggle('open', open); btn.textContent = open ? '‹' : '›'; }
  try{ apply(localStorage.getItem('sbOpen') === '1'); }catch(e){}
  btn.addEventListener('click', function(){
    var open = !sb.classList.contains('open');
    apply(open);
    try{ localStorage.setItem('sbOpen', open ? '1' : '0'); }catch(e){}
  });
}''',
    refs=refs('m3', 'shadcn', 'antd'),
    env_notes='无依赖。',
    demo_hint='点右下 ‹ 展开',
)

# ───────────────────────── 布局 ─────────────────────────

F19 = item(
    id='F19', slug='bento-grid', name='卡片网格', cat='04-布局', catname='布局', diff='★★☆', tag='布局',
    mech='Bento 栅格：跨列 / 跨行的卡片用 grid-column: span 2 组合，hover 时整卡上浮 3px + 阴影加深 + 内部高光跟随指针。',
    params='gap 10 · 圆角 16 · hover 上浮 3px/180ms · 高光半径 160px',
    verify='组合不同尺寸不出现空洞；hover 只影响当前卡；触屏无 hover 时用按压反馈。',
    steps=['用 grid-auto-rows: minmax(56px, auto) + span 组合，先排大卡再排小卡避免空洞。'],
    redline=['不许用绝对定位摆 bento（无法响应式）。'],
    fails=[('移动端空洞', '固定 span', '窄屏把所有 span 归 1')],
    prompt='''做 Bento 卡片网格：6 张卡，尺寸组合 2×2 + 2×1 + 1×1 等。
【布局】CSS Grid，grid-auto-rows: 56px，卡片用 grid-area/span 组合；gap 10；圆角 16。
【交互】hover：translateY(-3px)、阴影加深、内部径向高光跟随指针（--mx/--my CSS 变量）。
【响应】<520px 时全部 span 归 1，不留空洞。
【自检】任意宽度下无空洞；hover 只动当前卡；指针高光平滑。''',
    html='''<div class="bg">
  <div class="bg-c big"><b>22</b><span>素材</span><i></i></div>
  <div class="bg-c"><b>8</b><span>分类</span><i></i></div>
  <div class="bg-c"><b>46</b><span>组件</span><i></i></div>
  <div class="bg-c wide"><b>4-pass</b><span>玻璃渲染</span><i></i></div>
  <div class="bg-c"><b>60fps</b><span>动效</span><i></i></div>
  <div class="bg-c tall"><b>MIT</b><span>许可</span><i></i></div>
</div>
<div class="cap">hover 上浮 + 指针高光</div>''',
    css='''.dz .bg{display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:40px;gap:6px;width:100%;max-width:262px}
.dz .bg-c{position:relative;border-radius:11px;padding:6px 8px;overflow:hidden;
  background:linear-gradient(155deg,rgba(255,255,255,.09),rgba(255,255,255,.025));
  border:1px solid var(--line);display:flex;flex-direction:column;justify-content:flex-end;
  transition:transform .18s var(--spring),box-shadow .18s;will-change:transform}
.dz .bg-c i{position:absolute;inset:0;opacity:0;transition:opacity .2s;pointer-events:none;
  background:radial-gradient(160px circle at var(--mx,50%) var(--my,0%),rgba(157,204,255,.22),transparent 60%)}
.dz .bg-c:hover{transform:translateY(-3px);box-shadow:0 12px 26px rgba(0,0,0,.45)}
.dz .bg-c:hover i{opacity:1}
.dz .bg-c b{font-size:12px;line-height:1;letter-spacing:-.02em}
.dz .bg-c span{font-size:8.5px;color:var(--dim);margin-top:1px}
.dz .bg-c.big{grid-column:span 2;grid-row:span 2}
.dz .bg-c.wide{grid-column:span 2}
.dz .bg-c.tall{grid-row:span 2}''',
    js='''function(root){
  root.querySelectorAll('.bg-c').forEach(function(c){
    c.addEventListener('pointermove', function(e){
      var r = c.getBoundingClientRect();
      c.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      c.style.setProperty('--my', (e.clientY - r.top) + 'px');
    });
  });
}''',
    refs=refs('wind', 'm3', 'yzui'),
    env_notes='无依赖；把卡片换成你的内容即可。',
    demo_hint='鼠标移上去看高光',
)

F20 = item(
    id='F20', slug='grouped-list', name='分组列表', cat='04-布局', catname='布局', diff='★☆☆', tag='布局',
    mech='iOS 风格 inset grouped list：分组圆角 14、组间标题 12px 大写、组内行 44px 高、分割线从文字起点开始（不顶到左边）。',
    params='行高 44 · 分组圆角 14 · 分割线 inset 16 · 组间距 18',
    verify='分割线不跨过左侧图标；长文案单行省略；点击有 120ms 高亮。',
    steps=['分割线用 ::after 定位在行内，left 与文字对齐。'],
    redline=['不许每行都写 border-bottom（最后一行会多一条）。'],
    fails=[('最后一行多线', '每行都加边框', '用 :not(:last-child) 或伪元素')],
    prompt='''做 iOS 风格分组列表：两组（账户 / 偏好），每组 3 行。
【样式】分组卡片圆角 14、背景 #161f28；组标题 11px 大写次级色，左右各 6px；
行高 44，左侧图标 18px，右侧值 + 箭头；分割线从文字起点开始（left:38px），最后一行无线。
【交互】整行可点，按下 120ms 高亮；长文案单行省略。
【自检】最后一行无分割线；分割线不跨图标；按下高亮不超过 150ms。''',
    html='''<div style="width:250px">
  <div class="gl-h">账户</div>
  <div class="gl">
    <div class="gl-r"><b>◉</b><span>个人资料</span><i>林小满</i><em>›</em></div>
    <div class="gl-r"><b>◈</b><span>订阅</span><i>Pro</i><em>›</em></div>
    <div class="gl-r"><b>⇪</b><span>导出数据</span><i></i><em>›</em></div>
  </div>
  <div class="gl-h">偏好</div>
  <div class="gl">
    <div class="gl-r"><b>◐</b><span>外观</span><i>跟随系统</i><em>›</em></div>
  </div>
</div>
<div class="cap">分割线从文字起点开始</div>''',
    css='''.dz .gl-h{font-size:9.5px;color:var(--dim);letter-spacing:.1em;text-transform:uppercase;margin:0 6px 4px}
.dz .gl{border-radius:12px;background:var(--card);border:1px solid var(--line);overflow:hidden;margin-bottom:7px}
.dz .gl-r{position:relative;display:flex;align-items:center;gap:9px;height:30px;padding:0 11px;
  font-size:11.5px;color:var(--ink);transition:background .12s}
.dz .gl-r:active{background:rgba(255,255,255,.09)}
.dz .gl-r + .gl-r::before{content:"";position:absolute;left:36px;right:0;top:0;height:1px;background:rgba(255,255,255,.08)}
.dz .gl-r b{width:18px;text-align:center;color:var(--acc);font-weight:400;font-size:13px}
.dz .gl-r span{flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.dz .gl-r i{font-style:normal;color:var(--dim);font-size:11px}
.dz .gl-r em{font-style:normal;color:var(--dim);font-size:13px}''',
    js='''function(root){}''',
    refs=refs('hig', 'miuix', 'm3'),
    env_notes='无依赖。',
    demo_hint='iOS 分组列表',
)

F21 = item(
    id='F21', slug='masonry', name='瀑布流', cat='04-布局', catname='布局', diff='★★☆', tag='布局',
    mech='CSS columns 实现的瀑布流：列宽 110px、gap 8，卡片高度由内容决定；配图用渐变块占位，避免加载抖动。',
    params='columns: 110px · column-gap 8 · break-inside avoid',
    verify='不同高度卡片不跨列断裂；窗口变化列数自动调整；滚动时无重排抖动。',
    steps=['用 columns + break-inside:avoid 是成本最低的瀑布流；宽度差异大时再上 JS 分列。'],
    redline=['不许给每列写死高度（会留白）。'],
    fails=[('卡片被切断', '没有 break-inside', '加 break-inside:avoid; page-break-inside:avoid')],
    prompt='''做瀑布流：8 张不同高度的卡片（渐变占位 + 标题 + 时长）。
【实现】CSS columns: 110px，column-gap 8，卡片 break-inside: avoid，圆角 10。
【要求】窗口从 320 到 900 宽度变化时列数自动调整，无断卡；卡片 hover 轻微上浮。
【自检】任意宽度下无卡片被切断；滚动 60fps；卡片间距均匀。''',
    html='''<div class="ms">
  <div class="ms-c" style="--h:70px"><i></i>玻璃折射</div>
  <div class="ms-c" style="--h:46px"><i></i>弹簧拖拽</div>
  <div class="ms-c" style="--h:56px"><i></i>错峰入场</div>
  <div class="ms-c" style="--h:38px"><i></i>环形进度</div>
  <div class="ms-c" style="--h:50px"><i></i>骨架屏</div>
  <div class="ms-c" style="--h:62px"><i></i>底栏胶囊</div>
</div>
<div class="cap">列数随宽度自适应</div>''',
    css='''.dz .ms{columns:104px;column-gap:7px;width:100%;max-width:280px}
.dz .ms-c{break-inside:avoid;margin-bottom:7px;border-radius:10px;overflow:hidden;background:var(--card);
  border:1px solid var(--line);font-size:9.5px;color:var(--soft);padding-bottom:5px;text-align:center;
  transition:transform .18s var(--spring)}
.dz .ms-c:hover{transform:translateY(-2px)}
.dz .ms-c i{display:block;height:var(--h);margin-bottom:4px;
  background:linear-gradient(150deg,rgba(157,204,255,.35),rgba(95,219,168,.18) 70%,transparent)}''',
    js='''function(root){}''',
    refs=refs('wind', 'antd'),
    env_notes='无依赖。',
    demo_hint='纯 CSS 瀑布流',
)

F22 = item(
    id='F22', slug='responsive-grid', name='响应式栅格', cat='04-布局', catname='布局', diff='★★☆', tag='布局',
    mech='断点标尺可视化：拖动容器宽度，实时显示当前断点（xs/sm/md/lg）与列数；列用 minmax + auto-fit 自适应。',
    params='断点 360 / 560 / 760 · 列宽 minmax(64px,1fr) · gap 8',
    verify='跨断点时列数正确变化；标尺指针跟随；无横向滚动。',
    steps=['用 clamp + auto-fit 减少显式媒体查询，断点只用于排版细节。'],
    redline=['不许只写 max-width 而没有 min-width 适配（小屏会挤）。'],
    fails=[('列数算错', '用 container 宽度算但读了 window', '用 ResizeObserver 读容器')],
    prompt='''做响应式栅格演示：一个可拖动宽度的容器（260–100%）+ 内部 8 个格子。
【行为】grid-template-columns: repeat(auto-fit, minmax(64px, 1fr))；容器宽度变化时列数实时变化；
顶部标尺显示当前宽度、断点（<360 xs / <560 sm / <760 md / 其他 lg）与列数。
【自检】拖到任意宽度无横向滚动；列数 = floor((w+gap)/(64+gap))；断点标签实时更新。''',
    html='''<div style="width:100%">
  <div class="rg-ruler"><span class="rg-tag">md · 4 列</span><b class="rg-handle">⇔</b></div>
  <div class="rg-wrap" style="width:80%">
    <div class="rg"></div>
  </div>
</div>
<div class="cap">左右拖动 ⇔ 改变容器宽度</div>''',
    css='''.dz .rg-wrap{width:80%;border:1px dashed rgba(157,204,255,.5);border-radius:10px;padding:6px;position:relative;margin:0 auto}
.dz .rg{display:grid;grid-template-columns:repeat(auto-fit,minmax(56px,1fr));gap:6px}
.dz .rg div{height:26px;border-radius:7px;background:linear-gradient(150deg,rgba(157,204,255,.28),rgba(157,204,255,.08));
  border:1px solid rgba(157,204,255,.22)}
.dz .rg-ruler{display:flex;align-items:center;gap:8px;margin-bottom:7px;justify-content:center}
.dz .rg-tag{font-size:10.5px;padding:2px 8px;border-radius:99px;background:rgba(157,204,255,.16);color:var(--acc)}
.dz .rg-handle{position:absolute;right:-9px;top:50%;transform:translateY(-50%);width:18px;height:18px;
  border-radius:50%;background:var(--acc);color:#06121c;font-size:9px;display:grid;place-items:center;cursor:ew-resize}
.dz .rg-wrap{position:relative;margin:0 auto}''',
    js='''function(root){
  var wrap = root.querySelector('.rg-wrap'), tag = root.querySelector('.rg-tag'), grid = root.querySelector('.rg');
  grid.innerHTML = Array.from({length:8}).map(function(){ return '<div></div>'; }).join('');
  function sync(){
    var w = wrap.clientWidth, cols = getComputedStyle(grid).gridTemplateColumns.split(' ').length;
    var bp = w < 360 ? 'xs' : w < 560 ? 'sm' : w < 760 ? 'md' : 'lg';
    tag.textContent = bp + ' · ' + cols + ' 列 · ' + Math.round(w) + 'px';
  }
  var h = root.querySelector('.rg-handle'), drag = false;
  h.addEventListener('pointerdown', function(e){ drag = true; e.stopPropagation(); });
  window.addEventListener('pointermove', function(e){
    if(!drag) return;
    var r = root.getBoundingClientRect();
    var w = Math.max(120, Math.min(r.width - 20, e.clientX - r.left));
    wrap.style.width = w + 'px'; sync();
  });
  window.addEventListener('pointerup', function(){ drag = false; });
  sync(); window.addEventListener('resize', sync);
}''',
    refs=refs('wind', 'm3'),
    env_notes='无依赖。',
    demo_hint='拖右边的小圆点',
)

F23 = item(
    id='F23', slug='sticky-stack', name='粘性堆叠', cat='04-布局', catname='布局', diff='★★☆', tag='布局',
    mech='原生滚动 + sticky 叠压：每屏 sticky top:0，下一屏压上来时用滚动位置反算进度，驱动封面缩放与标题擦除。',
    params='sticky top 0 · 每屏高 100% · 缩放 1→0.9 随进度',
    verify='scrollY 到每屏边界时缩放正确；不出现双屏同高亮；反向滚动对称。',
    steps=['用 getBoundingClientRect 算每屏覆盖进度，避免累加误差。'],
    redline=['不许用 transform 模拟滚动（会失去原生惯性）。'],
    fails=[('叠压闪烁', 'sticky 父级 overflow:hidden', '去掉父级 overflow，改用 clip')],
    prompt='''做粘性堆叠：4 屏，每屏 sticky top:0，下一屏滚上来压住上一屏。
【效果】每屏封面随被覆盖进度从 1 缩到 0.9、透明度轻微下降；上一屏标题在进度 >60% 时淡出。
【实现】原生滚动 + position: sticky，进度用 getBoundingClientRect 计算，禁止 transform 模拟滚动。
【自检】滚动到任意位置缩放正确；反向滚动对称；滚动时无闪烁（父级不要 overflow:hidden）。''',
    html='''<div class="ss"><div class="ss-inner">
  <div class="ss-s" style="--c1:#274a63">01 · 折射</div>
  <div class="ss-s" style="--c1:#3a3560">02 · 色散</div>
  <div class="ss-s" style="--c1:#1f5048">03 · 菲涅尔</div>
</div></div>
<div class="cap">在框里滚动，屏与屏互相压住</div>''',
    css='''.dz .ss{position:absolute;inset:0;overflow:auto;scrollbar-width:none}
.dz .ss::-webkit-scrollbar{display:none}
.dz .ss-inner{padding:10px 12px}
.dz .ss-s{position:sticky;top:8px;height:104px;border-radius:13px;margin-bottom:8px;padding:12px;
  font-size:12px;font-weight:700;color:#fff;display:flex;align-items:flex-end;
  background:linear-gradient(160deg,var(--c1),#10161c 88%);
  box-shadow:0 -10px 22px rgba(0,0,0,.45);border:1px solid rgba(255,255,255,.12);
  transition:transform .12s linear,opacity .12s linear;will-change:transform}''',
    js='''function(root){
  var sc = root.querySelector('.ss'), items = [...root.querySelectorAll('.ss-s')];
  sc.addEventListener('scroll', function(){
    items.forEach(function(el, i){
      var next = items[i+1];
      if(!next){ return; }
      var r = next.getBoundingClientRect(), sr = sc.getBoundingClientRect();
      var p = Math.max(0, Math.min(1, (sr.bottom - r.top) / r.height));
      el.style.transform = 'scale(' + (1 - p*0.1).toFixed(3) + ')';
      el.style.opacity = (1 - p*0.35).toFixed(2);
    });
  }, {passive:true});
}''',
    refs=refs('motionweb', 'hig'),
    env_notes='无依赖。',
    demo_hint='向上滚动看屏压屏',
)

F24 = item(
    id='F24', slug='safe-area', name='安全区与折叠', cat='04-布局', catname='布局', diff='★★☆', tag='布局',
    mech='刘海 / 底部指示条模拟：内容必须避开 notch 与 home indicator，用 env(safe-area-inset-*) 与 padding 折叠；'
         '错误示范用红色标出被遮挡区域。',
    params='顶部 notch 28px · 底部 20px · 安全区 inset 8px',
    verify='切换「安全区」开关时，标题不被刘海遮挡、底栏不被指示条压住；错误示范必须明显可见。',
    steps=['用 padding: env(safe-area-inset-top) 而不是固定像素；模拟时用 CSS 变量替代。'],
    redline=['不许把关键操作放在底部 20px 内（会被系统手势抢走）。'],
    fails=[('内容被刘海咬掉', '全屏 100vh 无内边距', '给容器加 safe-area padding')],
    prompt='''做安全区演示：一个手机外框（带刘海与底部指示条），内部顶部标题 + 内容 + 底部操作条。
【开关】「安全区」开：容器顶部 padding 28、底部 20，内容完全避开；
关：内容贴边，用红色描出被遮挡区域并显示「被遮挡」标记。
【要求】用 CSS 变量 --sat/--sab 模拟 env(safe-area-inset-*)；外框圆角 28、边框 1px。
【自检】开/关两态遮挡区域差异肉眼可见；底部按钮不被指示条压住；切换无抖动。''',
    html='''<div class="sa">
  <div class="sa-notch"></div>
  <div class="sa-scr">
    <div class="sa-head">素材库</div>
    <div class="sa-body">内容区</div>
    <div class="sa-foot"><button>继续</button></div>
  </div>
  <div class="sa-ind"></div>
  <button class="sa-tg">安全区：开</button>
</div>
<div class="cap">点右下切换，看被刘海咬掉的样子</div>''',
    css='''.dz .sa{position:relative;width:150px;height:150px;border-radius:22px;border:1px solid var(--line2);
  background:#0a1016;overflow:hidden;box-shadow:0 10px 26px rgba(0,0,0,.5)}
.dz .sa-scr{position:absolute;inset:0;display:flex;flex-direction:column;
  padding:var(--sat,28px) 8px var(--sab,20px);transition:padding .25s var(--ease)}
.dz .sa.off{--sat:0px;--sab:0px}
.dz .sa-notch{position:absolute;top:0;left:50%;transform:translateX(-50%);width:56px;height:16px;
  border-radius:0 0 10px 10px;background:#000;z-index:3}
.dz .sa-ind{position:absolute;bottom:5px;left:50%;transform:translateX(-50%);width:44px;height:4px;
  border-radius:2px;background:rgba(255,255,255,.4);z-index:3}
.dz .sa-head{font-size:11px;font-weight:700;color:var(--ink);padding-left:4px}
.dz .sa-body{flex:1;margin-top:6px;border-radius:9px;background:repeating-linear-gradient(180deg,rgba(255,255,255,.06) 0 18px,transparent 18px 24px)}
.dz .sa-foot button{width:100%;height:26px;border-radius:8px;background:var(--acc);color:#06121c;font-size:11px;font-weight:700}
.dz .sa.off .sa-head,.dz .sa.off .sa-foot{outline:1.5px dashed var(--danger);outline-offset:1px}
.dz .sa-tg{position:absolute;right:6px;bottom:22px;z-index:5;font-size:9px;padding:4px 7px;border-radius:7px;
  background:rgba(0,0,0,.6);border:1px solid var(--line);color:var(--ink)}''',
    js='''function(root){
  var sa = root.querySelector('.sa'), tg = root.querySelector('.sa-tg');
  tg.addEventListener('click', function(){
    sa.classList.toggle('off');
    tg.textContent = '安全区：' + (sa.classList.contains('off') ? '关' : '开');
  });
}''',
    refs=refs('hig', 'ionic', 'm3'),
    env_notes='无依赖；实机请用 env(safe-area-inset-top/bottom)。',
    demo_hint='点右下角切换',
)

add(F13, F14, F15, F16, F17, F18, F19, F20, F21, F22, F23, F24)
