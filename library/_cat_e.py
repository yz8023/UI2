# -*- coding: utf-8 -*-
"""F38–F42：动效"""
from _cat_base import item, add, refs

F38 = item(
    id='F38', slug='spring-drag', name='弹簧拖拽', cat='07-动效', catname='动效', diff='★★★', tag='动效',
    mech='真正的弹簧积分（不是 CSS 过渡猜的）：每帧 v += (目标-当前)×刚度×dt - v×阻尼×dt，'
         '松手后靠速度自然回弹；拖拽时记录指针速度作为初始速度，甩出去才有惯性。',
    params='刚度 k=170 · 阻尼 c=18 · dt 上限 1/30s · 甩出速度 = 最近 60ms 平均',
    verify='拿到 60fps（无掉帧）；松手回弹不振荡超过 2 次；快速甩出有明显过冲。',
    steps=['每帧读 dt 并 clamp(1/120, 1/30)，避免切后台回来时炸开。',
           '速度用最近 5 个指针采样做时间加权平均，避免最后一帧抖动影响手感。'],
    redline=['不许用 CSS transition 假装弹簧（无法带上初始速度）。'],
    fails=[('回弹抽搐', '没有按 dt 积分（按帧数）', 'v += a*dt，且 dt 夹紧')],
    prompt='''做一个可拖拽的球，用真正的弹簧物理回位。
【物理】每帧：a = -k*(x - target) - c*v；v += a*dt；x += v*dt；k=170、c=18，dt 夹在 1/120~1/30。
【拖拽】pointerdown 抓取，move 时直接把 x 设为指针位置并记录速度（最近 60ms 的平均），松手时把该速度注入 v。
【易用】限制在容器内，越界时给 target 加软约束（回弹）。
【自检】松手后停在目标点；回弹过冲不超过 2 次；快速甩出能看到明显惯性；切后台回来不炸。''',
    html='''<div class="sd"><div class="sd-ball"></div><div class="sd-tgt"></div></div>
<div class="sd-meta"><span>v = <b class="sd-v">0</b></span><span>k=170 c=18</span></div>
<div class="cap">拖它，然后甩出去</div>''',
    css='''.dz .sd{position:relative;width:250px;height:104px;border-radius:12px;background:rgba(255,255,255,.04);
  border:1px dashed rgba(255,255,255,.14);overflow:hidden;touch-action:none}
.dz .sd-ball{position:absolute;left:8px;top:8px;width:30px;height:30px;border-radius:50%;
  background:radial-gradient(circle at 32% 28%,#cfe6ff,#79b4f0 55%,#2f6dab);
  box-shadow:0 6px 16px rgba(60,140,220,.45),inset 0 -2px 6px rgba(0,0,0,.25);cursor:grab;will-change:transform}
.dz .sd-ball.grab{cursor:grabbing;box-shadow:0 10px 22px rgba(60,140,220,.6),inset 0 -2px 6px rgba(0,0,0,.25)}
.dz .sd-tgt{position:absolute;left:8px;top:8px;width:30px;height:30px;border-radius:50%;
  border:1.5px dashed rgba(157,204,255,.45)}
.dz .sd-meta{display:flex;gap:14px;font-size:9.5px;color:var(--dim);margin-top:6px;font-variant-numeric:tabular-nums}
.dz .sd-meta b{color:var(--acc);font-weight:600}''',
    js='''function(root){
  var box = root.querySelector('.sd'), ball = root.querySelector('.sd-ball'),
      tgt = root.querySelector('.sd-tgt'), vEl = root.querySelector('.sd-v');
  var W = 0, H = 0, BS = 30, k = 170, c = 18;
  var x = 8, y = 8, vx = 0, vy = 0, tx = 8, ty = 8;
  var dragging = false, last = 0, samples = [], raf = 0;
  function measure(){
    W = box.clientWidth; H = box.clientHeight;
    tx = 8; ty = 8;
  }
  measure();
  var ro = window.ResizeObserver ? new ResizeObserver(measure) : null; if(ro) ro.observe(box);
  function step(t){
    var dt = Math.min(1/30, Math.max(1/120, (t - (last || t)) / 1000)); last = t;
    if(!dragging){
      var ax = -k * (x - tx) - c * vx, ay = -k * (y - ty) - c * vy;
      vx += ax * dt; vy += ay * dt;
      x += vx * dt; y += vy * dt;
      if(Math.abs(vx) < .02 && Math.abs(vx) && Math.abs(x - tx) < .3) { x = tx; vx = 0; }
      if(Math.abs(vy) < .02 && Math.abs(y - ty) < .3) { y = ty; vy = 0; }
    }
    ball.style.transform = 'translate3d(' + x.toFixed(2) + 'px,' + y.toFixed(2) + 'px,0)';
    vEl.textContent = Math.round(Math.hypot(vx, vy));
    raf = requestAnimationFrame(step);
  }
  raf = requestAnimationFrame(step);
  ball.addEventListener('pointerdown', function(e){
    dragging = true; ball.classList.add('grab'); ball.setPointerCapture(e.pointerId);
    samples = [{t: performance.now(), x: x, y: y}];
  });
  ball.addEventListener('pointermove', function(e){
    if(!dragging) return;
    var r = box.getBoundingClientRect();
    x = Math.max(0, Math.min(W - BS, e.clientX - r.left - BS/2));
    y = Math.max(0, Math.min(H - BS, e.clientY - r.top - BS/2));
    var now = performance.now();
    samples.push({t: now, x: x, y: y});
    while(samples.length > 6) samples.shift();
  });
  ball.addEventListener('pointerup', function(){
    dragging = false; ball.classList.remove('grab');
    var now = performance.now(), old = samples.find(function(s){ return now - s.t < 90; }) || samples[0];
    if(old && now - old.t > 8){
      vx = (x - old.x) / (now - old.t) * 1000;
      vy = (y - old.y) / (now - old.t) * 1000;
      vx = Math.max(-1800, Math.min(1800, vx)); vy = Math.max(-1800, Math.min(1800, vy));
    }
  });
}''',
    refs=refs('motion', 'motionweb', 'radix'),
    env_notes='无依赖；这就是 Framer Motion / react-spring 的物理内核（k/c 换算成 stiffness/damping）。',
    demo_hint='拖小球甩出去',
)

