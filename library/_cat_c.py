# -*- coding: utf-8 -*-
"""F25–F31：反馈"""
from _cat_base import item, add, refs

F25 = item(
    id='F25', slug='toast', name='轻提示', cat='05-反馈', catname='反馈', diff='★☆☆', tag='反馈',
    mech='顶部浮入 + 自动消失：进入用 translateY(-10px)→0 + 缩放 0.96→1，退出用同曲线反向；多条 Toast 竖直堆叠，'
         '最多 3 条，超出时挤掉最老的。',
    params='进入 260ms 弹簧 · 停留 2.2s · 退出 200ms · 同时最多 3 条',
    verify='连点 5 次最多 3 条；每条独立计时；页面切走时全部清理。',
    steps=['每个 toast 用独立 setTimeout；容器 flex column，新 toast 从顶部插入。'],
    redline=['不许用 alert / confirm 代替（会阻塞界面）。'],
    fails=[('toast 叠成一片', '绝对定位于同一点', '容器 flex column + gap')],
    prompt='''做轻提示（toast）系统：API 为 toast(msg, type)，type = info/success/warn。
【动效】进入：opacity 0→1、translateY(-10px)→0、scale .96→1，260ms 弹簧；
退出：反向 200ms；自动停留 2.2s。
【堆叠】多条竖直堆叠（gap 6），最多同时 3 条，超出的挤掉最老的；每条独立计时器。
【自检】连点 8 次最多 3 条且不会一起消失；成功/警告图标颜色不同；动画期间不抖动。''',
    html='''<div class="ts-wrap"><div class="ts" id="ts"></div></div>
<button class="btn pri ts-go">点我弹一条</button>
<div class="cap">最多同时 3 条，依次挤出</div>''',
    css='''.dz .ts-wrap{position:absolute;top:10px;left:0;right:0;display:flex;flex-direction:column;align-items:center;gap:5px;
  pointer-events:none;z-index:9}
.dz .ts{display:flex;flex-direction:column;gap:5px;align-items:center}
.dz .toast{display:flex;align-items:center;gap:6px;padding:7px 12px;border-radius:10px;font-size:11px;
  background:rgba(24,33,42,.96);border:1px solid var(--line2);color:var(--ink);box-shadow:0 10px 24px rgba(0,0,0,.5);
  animation:tsIn .26s var(--spring) both;max-width:240px}
.dz .toast.out{animation:tsOut .2s var(--ease) both}
.dz .toast b{font-size:12px}
.dz .toast.ok b{color:var(--ok)}
.dz .toast.warn b{color:var(--warn)}
@keyframes tsIn{from{opacity:0;transform:translateY(-10px) scale(.96)}to{opacity:1;transform:none}}
@keyframes tsOut{to{opacity:0;transform:translateY(-8px) scale(.97)}}''',
    js='''function(root){
  var box = root.querySelector('.ts'), n = 0;
  var types = [['', '已保存到素材库'], ['ok', '复制成功'], ['warn', '网络不可用，已使用缓存']];
  root.querySelector('.ts-go').addEventListener('click', function(){
    var t = types[n++ % 3];
    var el = document.createElement('div');
    el.className = 'toast ' + t[0];
    el.innerHTML = '<b>' + (t[0]==='ok'?'✓':t[0]==='warn'?'!':'i') + '</b><span>' + t[1] + '</span>';
    box.appendChild(el);
    var all = box.children;
    if(all.length > 3){ kill(all[0]); }
    var timer = setTimeout(function(){ kill(el); }, 2200);
    function kill(node){
      clearTimeout(timer);
      node.classList.add('out');
      setTimeout(function(){ node.remove(); }, 210);
    }
  });
}''',
    refs=refs('m3', 'antd', 'shadcn'),
    env_notes='无依赖。',
    demo_hint='连点几次按钮',
)

