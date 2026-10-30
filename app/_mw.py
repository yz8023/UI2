# -*- coding: utf-8 -*-
"""motion-web 体验馆：20 个配方（可跑）+ 4 个令牌实验室 + 25 篇规范的索引。

配方标题 / What / Use 取自上游 references/pattern-recipes.md 的真实条目；
演示代码是按同样机制重写的，不含上游源码。
"""
from _spec import SPECS, RECIPES

# ─────────────── 20 个配方：[no, 名, html, css, js] ───────────────
DEMOS = {}

DEMOS[1] = ('''
<div class="split"><span class="ln"><i>MOTION</i></span><span class="ln"><i>IS THE</i></span>
<span class="ln"><i>ADVANTAGE</i></span></div>
<div class="cap">点一下重播 · 每行 90ms 错峰</div>''', '''
.mr .split{display:flex;flex-direction:column;gap:3px;align-items:flex-start}
.mr .ln{display:block;overflow:hidden;line-height:.98}
.mr .ln i{display:block;font-style:normal;font-size:30px;font-weight:800;letter-spacing:-.03em;
  transform:translateY(105%);transition:transform .72s cubic-bezier(.16,1,.3,1)}
.mr .ln:nth-child(2) i{transition-delay:.09s}
.mr .ln:nth-child(3) i{transition-delay:.18s}
.mr.go .ln i{transform:none}''', '''
function(root){
  function play(){ root.classList.remove('go'); void root.offsetWidth; root.classList.add('go'); }
  root.addEventListener('click', play);
  play();
}''')

DEMOS[2] = ('''
<button class="mag">把鼠标放上来</button>
<div class="cap">磁吸半径 90px · 最大位移 18px</div>''', '''
.mr .mag{position:relative;height:40px;padding:0 22px;border-radius:99px;font-size:12.5px;font-weight:700;
  color:#06121c;background:linear-gradient(180deg,#cfe3ff,#9dccff);border:0;cursor:pointer;
  transition:transform .18s cubic-bezier(.2,.9,.3,1.15);will-change:transform}''', '''
function(root){
  var b = root.querySelector('.mag');
  root.addEventListener('pointermove', function(e){
    var r = b.getBoundingClientRect(), cx = r.left + r.width/2, cy = r.top + r.height/2;
    var dx = e.clientX - cx, dy = e.clientY - cy, d = Math.hypot(dx, dy), R = 120;
    if(d < R){ var k = (1 - d/R) * .55; b.style.transform = 'translate(' + (dx*k).toFixed(1) + 'px,' + (dy*k).toFixed(1) + 'px)'; }
    else b.style.transform = '';
  });
  root.addEventListener('pointerleave', function(){ b.style.transform = ''; });
}''')

DEMOS[3] = ('''
<div class="cur"><div class="im"></div><div class="im im2"></div></div>
<div class="cap">点一下：clip-path 从 0 开到全开</div>''', '''
.mr .cur{position:relative;width:190px;height:120px;border-radius:12px;overflow:hidden;cursor:pointer}
.mr .im{position:absolute;inset:0;background:linear-gradient(140deg,#2d5f86,#14202b)}
.mr .im2{background:linear-gradient(140deg,#3f7f6a,#5fdba8);clip-path:inset(0 0 100% 0);
  transition:clip-path .9s cubic-bezier(.16,1,.3,1)}
.mr.go .im2{clip-path:inset(0 0 0 0)}''', '''
function(root){
  function play(){ root.classList.remove('go'); void root.offsetWidth; root.classList.add('go'); }
  root.addEventListener('click', play); play();
}''')

DEMOS[4] = ('''
<div class="sk"><div class="sk-in">SCROLL<br>VELOCITY</div></div>
<div class="cap">滚得越快，倾得越多；停下回弹</div>''', '''
.mr .sk{height:120px;display:grid;place-items:center;overflow:hidden}
.mr .sk-in{font-size:26px;font-weight:800;letter-spacing:-.03em;line-height:1;
  transition:transform .16s ease-out;will-change:transform}''', '''
function(root){
  var el = root.querySelector('.sk-in'), last = 0, skew = 0, raf = 0;
  function tick(){
    skew *= .86;
    el.style.transform = 'skewY(' + skew.toFixed(2) + 'deg) scaleY(' + (1 + Math.abs(skew)/90).toFixed(3) + ')';
    if(Math.abs(skew) > .05) raf = requestAnimationFrame(tick);
    else { el.style.transform = ''; raf = 0; }
  }
  root.addEventListener('pointermove', function(e){
    var v = e.clientX - last; last = e.clientX;
    skew = Math.max(-9, Math.min(9, skew - v * .09));
    if(!raf) raf = requestAnimationFrame(tick);
  });
  root.addEventListener('pointerleave', function(){ last = 0; });
}''')

