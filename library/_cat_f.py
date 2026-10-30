# -*- coding: utf-8 -*-
"""F43–F46：应用模板"""
from _cat_base import item, add, refs

F43 = item(
    id='F43', slug='onboarding', name='引导页', cat='08-应用模板', catname='应用模板', diff='★★☆', tag='模板',
    mech='三屏引导：横向滑动 + 插画逐屏入场（同屏元素错峰 70ms）+ 底部进度胶囊；最后一屏按钮变「开始使用」。',
    params='每屏 100% 宽 · 滑动 380ms · 元素错峰 70ms · 进度胶囊 18/6px',
    verify='滑到第三屏按钮文案切换；进度胶囊跟随；滑动与点击同步。',
    steps=['容器 width: n×100%，track translateX；插画用 SVG 与主题色渐变，避免外部图片。'],
    redline=['不许引导页超过 3 屏（第 4 屏开始没人看）。'],
    fails=[('滑动后进度不更新', '只用 CSS scroll-snap 没有同步状态', 'scroll 事件换算 index')],
    prompt='''做三屏引导页：每屏插图（SVG 线描/渐变）+ 标题 + 一句说明。
【滑动】容器宽 300%，track 用 translateX(-i*100%)，380ms；支持手指左右拖拽超过 50px 切换。
【入场】每屏激活时内部元素 opacity+translateY(10px) 逐项 70ms 错峰进入。
【底部】进度胶囊：当前项宽 18 其余 6，颜色主题色；按钮末屏文案改为「开始使用」。
【自检】三屏内容不串；进度与当前屏一致；拖拽与点击结果一致；末屏按钮文案正确。''',
    html='''<div class="ob">
  <div class="ob-vp"><div class="ob-track" id="obTrack">
    <div class="ob-p"><svg viewBox="0 0 80 60" fill="none" stroke="#9dccff" stroke-width="2"
      stroke-linecap="round"><rect x="12" y="14" width="56" height="34" rx="6"/><path d="M24 30h18M24 38h28"/></svg>
      <h3>素材即代码</h3><p>每条素材都带可直接复制的实现与提示词</p></div>
    <div class="ob-p"><svg viewBox="0 0 80 60" fill="none" stroke="#5fdbA8" stroke-width="2"
      stroke-linecap="round"><circle cx="40" cy="30" r="16"/><path d="M33 30l5 5 10-11"/></svg>
      <h3>效果可验</h3><p>每条素材都有判据与失败指纹，改坏了能一眼看出</p></div>
    <div class="ob-p"><svg viewBox="0 0 80 60" fill="none" stroke="#c9a0ff" stroke-width="2"
      stroke-linecap="round"><path d="M18 42l14-16 10 9 20-20"/><path d="M18 48h44"/></svg>
      <h3>离线可用</h3><p>全部素材随 APK 内置，断网也能打开</p></div>
  </div></div>
  <div class="ob-dots" id="obDots"><i class="on"></i><i></i><i></i></div>
  <button class="btn pri ob-next" id="obNext">下一步</button>
</div>
<div class="cap">左右拖拽或点「下一步」</div>''',
    css='''.dz .ob{position:absolute;inset:0;display:flex;flex-direction:column;padding:9px 12px 10px}
.dz .ob-vp{flex:1;overflow:hidden}
.dz .ob-track{display:flex;width:300%;height:100%;transition:transform .38s var(--ease)}
.dz .ob-p{width:33.333%;padding-right:12px;display:flex;flex-direction:column;justify-content:center;align-items:flex-start}
.dz .ob-p svg{width:52px;height:40px;margin-bottom:6px;opacity:0;transform:translateY(10px)}
.dz .ob-p h3{font-size:12px;margin-bottom:4px;opacity:0;transform:translateY(10px)}
.dz .ob-p p{font-size:10px;color:var(--dim);line-height:1.65;opacity:0;transform:translateY(10px)}
.dz .ob-p.act svg,.dz .ob-p.act h3,.dz .ob-p.act p{animation:obIn .42s var(--ease) forwards}
.dz .ob-p.act h3{animation-delay:70ms}
.dz .ob-p.act p{animation-delay:140ms}
@keyframes obIn{to{opacity:1;transform:none}}
.dz .ob-dots{display:flex;gap:5px;margin:5px 0 7px}
.dz .ob-dots i{width:6px;height:6px;border-radius:99px;background:rgba(255,255,255,.2);transition:.3s var(--ease)}
.dz .ob-dots i.on{width:18px;background:var(--acc)}
.dz .ob-next{height:28px;font-size:11px;width:100%}''',
    js='''function(root){
  var track = root.querySelector('#obTrack'), dots = [...root.querySelectorAll('#obDots i')],
      next = root.querySelector('#obNext'), vp = root.querySelector('.ob-vp'),
      ps = [...root.querySelectorAll('.ob-p')];
  var i = 0;
  function go(n){
    i = Math.max(0, Math.min(ps.length-1, n));
    track.style.transform = 'translateX(' + (-i * 100/ps.length) + '%)';
    dots.forEach(function(d, k){ d.classList.toggle('on', k === i); });
    ps.forEach(function(p, k){ p.classList.toggle('act', k === i); });
    next.textContent = i === ps.length - 1 ? '开始使用' : '下一步';
  }
  next.addEventListener('click', function(){ go(i + 1 >= ps.length ? 0 : i + 1); });
  var sx = 0, dx = 0, drag = false;
  vp.addEventListener('pointerdown', function(e){ drag = true; sx = e.clientX; track.style.transition = 'none'; });
  window.addEventListener('pointermove', function(e){
    if(!drag) return;
    dx = e.clientX - sx;
    track.style.transform = 'translateX(calc(' + (-i * 100/ps.length) + '% + ' + dx + 'px))';
  });
  window.addEventListener('pointerup', function(){
    if(!drag) return;
    drag = false; track.style.transition = '';
    if(dx < -50) go(i+1); else if(dx > 50) go(i-1); else go(i);
    dx = 0;
  });
  requestAnimationFrame(function(){ go(0); });
}''',
    refs=refs('ionic', 'hig', 'm3'),
    env_notes='无依赖。',
    demo_hint='拖拽或点下一步',
)