F26 = item(
    id='F26', slug='dialog', name='对话框', cat='05-反馈', catname='反馈', diff='★★☆', tag='反馈',
    mech='缩放淡入 + 焦点圈定：对话框用 scale(.92)→1 弹簧入场；打开时把焦点移到主按钮，Esc 关闭，'
         '遮罩点击关闭（危险操作不允许点遮罩关闭）。',
    params='入场 280ms cubic-bezier(.2,.9,.3,1.2) · 遮罩 45% · 圆角 16',
    verify='连续开关 10 次无残影；Esc 与遮罩行为正确；焦点不跑到背景。',
    steps=['用 <dialog> 或自建；自建要手动管 aria-hidden 与 tabindex。'],
    redline=['不许在危险确认里让遮罩可点关闭（误触成本太高）。'],
    fails=[('对话框被裁切', '父级 overflow:hidden', '挂到 body 或用 fixed 定位')],
    prompt='''做确认对话框：标题 + 说明 + 取消/确认（危险色）。
【动效】遮罩 200ms 淡入；卡片 scale(.92)→1 + 透明度，280ms cubic-bezier(.2,.9,.3,1.2)；
关闭反向 160ms。打开时焦点移到「取消」，Esc 关闭；点遮罩也关闭，但 danger=true 时禁止点遮罩关闭。
【自检】连开 10 次无残影；Esc 生效；背景不可滚动；按钮有 focus-visible 轮廓。''',
    html='''<button class="btn pri dg-open">删除素材</button>
<div class="dg-mask on"></div>
<div class="dg on" role="dialog" aria-modal="true">
  <div class="dg-ico">!</div>
  <div class="dg-t">删除这个素材？</div>
  <div class="dg-d">删除后无法恢复，已导出的代码不受影响。</div>
  <div class="dg-b"><button class="btn dg-no">取消</button><button class="btn dg-ok danger">删除</button></div>
</div>
<div class="cap">Esc / 取消 / 确认 都可关闭（危险态点遮罩无效）</div>''',
    css='''.dz .dg-mask{position:absolute;inset:0;background:#000;opacity:0;pointer-events:none;transition:opacity .2s}
.dz .dg{position:absolute;left:50%;top:50%;width:210px;transform:translate(-50%,-50%) scale(.92);opacity:0;
  pointer-events:none;background:#182129;border:1px solid var(--line2);border-radius:15px;padding:15px;
  box-shadow:0 24px 60px rgba(0,0,0,.6);transition:transform .28s cubic-bezier(.2,.9,.3,1.2),opacity .2s}
.dz .dg.on{opacity:1;transform:translate(-50%,-50%) scale(1);pointer-events:auto}
.dz .dg-mask.on{opacity:.5;pointer-events:auto}
.dz .dg-ico{width:26px;height:26px;border-radius:50%;display:grid;place-items:center;background:rgba(255,107,107,.18);
  color:var(--danger);font-weight:800;font-size:13px;margin-bottom:8px}
.dz .dg-t{font-size:13px;font-weight:700}
.dz .dg-d{font-size:10.5px;color:var(--dim);line-height:1.7;margin:5px 0 12px}
.dz .dg-b{display:flex;gap:7px}
.dz .dg-b .btn{flex:1;height:29px;font-size:11px}''',
    js='''function(root){
  var dg = root.querySelector('.dg'), mask = root.querySelector('.dg-mask');
  function open(){ dg.classList.add('on'); mask.classList.add('on'); }
  function close(){ dg.classList.remove('on'); mask.classList.remove('on'); }
  root.querySelector('.dg-open').addEventListener('click', function(e){ e.stopPropagation(); open(); });
  root.querySelectorAll('.dg-no,.dg-ok').forEach(function(b){ b.addEventListener('click', close); });
  window.addEventListener('keydown', function(e){ if(e.key === 'Escape') close(); });
  mask.addEventListener('click', function(){}); /* 危险态禁止点遮罩关闭 */
}''',
    refs=refs('m3', 'radix', 'antd'),
    env_notes='无依赖。',
    demo_hint='点按钮打开',
)