DEMOS[5] = ('''
<div class="rail"><div class="rail-in">
  <div class="c">01</div><div class="c">02</div><div class="c">03</div><div class="c">04</div><div class="c">05</div>
</div></div>
<div class="cap">横向拖动 · 惯性吸附</div>''', '''
.mr .rail{width:220px;overflow:hidden;cursor:grab;touch-action:none}
.mr .rail-in{display:flex;gap:8px;will-change:transform}
.mr .c{flex:0 0 auto;width:74px;height:96px;border-radius:12px;display:grid;place-items:center;
  font-size:18px;font-weight:800;color:rgba(255,255,255,.8);
  background:linear-gradient(150deg,#2b4d6d,#16222d);border:1px solid rgba(255,255,255,.12)}''', '''
function(root){
  var rail = root.querySelector('.rail'), inn = root.querySelector('.rail-in');
  var x = 0, sx = 0, drag = false, vx = 0, lastX = 0, max = 0;
  function clamp(){ max = Math.max(0, inn.scrollWidth - rail.clientWidth); x = Math.max(-max, Math.min(0, x)); }
  function apply(){ inn.style.transform = 'translateX(' + x + 'px)'; }
  rail.addEventListener('pointerdown', function(e){ drag = true; sx = e.clientX; lastX = e.clientX; vx = 0; });
  window.addEventListener('pointermove', function(e){
    if(!drag) return; var dx = e.clientX - lastX; lastX = e.clientX; vx = dx; x += dx; clamp(); apply();
  });
  window.addEventListener('pointerup', function(){
    if(!drag) return; drag = false;
    x += vx * 6; clamp(); inn.style.transition = 'transform .5s cubic-bezier(.16,1,.3,1)'; apply();
    setTimeout(function(){ inn.style.transition = ''; }, 520);
  });
  clamp(); apply();
}''')

DEMOS[6] = ('''
<div class="par"><div class="ly l1"></div><div class="ly l2"></div><div class="ly l3"></div>
<div class="tx">PARALLAX</div></div>
<div class="cap">三层景深 · 0.12 / 0.28 / 0.5</div>''', '''
.mr .par{position:relative;width:210px;height:130px;border-radius:12px;overflow:hidden;background:#0f1822}
.mr .ly{position:absolute;inset:-10% -20%}
.mr .l1{background:radial-gradient(60% 60% at 30% 30%,rgba(126,180,240,.5),transparent 70%)}
.mr .l2{background:radial-gradient(50% 50% at 70% 40%,rgba(95,219,168,.42),transparent 70%)}
.mr .l3{background:radial-gradient(45% 45% at 45% 80%,rgba(201,160,255,.5),transparent 70%)}
.mr .tx{position:absolute;inset:0;display:grid;place-items:center;font-size:15px;font-weight:800;letter-spacing:.1em}''', '''
function(root){
  var ls = [root.querySelector('.l1'), root.querySelector('.l2'), root.querySelector('.l3')];
  var k = [.12, .28, .5];
  root.addEventListener('pointermove', function(e){
    var r = root.getBoundingClientRect(), dx = (e.clientX - r.left) / r.width - .5, dy = (e.clientY - r.top) / r.height - .5;
    ls.forEach(function(l, i){ l.style.transform = 'translate3d(' + (dx * 40 * k[i] * 4).toFixed(1) + 'px,' + (dy * 40 * k[i] * 4).toFixed(1) + 'px,0)'; });
  });
}''')