F39 = item(
    id='F39', slug='staggered-reveal', name='错峰入场', cat='07-动效', catname='动效', diff='★★☆', tag='动效',
    mech='列表错峰：每项延迟 = index × 40ms，位移 14px + 透明度，用 cubic-bezier(.2,.9,.3,1.12) 收尾带回弹；'
         '同一批只播一次，滚动进入视口时触发。',
    params='单次 420ms · 错峰 40ms · 位移 14px · 上限 12 项（超过后延迟封顶）',
    verify='元素在视口内才播；超过 12 项不会越来越慢；重播按钮能把状态清干净。',
    steps=['用 IntersectionObserver 加 once 标记；延迟 index*40 但 clamp 到 480ms。'],
    redline=['不许给每一项都用同一个长延迟（用户会觉得卡）。'],
    fails=[('刷新后空白', '动画依赖初始 opacity:0 但没触发', '用 easing both + IO 兜底')],
    prompt='''做错峰入场列表（9 项）。
【动效】每项 opacity 0→1、translateY(14px)→0，420ms cubic-bezier(.2,.9,.3,1.12)，逐项延迟 40ms
（超过 12 项后延迟封顶在 480ms，避免长列表尾巴太长）。
【触发】进入视口 15% 才播，且只播一次；提供「重播」按钮。
【自检】首项与末项延迟差正确；重播无残留；滚动回来不重放。''',
    html='''<div class="sr" id="sr"></div>
<button class="btn sr-again">重播</button>
<div class="cap">逐项 40ms 错峰</div>''',
    css='''.dz .sr{display:flex;flex-direction:column;gap:5px;width:230px}
.dz .sr-i{display:flex;align-items:center;gap:7px;padding:5px 9px;border-radius:9px;background:var(--card);
  border:1px solid var(--line);font-size:10.5px;color:var(--soft);opacity:0;transform:translateY(14px)}
.dz .sr-i.go{animation:srIn .42s cubic-bezier(.2,.9,.3,1.12) forwards}
@keyframes srIn{to{opacity:1;transform:none}}
.dz .sr-i b{width:15px;height:15px;border-radius:5px;display:grid;place-items:center;font-size:8px;
  background:rgba(157,204,255,.16);color:var(--acc);font-weight:700}
.dz .sr-again{height:24px;padding:0 10px;font-size:10px;margin-top:6px}''',
    js='''function(root){
  var box = root.querySelector('#sr');
  var names = ['按钮 Button','输入框 TextField','开关 Switch','滑块 Slider','勾选 Checkbox',
               '头像 Avatar'];
  box.innerHTML = names.map(function(n, i){
    return '<div class="sr-i"><b>' + (i+1) + '</b>' + n + '</div>';
  }).join('');
  function play(){
    var els = [...box.children];
    els.forEach(function(el, i){
      el.classList.remove('go');
      void el.offsetWidth;
      el.style.animationDelay = Math.min(i * 40, 480) + 'ms';
      el.classList.add('go');
    });
  }
  var io = window.IntersectionObserver ? new IntersectionObserver(function(es){
    es.forEach(function(e){ if(e.isIntersecting){ play(); io.disconnect(); } });
  }, {threshold: .15}) : null;
  if(io) io.observe(box); else play();
  root.querySelector('.sr-again').addEventListener('click', play);
}''',
    refs=refs('motion', 'motionweb', 'm3'),
    env_notes='无依赖。',
    demo_hint='点重播看错峰',
)