F44 = item(
    id='F44', slug='login', name='登录页', cat='08-应用模板', catname='应用模板', diff='★★☆', tag='模板',
    mech='登录表单的负向反馈：字段聚焦时标签上浮，错误时输入框描边抖动 320ms 并显示行内错误；'
         '提交中按钮锁宽 + 三点脉冲。',
    params='标签上浮 200ms · 抖动 320ms ±6px · 按钮锁宽 · 错误描边 1.5px',
    verify='空提交两条错误同时出现；抖动只播一次；合法提交进入 loading 不重复触发。',
    steps=['错误提示占位要预留高度（min-height），否则出现时会把下面的按钮顶下去。'],
    redline=['不许用 alert 展示表单错误。'],
    fails=[('抖动连成一片', '每次输入都重播', '只在提交时增加 shake 类，动画结束移除')],
    prompt='''做登录页：邮箱 + 密码 + 记住我 + 登录按钮 + 「用验证码登录」。
【焦点】输入框聚焦时标签从占位位置缩到左上 9.5px（200ms），描边变主题色。
【错误】提交时校验：空/格式错误 → 输入框描边红色 + 抖动 320ms（±6px，只播一次）+ 行内错误文案（预留高度）。
【提交】校验通过后按钮锁宽并显示三点脉冲 1.2s，期间不可重复点击。
【自检】两个字段同时错误时抖动不叠加；错误文案出现不推动布局；连点只提交一次。''',
    html='''<div class="lg">
  <div class="lg-t">欢迎回来</div>
  <div class="lg-s">登录以同步你的素材库</div>
  <label class="lg-f"><input type="email" placeholder=" " value=""><span>邮箱</span><em>请输入邮箱</em></label>
  <label class="lg-f"><input type="password" placeholder=" "><span>密码</span><em>密码至少 6 位</em></label>
  <div class="lg-row"><label class="lg-cb"><input type="checkbox" checked><i></i>记住我</label><a>忘记密码？</a></div>
  <button class="btn pri lg-go">登录</button>
  <div class="lg-alt">用验证码登录</div>
</div>
<div class="cap">直接点登录，看错误与抖动</div>''',
    css='''.dz .lg{width:222px}
.dz .lg-t{font-size:13px;font-weight:800}
.dz .lg-s{font-size:9.5px;color:var(--dim);margin:2px 0 7px}
.dz .lg-f{position:relative;display:block;margin-bottom:8px}
.dz .lg-f input{width:100%;height:28px;border-radius:9px;background:rgba(255,255,255,.05);
  border:1.5px solid var(--line);padding:10px 9px 0;font-size:11px;color:var(--ink);outline:none;transition:border-color .2s}
.dz .lg-f input:focus{border-color:var(--acc)}
.dz .lg-f span{position:absolute;left:10px;top:9px;font-size:10.5px;color:var(--dim);pointer-events:none;
  transition:.2s var(--ease)}
.dz .lg-f input:focus + span,.dz .lg-f input:not(:placeholder-shown) + span{top:3px;font-size:8px;color:var(--acc)}
.dz .lg-f em{position:absolute;left:2px;bottom:-10px;font-style:normal;font-size:8.5px;color:var(--danger);
  opacity:0;transition:opacity .18s;min-height:0}
.dz .lg-f.bad input{border-color:var(--danger)}
.dz .lg-f.bad em{opacity:1}
.dz .lg-f.bad{animation:lgShake .32s var(--ease)}
@keyframes lgShake{0%,100%{transform:none}20%{transform:translateX(-6px)}40%{transform:translateX(5px)}
  60%{transform:translateX(-3px)}80%{transform:translateX(2px)}}
.dz .lg-row{display:flex;align-items:center;justify-content:space-between;font-size:9px;color:var(--dim);margin:10px 0 7px}
.dz .lg-row a{color:var(--acc);cursor:pointer}
.dz .lg-cb{display:flex;align-items:center;gap:5px;cursor:pointer}
.dz .lg-cb input{display:none}
.dz .lg-cb i{width:12px;height:12px;border-radius:4px;border:1.5px solid var(--line2);transition:.16s}
.dz .lg-cb input:checked + i{background:var(--acc);border-color:var(--acc)}
.dz .lg-go{width:100%;height:28px;font-size:11px}
.dz .lg-alt{text-align:center;font-size:9.5px;color:var(--dim);margin-top:7px;cursor:pointer}''',
    js='''function(root){
  var fs = [...root.querySelectorAll('.lg-f')], go = root.querySelector('.lg-go');
  var busy = false;
  go.addEventListener('click', function(){
    if(busy) return;
    var bad = 0;
    fs.forEach(function(f){
      var v = f.querySelector('input').value.trim();
      var ok = f.querySelector('input').type === 'email' ? /^[^@]+@[^@]+\\.[^@]+$/.test(v) : v.length >= 6;
      f.classList.remove('bad'); void f.offsetWidth;
      if(!ok){ f.classList.add('bad'); bad++; }
    });
    if(bad) return;
    busy = true;
    var w = go.offsetWidth;
    go.style.minWidth = w + 'px';
    go.style.color = 'transparent';
    go.innerHTML = '<span class="dots" style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;gap:3px">' +
      '<i style="width:5px;height:5px;border-radius:50%;background:#06121c;animation:lbPulse 1.1s infinite .0s"></i>' +
      '<i style="width:5px;height:5px;border-radius:50%;background:#06121c;animation:lbPulse 1.1s infinite .16s"></i>' +
      '<i style="width:5px;height:5px;border-radius:50%;background:#06121c;animation:lbPulse 1.1s infinite .32s"></i></span>';
    setTimeout(function(){
      go.style.color = ''; go.style.minWidth = ''; go.textContent = '登录'; busy = false;
      go.textContent = '登录成功 ✓';
    }, 1200);
  });
  root.querySelectorAll('.lg-f input').forEach(function(inp){
    inp.addEventListener('input', function(){ inp.closest('.lg-f').classList.remove('bad'); });
  });
}''',
    refs=refs('shadcn', 'm3', 'antd'),
    env_notes='无依赖。',
    demo_hint='空着点「登录」',
)