F27 = item(
    id='F27', slug='action-sheet', name='底部操作面板', cat='05-反馈', catname='反馈', diff='★★☆', tag='反馈',
    mech='从底部上滑的面板：拖动把手可下拉关闭，位移超过 35% 或速度达标时关闭；选项逐项上浮入场。',
    params='圆角 20 · 入场 320ms 弹簧 · 关闭阈值 35% · 选项错峰 35ms',
    verify='拖到一半松手回弹；拉到阈值以下关闭；遮罩点击关闭；选项点击后自动收起。',
    steps=['面板 transform: translateY(100%) 起手，open 时 translateY(0)。'],
    redline=['不许没有遮罩（会和背景内容抢注意力）。'],
    fails=[('面板下方露白', '高度用了 calc 而不是 100%+安全区', '底部加 padding-bottom 安全区')],
    prompt='''做底部操作面板（action sheet）：一个把手 + 4 个操作项 + 取消。
【动效】从 translateY(100%) 上滑到 0，320ms 弹簧；遮罩淡入 40% 黑；选项每项延迟 35ms 上浮入场。
【手势】按住把手下拉，位移 >35% 或速度 >0.5px/ms 关闭，否则回弹。
【自检】半程松手回弹；阈值一下关闭；选项点击后面板收起；拖拽时遮罩同步变淡。''',
    html='''<button class="btn pri bp-open">打开面板</button>
<div class="bp-mask on"></div>
<div class="bp on">
  <div class="bp-h"></div>
  <a class="bp-i"><b>⇩</b>保存到本地</a>
  <a class="bp-i"><b>⧉</b>复制提示词</a>
  <a class="bp-i"><b>⤴</b>分享给同事</a>
  <a class="bp-i"><b>⌫</b><span class="danger-t">删除</span></a>
  <button class="bp-c">取消</button>
</div>
<div class="cap">按住把手下拉可关闭</div>''',
    css='''.dz .bp-mask{position:absolute;inset:0;background:#000;opacity:0;pointer-events:none;transition:opacity .28s}
.dz .bp{position:absolute;left:0;right:0;bottom:0;border-radius:18px 18px 0 0;background:#182129;
  border-top:1px solid var(--line2);padding:6px 10px 10px;transform:translateY(100%);
  transition:transform .32s var(--spring);box-shadow:0 -16px 40px rgba(0,0,0,.5);z-index:3}
.dz .bp.on{transform:none}
.dz .bp-mask.on{opacity:.45;pointer-events:auto}
.dz .bp-h{width:34px;height:3px;border-radius:2px;background:rgba(255,255,255,.28);margin:2px auto 8px;cursor:grab}
.dz .bp-i{display:flex;align-items:center;gap:9px;height:33px;padding:0 8px;border-radius:9px;font-size:11.5px;
  color:var(--ink);opacity:0;transform:translateY(8px)}
.dz .bp.on .bp-i{animation:bpIn .3s var(--ease) both}
.dz .bp.on .bp-i:nth-child(2){animation-delay:.03s}
.dz .bp.on .bp-i:nth-child(3){animation-delay:.06s}
.dz .bp.on .bp-i:nth-child(4){animation-delay:.09s}
.dz .bp.on .bp-i:nth-child(5){animation-delay:.12s}
@keyframes bpIn{to{opacity:1;transform:none}}
.dz .bp-i b{width:15px;text-align:center;color:var(--acc);font-weight:400}
.dz .danger-t{color:var(--danger)}
.dz .bp-c{width:100%;height:31px;border-radius:9px;background:rgba(255,255,255,.07);font-size:11.5px;color:var(--soft);margin-top:5px}''',
    js='''function(root){
  var bp = root.querySelector('.bp'), mask = root.querySelector('.bp-mask'), h = root.querySelector('.bp-h');
  function open(){ bp.classList.add('on'); mask.classList.add('on'); }
  function close(){ bp.classList.remove('on'); mask.classList.remove('on'); }
  root.querySelector('.bp-open').addEventListener('click', open);
  mask.addEventListener('click', close);
  root.querySelector('.bp-c').addEventListener('click', close);
  root.querySelectorAll('.bp-i').forEach(function(a){ a.addEventListener('click', close); });
  var sy = 0, dy = 0, drag = false, t0 = 0;
  h.addEventListener('pointerdown', function(e){ drag = true; sy = e.clientY; t0 = performance.now(); bp.style.transition = 'none'; });
  window.addEventListener('pointermove', function(e){
    if(!drag) return;
    dy = Math.max(0, e.clientY - sy);
    bp.style.transform = 'translateY(' + dy + 'px)';
    mask.style.opacity = Math.max(0, .45 - dy / 300);
  });
  window.addEventListener('pointerup', function(){
    if(!drag) return;
    drag = false; bp.style.transition = ''; mask.style.opacity = '';
    if(dy > bp.offsetHeight * .35 || dy / Math.max(1, performance.now() - t0) > .5){ close(); bp.style.transform = ''; }
    else bp.style.transform = '';
    dy = 0;
  });
}''',
    refs=refs('hig', 'ionic', 'm3'),
    env_notes='无依赖。',
    demo_hint='打开后拉把手',
)

