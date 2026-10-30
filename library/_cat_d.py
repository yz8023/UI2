# -*- coding: utf-8 -*-
"""F32–F37：数据展示"""
from _cat_base import item, add, refs

F32 = item(
    id='F32', slug='line-chart', name='折线图', cat='06-数据展示', catname='数据展示', diff='★★★', tag='数据',
    mech='SVG 折线 + 面积渐变 + 描边生长：path 用 pathLength=1 把 dashoffset 从 1 动画到 0（1.2s），'
         '面积同时淡入；悬停时用二分查找最近的点，垂直参考线跟随。',
    params='描边 2px · 生长 1.2s ease-out · 面积渐变 0.22→0 · 点半径 3.2',
    verify='描边一次画完；悬停参考线吸附到最近点；离散点数量变化时曲线仍平滑。',
    steps=['用 Catmull-Rom 转贝塞尔把折线变平滑，控制点系数 1/6。',
           '面积 path 由折线闭合到底部得到，单独一层渐变填充。'],
    redline=['不许为了"平滑"把数据点削掉（曲线必须穿过真实点）。'],
    fails=[('曲线不经过数据点', '用了简单二次贝塞尔近似', 'Catmull-Rom 转三次贝塞尔')],
    prompt='''做折线图（7 个数据点）。
【绘制】SVG viewBox 0 0 260 110；用 Catmull-Rom 转三次贝塞尔让折线平滑且必须穿过每个真实点；
描边 2px、圆头；下方面积用同一条路径闭合到底部，填充线性渐变（0.22 → 0）。
【动效】pathLength=1，stroke-dashoffset 1→0，1.2s ease-out；面积 opacity 0→1 延迟 0.3s。
【交互】pointermove 时按 x 找最近点，画垂直虚线 + 高亮点 + 数值气泡；离开时淡出。
【自检】曲线穿过 7 个点；描边一次流畅画完；气泡吸附最近点不抖动。''',
    html='''<div class="lc">
  <svg viewBox="0 0 250 100" preserveAspectRatio="none">
    <defs><linearGradient id="lcG" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#9dccff" stop-opacity=".45"/><stop offset="1" stop-color="#9dccff" stop-opacity="0"/>
    </linearGradient></defs>
    <g class="lc-grid"><line x1="0" y1="25" x2="250" y2="25"/><line x1="0" y1="50" x2="250" y2="50"/>
      <line x1="0" y1="75" x2="250" y2="75"/></g>
    <path class="lc-area" d=""/>
    <path class="lc-line" d="" pathLength="1"/>
    <line class="lc-cursor" y1="0" y2="100" x1="-9" x2="-9"/>
    <circle class="lc-dot" r="3.2" cx="-9" cy="-9"/>
  </svg>
  <div class="lc-tip">0</div>
</div>
<div class="cap">悬停看数值</div>''',
    css='''.dz .lc{position:relative;width:250px;height:110px}
.dz .lc svg{width:250px;height:100px;overflow:visible}
.dz .lc-grid line{stroke:rgba(255,255,255,.07);stroke-width:1;vector-effect:non-scaling-stroke}
.dz .lc-line{fill:none;stroke:#9dccff;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;
  stroke-dasharray:1;stroke-dashoffset:1;animation:lcDraw 1.2s var(--ease) forwards}
@keyframes lcDraw{to{stroke-dashoffset:0}}
.dz .lc-area{fill:url(#lcG);opacity:0;animation:lcA .5s .35s var(--ease) forwards}
@keyframes lcA{to{opacity:1}}
.dz .lc-cursor{stroke:rgba(157,204,255,.65);stroke-width:1;stroke-dasharray:2 2;opacity:0;transition:opacity .15s}
.dz .lc-dot{fill:#0d141b;stroke:#9dccff;stroke-width:2;opacity:0;transition:opacity .15s}
.dz .lc-tip{position:absolute;top:-6px;left:0;transform:translate(-50%,-100%);font-size:9.5px;padding:2px 6px;
  border-radius:5px;background:#243039;border:1px solid var(--line2);opacity:0;transition:opacity .15s;white-space:nowrap}''',
    js='''function(root){
  var data = [42, 58, 40, 72, 63, 88, 76], W = 250, H = 100, P = 6;
  var n = data.length, max = 95, min = 20;
  var pts = data.map(function(v, i){
    return [P + i * (W - P*2) / (n-1), H - P - (v - min) / (max - min) * (H - P*2)];
  });
  function cr(p){
    var d = 'M' + p[0][0].toFixed(1) + ' ' + p[0][1].toFixed(1);
    for(var i = 0; i < p.length - 1; i++){
      var p0 = p[i-1] || p[i], p1 = p[i], p2 = p[i+1], p3 = p[i+2] || p2;
      var c1 = [p1[0] + (p2[0]-p0[0])/6, p1[1] + (p2[1]-p0[1])/6];
      var c2 = [p2[0] - (p3[0]-p1[0])/6, p2[1] - (p3[1]-p1[1])/6];
      d += 'C' + c1[0].toFixed(1) + ' ' + c1[1].toFixed(1) + ',' + c2[0].toFixed(1) + ' ' + c2[1].toFixed(1) +
           ',' + p2[0].toFixed(1) + ' ' + p2[1].toFixed(1);
    }
    return d;
  }
  var line = root.querySelector('.lc-line'), area = root.querySelector('.lc-area');
  var d = cr(pts);
  line.setAttribute('d', d);
  area.setAttribute('d', d + 'L' + pts[n-1][0] + ' ' + H + 'L' + pts[0][0] + ' ' + H + 'Z');
  var cur = root.querySelector('.lc-cursor'), dot = root.querySelector('.lc-dot'), tip = root.querySelector('.lc-tip');
  var svg = root.querySelector('.lc svg');
  svg.addEventListener('pointermove', function(e){
    var r = svg.getBoundingClientRect(), x = (e.clientX - r.left) / r.width * W;
    var best = 0, bd = 1e9;
    pts.forEach(function(p, i){ var dd = Math.abs(p[0] - x); if(dd < bd){ bd = dd; best = i; } });
    var p = pts[best];
    cur.setAttribute('x1', p[0]); cur.setAttribute('x2', p[0]); cur.style.opacity = 1;
    dot.setAttribute('cx', p[0]); dot.setAttribute('cy', p[1]); dot.style.opacity = 1;
    tip.textContent = data[best]; tip.style.left = (p[0] / W * 100) + '%';
    tip.style.top = (p[1] / H * 100) + '%'; tip.style.opacity = 1;
  });
  svg.addEventListener('pointerleave', function(){
    cur.style.opacity = 0; dot.style.opacity = 0; tip.style.opacity = 0;
  });
}''',
    refs=refs('antd', 'shadcn', 'm3'),
    env_notes='无依赖；数据驱动时把 data 换成你的数组即可。',
    demo_hint='在图上移动鼠标',
)