F40 = item(
    id='F40', slug='swipe-card', name='手势卡片', cat='07-动效', catname='动效', diff='★★★', tag='动效',
    mech='滑动卡片的双阶段判定：拖拽时卡片旋转 = 位移×0.05、遮罩左右两色透明度随位移变化；'
         '超过阈值飞出并复位下一张；未超过则弹簧回位。',
    params='旋转系数 0.05 · 飞出阈值 80px · 飞出 340ms · 阈值内回弹 k=200 c=22',
    verify='拖拽时左右标记正确；甩飞后下一张顶上；连续甩 3 张不重叠。',
    steps=['栈内每张卡按 index 反向偏移（translateY 8px×i, scale 1-0.04×i）营造层次。'],
    redline=['不许只做一个方向（左右都要有语义）。'],
    fails=[('卡片飞出后空白', '没有把飞出卡移到栈底', '飞出结束 appendChild 到末尾并复位 transform')],
    prompt='''做可滑动卡片（3 张），左滑「跳过」绿，右滑「收藏」蓝。
【拖拽】pointermove 时卡片跟着走，旋转 = dx*0.05 度；左/右标记透明度 = |dx|/100；
背后两张卡按 index 反向偏移（translateY 8*i、scale 1-0.04*i）形成层次。
【判定】|dx|>80 飞出（340ms，位移到 ±140%），否则 340ms 弹簧回位（k=200/c=22）。
【自检】连甩 3 张都有下一张顶上；飞出后卡片被移到栈底并复位；旋转不超过 ±18°。''',
    html='''<div class="sw"><div class="sw-stack" id="swStack"></div></div>
<div class="sw-tip">拖动卡片 · 超过 80px 飞出</div>''',
    css='''.dz .sw{position:relative;width:170px;height:112px;margin-bottom:6px}
.dz .sw-card{position:absolute;inset:0;border-radius:13px;padding:11px;overflow:hidden;
  background:linear-gradient(155deg,#223243,#16202a);border:1px solid var(--line2);
  box-shadow:0 14px 30px rgba(0,0,0,.5);cursor:grab;touch-action:none;will-change:transform}
.dz .sw-card:nth-child(1){z-index:3}.dz .sw-card:nth-child(2){z-index:2}.dz .sw-card:nth-child(3){z-index:1}
.dz .sw-card h4{font-size:12px;margin-bottom:3px}
.dz .sw-card p{font-size:9.5px;color:var(--dim);line-height:1.55}
.dz .sw-tag{position:absolute;top:9px;font-size:10px;font-weight:800;letter-spacing:.1em;padding:2px 6px;
  border-radius:5px;border:1.5px solid;opacity:0}
.dz .sw-tag.no{left:9px;color:#ff9a9a;border-color:#ff9a9a;transform:rotate(-8deg)}
.dz .sw-tag.yes{right:9px;color:#9dccff;border-color:#9dccff;transform:rotate(8deg)}
.dz .sw-tip{font-size:9.5px;color:var(--dim)}''',
    js='''function(root){
  var stack = root.querySelector('#swStack');
  var data = [['液态玻璃','4-pass 折射 + 色散 + 菲涅尔高光'],
              ['错峰入场','40ms 步进 + 回弹曲线'],
              ['弹簧拖拽','按 dt 积分，注入甩出速度']];
  data.forEach(function(d, i){
    var el = document.createElement('div');
    el.className = 'sw-card'; el.dataset.i = i;
    el.innerHTML = '<span class="sw-tag no">跳过</span><span class="sw-tag yes">收藏</span>' +
      '<h4>' + d[0] + '</h4><p>' + d[1] + '</p>';
    stack.appendChild(el);
  });
  var cards = [...stack.children];
  function layout(){
    cards.forEach(function(c, i){
      c.style.transition = 'transform .34s var(--spring)';
      c.style.transform = 'translateY(' + (i*8) + 'px) scale(' + (1 - i*0.04) + ')';
      c.style.opacity = i > 2 ? 0 : 1;
      c.style.zIndex = 10 - i;
      var no = c.querySelector('.no'), yes = c.querySelector('.yes');
      no.style.opacity = 0; yes.style.opacity = 0;
    });
  }
  layout();
  var sx = 0, dx = 0, drag = null;
  stack.addEventListener('pointerdown', function(e){
    var c = cards[0];
    if(!c || !c.contains(e.target)) return;
    drag = c; sx = e.clientX; dx = 0;
    c.style.transition = 'none'; c.setPointerCapture(e.pointerId);
  });
  window.addEventListener('pointermove', function(e){
    if(!drag) return;
    dx = e.clientX - sx;
    var rot = Math.max(-18, Math.min(18, dx * .05));
    drag.style.transform = 'translate(' + dx + 'px,' + (Math.abs(dx) * .04) + 'px) rotate(' + rot + 'deg)';
    drag.querySelector('.no').style.opacity = Math.max(0, -dx / 100);
    drag.querySelector('.yes').style.opacity = Math.max(0, dx / 100);
  });
  window.addEventListener('pointerup', function(){
    if(!drag) return;
    var c = drag; drag = null;
    if(Math.abs(dx) > 80){
      c.style.transition = 'transform .34s cubic-bezier(.3,.9,.3,1),opacity .34s';
      c.style.transform = 'translate(' + (dx > 0 ? 150 : -150) + '%,0) rotate(' + (dx > 0 ? 18 : -18) + 'deg)';
      c.style.opacity = 0;
      setTimeout(function(){
        cards.push(cards.shift());
        layout();
      }, 340);
    } else {
      layout();
    }
    dx = 0;
  });
}''',
    refs=refs('motion', 'ionic', 'motionweb'),
    env_notes='无依赖。',
    demo_hint='左拖或右拖卡片',
)