F45 = item(
    id='F45', slug='settings', name='设置页', cat='08-应用模板', catname='应用模板', diff='★★☆', tag='模板',
    mech='设置项的组合：开关行（点击整行切换）、带值行、危险行；分组标题小写字母间距；切换开关有 200ms 弹性位移。',
    params='行高 38 · 开关 34×19 · 圆钮位移 15px/220ms 弹簧 · 分组间距 14',
    verify='点整行也能切开关；状态即时反映；危险项有二次确认。',
    steps=['把行做成 <label> 让点击区域覆盖整行，键盘也能空格切换。'],
    redline=['不许开关只有 8px 的可点区域（手指点不中）。'],
    fails=[('开关状态与视觉不同步', '用 CSS :checked 但 DOM 状态被 JS 改了', '状态只由一个来源驱动')],
    prompt='''做设置页：三个分组（通用 / 通知 / 危险区）。
【开关】34×19 圆角 99，圆钮 15px，切换 220ms 弹簧；点击整行可切换（用 label 包裹），键盘空格也能切。
【行样式】行高 38，左侧标题 + 右侧值/开关/箭头，分割线从标题起点开始，最后一行无线。
【危险】「清除全部数据」红色文字，点击弹二次确认。
【自检】点整行切换生效；连续点击 20 次状态不丢；键盘可达；危险项必须二次确认。''',
    html='''<div class="sg">
  <div class="sg-h">通用</div>
  <div class="sg-g">
    <label class="sg-r"><span>深色外观</span><input type="checkbox" checked><i></i></label>
    <label class="sg-r"><span>启动时恢复上次位置</span><input type="checkbox"><i></i></label>
    <div class="sg-r"><span>字号</span><b>标准 ›</b></div>
  </div>
  <div class="sg-h">通知</div>
  <div class="sg-g">
    <label class="sg-r"><span>素材更新提醒</span><input type="checkbox" checked><i></i></label>
  </div>
  <div class="sg-g"><div class="sg-r danger">清除全部数据</div></div>
</div>
<div class="cap">点整行都能切换</div>''',
    css='''.dz .sg{width:236px}
.dz .sg-h{font-size:9.5px;color:var(--dim);letter-spacing:.1em;margin:0 6px 5px}
.dz .sg-g{border-radius:11px;background:var(--card);border:1px solid var(--line);overflow:hidden;margin-bottom:7px}
.dz .sg-r{position:relative;display:flex;align-items:center;justify-content:space-between;height:28px;
  padding:0 10px;font-size:10.5px;color:var(--soft);cursor:pointer}
.dz .sg-r + .sg-r{border-top:1px solid rgba(255,255,255,.06)}
.dz .sg-r b{font-weight:400;color:var(--dim);font-size:10px}
.dz .sg-r input{display:none}
.dz .sg-r i{width:32px;height:18px;border-radius:99px;background:rgba(255,255,255,.14);position:relative;
  transition:background .2s;flex:0 0 auto}
.dz .sg-r i::after{content:"";position:absolute;left:2px;top:2px;width:14px;height:14px;border-radius:50%;
  background:#fff;transition:transform .22s var(--spring)}
.dz .sg-r input:checked + i{background:var(--acc)}
.dz .sg-r input:checked + i::after{transform:translateX(14px)}
.dz .sg-r.danger{color:var(--danger);justify-content:center}''',
    js='''function(root){
  root.querySelector('.sg-r.danger').addEventListener('click', function(){
    this.textContent = this.dataset.w || (this.dataset.w = this.textContent);
    this.textContent = '再点一次确认';
    var self = this;
    setTimeout(function(){ self.textContent = self.dataset.w; }, 1800);
  });
}''',
    refs=refs('hig', 'miuix', 'm3'),
    env_notes='无依赖。',
    demo_hint='点行切换开关',
)