DEMOS[7] = ('''
<canvas class="trail" width="300" height="210"></canvas>
<div class="cap">移动鼠标 / 手指</div>''', '''
.mr{padding:0}
.mr .trail{width:100%;height:100%;display:block;border-radius:0}''', '''
function(root){
  var c = root.querySelector('.trail'), x = c.getContext('2d'), W = 300, H = 210;
  var pts = [], mx = 150, my = 105, on = false;
  root.addEventListener('pointermove', function(e){
    var r = c.getBoundingClientRect(); mx = (e.clientX - r.left) / r.width * W; my = (e.clientY - r.top) / r.height * H; on = true;
  });
  function loop(){
    x.clearRect(0, 0, W, H);
    pts.push({x:mx, y:my});
    if(pts.length > 26) pts.shift();
    for(var i = 0; i < pts.length; i++){
      var p = pts[i], t = i / pts.length;
      x.beginPath(); x.arc(p.x, p.y, 1 + t * 7, 0, 6.283);
      x.fillStyle = 'rgba(157,204,255,' + (t * .5).toFixed(2) + ')'; x.fill();
    }
    requestAnimationFrame(loop);
  }
  loop();
}''')

DEMOS[8] = ('''
<div class="rt"><div class="thumb" id="rtT">04</div>
<div class="pg"><span>← 返回</span><b>页面转场</b></div></div>
<div class="cap">点缩略图：FLIP 共享元素</div>''', '''
.mr .rt{position:relative;width:100%;height:100%;padding:14px}
.mr .thumb{width:64px;height:44px;border-radius:9px;display:grid;place-items:center;font-weight:800;font-size:13px;
  background:linear-gradient(150deg,#2d5473,#16222d);border:1px solid rgba(255,255,255,.18);cursor:pointer}
.mr .pg{position:absolute;inset:0;background:#0d141b;padding:14px;opacity:0;pointer-events:none;transition:opacity .18s}
.mr .pg.on{opacity:1;pointer-events:auto}
.mr .pg b{display:block;margin-top:10px;font-size:15px}
.mr .pg span{font-size:10.5px;color:#9dccff;cursor:pointer}
.mr .pg::after{content:"";position:absolute;left:14px;right:14px;top:52px;height:100px;border-radius:12px;
  background:linear-gradient(150deg,#2d5473,#16222d);border:1px solid rgba(255,255,255,.16)}''', '''
function(root){
  var t = root.querySelector('#rtT'), pg = root.querySelector('.pg');
  function flip(from, to){
    var a = from.getBoundingClientRect(), b = to.getBoundingClientRect();
    var sx = a.width / b.width, sy = a.height / b.height;
    to.style.transition = 'none';
    to.style.transformOrigin = 'top left';
    to.style.transform = 'translate(' + (a.left - b.left) + 'px,' + (a.top - b.top) + 'px) scale(' + sx + ',' + sy + ')';
    requestAnimationFrame(function(){
      to.style.transition = 'transform .42s cubic-bezier(.2,.9,.3,1)';
      to.style.transform = 'none';
    });
  }
  t.addEventListener('click', function(){ pg.classList.add('on'); flip(t, pg.querySelector('b')); });
  pg.querySelector('span').addEventListener('click', function(){ pg.classList.remove('on'); });
}''')

DEMOS[9] = ('''
<div class="pin"><div class="pin-in">
  <div class="st on">01 · 钉住</div><div class="st">02 · 分段</div><div class="st">03 · 收尾</div>
</div><div class="prog"><i></i></div></div>
<div class="cap">在框里滚动：整段钉住，内容分段推进</div>''', '''
.mr{padding:0;overflow:hidden}
.mr .pin{height:100%;overflow:auto;scrollbar-width:none;position:relative}
.mr .pin::-webkit-scrollbar{display:none}
.mr .pin-in{position:sticky;top:0;height:100%;display:flex;flex-direction:column;justify-content:center;
  gap:8px;padding:0 20px}
.mr .st{font-size:16px;font-weight:800;color:rgba(255,255,255,.18);transition:.3s}
.mr .st.on{color:#e9f0f8}
.mr .prog{position:sticky;bottom:0;height:3px;background:rgba(255,255,255,.1)}
.mr .prog i{display:block;height:100%;width:0;background:linear-gradient(90deg,#9dccff,#5fdba8)}
.mr .filler{height:400px}''', '''
function(root){
  var sc = root.querySelector('.pin'), steps = [].slice.call(root.querySelectorAll('.st')),
      bar = root.querySelector('.prog i');
  var f = document.createElement('div'); f.className = 'filler'; sc.querySelector('.pin-in').appendChild(f);
  sc.addEventListener('scroll', function(){
    var p = sc.scrollTop / Math.max(1, sc.scrollHeight - sc.clientHeight);
    bar.style.width = (p * 100).toFixed(1) + '%';
    var i = Math.min(steps.length - 1, Math.floor(p * steps.length + .2));
    steps.forEach(function(s, k){ s.classList.toggle('on', k <= i); });
  }, {passive:true});
}''')