F41 = item(
    id='F41', slug='page-transition', name='页面转场', cat='07-动效', catname='动效', diff='★★☆', tag='动效',
    mech='共享元素转场（简化版）：缩略图先飞到详情位置（FLIP），页面内容随后淡入；返回时反向飞回。'
         'FLIP 用 getBoundingClientRect 前后差值 + transform 反推，避免重排。',
    params='飞行 380ms cubic-bezier(.3,.9,.3,1) · 内容淡入延迟 120ms · 背景遮罩 220ms',
    verify='缩略图起点与终点语义正确；飞行中不模糊；返回后缩略图回到原位。',
    steps=['FLIP：记录 before rect，切换布局，读 after rect，再用 transform 补差 + transition 归零。'],
    redline=['不许用两个 DOM 复制品互相淡入淡出假装共享元素。'],
    fails=[('飞行中变形拉伸', '同时改 width/height 且没设 object-fit', '用 transform: scale 而非宽高动画')],
    prompt='''做共享元素转场：列表里一个小卡片，点击后放大飞入详情页。
【FLIP】点击时记录卡片 rect，切到详情布局，读详情容器 rect，用 transform: translate+scale 把详情
"放"回原位，next frame 归零 transition 380ms cubic-bezier(.3,.9,.3,1)；详情内容 120ms 后淡入。
【返回】反向飞行，结束后显示列表卡片；背景遮罩 220ms 淡入。
【自检】飞行过程无拉伸变形；连续进入/返回 5 次不错位；Esc 可返回。''',
    html='''<div class="pt">
  <div class="pt-list"><div class="pt-thumb"><b>玻璃</b><span>4-pass</span></div>
    <div class="pt-thumb2">弹簧拖拽 · 错峰入场</div></div>
  <div class="pt-detail"><div class="pt-dt">液态玻璃<small>SDF + 折射 + 色散 + 菲涅尔</small></div>
    <div class="pt-back">‹ 返回</div></div>
</div>
<div class="cap">点卡片进入，点「返回」退出</div>''',
    css='''.dz .pt{position:absolute;inset:0;overflow:hidden}
.dz .pt-list{padding:12px;display:flex;flex-direction:column;gap:8px}
.dz .pt-thumb{width:76px;height:52px;border-radius:10px;cursor:pointer;
  background:linear-gradient(150deg,#2d5473,#16222d);border:1px solid var(--line2);
  display:flex;flex-direction:column;justify-content:flex-end;padding:6px;font-size:10px;font-weight:700}
.dz .pt-thumb span{font-size:8px;color:rgba(255,255,255,.6);font-weight:400}
.dz .pt-thumb2{border-radius:9px;background:rgba(255,255,255,.05);border:1px solid var(--line);
  padding:9px;font-size:10px;color:var(--dim)}
.dz .pt-detail{position:absolute;inset:0;background:#0d141b;opacity:0;pointer-events:none;
  transition:opacity .2s;padding:12px;z-index:5}
.dz .pt-detail.on{opacity:1;pointer-events:auto}
.dz .pt-dt{width:100%;height:100%;border-radius:12px;padding:14px;font-size:14px;font-weight:800;
  background:linear-gradient(150deg,#2d5473,#16222d);border:1px solid var(--line2);
  transform-origin:top left}
.dz .pt-dt small{display:block;font-size:10px;font-weight:400;color:rgba(255,255,255,.65);margin-top:4px}
.dz .pt-back{position:absolute;left:12px;top:8px;font-size:10.5px;color:var(--acc);cursor:pointer;
  background:rgba(0,0,0,.35);padding:3px 8px;border-radius:7px}''',
    js='''function(root){
  var thumb = root.querySelector('.pt-thumb'), detail = root.querySelector('.pt-detail'),
      dt = root.querySelector('.pt-dt'), back = root.querySelector('.pt-back');
  function flip(from, to, done){
    var a = from.getBoundingClientRect(), b = to.getBoundingClientRect();
    var sx = a.width / b.width, sy = a.height / b.height;
    var tx = a.left - b.left, ty = a.top - b.top;
    to.style.transition = 'none';
    to.style.transform = 'translate(' + tx + 'px,' + ty + 'px) scale(' + sx.toFixed(4) + ',' + sy.toFixed(4) + ')';
    requestAnimationFrame(function(){
      to.style.transition = 'transform .38s cubic-bezier(.3,.9,.3,1)';
      to.style.transform = 'none';
    });
  }
  thumb.addEventListener('click', function(){
    detail.classList.add('on');
    flip(thumb, dt);
  });
  back.addEventListener('click', function(){
    flip(thumb, dt);
    setTimeout(function(){ detail.classList.remove('on'); }, 300);
  });
}''',
    refs=refs('motion', 'm3', 'motionweb'),
    env_notes='无依赖；真实项目里返回手势也能接同一个 flip 函数。',
    demo_hint='点小卡片',
)