F46 = item(
    id='F46', slug='profile', name='个人主页', cat='08-应用模板', catname='应用模板', diff='★★☆', tag='模板',
    mech='头图视差 + 头像重叠 + 数字统计：滚动时头图按 0.35 系数上移并轻微放大，头像与内容卡上浮，'
         '数字错峰滚动到目标值。',
    params='头图视差 0.35 · 头图缩放 1→1.08 · 头像 52px 边框 2px · 数字错峰 90ms',
    verify='滚动时头图不露出底部空隙（放大补偿）；头像始终压在头图与内容卡之间。',
    steps=['头图容器 overflow:hidden + 内部 img/div scale(1.1)，位移不超过补偿量就不会露边。'],
    redline=['不许视差位移超过放大补偿（会露出空白边）。'],
    fails=[('头图下缘露黑边', 'scale 不够大', 'scale = 1 + 位移/高度 × 1.3')],
    prompt='''做个人主页：头图（渐变）+ 头像 + 昵称 + 三个统计数字 + 内容列表。
【视差】页面滚动时头图 translateY(scrollTop*0.35) 且 scale 从 1 增到 1.08（补偿位移，不露边）；标题透明度随滚动降低。
【层次】头像 52px、边框 2px 深色、margin-top -26px 压在两层之间；内容卡圆角 14。
【数字】三个统计（素材 46 / 分类 8 / 收藏 12）从 0 滚到目标，逐项 90ms 错峰。
【自检】滚到 120px 时头图无空隙；头像层级正确；数字最终准确。''',
    html='''<div class="pf"><div class="pf-sc" id="pfSc">
  <div class="pf-hd"><div class="pf-img"></div><div class="pf-mask"></div></div>
  <div class="pf-body">
    <div class="pf-av">林</div>
    <div class="pf-n">林小满 <em>Pro</em></div>
    <div class="pf-b">产品设计师 · 用素材拼界面</div>
    <div class="pf-stats" id="pfStats"></div>
    <div class="pf-grid"><div></div><div></div><div></div><div></div></div>
  </div>
</div></div>
<div class="cap">向上滚动看头图视差</div>''',
    css='''.dz .pf{position:absolute;inset:0;overflow:hidden}
.dz .pf-sc{position:absolute;inset:0;overflow:auto;scrollbar-width:none}
.dz .pf-sc::-webkit-scrollbar{display:none}
.dz .pf-hd{position:relative;height:86px;overflow:hidden}
.dz .pf-img{position:absolute;inset:-10px;background:
  radial-gradient(120% 120% at 20% 0%,#3f6fa8,transparent 60%),
  radial-gradient(90% 90% at 80% 20%,#4f9d84,transparent 60%),#131c25;
  transform-origin:center top;will-change:transform}
.dz .pf-mask{position:absolute;inset:0;background:linear-gradient(180deg,transparent,rgba(13,20,27,.85))}
.dz .pf-body{position:relative;margin-top:-26px;padding:0 12px 14px}
.dz .pf-av{width:48px;height:48px;border-radius:50%;border:2px solid #0d141b;display:grid;place-items:center;
  font-weight:800;font-size:15px;color:#06121c;background:linear-gradient(150deg,#9dccff,#5fdbA8)}
.dz .pf-n{font-size:13px;font-weight:800;margin-top:6px;display:flex;align-items:center;gap:5px}
.dz .pf-n em{font-style:normal;font-size:8px;font-weight:700;color:#06121c;background:var(--acc);
  padding:1px 5px;border-radius:4px}
.dz .pf-b{font-size:9.5px;color:var(--dim);margin:2px 0 10px}
.dz .pf-stats{display:flex;gap:18px;margin-bottom:10px}
.dz .pf-stats div{display:flex;flex-direction:column;gap:1px}
.dz .pf-stats b{font-size:13px;font-variant-numeric:tabular-nums}
.dz .pf-stats span{font-size:8.5px;color:var(--dim)}
.dz .pf-grid{display:grid;grid-template-columns:1fr 1fr;gap:7px}
.dz .pf-grid div{height:42px;border-radius:10px;border:1px solid var(--line);
  background:linear-gradient(150deg,rgba(157,204,255,.14),transparent)}''',
    js='''function(root){
  var sc = root.querySelector('#pfSc'), img = root.querySelector('.pf-img'), mask = root.querySelector('.pf-mask');
  var st = root.querySelector('#pfStats');
  var stats = [['46','素材'],['8','分类'],['12','收藏']];
  st.innerHTML = stats.map(function(s){
    return '<div><b data-v="' + s[0] + '">0</b><span>' + s[1] + '</span></div>';
  }).join('');
  [...st.querySelectorAll('b')].forEach(function(b, i){
    var to = +b.dataset.v, t0 = performance.now();
    setTimeout(function(){
      var s0 = performance.now();
      (function tick(t){
        var p = Math.min(1, (t - s0) / 900), e = 1 - Math.pow(1 - p, 3);
        b.textContent = Math.round(to * e);
        if(p < 1) requestAnimationFrame(tick);
      })(s0);
    }, i * 90);
  });
  var pending = false;
  sc.addEventListener('scroll', function(){
    if(pending) return; pending = true;
    requestAnimationFrame(function(){
      var y = Math.min(sc.scrollTop, 86);
      img.style.transform = 'translate3d(0,' + (y * .35).toFixed(1) + 'px,0) scale(' + (1 + y/86*.12).toFixed(3) + ')';
      mask.style.opacity = (1 - y / 120).toFixed(2);
      pending = false;
    });
  }, {passive:true});
}''',
    refs=refs('hig', 'miuix', 'm3'),
    env_notes='无依赖。',
    demo_hint='滚动看头图视差',
)

add(F43, F44, F45, F46)