DEMOS[10] = ('''
<div class="cnt"><b id="cn">0</b><span>条素材</span></div>
<div class="cap">点一下：0 → 46，easeOutExpo</div>''', '''
.mr .cnt{display:flex;flex-direction:column;align-items:center;gap:2px}
.mr .cnt b{font-size:44px;font-weight:800;letter-spacing:-.04em;font-variant-numeric:tabular-nums}
.mr .cnt span{font-size:10px;color:rgba(233,240,247,.4)}''', '''
function(root){
  var el = root.querySelector('#cn'), t = 46;
  function run(){
    var t0 = performance.now();
    function step(now){
      var p = Math.min(1, (now - t0) / 1200), e = p === 1 ? 1 : 1 - Math.pow(2, -10 * p);
      el.textContent = Math.round(t * e);
      if(p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  root.addEventListener('click', run); run();
}''')

DEMOS[11] = ('''
<svg width="0" height="0" style="position:absolute"><filter id="goo">
  <feGaussianBlur in="SourceGraphic" stdDeviation="7" result="b"/>
  <feColorMatrix in="b" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 20 -9" result="g"/>
  <feBlend in="SourceGraphic" in2="g"/></filter></svg>
<div class="goo"><i></i><i></i><i class="main"></i></div>
<div class="cap">移动鼠标：两块黏在一起再分开</div>''', '''
.mr .goo{position:relative;width:220px;height:120px;filter:url(#goo)}
.mr .goo i{position:absolute;border-radius:50%;background:#9dccff;width:44px;height:44px;left:20px;top:38px;
  transition:transform .12s linear}
.mr .goo i:nth-child(2){left:auto;right:20px;background:#5fdba8;transform:translate(0,0)}
.mr .goo i.main{left:88px;top:38px;background:#cfe3ff}''', '''
function(root){
  var a = root.querySelectorAll('.goo i');
  root.addEventListener('pointermove', function(e){
    var r = root.getBoundingClientRect();
    var dx = (e.clientX - r.left - r.width/2) * .16, dy = (e.clientY - r.top - r.height/2) * .16;
    a[2].style.transform = 'translate(' + dx + 'px,' + dy + 'px)';
    a[0].style.transform = 'translate(' + (dx * .5) + 'px,' + (dy * .5) + 'px)';
    a[1].style.transform = 'translate(' + (-dx * .5) + 'px,' + (-dy * .5) + 'px)';
  });
}''')

DEMOS[12] = ('''
<div class="sm"><div class="sm-in">
  <div class="blk">Lenis 式惯性</div><div class="blk">滚动位置 lerp 到目标</div><div class="blk">再交给 ScrollTrigger</div><div class="blk">收尾</div>
</div></div>
<div class="cap">滚轮/拖动：位移被 lerp 追平</div>''', '''
.mr{padding:0}
.mr .sm{height:100%;overflow:hidden;position:relative}
.mr .sm-in{position:absolute;left:0;right:0;top:0;padding:14px;display:flex;flex-direction:column;gap:8px}
.mr .blk{height:52px;border-radius:11px;display:flex;align-items:center;padding:0 14px;font-size:11.5px;
  color:rgba(233,240,247,.7);background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1)}''', '''
function(root){
  var box = root.querySelector('.sm'), inn = root.querySelector('.sm-in'), target = 0, cur = 0;
  box.addEventListener('wheel', function(e){ e.preventDefault(); target += e.deltaY * .9; }, {passive:false});
  var sy = 0, drag = false;
  box.addEventListener('pointerdown', function(e){ drag = true; sy = e.clientY; });
  window.addEventListener('pointermove', function(e){ if(drag){ target -= (e.clientY - sy) * 1.2; sy = e.clientY; } });
  window.addEventListener('pointerup', function(){ drag = false; });
  function loop(){
    target = Math.max(0, Math.min(inn.scrollHeight - box.clientHeight + 28, target));
    cur += (target - cur) * .12;
    inn.style.transform = 'translateY(' + (-cur).toFixed(2) + 'px)';
    requestAnimationFrame(loop);
  }
  loop();
}''')