F28 = item(
    id='F28', slug='skeleton', name='骨架屏', cat='05-反馈', catname='反馈', diff='★☆☆', tag='反馈',
    mech='骨架 → 内容的无缝替换：骨架用 1.6s 横向扫光，真内容带入 220ms 淡入，两者尺寸完全一致，避免布局跳动。',
    params='扫光 1.6s linear 无限 · 骨架圆角 6 · 内容淡入 220ms',
    verify='切换瞬间高度不变（用 JS 打印 offsetHeight）；扫光顺滑；三次切换都对齐。',
    steps=['骨架盒子与内容盒子的行高、内外边距严格一致，最好共用同一套 class。'],
    redline=['不许骨架和内容尺寸不同（会跳动，比没有骨架更糟）。'],
    fails=[('切换时跳动', '骨架行高与内容不同', '共用行高变量')],
    prompt='''做骨架屏：卡片含头像（32 圆）、标题条、两行正文。
【扫光】骨架背景 linear-gradient 105deg 从 -20% 扫到 120%，1.6s linear 无限；圆角 6。
【切换】1.6s 后换成真实内容，淡入 220ms；骨架与内容的行高 / 内边距必须一致。
【自检】切换瞬间用 offsetHeight 打印高度差为 0；扫光无卡顿；连续切换 3 次都对齐。''',
    html='''<div class="sk-card" id="skc">
  <div class="sk-av"></div>
  <div class="sk-lines"><div class="sk-l w60"></div><div class="sk-l w90"></div><div class="sk-l w40"></div></div>
</div>
<button class="btn sk-again">重新加载</button>
<div class="cap">骨架尺寸 = 内容尺寸，切换不跳</div>''',
    css='''.dz .sk-card{width:240px;padding:11px;border-radius:13px;background:var(--card);border:1px solid var(--line);
  display:flex;gap:10px;min-height:70px}
.dz .sk-av{width:32px;height:32px;border-radius:50%;flex:0 0 auto;
  background:linear-gradient(105deg,#1e2933 30%,#2b3946 50%,#1e2933 70%) 0 0/300% 100%;animation:sk 1.6s linear infinite}
.dz .sk-lines{flex:1;display:flex;flex-direction:column;gap:7px;justify-content:center}
.dz .sk-l{height:10px;border-radius:5px;
  background:linear-gradient(105deg,#1e2933 30%,#2b3946 50%,#1e2933 70%) 0 0/300% 100%;animation:sk 1.6s linear infinite}
.dz .sk-l.w60{width:60%}.dz .sk-l.w90{width:90%}.dz .sk-l.w40{width:40%}
@keyframes sk{from{background-position:120% 0}to{background-position:-120% 0}}
.dz .sk-real{animation:skIn .22s var(--ease) both}
@keyframes skIn{from{opacity:0}to{opacity:1}}
.dz .sk-real .sk-t{font-size:12px;font-weight:700;margin-bottom:3px}
.dz .sk-real .sk-p{font-size:10.5px;color:var(--dim);line-height:1.6}
.dz .sk-real .sk-av{background:linear-gradient(150deg,#9dccff,#5fdbA8);animation:none;display:grid;place-items:center;
  color:#06121c;font-weight:800;font-size:12px}''',
    js='''function(root){
  var card = root.querySelector('#skc'), timer;
  var skeleton = card.innerHTML;
  function run(){
    card.innerHTML = skeleton;
    clearTimeout(timer);
    timer = setTimeout(function(){
      var h0 = card.offsetHeight;
      card.innerHTML = '<div class="sk-real" style="display:flex;gap:10px;width:100%">' +
        '<div class="sk-av">林</div><div><div class="sk-t">林小满</div>' +
        '<div class="sk-p">把 yz8023/ui 的引用方案整套搬进素材库，每条素材都有参考来源与判据。</div></div></div>';
      card.firstChild.style.minHeight = h0 + 'px';
    }, 1600);
  }
  run();
  root.querySelector('.sk-again').addEventListener('click', run);
}''',
    refs=refs('antd', 'shadcn', 'm3'),
    env_notes='无依赖。',
    demo_hint='看骨架如何换成内容',
)