F33 = item(
    id='F33', slug='bar-chart', name='柱状图', cat='06-数据展示', catname='数据展示', diff='★★☆', tag='数据',
    mech='柱子按序错峰生长（每根延迟 55ms），高度用 transform: scaleY 从底部展开（不用 height，避免重排）；'
         '悬停时同组其它柱降到 45% 亮度。',
    params='错峰 55ms · 生长 640ms cubic-bezier(.2,.9,.3,1) · origin bottom · 悬停压暗 0.45',
    verify='柱子从底部向上长（不是从顶部掉下）；悬停时其它柱变暗；数值标注与实际高度一致。',
    steps=['柱容器给固定高度，内部 i 用 height:100% + transform-origin: bottom。'],
    redline=['不许用 height 动画做生长（会触发布局，掉帧）。'],
    fails=[('柱子从中间长出', '没有设 transform-origin', 'transform-origin: bottom')],
    prompt='''做柱状图（6 根，双色区分「本周 / 上周」）。
【生长】每根柱 transform: scaleY(0)→1，transform-origin: bottom，640ms cubic-bezier(.2,.9,.3,1)，
逐根延迟 55ms；柱顶数值淡入延迟到该柱长完后。
【交互】悬停某根柱：该柱提亮 + 顶部显示数值气泡；同组其它柱 opacity 0.45。
【自检】柱子从底部生长；6 根全部长完约 1s；悬停不会让布局抖动（用 outline 不用 border）。''',
    html='''<div class="bc2" id="bc2"></div>
<button class="btn bc2-again">重播</button>
<div class="cap">错峰 55ms，从底部长出</div>''',
    css='''.dz .bc2{display:flex;align-items:flex-end;gap:9px;height:104px;padding:0 4px 16px;position:relative}
.dz .bc2 .bar{position:relative;width:22px;height:100%;display:flex;align-items:flex-end;cursor:pointer}
.dz .bc2 .bar i{display:block;width:100%;border-radius:5px 5px 2px 2px;transform-origin:bottom;
  transform:scaleY(0);background:linear-gradient(180deg,#9dccff,#4a86c9);
  transition:opacity .18s,filter .18s}
.dz .bc2 .bar:nth-child(even) i{background:linear-gradient(180deg,#5fdbA8,#2c8f6b)}
.dz .bc2 .bar span{position:absolute;bottom:-14px;left:50%;transform:translateX(-50%);font-size:8.5px;color:var(--dim);white-space:nowrap}
.dz .bc2 .bar b{position:absolute;top:-13px;left:50%;transform:translateX(-50%);font-size:9px;color:var(--acc);opacity:0;transition:opacity .18s}
.dz .bc2:hover .bar i{opacity:.45}
.dz .bc2 .bar:hover i{opacity:1;filter:brightness(1.15)}
.dz .bc2 .bar:hover b{opacity:1}
.dz .bc2-again{height:24px;padding:0 10px;font-size:10px;margin-top:4px}''',
    js='''function(root){
  var box = root.querySelector('#bc2');
  var data = [['一', 46], ['二', 68], ['三', 38], ['四', 84], ['五', 57], ['六', 72]];
  function build(){
    box.innerHTML = data.map(function(d){
      return '<div class="bar"><b>' + d[1] + '</b><i></i><span>周' + d[0] + '</span></div>';
    }).join('');
    var is = [...box.querySelectorAll('.bar i')];
    is.forEach(function(el, i){
      el.style.height = data[i][1] + '%';
      el.style.transition = 'transform .64s cubic-bezier(.2,.9,.3,1) ' + (i*55) + 'ms';
      requestAnimationFrame(function(){ el.style.transform = 'scaleY(1)'; });
    });
  }
  build();
  root.querySelector('.bc2-again').addEventListener('click', function(){
    var is = [...box.querySelectorAll('.bar i')];
    is.forEach(function(el){ el.style.transition = 'none'; el.style.transform = 'scaleY(0)'; });
    requestAnimationFrame(build);
  });
}''',
    refs=refs('antd', 'm3'),
    env_notes='无依赖。',
    demo_hint='悬停柱子看数值',
)