F42 = item(
    id='F42', slug='scroll-parallax', name='滚动视差', cat='07-动效', catname='动效', diff='★★☆', tag='动效',
    mech='多层视差 + 帧内归一化：每层 translateY = 滚动量 × 系数，系数用 data 属性声明；'
         '所有更新在一次 rAF 里完成，读一次 scrollY 写多份 transform。',
    params='层系数 0.15 / 0.35 / 0.6 · rAF 单帧批处理 · 惯性 0.12',
    verify='滚到底部时层间位移关系正确；无掉帧；反向滚动对称。',
    steps=['读写在 rAF 里分离：先读 scrollY，再统一写 style.transform。'],
    redline=['不许在 scroll 回调里读 offsetTop（强制同步布局，必掉帧）。'],
    fails=[('滚动卡顿', '每层都 layout 一次', '批量读写 + will-change: transform')],
    prompt='''做滚动视差：一个可滚动区域，背景 3 层（远山/中景/近景）以不同速度平移。
【系数】远 0.15、中 0.35、近 0.6；滚动时每层 translateY = -scrollTop * 系数。
【性能】所有更新在同一个 rAF 内完成，先读后写；层加 will-change: transform。
【自检】滚动时无卡顿（Chrome Performance 面板 60fps）；到底部时层间差距肉眼明显；反向滚动一致。''',
    html='''<div class="px"><div class="px-sc" id="pxSc">
  <div class="px-layer far"></div><div class="px-layer mid"></div><div class="px-layer near"></div>
  <div class="px-txt">向下滚动<br><small>三层视差 · rAF 批处理</small></div>
  <div class="px-fill"></div>
</div></div>
<div class="cap">在框里滚动</div>''',
    css='''.dz .px{position:absolute;inset:0;overflow:hidden}
.dz .px-sc{position:absolute;inset:0;overflow:auto;scrollbar-width:none}
.dz .px-sc::-webkit-scrollbar{display:none}
.dz .px-layer{position:absolute;left:-10%;right:-10%;height:120px;will-change:transform}
.dz .px-layer.far{top:0;background:radial-gradient(120% 80% at 30% 100%,rgba(157,204,255,.16),transparent 70%)}
.dz .px-layer.mid{top:26px;height:100px;
  background:radial-gradient(100% 70% at 70% 100%,rgba(95,219,168,.16),transparent 70%)}
.dz .px-layer.near{top:52px;height:80px;
  background:radial-gradient(90% 60% at 40% 100%,rgba(201,160,255,.18),transparent 70%)}
.dz .px-txt{position:relative;z-index:2;padding:76px 14px 10px;font-size:13px;font-weight:800;line-height:1.5}
.dz .px-txt small{font-size:9.5px;color:var(--dim);font-weight:400}
.dz .px-fill{height:200px;background:repeating-linear-gradient(180deg,rgba(255,255,255,.05) 0 40px,transparent 40px 52px);
  margin:0 14px 14px;border-radius:10px}''',
    js='''function(root){
  var sc = root.querySelector('#pxSc'), far = root.querySelector('.far'),
      mid = root.querySelector('.mid'), near = root.querySelector('.near');
  var pending = false;
  sc.addEventListener('scroll', function(){
    if(pending) return;
    pending = true;
    requestAnimationFrame(function(){
      var y = sc.scrollTop;
      far.style.transform = 'translate3d(0,' + (y * .15).toFixed(1) + 'px,0)';
      mid.style.transform = 'translate3d(0,' + (y * .35).toFixed(1) + 'px,0)';
      near.style.transform = 'translate3d(0,' + (y * .6).toFixed(1) + 'px,0)';
      pending = false;
    });
  }, {passive:true});
}''',
    refs=refs('motionweb', 'motion'),
    env_notes='无依赖。',
    demo_hint='滚动看三层速度差',
)

add(F38, F39, F40, F41, F42)