F29 = item(
    id='F29', slug='empty-state', name='空状态', cat='05-反馈', catname='反馈', diff='★☆☆', tag='反馈',
    mech='空状态的插画用 SVG 描边路径 + 逐段绘制动画（stroke-dashoffset），配一行说明与一个主操作；'
         '文案要给出下一步，不要只说「暂无数据」。',
    params='描边 1.6s 一次 · 插画 84px · 主按钮在说明下方 14px',
    verify='插画路径绘制完整；主按钮可点；窄屏不挤；空状态从触发到出现有 180ms 淡入。',
    steps=['SVG 用 pathLength=1 让 dashoffset 归一到 1，避免逐条算长度。'],
    redline=['不许空状态只有文字没有出口按钮。'],
    fails=[('线条画到一半停住', '没有设置 fill-mode forwards', 'animation: ... forwards')],
    prompt='''做空状态页：SVG 线描插画（盒子 + 星星）+ 标题「还没有素材」+ 说明「创建第一条素材，或从模板导入」+
主按钮「新建素材」+ 次按钮「浏览模板」。
【动效】插画 pathLength=1，stroke-dashoffset 1→0，1.6s ease-out 一次；随后整块淡入 180ms。
【自检】线条全部画完不残留；两个按钮都可点；宽度 280 时不换行溢出。''',
    html='''<div class="es">
  <svg viewBox="0 0 96 76" width="62" height="50" fill="none" stroke="var(--acc)" stroke-width="2"
       stroke-linecap="round" stroke-linejoin="round">
    <path pathLength="1" d="M20 34l6 26h44l6-26"/>
    <path pathLength="1" d="M14 34h68"/>
    <path pathLength="1" d="M40 20h16l4 14H36z"/>
    <path pathLength="1" d="M74 12l2 5 5 2-5 2-2 5-2-5-5-2 5-2z"/>
  </svg>
  <div class="es-t">还没有素材</div>
  <div class="es-d">创建第一条素材，或从模板导入</div>
  <button class="btn pri es-b">新建素材</button>
  <button class="btn es-b2">浏览模板</button>
</div>
<div class="cap">线描插画 + 明确的下一步</div>''',
    css='''.dz .es{display:flex;flex-direction:column;align-items:center;text-align:center;gap:3px}
.dz .es svg path{stroke-dasharray:1;stroke-dashoffset:1;animation:esDraw 1.6s var(--ease) forwards}
.dz .es svg path:nth-child(2){animation-delay:.18s}
.dz .es svg path:nth-child(3){animation-delay:.34s}
.dz .es svg path:nth-child(4){animation-delay:.5s}
@keyframes esDraw{to{stroke-dashoffset:0}}
.dz .es-t{font-size:12px;font-weight:700;margin-top:2px}
.dz .es-d{font-size:10.5px;color:var(--dim);max-width:190px;line-height:1.6}
.dz .es-b{margin-top:6px;height:26px;padding:0 15px;font-size:10.5px}
.dz .es-b2{height:22px;padding:0 10px;font-size:10px;color:var(--dim);background:none}''',
    js='''function(root){
  root.querySelector('.es-b').addEventListener('click', function(){
    var svg = root.querySelector('.es svg');
    svg.querySelectorAll('path').forEach(function(p){
      p.style.animation = 'none'; void p.offsetWidth; p.style.animation = '';
    });
  });
}''',
    refs=refs('antd', 'm3', 'shadcn'),
    env_notes='无依赖。',
    demo_hint='点按钮重播绘制',
)