F34 = item(
    id='F34', slug='donut-chart', name='环形图', cat='06-数据展示', catname='数据展示', diff='★★★', tag='数据',
    mech='多段弧按占比顺序绘制：每段 stroke-dashoffset 从整周长收紧到自己的可见长度，段间留 3° 间隙；'
         '中心数字同步缓动；悬停某段时该段半径外扩 3px。',
    params='r=26 · 描边 8 · 间隙 3° · 每段 520ms 延迟 90ms · 外扩 3px',
    verify='四段总和为 360°；段间间隙一致；中心数字等于最大占比或总和；悬停只影响当前段。',
    steps=['dasharray = (可见长度, 周长)；dashoffset = -已经占用的长度，实现顺序排列。'],
    redline=['不许每段单独用 rotate 堆叠（悬停外扩会错位）。'],
    fails=[('段间无间隙', '没有扣减间隙角度', '每段可见角度 = 占比×360 - 3')],
    prompt='''做环形图（4 段，占比 38 / 27 / 20 / 15）。
【结构】SVG r=26、stroke-width 8、圆头端点；从 12 点开始，顺时针排列；
每段用 stroke-dasharray = (段长, 周长)、stroke-dashoffset = -前段累计，段间留 3° 间隙。
【动效】打开时每段从整周长收紧到自身长度（520ms，逐段延迟 90ms）；中心数字从 0 缓动到 38%。
【交互】悬停某段：该段 stroke-width 8→11 + 轻微外扩，其它段降到 40% 不透明；离开复原。
【自检】四段合计 360°；间隙均匀；悬停不改变整体外框尺寸。''',
    html='''<div class="dn">
  <svg viewBox="0 0 72 72" width="112" height="112">
    <circle cx="36" cy="36" r="26" fill="none" stroke="rgba(255,255,255,.07)" stroke-width="8"/>
  </svg>
  <div class="dn-c"><b class="dn-n">0</b><span>占比 %</span></div>
</div>
<div class="dn-lg"><i style="--c:#9dccff"></i>基础组件<i style="--c:#5fdbA8"></i>布局</div>
<div class="cap">悬停某段会变粗</div>''',
    css='''.dz .dn{position:relative;display:grid;place-items:center}
.dz .dn svg{transform:rotate(-90deg)}
.dz .dn svg circle.seg{transition:stroke-width .2s,opacity .2s;cursor:pointer}
.dz .dn.single svg circle.seg:not(.hot){opacity:.35}
.dz .dn-c{position:absolute;display:flex;flex-direction:column;align-items:center;gap:0}
.dz .dn-c b{font-size:17px;font-weight:800;letter-spacing:-.03em}
.dz .dn-c span{font-size:8.5px;color:var(--dim)}
.dz .dn-lg{display:flex;align-items:center;gap:5px;font-size:9.5px;color:var(--dim);margin-top:6px}
.dz .dn-lg i{width:7px;height:7px;border-radius:2px;background:var(--c);display:inline-block}
.dz .dn-lg i + *{margin-right:6px}''',
    js='''function(root){
  var box = root.querySelector('.dn'), svg = box.querySelector('svg');
  var R = 26, C = 2 * Math.PI * R;
  var segs = [['38', '#9dccff'], ['27', '#5fdbA8'], ['20', '#c9a0ff'], ['15', '#ffb86b']];
  var acc = 0, NS = 'http://www.w3.org/2000/svg';
  segs.forEach(function(s, i){
    var c = document.createElementNS(NS, 'circle');
    var len = parseFloat(s[0]) / 100 * C - 1.34;
    var off = acc;
    c.setAttribute('cx', 36); c.setAttribute('cy', 36); c.setAttribute('r', R);
    c.setAttribute('fill', 'none'); c.setAttribute('stroke', s[1]); c.setAttribute('stroke-width', 8);
    c.setAttribute('stroke-linecap', 'round');
    c.setAttribute('stroke-dasharray', len.toFixed(2) + ' ' + (C - len).toFixed(2));
    c.setAttribute('stroke-dashoffset', (-off).toFixed(2));
    c.setAttribute('class', 'seg');
    c.style.strokeDasharray = C + ' ' + C;
    c.style.strokeDashoffset = C;
    svg.appendChild(c);
    setTimeout(function(){
      c.style.transition = 'stroke-dasharray .52s var(--ease),stroke-dashoffset .52s var(--ease),stroke-width .2s,opacity .2s';
      c.style.strokeDasharray = len.toFixed(2) + ' ' + (C - len).toFixed(2);
      c.style.strokeDashoffset = (-off).toFixed(2);
    }, 120 + i * 90);
    c.addEventListener('pointerenter', function(){
      box.classList.add('single'); c.classList.add('hot');
      c.style.strokeWidth = 11;
    });
    c.addEventListener('pointerleave', function(){
      box.classList.remove('single'); c.classList.remove('hot');
      c.style.strokeWidth = 8;
    });
    acc += parseFloat(s[0]) / 100 * C;
  });
  var num = root.querySelector('.dn-n'), t0 = performance.now();
  function tick(t){
    var p = Math.min(1, (t - t0) / 900), e = 1 - Math.pow(1 - p, 3);
    num.textContent = Math.round(38 * e);
    if(p < 1) requestAnimationFrame(tick);
  }
  requestAnimationFrame(tick);
}''',
    refs=refs('antd', 'shadcn'),
    env_notes='无依赖。',
    demo_hint='悬停某一段',
)