DEMOS[13] = ('''
<div class="ah"><div class="ah-bar" id="ahb">背景感知 Header</div>
<div class="ah-zone light">亮区</div><div class="ah-zone dark">暗区</div><div class="ah-zone mid">中间</div></div>
<div class="cap">在框里滚动：条上的字自己反色</div>''', '''
.mr{padding:0}
.mr .ah{position:relative;height:100%;overflow:auto;scrollbar-width:none}
.mr .ah::-webkit-scrollbar{display:none}
.mr .ah-bar{position:sticky;top:0;z-index:2;height:40px;display:flex;align-items:center;padding:0 14px;
  font-size:12px;font-weight:700;transition:color .2s;backdrop-filter:blur(6px)}
.mr .ah-zone{height:96px;display:grid;place-items:center;font-size:11px;color:rgba(255,255,255,.5)}
.mr .ah-zone.light{background:#eef3f8;color:#22303f}
.mr .ah-zone.dark{background:#0c1117}
.mr .ah-zone.mid{background:#7f93a6}
.mr .ah-bar.inv{color:#16202a}''', '''
function(root){
  var sc = root.querySelector('.ah'), bar = root.querySelector('#ahb');
  sc.addEventListener('scroll', function(){
    var y = sc.scrollTop + 20;
    var light = y > 96 && y < 192 || y > 288;
    bar.classList.toggle('inv', light);
  }, {passive:true});
}''')

DEMOS[14] = ('''
<div class="ann"><span>点这里</span>
<svg viewBox="0 0 140 70"><ellipse class="ring" cx="70" cy="35" rx="62" ry="28" pathLength="1"/></svg></div>
<div class="cap">朱砂圈：1.1s 画完，随后呼吸</div>''', '''
.mr .ann{position:relative;width:150px;height:80px;display:grid;place-items:center}
.mr .ann span{font-size:13px;font-weight:700;letter-spacing:.02em}
.mr .ann svg{position:absolute;inset:0;width:100%;height:100%;fill:none;stroke:#e2705f;stroke-width:2.2;
  stroke-linecap:round;transform:rotate(-4deg)}
.mr .ring{stroke-dasharray:1;stroke-dashoffset:1;animation:annDraw 1.1s cubic-bezier(.2,.9,.3,1) forwards,
  annBreath 3.4s 1.2s ease-in-out infinite}
@keyframes annDraw{to{stroke-dashoffset:0}}
@keyframes annBreath{0%,100%{opacity:.85}50%{opacity:.45}}''', '''
function(root){}''')

DEMOS[15] = ('''
<canvas class="vc" width="300" height="210"></canvas>
<div class="cap">拖动帘子：绳子的悬垂会被带动</div>''', '''
.mr{padding:0}
.mr .vc{width:100%;height:100%;display:block;touch-action:none}''', '''
function(root){
  var c = root.querySelector('.vc'), g = c.getContext('2d'), W = 300, H = 210;
  var N = 13, cols = [], drag = -1;
  for(var i = 0; i < N; i++) cols.push({x: 24 + i * 21, y: 20, ox: 24 + i * 21, oy: 20, r: 44});
  c.addEventListener('pointerdown', function(e){
    var r = c.getBoundingClientRect(), x = (e.clientX - r.left) / r.width * W;
    drag = Math.max(0, Math.min(N - 1, Math.round((x - 24) / 21)));
  });
  c.addEventListener('pointermove', function(e){
    if(drag < 0) return;
    var r = c.getBoundingClientRect();
    cols[drag].y = Math.max(20, Math.min(H - 20, (e.clientY - r.top) / r.height * H));
  });
  window.addEventListener('pointerup', function(){ drag = -1; });
  function loop(){
    g.clearRect(0, 0, W, H);
    cols.forEach(function(p, i){
      var ay = (20 - p.y) * .28 - (p.y - p.oy) * .12;
      var vy = (p.y - p.oy) * .9 + ay;
      p.oy = p.y; p.y += vy;
      if(i > 0){ var q = cols[i-1], d = (q.y - p.y) * .12; p.y += d; }
    });
    for(var i = 0; i < N - 1; i++){
      var a = cols[i], b = cols[i+1];
      g.beginPath(); g.moveTo(a.x, a.y);
      g.quadraticCurveTo((a.x + b.x)/2, (a.y + b.y)/2 + 6, b.x, b.y);
      g.strokeStyle = 'rgba(157,204,255,.55)'; g.lineWidth = 1.2; g.stroke();
      g.fillStyle = 'rgba(207,227,255,.9)';
      g.beginPath(); g.arc(a.x, a.y, 2.6, 0, 6.283); g.fill();
    }
    requestAnimationFrame(loop);
  }
  loop();
}''')