F30 = item(
    id='F30', slug='progress', name='进度与环形', cat='05-反馈', catname='反馈', diff='★★☆', tag='反馈',
    mech='环形进度用 stroke-dashoffset 表示，数值用 requestAnimationFrame 缓动到目标值（避免百分比跳格）；'
         '线性进度条在 >100% 时显示条纹。',
    params='环 r=22 · 周长 138 · 缓动 700ms ease-out · 值域 0–100',
    verify='数值与弧长同步；0 与 100 边界正确；缓动结束停在精确目标值。',
    steps=['dasharray = 周长，dashoffset = 周长×(1-p)；起点用 rotate(-90) 把 0 放到 12 点。'],
    redline=['不许数值与弧长各用一套动画（会对不上）。'],
    fails=[('0% 时留一截', '没有减 dasharray 的圆头', '用 stroke-linecap: round 并处理极小值')],
    prompt='''做两种进度：环形（SVG）+ 线性（div）。
【环形】r=22、周长 2πr、起点 12 点（rotate(-90)）、圆头端点、渐变描边。
【数字】0→88% 用 rAF + easeOutCubic 缓动 700ms，数字与弧长同源。
【线性】宽度按同一数值；达到 100% 时切换成条纹动画。
【自检】边界 0 与 100 正确；缓动结束数值精确等于目标；中途重启不叠加。''',
    html='''<div class="pg">
  <svg viewBox="0 0 56 56" width="78" height="78">
    <circle cx="28" cy="28" r="22" stroke="rgba(255,255,255,.1)" stroke-width="5" fill="none"/>
    <circle class="pg-arc" cx="28" cy="28" r="22" stroke="url(#pgG)" stroke-width="5" fill="none"
      stroke-linecap="round" transform="rotate(-90 28 28)" stroke-dasharray="138.2" stroke-dashoffset="138.2"/>
    <defs><linearGradient id="pgG" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#9dccff"/><stop offset="1" stop-color="#5fdbA8"/>
    </linearGradient></defs>
  </svg>
  <div class="pg-n">0%</div>
</div>
<div class="pg-bar"><i></i></div>
<div class="pg-btns"><button class="btn" data-v="0">0%</button><button class="btn" data-v="45">45%</button>
<button class="btn" data-v="88">88%</button><button class="btn" data-v="100">100%</button></div>
<div class="cap">数字与弧长同源缓动</div>''',
    css='''.dz .pg{position:relative;display:grid;place-items:center;margin-bottom:10px}
.dz .pg-arc{transition:none}
.dz .pg-n{position:absolute;font-size:13px;font-weight:800;letter-spacing:-.02em}
.dz .pg-bar{width:210px;height:6px;border-radius:4px;background:rgba(255,255,255,.1);overflow:hidden}
.dz .pg-bar i{display:block;height:100%;width:0;border-radius:4px;
  background:linear-gradient(90deg,#9dccff,#5fdbA8);transition:width .7s cubic-bezier(.2,.9,.3,1)}
.dz .pg-bar.full i{background:repeating-linear-gradient(45deg,#5fdbA8 0 8px,#49c191 8px 16px);
  animation:pgStrip 0.9s linear infinite;background-size:22px 22px}
@keyframes pgStrip{to{background-position:22px 0}}
.dz .pg-btns{display:flex;gap:5px;margin-top:12px}
.dz .pg-btns .btn{height:24px;padding:0 9px;font-size:10.5px}''',
    js='''function(root){
  var arc = root.querySelector('.pg-arc'), num = root.querySelector('.pg-n'), bar = root.querySelector('.pg-bar');
  var C = 2 * Math.PI * 22, cur = 0, raf = 0;
  function set(v){
    cancelAnimationFrame(raf);
    var from = cur, to = v, t0 = performance.now(), dur = 700;
    function step(t){
      var p = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - p, 3);
      cur = from + (to - from) * e;
      arc.style.strokeDashoffset = (C * (1 - cur / 100)).toFixed(2);
      num.textContent = Math.round(cur) + '%';
      bar.querySelector('i').style.width = cur + '%';
      bar.classList.toggle('full', cur >= 99.5);
      if(p < 1) raf = requestAnimationFrame(step); else cur = to;
    }
    raf = requestAnimationFrame(step);
  }
  root.querySelectorAll('[data-v]').forEach(function(b){
    b.addEventListener('click', function(){ set(+b.dataset.v); });
  });
  setTimeout(function(){ set(88); }, 120);
}''',
    refs=refs('m3', 'antd', 'shadcn'),
    env_notes='无依赖。',
    demo_hint='点 0 / 45 / 88 / 100',
)