F35 = item(
    id='F35', slug='stat-card', name='数据卡', cat='06-数据展示', catname='数据展示', diff='★★☆', tag='数据',
    mech='数字滚动 + 迷你趋势线：数值用 rAF 从 0 滚到目标（easeOutExpo），趋势线同步描边生长，'
         '变化率用颜色与箭头双重编码（不只靠颜色）。',
    params='滚动 1.1s easeOutExpo · 趋势线 24px 高 · 变化率 ±% 带箭头',
    verify='数字停在精确值（不是近似）；千分位正确；箭头方向与正负一致。',
    steps=['用 Intl.NumberFormat 做千分位；rAF 里只更新 textContent，不触发重排。'],
    redline=['不许只靠颜色表达涨跌（色盲不可读）。'],
    fails=[('数字比 1 万显示成 10000.00', 'toFixed 没配千分位', 'Intl.NumberFormat("zh-CN")')],
    prompt='''做数据卡：标题「本月活跃」+ 数字 12,480 + 变化率 +8.2%（绿）+ 迷你趋势线。
【数字】rAF 1.1s easeOutExpo 从 0 滚到 12480，千分位用 Intl.NumberFormat('zh-CN')；
【趋势线】24px 高的 SVG 折线，pathLength 描边生长 1s，末端一个脉冲点。
【变化率】+8.2% 用绿色 + ↑ 箭头（箭头与颜色双重编码）；负值时红色 + ↓。
【自检】最终值精确 12,480；千分位正确；箭头与符号一致；卡内无溢出。''',
    html='''<div class="st">
  <div class="st-h">本月活跃 <em>↑ 8.2%</em></div>
  <div class="st-n" data-v="12480">0</div>
  <svg class="st-sp" viewBox="0 0 120 26" preserveAspectRatio="none">
    <path d="M2 22 L20 18 L38 20 L56 12 L74 14 L92 7 L116 4" pathLength="1"/>
  </svg>
  <div class="st-f">较上月 <b>+946</b></div>
</div>
<div class="cap">数字滚动 + 趋势描边</div>''',
    css='''.dz .st{width:200px;padding:12px;border-radius:13px;border:1px solid var(--line);background:var(--card)}
.dz .st-h{font-size:10px;color:var(--dim);display:flex;align-items:center;gap:6px}
.dz .st-h em{font-style:normal;color:var(--ok);font-size:9.5px;background:rgba(95,219,168,.14);
  padding:1px 5px;border-radius:5px}
.dz .st-n{font-size:25px;font-weight:800;letter-spacing:-.04em;margin:5px 0 2px;font-variant-numeric:tabular-nums}
.dz .st-sp{width:100%;height:26px;display:block}
.dz .st-sp path{fill:none;stroke:var(--ok);stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round;
  stroke-dasharray:1;stroke-dashoffset:1;animation:lcDraw 1s .1s var(--ease) forwards}
.dz .st-f{font-size:9.5px;color:var(--dim);margin-top:4px}
.dz .st-f b{color:var(--soft)}''',
    js='''function(root){
  var el = root.querySelector('.st-n'), target = +el.dataset.v;
  var fmt = new Intl.NumberFormat('zh-CN');
  var t0 = performance.now();
  function step(t){
    var p = Math.min(1, (t - t0) / 1100);
    var e = p === 1 ? 1 : 1 - Math.pow(2, -10 * p);
    el.textContent = fmt.format(Math.round(target * e));
    if(p < 1) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
}''',
    refs=refs('shadcn', 'antd', 'm3'),
    env_notes='无依赖。',
    demo_hint='数字从 0 滚到 12,480',
)