DEMOS[16] = ('''
<div class="nrv" id="nrv"><div class="b">CSS</div><div class="b">only</div><div class="b">stagger</div>
<div class="b">no observer</div></div>
<div class="cap">纯 CSS 错峰：animation-delay + sibling-index 思路</div>''', '''
.mr .nrv{display:flex;flex-direction:column;gap:6px;width:150px}
.mr .b{height:24px;border-radius:7px;display:flex;align-items:center;padding:0 10px;font-size:10.5px;
  color:rgba(233,240,247,.72);background:rgba(157,204,255,.14);border:1px solid rgba(157,204,255,.24);
  opacity:0;transform:translateY(10px);animation:nvIn .5s cubic-bezier(.16,1,.3,1) forwards}
.mr .b:nth-child(1){animation-delay:.02s}.mr .b:nth-child(2){animation-delay:.08s}
.mr .b:nth-child(3){animation-delay:.14s}.mr .b:nth-child(4){animation-delay:.2s}
@keyframes nvIn{to{opacity:1;transform:none}}''', '''
function(root){}''')

DEMOS[17] = ('''
<canvas class="cw" width="300" height="210"></canvas>
<div class="cap">拖动四角：图片被贴进任意四边形</div>''', '''
.mr{padding:0}
.mr .cw{width:100%;height:100%;display:block;touch-action:none}''', '''
function(root){
  var c = root.querySelector('.cw'), g = c.getContext('2d'), W = 300, H = 210;
  var pts = [[70,50],[230,44],[226,166],[66,172]], drag = -1;
  c.addEventListener('pointerdown', function(e){
    var r = c.getBoundingClientRect(), x = (e.clientX - r.left)/r.width*W, y = (e.clientY - r.top)/r.height*H;
    var best = -1, bd = 1e9;
    pts.forEach(function(p, i){ var d = Math.hypot(p[0]-x, p[1]-y); if(d < bd){ bd = d; best = i; } });
    if(bd < 44) drag = best;
  });
  c.addEventListener('pointermove', function(e){
    if(drag < 0) return;
    var r = c.getBoundingClientRect();
    pts[drag] = [(e.clientX - r.left)/r.width*W, (e.clientY - r.top)/r.height*H];
  });
  window.addEventListener('pointerup', function(){ drag = -1; });
  function tri(a,b,cc,uv){ g.save(); g.beginPath();
    g.moveTo(a[0],a[1]); g.lineTo(b[0],b[1]); g.lineTo(cc[0],cc[1]); g.closePath(); g.clip();
    var x0=uv[0][0],y0=uv[0][1],x1=uv[1][0],y1=uv[1][1],x2=uv[2][0],y2=uv[2][1];
    var ax=(x0+x2)/2, ay=(y0+y2)/2;
    g.transform(-(ax-x1), -(ay-y1), ax, ay, 0, 0);
    g.transform(1,0,0,1,-ax,-ay);
    g.fillStyle = '#9dccff'; g.fillRect(0,0,W,H); g.restore(); }
  function loop(){
    g.clearRect(0,0,W,H);
    var a=pts[0], b=pts[1], cc=pts[2], d=pts[3];
    var grad = g.createLinearGradient(a[0],a[1],cc[0],cc[1]);
    grad.addColorStop(0,'#3c6f9e'); grad.addColorStop(1,'#1a2a38');
    g.fillStyle = grad; g.beginPath();
    g.moveTo(a[0],a[1]); g.lineTo(b[0],b[1]); g.lineTo(cc[0],cc[1]); g.lineTo(d[0],d[1]); g.closePath(); g.fill();
    g.strokeStyle='rgba(207,227,255,.75)'; g.lineWidth = 1.5; g.stroke();
    pts.forEach(function(p){ g.beginPath(); g.arc(p[0],p[1],4.5,0,6.283);
      g.fillStyle='#0b1118'; g.fill(); g.strokeStyle='#cfe3ff'; g.stroke(); });
    g.fillStyle='rgba(255,255,255,.5)'; g.font='9px sans-serif'; g.fillText('corner-pin warp', 12, 200);
    requestAnimationFrame(loop);
  }
  loop();
}''')