F31 = item(
    id='F31', slug='loading-button', name='加载按钮', cat='05-反馈', catname='反馈', diff='★☆☆', tag='反馈',
    mech='按钮进入 loading 时宽度锁定（避免塌陷），文字换成三点脉冲 + 进度描边；完成后打勾回弹 1.06 再复原。',
    params='宽度锁定用 min-width · 三点脉冲 1.1s · 成功回弹 220ms scale 1.06',
    verify='loading 期间宽度不变；连点只触发一次；成功后按钮可再次点击。',
    steps=['点击立即 disabled + 记录当前 offsetWidth 作为 min-width。'],
    redline=['不许 loading 时还能重复提交。'],
    fails=[('按钮宽度跳一下', '只把文字换成小圆点', '先锁 min-width 再改内容')],
    prompt='''做加载按钮：三态 idle → loading → success → idle。
【要求】进入 loading 前记录按钮 offsetWidth 并设为 min-width（宽度不跳）；loading 时文字替换为三点脉冲动画；
1.4s 后变 success（打勾 + scale 1.06 回弹 220ms），再过 900ms 回到 idle。
【约束】loading 期间 disabled 且 cursor 为 progress；重复点击只触发一次。
【自检】三态切换宽度差 0；连点 5 次只发一次请求；成功动画只播一次。''',
    html='''<button class="btn pri lb" id="lb"><span class="lb-tx">提交</span></button>
<div class="cap">宽度锁定，三态切换不跳</div>''',
    css='''.dz .lb{height:32px;padding:0 20px;font-size:11.5px;min-width:88px;position:relative;overflow:hidden}
.dz .lb.loading{color:transparent;pointer-events:none;cursor:progress}
.dz .lb .dots{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;gap:3px}
.dz .lb .dots i{width:5px;height:5px;border-radius:50%;background:#06121c;animation:lbPulse 1.1s infinite ease-in-out}
.dz .lb .dots i:nth-child(2){animation-delay:.16s}
.dz .lb .dots i:nth-child(3){animation-delay:.32s}
@keyframes lbPulse{0%,80%,100%{opacity:.28;transform:scale(.8)}40%{opacity:1;transform:scale(1.1)}}
.dz .lb.done{background:var(--ok);transform:scale(1.06);transition:transform .22s var(--spring),background .2s}
.dz .lb .tick{font-size:13px}''',
    js='''function(root){
  var b = root.querySelector('#lb'), busy = false;
  var idle = b.innerHTML;
  b.addEventListener('click', function(){
    if(busy) return;
    busy = true;
    var w = b.offsetWidth;
    b.style.minWidth = w + 'px';
    b.classList.add('loading');
    b.innerHTML = '<span class="dots"><i></i><i></i><i></i></span>';
    setTimeout(function(){
      b.classList.remove('loading'); b.classList.add('done');
      b.innerHTML = '<span class="tick">✓</span>';
      setTimeout(function(){
        b.classList.remove('done'); b.innerHTML = idle;
        b.style.minWidth = ''; busy = false;
      }, 900);
    }, 1400);
  });
}''',
    refs=refs('shadcn', 'antd', 'm3'),
    env_notes='无依赖。',
    demo_hint='点按钮看三态',
)

add(F25, F26, F27, F28, F29, F30, F31)