F36 = item(
    id='F36', slug='table', name='数据表格', cat='06-数据展示', catname='数据展示', diff='★★☆', tag='数据',
    mech='表头吸顶 + 行错峰入场 + 排序指示器；行高 34、粘性表头带描边阴影（滚动时才出现）。',
    params='行高 34 · 入场 240ms 错峰 28ms · 表头 shadow 在 scrollTop>2 时出现',
    verify='表头始终可见；排序箭头切换正确；行入场不导致表头抖动。',
    steps=['用 position: sticky 的表头 + 容器滚动；滚动时给表头加 class 切阴影。'],
    redline=['不许用 <table> 的 border-collapse 配合 sticky（部分浏览器 sticky 失效）。'],
    fails=[('表头随页面滚走', 'sticky 的父级 overflow: auto 但表头不在滚动容器内', '表头放在滚动容器里并加背景色')],
    prompt='''做数据表格：5 列（名称 / 分类 / 状态 / 更新 / 操作），6 行。
【样式】行高 34、表头 10.5px 大写字距、斑马纹极弱（3%）、状态用色点 + 文字；
【行为】表头 position:sticky top:0 且不透明；容器 scrollTop>2 时给表头加深阴影；
点击「更新」列排序，箭头升/降切换；行入场 opacity+translateY(6px)，逐行 28ms 延迟。
【自检】表头滚动时始终遮住内容；排序结果正确；行入场不引起横向抖动。''',
    html='''<div class="tb2"><div class="tb2-sc">
  <table>
    <thead><tr><th>名称</th><th>分类</th><th>状态</th><th class="srt">更新 ›</th></tr></thead>
    <tbody id="tb2b"></tbody>
  </table>
</div></div>
<div class="cap">点「更新」排序</div>''',
    css='''.dz .tb2{width:262px}
.dz .tb2-sc{max-height:126px;overflow:auto;border-radius:11px;border:1px solid var(--line);background:var(--card);
  scrollbar-width:thin}
.dz table{width:100%;border-collapse:separate;border-spacing:0;font-size:10.5px}
.dz thead th{position:sticky;top:0;z-index:2;background:#161f28;font-weight:500;color:var(--dim);
  font-size:9.5px;letter-spacing:.06em;text-align:left;padding:6px 9px;transition:box-shadow .2s}
.dz thead th.srt{cursor:pointer;color:var(--acc)}
.dz .tb2-sc.sc thead th{box-shadow:0 1px 0 rgba(255,255,255,.1),0 6px 12px rgba(0,0,0,.35)}
.dz tbody td{padding:0 9px;height:30px;border-top:1px solid rgba(255,255,255,.06);color:var(--soft);white-space:nowrap}
.dz tbody tr{opacity:0;transform:translateY(6px);animation:tbIn .24s var(--ease) forwards}
@keyframes tbIn{to{opacity:1;transform:none}}
.dz .dot{display:inline-block;width:5px;height:5px;border-radius:50%;margin-right:4px;vertical-align:1px}
.dz .dot.on{background:var(--ok)}.dz .dot.off{background:var(--dim)}''',
    js='''function(root){
  var body = root.querySelector('#tb2b'), sc = root.querySelector('.tb2-sc');
  var rows = [['按钮组','基础','启用','10-28'],['抽屉导航','导航','启用','10-27'],
              ['环形图','图表','草稿','10-26'],['骨架屏','反馈','启用','10-24'],
              ['瀑布流','布局','启用','10-22'],['底部面板','反馈','草稿','10-20']];
  var asc = false;
  function draw(){
    rows.sort(function(a,b){ return asc ? (a[3] < b[3] ? -1 : 1) : (a[3] > b[3] ? -1 : 1); });
    body.innerHTML = rows.map(function(r, i){
      return '<tr style="animation-delay:' + (i*28) + 'ms"><td>' + r[0] + '</td><td>' + r[1] + '</td>' +
        '<td><i class="dot ' + (r[2]==='启用'?'on':'off') + '"></i>' + r[2] + '</td><td>' + r[3] + '</td></tr>';
    }).join('');
  }
  draw();
  root.querySelector('.srt').addEventListener('click', function(){
    asc = !asc; this.textContent = asc ? '更新 ˄' : '更新 ˅'; draw();
  });
  sc.addEventListener('scroll', function(){ sc.classList.toggle('sc', sc.scrollTop > 2); });
}''',
    refs=refs('antd', 'shadcn', 'm3'),
    env_notes='无依赖。',
    demo_hint='滚一下、点一下排序',
)