DEMOS[18] = ('''
<canvas class="cc" width="300" height="210"></canvas>
<div class="cap">拖动：一串卡片挂在光标下摆动</div>''', '''
.mr{padding:0}
.mr .cc{width:100%;height:100%;display:block;touch-action:none}''', '''
function(root){
  var c = root.querySelector('.cc'), g = c.getContext('2d'), W = 300, H = 210;
  var N = 8, nodes = [], mx = 150, my = 60;
  for(var i = 0; i < N; i++) nodes.push({x: 150, y: 60 + i * 12, ox: 150, oy: 60 + i * 12});
  c.addEventListener('pointermove', function(e){
    var r = c.getBoundingClientRect(); mx = (e.clientX-r.left)/r.width*W; my = (e.clientY-r.top)/r.height*H;
  });
  function loop(){
    nodes[0].x += (mx - nodes[0].x) * .3; nodes[0].y += (my - nodes[0].y) * .3;
    for(var i = 1; i < N; i++){
      var p = nodes[i], q = nodes[i-1];
      var dx = p.x - q.x, dy = p.y - q.y, d = Math.hypot(dx, dy) || 1;
      var tx = q.x + dx / d * 15, ty = q.y + dy / d * 15;
      var vx = (p.x - p.ox) * .86, vy = (p.y - p.oy) * .86;
      p.ox = p.x; p.oy = p.y;
      p.x = p.x + vx + (tx - p.x) * .6;
      p.y = p.y + vy + (ty - p.y) * .6 + .35;
    }
    g.clearRect(0, 0, W, H);
    nodes.forEach(function(p, i){
      var s = Math.max(6, 18 - i * 1.4);
      g.save(); g.translate(p.x, p.y); g.rotate((p.x - p.ox) * .04);
      g.fillStyle = 'rgba(' + (157 - i*6) + ',' + (204 - i*8) + ',255,' + (0.92 - i*.08) + ')';
      g.fillRect(-s, -s*.7, s*2, s*1.4); g.restore();
      if(i) { g.beginPath(); g.moveTo(nodes[i-1].x, nodes[i-1].y); g.lineTo(p.x, p.y);
        g.strokeStyle = 'rgba(157,204,255,.25)'; g.stroke(); }
    });
    requestAnimationFrame(loop);
  }
  loop();
}''')

DEMOS[19] = ('''
<canvas class="sl" width="300" height="210"></canvas>
<div class="cap">按住中点拖动：两端钉死，中段乱写</div>''', '''
.mr{padding:0}
.mr .sl{width:100%;height:100%;display:block;touch-action:none}''', '''
function(root){
  var c = root.querySelector('.sl'), g = c.getContext('2d'), W = 300, H = 210;
  var a = [34, 60], b = [266, 150], sag = 40, drag = false;
  c.addEventListener('pointerdown', function(){ drag = true; });
  window.addEventListener('pointerup', function(){ drag = false; });
  function loop(){
    if(drag) sag = Math.min(120, Math.max(0, sag)); else sag += (40 - sag) * .06;
    g.clearRect(0, 0, W, H);
    g.beginPath(); g.moveTo(a[0], a[1]);
    g.quadraticCurveTo((a[0]+b[0])/2, (a[1]+b[1])/2 + sag * 2, b[0], b[1]);
    g.strokeStyle = '#9dccff'; g.lineWidth = 2; g.lineCap = 'round'; g.stroke();
    [[a,'锚点'],[b,'端点']].forEach(function(p){
      g.beginPath(); g.arc(p[0][0], p[0][1], 5, 0, 6.283); g.fillStyle='#e9f0f8'; g.fill();
      g.fillStyle='rgba(233,240,248,.55)'; g.font='9px sans-serif'; g.fillText(p[1], p[0][0]-8, p[0][1]-10);
    });
    g.fillStyle='rgba(233,240,248,.32)'; g.font='9px sans-serif';
    g.fillText('mid-point sags by ' + Math.round(sag) + 'px', 92, 196);
    requestAnimationFrame(loop);
  }
  loop();
}''')