F37 = item(
    id='F37', slug='timeline', name='时间线', cat='06-数据展示', catname='数据展示', diff='★★☆', tag='数据',
    mech='左侧竖线随滚动生长：线用 scaleY 从 0 长到当前可见进度，节点在进入视口 20% 时点亮并弹一下。',
    params='线宽 2 · 节点 9px · 点亮 320ms 弹簧 · 触发线 20%',
    verify='滚动时线只长不缩（除非向上滚）；节点点亮一次不重复；末端节点有强调色。',
    steps=['用 IntersectionObserver 触发点亮，线的进度用 scroll 事件的 rAF 节流更新。'],
    redline=['不许动画从下往上长（违背时间方向）。'],
    fails=[('节点反复闪', '每次 scroll 都重放动画', '用 once 标记')],
    prompt='''做时间线：5 个节点（版本 v1.0 → v1.4），左侧竖线 + 圆点 + 右侧卡片。
【生长】竖线 transform: scaleY 从 0 到当前进度（transform-origin: top），随容器滚动更新；
【点亮】节点进入视口 20% 时圆点放大 1→1.35→1（320ms 弹簧），卡片淡入上移 6px；
【样式】最新节点用主题色 + 发光，旧节点灰色；卡片显示版本、日期、两条变更。
【自检】向下滚线只长不缩；节点只点亮一次；向上滚不重放。''',
    html='''<div class="tl"><div class="tl-sc">
  <div class="tl-line"><i></i></div>
  <div class="tl-list" id="tlList"></div>
</div></div>
<div class="cap">在框里向下滚</div>''',
    css='''.dz .tl{width:250px}
.dz .tl-sc{position:relative;max-height:132px;overflow:auto;padding:2px 0 2px 0;scrollbar-width:none}
.dz .tl-sc::-webkit-scrollbar{display:none}
.dz .tl-line{position:absolute;left:5px;top:6px;bottom:6px;width:2px;background:rgba(255,255,255,.09);border-radius:2px}
.dz .tl-line i{display:block;width:100%;height:100%;transform-origin:top;transform:scaleY(0);
  background:linear-gradient(180deg,#9dccff,#5fdbA8);border-radius:2px;transition:transform .12s linear}
.dz .tl-list{position:relative;padding-left:18px}
.dz .tl-i{position:relative;padding:0 0 12px}
.dz .tl-i::before{content:"";position:absolute;left:-16.5px;top:4px;width:7px;height:7px;border-radius:50%;
  background:#2a3846;border:1.5px solid #3d4d5e;transition:.3s var(--spring);transform:scale(1)}
.dz .tl-i.on::before{background:var(--acc);border-color:var(--acc);transform:scale(1.35);
  box-shadow:0 0 0 3px rgba(157,204,255,.16)}
.dz .tl-i:last-child::before{background:var(--ok);border-color:var(--ok)}
.dz .tl-i div{opacity:0;transform:translateY(6px);transition:.32s var(--ease)}
.dz .tl-i.on div{opacity:1;transform:none}
.dz .tl-v{font-size:11px;font-weight:700}
.dz .tl-d{font-size:9px;color:var(--dim);margin:1px 0 2px}
.dz .tl-c{font-size:9.5px;color:var(--soft);line-height:1.55}''',
    js='''function(root){
  var list = root.querySelector('#tlList'), sc = root.querySelector('.tl-sc'), line = root.querySelector('.tl-line i');
  var items = [['v1.4','2026-10-28','把引用方案移植进素材库'],['v1.3','2026-10-20','新增 8 个分类 46 条素材'],
    ['v1.2','2026-10-11','玻璃渲染 4-pass 优化'],['v1.1','2026-09-30','原生桥：剪贴板 / 分享'],
    ['v1.0','2026-09-18','首个可安装 APK']];
  list.innerHTML = items.map(function(it){
    return '<div class="tl-i"><div><div class="tl-v">' + it[0] + '</div><div class="tl-d">' + it[1] +
      '</div><div class="tl-c">' + it[2] + '</div></div></div>';
  }).join('');
  var els = [...list.querySelectorAll('.tl-i')];
  if(window.IntersectionObserver){
    var io = new IntersectionObserver(function(es){
      es.forEach(function(e){
        if(e.isIntersecting && !e.target.dataset.once){
          e.target.dataset.once = '1'; e.target.classList.add('on');
        }
      });
    }, {root: sc, threshold: .2});
    els.forEach(function(e){ io.observe(e); });
  } else { els.forEach(function(e){ e.classList.add('on'); }); }
  function up(){
    var r = sc.getBoundingClientRect(), h = sc.scrollHeight, total = Math.max(1, h - r.height);
    var p = Math.min(1, (sc.scrollTop + r.height * .55) / total + .18);
    line.style.transform = 'scaleY(' + p.toFixed(3) + ')';
  }
  sc.addEventListener('scroll', up, {passive:true});
  up();
}''',
    refs=refs('m3', 'antd', 'shadcn'),
    env_notes='无依赖。',
    demo_hint='滚动点亮节点',
)

add(F32, F33, F34, F35, F36, F37)