DEMOS[20] = ('''
<canvas class="ce" width="300" height="210"></canvas>
<div class="cap">几百个小点：数量本身就是构图</div>''', '''
.mr{padding:0}
.mr .ce{width:100%;height:100%;display:block}''', '''
function(root){
  var c = root.querySelector('.ce'), g = c.getContext('2d'), W = 300, H = 210;
  var pts = [];
  for(var i = 0; i < 620; i++){
    var t = i / 620, a = t * Math.PI * 5.2 + Math.sin(t * 9) * .9;
    var r = 12 + Math.pow(t, .62) * 96;
    pts.push([150 + Math.cos(a) * r * 1.05, 108 + Math.sin(a) * r * .72,
              1 + (1 - t) * 2.4, 'rgba(157,204,255,' + (.16 + t * .6).toFixed(2) + ')']);
  }
  function draw(){
    g.clearRect(0, 0, W, H);
    pts.forEach(function(p){ g.beginPath(); g.arc(p[0], p[1], p[2], 0, 6.283); g.fillStyle = p[3]; g.fill(); });
  }
  draw();
}''')

RECIPE_DEMOS = []
for r in RECIPES:
    d = DEMOS.get(r['no'])
    if not d:
        d = ('<div class="cap">演示生成中</div>', '', 'function(root){}')
    RECIPE_DEMOS.append(dict(no=r['no'], name=r['name'], what=r['what'], use=r['use'],
                             html=d[0], css=d[1], js=d[2]))

# ─────────────── 4 个令牌实验室 ───────────────
TOKENS = {
    'duration': [
        ('instant', '80–100ms', '光标反馈、tooltip 显隐', 90),
        ('fast', '150–200ms', 'hover、按钮按下、开关', 180),
        ('standard', '280–350ms', '卡片展开、面板滑出、抽屉', 320),
        ('medium', '400–500ms', '区块入场、图片打开', 460),
        ('slow', '600–800ms', '页面进入、hero 文字、路由', 700),
        ('cinematic', '1000–1400ms', '开场、幕布、戏剧性入场', 1200),
        ('ambient', 'continuous', '背景循环、粒子、呼吸光', 0),
    ],
    'easing': [
        ('ease-out-expo', 'cubic-bezier(.16,1,.3,1)', '快进慢停，入场默认'),
        ('ease-in-expo', 'cubic-bezier(.7,0,.84,0)', '慢起硬出，只用于退场'),
        ('ease-in-out-quart', 'cubic-bezier(.76,0,.24,1)', '对称顺滑，循环'),
        ('ease-out-back', 'cubic-bezier(.34,1.56,.64,1)', '轻微过冲，俏皮 hover'),
        ('ease-out-circ', 'cubic-bezier(0,.55,.45,1)', '极快减速，机械感'),
        ('ease-sharp', 'cubic-bezier(.65,0,.45,1)', '硬朗的品牌冲击'),
        ('ease-standard', 'cubic-bezier(.4,0,.2,1)', 'Material 默认'),
        ('ease-expressive', 'cubic-bezier(.68,-.6,.32,1.6)', '两端都过冲，慎用'),
        ('linear', 'linear', '滚动擦除、着色器 uniform'),
    ],
    'spring': [
        ('spring-gentle', 100, 15, 1, '柔和缓慢无回弹，环境式入场'),
        ('spring-default', 200, 22, 1, '自然手感，卡片 hover、抽屉'),
        ('spring-snappy', 350, 28, 1, '高级快速吸附，按钮反馈'),
        ('spring-bouncy', 200, 10, 1, '俏皮过冲，游戏化图标'),
        ('spring-heavy', 150, 35, 1.5, '沉重迟钝，大面板'),
        ('spring-stiff', 500, 40, 1, '近乎瞬时，光标跟随'),
    ],
    'stagger': [
        ('tight-grid', 40, '数据网格行、工具面板'),
        ('standard-list', 75, '卡片列表、特性网格、导航'),
        ('editorial-line', 90, '文字逐行、文章区块'),
        ('dramatic-cascade', 150, '获奖站点 hero、横幅揭示'),
        ('no-stagger', 0, '单一 CTA、干脆的品牌动作'),
    ],
}
