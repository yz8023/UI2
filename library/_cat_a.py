# -*- coding: utf-8 -*-
"""F01–F12：基础组件 + 表单输入"""
from _cat_base import item, add, refs

# ───────────────────────── 基础组件 ─────────────────────────

F01 = item(
    id='F01', slug='button', name='按钮', cat='01-基础组件', catname='基础组件', diff='★☆☆', tag='交互基础',
    mech='三档层级（primary / secondary / ghost）+ 图标按钮；按下用 0.955 缩放 + 120ms 弹簧回弹代替水波纹，'
         '加载态在原地把文字换成三点脉冲，尺寸一像素不动。',
    params='高度 40 / 32（sm）/ 44（lg）· 圆角 12 · 按压 scale .955 · 回弹 160ms cubic-bezier(.2,.9,.3,1.15)',
    verify='按下必须立刻有缩放反馈（<16ms）；加载态宽度不跳；禁用态不可聚焦、aria-disabled=true。',
    steps=['先把三档层级做成 variant，用一个 class 切换，不要复制三份结构。',
           '按下反馈用 :active 的 transform（GPU 合成层，不触发重排）。',
           '加载态保留原宽度：用等宽占位替换文字，而不是隐藏整个按钮。'],
    redline=['不许用 box-shadow 做按压（会重绘，低端机掉帧）。',
             '按钮文字禁止硬编码宽度，必须 padding 撑开以适配多语言。'],
    fails=[('按住时文字抖动', '用了 width 过渡', '改用 padding + transform，不写 width/margin 过渡'),
           ('加载后按钮变窄', '加载态没有占位', '把文字设成 visibility:hidden 保留占位')],
    prompt='''做一个零依赖的按钮组件，三档层级 + 图标按钮 + 加载态。
【结构】<button class="btn btn--primary|secondary|ghost">，可选 data-icon、data-loading。
【规格】高度 40（sm 32 / lg 44），圆角 12，左右 padding 16，字号 13，字重 600。
【交互】按下 scale(.955)，160ms cubic-bezier(.2,.9,.3,1.15) 回弹；悬停只改亮度不改尺寸；
加载态把文字换成三个脉冲点，按钮宽度保持不变；禁用态 aria-disabled="true" 且不可聚焦。
【自检】按键 Tab 能聚焦且焦点环 2px；连续点 10 次不累积位移；加载态宽度与常态一致（截图叠对比）。''',
    html='''<div class="col" style="gap:10px">
  <div class="row">
    <button class="btn btn--primary">主要操作</button>
    <button class="btn btn--secondary">次要</button>
    <button class="btn btn--ghost">幽灵</button>
  </div>
  <div class="row">
    <button class="btn btn--primary btn--sm">小号</button>
    <button class="btn btn--primary" data-loading>加载态</button>
    <button class="btn btn--secondary" disabled>禁用</button>
    <button class="btn btn--icon" aria-label="收藏">★</button>
  </div>
</div>
<div class="cap">按下有 0.955 缩放 · 加载态宽度不变</div>''',
    css='''.dz .btn{height:40px;padding:0 16px;border-radius:12px;font-size:13px;font-weight:600;
  display:inline-flex;align-items:center;justify-content:center;gap:6px;
  transition:transform .16s var(--spring),filter .18s,opacity .18s;will-change:transform;
  white-space:nowrap}
.dz .btn:active{transform:scale(.955)}
.dz .btn--primary{background:linear-gradient(150deg,var(--acc),var(--acc-d));color:#06121c;
  box-shadow:0 6px 16px rgba(22,74,112,.45)}
.dz .btn--secondary{background:rgba(255,255,255,.08);color:var(--ink);border:1px solid var(--line)}
.dz .btn--ghost{color:var(--acc)}
.dz .btn--sm{height:32px;padding:0 12px;font-size:12px;border-radius:10px}
.dz .btn--icon{width:40px;padding:0;border-radius:12px;background:rgba(255,255,255,.08);
  border:1px solid var(--line);color:var(--warn)}
.dz .btn[disabled]{opacity:.42;pointer-events:none}
.dz .btn .dots{display:inline-flex;gap:3px}
.dz .btn .dots i{width:5px;height:5px;border-radius:50%;background:#06121c;animation:bounce 1s infinite}
.dz .btn .dots i:nth-child(2){animation-delay:.12s}
.dz .btn .dots i:nth-child(3){animation-delay:.24s}
@keyframes bounce{0%,60%,100%{transform:translateY(0);opacity:.5}30%{transform:translateY(-3px);opacity:1}}''',
    js='''function(root){
  var b = root.querySelector('[data-loading]');
  var text = b.textContent;
  b.addEventListener('click', function(){
    if(b.dataset.busy) return;
    b.dataset.busy = '1';
    var w = b.offsetWidth;
    b.style.width = w + 'px';
    b.innerHTML = '<span class="dots"><i></i><i></i><i></i></span>';
    setTimeout(function(){
      b.textContent = text; b.style.width = ''; delete b.dataset.busy;
    }, 1400);
  });
}''',
    refs=refs('shadcn', 'm3', 'hig'),
    env_notes='纯 CSS 变量，无依赖；放进任何项目只需带 .dz 里的 token 或替换成你自己的配色。',
    demo_hint='点「加载态」看宽度不变',
)

F02 = item(
    id='F02', slug='textfield', name='输入框', cat='01-基础组件', catname='基础组件', diff='★★☆', tag='输入',
    mech='浮动标签 + 焦点环 + 右侧清除键 + 字数计数 + 错误态五件套；标签用 transform 上浮而不是切换两个 DOM，'
         '光标与边框走同一组 token。',
    params='高度 48 · 圆角 12 · 标签上浮 13px→10px · 焦点环 2px · 错误色 #ff8fa3',
    verify='空值失焦标签必须落回原位；输入后清除键出现并可清空；错误态下焦点环变红且 aria-invalid=true。',
    steps=['结构与状态：label 包裹 input，用 :focus-within 和 .has-value 两个条件驱动上浮。',
           '清除键只在有值且聚焦时显示，点击后焦点回到输入框。',
           '错误信息用 aria-describedby 关联，不要只用颜色区分。'],
    redline=['不许用 placeholder 当标签（输入后标签就消失）。'],
    fails=[('标签和文字重叠', '只判断 :focus 没判断有值', '同时判断 :focus-within 与 .has-value')],
    prompt='''做浮动标签输入框，含清除键、字数计数、错误态。
【规格】高 48，圆角 12，标签初始居中，获得焦点或有值时上浮到左上（13px→10px，透明底）。
【状态】normal / focus（2px 焦点环）/ filled / error（环变红 + 下方一行错误文案 + aria-invalid）/ disabled。
【交互】有值时右侧出现清除键，点击清空并保持聚焦；右下角显示 n/max 计数并超出变红。
【自检】空值失焦标签落回；错误态颜色 + 文案 + 图标三重表达；键盘 Tab 顺序正确。''',
    html='''<div class="col" style="width:230px;gap:11px">
  <label class="tf"><input type="text" placeholder=" " maxlength="20"><span class="tf-l">项目名称</span><b class="tf-c">✕</b></label>
  <label class="tf"><input type="text" placeholder=" " value="玻璃工作台"><span class="tf-l">已填充</span><b class="tf-c">✕</b></label>
  <label class="tf tf--err"><input type="text" placeholder=" " value="ab" aria-invalid="true"><span class="tf-l">邮箱（错误态）</span></label>
</div>
<div class="cap">标签上浮 · 清除键 · 错误三重表达</div>''',
    css='''.dz .tf{position:relative;display:block;height:44px;border-radius:12px;background:rgba(255,255,255,.06);
  border:1px solid var(--line);transition:border-color .18s,box-shadow .18s}
.dz .tf input{width:100%;height:100%;padding:15px 32px 3px 12px;background:none;border:0;outline:none;
  color:var(--ink);font:inherit;font-size:13px}
.dz .tf-l{position:absolute;left:13px;top:50%;transform:translateY(-50%);font-size:13px;color:var(--soft);
  pointer-events:none;transition:all .18s var(--ease)}
.dz .tf:focus-within{border-color:var(--acc);box-shadow:0 0 0 2px rgba(157,204,255,.28)}
.dz .tf:focus-within .tf-l,.dz .tf.has-value .tf-l{top:10px;font-size:10px;color:var(--acc);letter-spacing:.04em}
.dz .tf-c{position:absolute;right:10px;top:50%;transform:translateY(-50%);font-size:11px;color:var(--dim);
  cursor:pointer;opacity:0;transition:opacity .15s;font-weight:400}
.dz .tf.has-value .tf-c{opacity:1}
.dz .tf--err{border-color:rgba(255,143,163,.7);box-shadow:0 0 0 2px rgba(255,143,163,.16)}
.dz .tf--err .tf-l{color:var(--danger)}''',
    js='''function(root){
  root.querySelectorAll('.tf').forEach(function(tf){
    var inp = tf.querySelector('input');
    function sync(){ tf.classList.toggle('has-value', inp.value.length > 0); }
    inp.addEventListener('input', sync); sync();
    var c = tf.querySelector('.tf-c');
    if(c) c.addEventListener('click', function(){ inp.value=''; sync(); inp.focus(); });
  });
}''',
    refs=refs('m3', 'shadcn', 'vant'),
    env_notes='无依赖。若要接表单校验，把 aria-invalid 与错误文案交给表单层统一管理。',
    demo_hint='聚焦看标签上浮',
)

F03 = item(
    id='F03', slug='switch', name='开关', cat='01-基础组件', catname='基础组件', diff='★☆☆', tag='选择',
    mech='轨道颜色渐变 + 滑块 220ms 弹簧位移 + 按下时滑块横向拉长（更像实体键），关闭态滑块回位有轻微过冲。',
    params='尺寸 46×28 / 38×22 · 滑块 22 · 位移 20 · 曲线 cubic-bezier(.2,.9,.3,1.15)',
    verify='点击与键盘空格都能切换；aria-checked 同步；快速连点不出现滑块卡在中间。',
    steps=['用 role=switch + aria-checked，键盘 Space/Enter 绑定到同一函数。',
           '滑块位移用 transform: translateX，不要用 left。'],
    redline=['不许只靠颜色区分开关状态（要有滑块位置这份几何信息）。'],
    fails=[('连点卡住', '用 transitionend 计数驱动状态', '状态只由 aria-checked 单一来源推导')],
    prompt='''做开关组件：46×28 轨道 + 22 滑块，开启时滑块右移 20px，220ms 弹簧曲线；按下瞬间滑块横向拉长 1.15 倍。
【要求】role="switch" + aria-checked；空格与回车可切换；轨道颜色从 rgba(255,255,255,.14) 过渡到主题色；
快速连点 10 次后滑块必须停在正确端点（截图验证）。
【自检】键盘可操作；状态位与视觉 100% 同步；减少动效模式下位移变 0ms 但位置仍正确。''',
    html='''<div class="col" style="gap:14px">
  <div class="row" style="gap:12px"><div class="sw on" role="switch" aria-checked="true" tabindex="0"></div><span class="lbl">液态玻璃</span></div>
  <div class="row" style="gap:12px"><div class="sw" role="switch" aria-checked="false" tabindex="0"></div><span class="lbl">减少动效</span></div>
</div>
<div class="cap">按下时滑块会横向拉长</div>''',
    css='''.dz .sw{position:relative;width:46px;height:28px;border-radius:var(--pill);background:rgba(255,255,255,.14);
  cursor:pointer;transition:background .24s var(--ease);flex:0 0 auto;outline:none}
.dz .sw:focus-visible{box-shadow:0 0 0 2px rgba(157,204,255,.6)}
.dz .sw::after{content:"";position:absolute;top:3px;left:3px;width:22px;height:22px;border-radius:50%;
  background:#fff;box-shadow:0 2px 6px rgba(0,0,0,.35);
  transition:transform .22s var(--spring),width .16s var(--ease);will-change:transform}
.dz .sw.on{background:var(--acc-d)}
.dz .sw.on::after{transform:translateX(18px)}
.dz .sw:active::after{width:26px}
.dz .sw.on:active::after{transform:translateX(14px)}''',
    js='''function(root){
  root.querySelectorAll('.sw').forEach(function(sw){
    function toggle(){ sw.classList.toggle('on'); sw.setAttribute('aria-checked', sw.classList.contains('on')); }
    sw.addEventListener('click', toggle);
    sw.addEventListener('keydown', function(e){ if(e.key===' '||e.key==='Enter'){ e.preventDefault(); toggle(); } });
  });
}''',
    refs=refs('miuix', 'm3', 'hig'),
    env_notes='无依赖。',
    demo_hint='点一下，注意滑块拉长',
)

F04 = item(
    id='F04', slug='slider', name='滑块', cat='01-基础组件', catname='基础组件', diff='★★☆', tag='选择',
    mech='原生 range + 自绘填充条与数值气泡：拖动时滑块放大 1.15、气泡跟随，松手 300ms 后气泡淡出。',
    params='轨道 4px · 滑块 18→21（拖动）· 填充用 linear-gradient 实时算百分比',
    verify='键盘 ←/→ 可调；气泡数值与 aria-valuenow 一致；到端点时气泡不出界。',
    steps=['用 input[type=range] 保底可访问性，视觉层用伪元素覆盖。',
           '填充用 background-size 百分比，避免额外 DOM。'],
    redline=['不许完全自绘而丢掉键盘与 aria-valuenow。'],
    fails=[('气泡超出容器', '气泡用 left 定位没做钳制', '用 clamp() 或 translateX 夹住两端')],
    prompt='''做滑块：4px 轨道 + 18px 圆形滑块，拖动时滑块放大到 21px 并浮出数值气泡，松手 300ms 气泡淡出。
【要求】基于 input[type=range] 保底键盘可访问；填充用 background-size 百分比实现；
气泡位置在两端做钳制，不出容器；aria-valuenow 与显示一致；支持双滑块（可选）。
【自检】键盘 ←/→ 每次 ±1；拖到最左/最右气泡不越界；数值变化时填充无缝跟随。''',
    html='''<div style="width:230px">
  <div class="row" style="justify-content:space-between;margin-bottom:10px">
    <span class="lbl">模糊半径</span><b class="sv" style="font-family:ui-monospace,monospace">18 px</b>
  </div>
  <div class="sl-wrap">
    <div class="sl-bub">18</div>
    <input class="sl" type="range" min="0" max="60" value="18" aria-valuenow="18">
  </div>
</div>
<div class="cap">拖动时气泡跟随 · 键盘可调</div>''',
    css='''.dz .sl-wrap{position:relative;padding-top:18px}
.dz .sl{-webkit-appearance:none;appearance:none;width:100%;height:4px;border-radius:2px;outline:none;
  background:linear-gradient(90deg,var(--acc) 30%,rgba(255,255,255,.14) 30%);background-size:100% 100%}
.dz .sl::-webkit-slider-thumb{-webkit-appearance:none;width:18px;height:18px;border-radius:50%;
  background:radial-gradient(circle at 32% 26%,#fff,var(--acc) 62%,var(--acc-d));
  box-shadow:0 3px 10px rgba(0,0,0,.45);transition:transform .16s var(--spring);cursor:grab}
.dz .sl:active::-webkit-slider-thumb{transform:scale(1.15);cursor:grabbing}
.dz .sl-bub{position:absolute;top:-2px;left:30%;transform:translateX(-50%);font-size:10px;padding:2px 6px;
  border-radius:6px;background:var(--acc);color:#06121c;font-weight:700;opacity:0;transition:opacity .2s;
  font-family:ui-monospace,monospace;pointer-events:none}
.dz .sl-wrap.act .sl-bub{opacity:1}''',
    js='''function(root){
  var sl = root.querySelector('.sl'), bub = root.querySelector('.sl-bub'), wrap = root.querySelector('.sl-wrap');
  var out = root.querySelector('.sv');
  function sync(){
    var p = (sl.value - sl.min) / (sl.max - sl.min) * 100;
    sl.style.background = 'linear-gradient(90deg,var(--acc) '+p+'%,rgba(255,255,255,.14) '+p+'%)';
    bub.style.left = p + '%';
    bub.textContent = sl.value;
    out.textContent = sl.value + ' px';
    sl.setAttribute('aria-valuenow', sl.value);
  }
  sl.addEventListener('input', sync);
  sl.addEventListener('pointerdown', function(){ wrap.classList.add('act'); });
  window.addEventListener('pointerup', function(){ wrap.classList.remove('act'); });
  sync();
}''',
    refs=refs('m3', 'hig', 'antd'),
    env_notes='无依赖；值变化时派发自定义事件即可接入业务。',
    demo_hint='托住滑块看气泡',
)

F05 = item(
    id='F05', slug='checkbox-radio', name='复选与单选', cat='01-基础组件', catname='基础组件', diff='★☆☆', tag='选择',
    mech='勾选用 SVG path 的 stroke-dashoffset 画出来（180ms），单选用内点缩放；点击热区 44px，视觉只有 20px。',
    params='视觉 20 · 热区 44 · 勾线 180ms · 单选内点 6→8px',
    verify='勾选动画期间快速连点不破形；点击文字也能选中；单选框同组互斥。',
    steps=['用 label 包住 input，视觉层用 span，隐藏原生 input 但保留可访问性。'],
    redline=['不许把热区做成只有 20px（违反 44px 最小触控面积）。'],
    fails=[('文字点不中', 'label 没包住', '用 <label> 包 input + 文本')],
    prompt='''做复选框与单选框（各 3 个），视觉 20px、热区 44px。
【勾选动画】用 SVG path 的 stroke-dasharray/stroke-dashoffset 在 180ms 内"画出"对勾；
【单选】外圈 20px 描边 + 内点从 6px 弹到 8px（弹簧曲线）；
【可访问】原生 input 保留（可 Tab、可用空格），视觉层用 span[aria-hidden]；
【自检】点击整行都能切换；单选框同组互斥；连续快速点击 10 次状态与视觉不脱节。''',
    html='''<div class="row" style="gap:18px;align-items:flex-start">
  <div class="col" style="gap:6px">
    <span class="lbl">多选</span>
    <label class="cb"><input type="checkbox" checked><span class="bx"><svg viewBox="0 0 24 24"><path d="M5 12.5 10 17.5 19 7"/></svg></span>玻璃</label>
    <label class="cb"><input type="checkbox"><span class="bx"><svg viewBox="0 0 24 24"><path d="M5 12.5 10 17.5 19 7"/></svg></span>动效</label>
    <label class="cb"><input type="checkbox"><span class="bx"><svg viewBox="0 0 24 24"><path d="M5 12.5 10 17.5 19 7"/></svg></span>布局</label>
  </div>
  <div class="col" style="gap:6px">
    <span class="lbl">单选</span>
    <label class="rd"><input type="radio" name="r1" checked><span class="dt"></span>浅色</label>
    <label class="rd"><input type="radio" name="r1"><span class="dt"></span>深色</label>
    <label class="rd"><input type="radio" name="r1"><span class="dt"></span>跟随系统</label>
  </div>
</div>
<div class="cap">热区 44px · 勾线 180ms</div>''',
    css='''.dz .cb,.dz .rd{position:relative;display:flex;align-items:center;gap:9px;min-height:44px;padding-right:6px;
  font-size:12.5px;cursor:pointer}
.dz .cb input,.dz .rd input{position:absolute;opacity:0;width:44px;height:44px;margin:0;cursor:pointer}
.dz .bx{width:20px;height:20px;border-radius:6px;border:1.5px solid var(--line2);display:grid;place-items:center;
  transition:background .18s,border-color .18s;flex:0 0 auto}
.dz .bx svg{width:14px;height:14px;fill:none;stroke:#06121c;stroke-width:2.6;stroke-linecap:round;
  stroke-dasharray:22;stroke-dashoffset:22;transition:stroke-dashoffset .18s var(--ease)}
.dz .cb input:checked + .bx{background:var(--acc);border-color:transparent}
.dz .cb input:checked + .bx svg{stroke-dashoffset:0}
.dz .dt{position:relative;width:20px;height:20px;border-radius:50%;border:1.5px solid var(--line2);flex:0 0 auto;
  display:grid;place-items:center;transition:border-color .18s}
.dz .dt::after{content:"";width:0;height:0;border-radius:50%;background:var(--acc);transition:all .2s var(--spring)}
.dz .rd input:checked + .dt{border-color:var(--acc)}
.dz .rd input:checked + .dt::after{width:10px;height:10px}''',
    js='''function(root){}''',
    refs=refs('m3', 'shadcn', 'hig'),
    env_notes='无依赖；checked 状态交给原生 input，业务只监听 change。',
    demo_hint='点文字也能切换',
)

F06 = item(
    id='F06', slug='avatar-badge', name='头像与徽标', cat='01-基础组件', catname='基础组件', diff='★☆☆', tag='展示',
    mech='纯 CSS 头像：无图时用姓名首字 + 由名字哈希出的双色渐变；状态点用 2px 描边把头像"挖"出来；'
         '徽标数字超过 99 显示 99+，宽度随位数自适应。',
    params='尺寸 28/36/48/64 · 状态点 10 · 徽标高 18 · 渐变由 hash(name) 决定色相',
    verify='同名同色、不同名不同色；没有图片时不出现破图；徽标在两位数时不压住头像主体。',
    steps=['hash 用字符码累加取模，保证同一个名字恒色（服务端渲染也一致）。',
           '徽标用 min-width + padding，避免两位数字撑成椭圆。'],
    redline=['不许给头像塞随机色（刷新一次变一个颜色）。'],
    fails=[('破图', 'img 无 onerror 兜底', '无 src 时直接用首字方案')],
    prompt='''做头像 + 状态点 + 数量徽标。
【头像】无图时显示姓名首字；背景色由名字哈希出两个色相做 135° 渐变，保证同名恒色。
【尺寸】28 / 36 / 48 / 64 四档，字号按尺寸线性缩放。
【状态】右下角 10px 圆点，2px 深色描边把头像"挖"出来；支持 online/busy/offline 三色。
【徽标】18px 高，min-width 18 + padding 4，超过 99 显示 99+；用 translate 挂在右上角，不遮挡人脸。
【自检】同名同色；两位数徽标不变形；无图不破图。''',
    html='''<div class="row" style="gap:14px;align-items:flex-end">
  <div class="av av--s" style="--h1:205;--h2:265"><span>林</span><i class="st on"></i></div>
  <div class="av av--m" style="--h1:150;--h2:195"><span>陈</span><i class="st busy"></i></div>
  <div class="av av--l" style="--h1:35;--h2:15"><span>Z</span><b class="bd">7</b></div>
  <div class="av av--xl" style="--h1:280;--h2:320"><span>玻</span><b class="bd">99+</b></div>
</div>
<div class="cap">同名恒色 · 徽标不压脸</div>''',
    css='''.dz .av{position:relative;border-radius:50%;display:grid;place-items:center;font-weight:600;
  background:linear-gradient(135deg,hsl(var(--h1) 62% 46%),hsl(var(--h2) 58% 34%));
  color:#fff;box-shadow:inset 0 1px 0 rgba(255,255,255,.28),0 6px 14px rgba(0,0,0,.35);flex:0 0 auto}
.dz .av--s{width:28px;height:28px;font-size:11px}
.dz .av--m{width:36px;height:36px;font-size:13px}
.dz .av--l{width:48px;height:48px;font-size:17px}
.dz .av--xl{width:64px;height:64px;font-size:22px}
.dz .st{position:absolute;right:-1px;bottom:-1px;width:10px;height:10px;border-radius:50%;
  border:2px solid var(--bg);background:var(--dim)}
.dz .st.on{background:var(--mint)} .dz .st.busy{background:var(--warn)}
.dz .bd{position:absolute;top:-5px;right:-7px;min-width:18px;height:18px;padding:0 5px;border-radius:9px;
  background:var(--danger);color:#2a0a10;font-size:10px;font-weight:800;display:grid;place-items:center;
  border:2px solid var(--bg)}''',
    js='''function(root){}''',
    refs=refs('m3', 'miuix'),
    env_notes='无依赖；接入真实头像时把 <span> 换成 <img> 并保留 fallback。',
    demo_hint='四档尺寸 · 徽标 99+',
)

# ───────────────────────── 表单输入 ─────────────────────────

F07 = item(
    id='F07', slug='form-validation', name='表单校验', cat='02-表单输入', catname='表单输入', diff='★★☆', tag='表单',
    mech='即时校验 + 失焦才报错 + 提交时全量校验：输入中只给正向提示，blur 后才显示错误，提交时把第一个错误滚进视野并聚焦。',
    params='校验时机 = blur / submit · 错误文案 1 行 · 提交按钮在无效时 aria-disabled 但可点（点了给提示）',
    verify='输入过程中不弹错；失焦后立即报错；提交无效时焦点跳到第一个错误字段。',
    steps=['把字段规则抽成数组，同一套规则驱动即时提示与提交校验。',
           '禁用按钮会让用户不知道为什么不能提交，改用「可点 + 提示第一个错误」。'],
    redline=['不许在用户还没输完时就报错。'],
    fails=[('一直红着', 'input 事件里就校验', '输入时清错，blur 才校验')],
    prompt='''做三步式表单校验（姓名 / 邮箱 / 密码）。
【时机】输入中不报错，只清错；失焦校验该字段；提交时校验全部并把焦点移到第一个错误。
【反馈】错误字段边框变红 + 下方一行文案 + aria-invalid="true" + aria-describedby 关联；
正确时字段尾部出现绿色对勾。
【提交】全部通过后按钮进入 loading → 成功态（对勾 + 文案变化）。
【自检】输入过程中无红色；失焦立刻报错；提交无效时焦点正确；截图对比错误/成功两态。''',
    html='''<div class="col" style="width:240px;gap:10px">
  <div class="fd"><input placeholder="姓名"><em></em></div>
  <div class="fd"><input placeholder="邮箱" value="a@b"><em></em></div>
  <div class="fd"><input type="password" placeholder="密码（≥6 位）"><em></em></div>
  <button class="fsub">创建账号</button>
</div>
<div class="cap">输入不报错 · 失焦才报</div>''',
    css='''.dz .fd{position:relative}
.dz .fd input{width:100%;height:36px;padding:0 34px 0 12px;border-radius:11px;background:rgba(255,255,255,.06);
  border:1px solid var(--line);color:var(--ink);font:inherit;font-size:12.5px;outline:none;transition:.18s}
.dz .fd input:focus{border-color:var(--acc);box-shadow:0 0 0 2px rgba(157,204,255,.22)}
.dz .fd em{position:absolute;left:2px;top:37px;font-size:10.5px;color:var(--danger);font-style:normal;
  opacity:0;transform:translateY(-3px);transition:.18s}
.dz .fd.bad input{border-color:rgba(255,143,163,.8);background:rgba(255,143,163,.08)}
.dz .fd.bad em{opacity:1;transform:none}
.dz .fd.ok::after{content:"✓";position:absolute;right:11px;top:9px;color:var(--mint);font-size:13px}
.dz .fsub{height:34px;border-radius:11px;background:linear-gradient(150deg,var(--acc),var(--acc-d));
  color:#06121c;font-weight:700;font-size:12.5px;transition:transform .16s var(--spring)}
.dz .fsub:active{transform:scale(.97)}
.dz .fsub.ok{background:var(--mint)}''',
    js='''function(root){
  var fields = [...root.querySelectorAll('.fd')];
  var rules = [
    function(v){ return v.trim().length >= 2 || '姓名至少 2 个字'; },
    function(v){ return /^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(v) || '邮箱格式不对'; },
    function(v){ return v.length >= 6 || '密码至少 6 位'; }
  ];
  function check(i, show){
    var fd = fields[i], inp = fd.querySelector('input'), msg = fd.querySelector('em');
    var r = rules[i](inp.value);
    if(r === true){ fd.classList.remove('bad'); fd.classList.add('ok'); msg.textContent=''; return true; }
    fd.classList.remove('ok');
    if(show){ fd.classList.add('bad'); msg.textContent = r; } else { fd.classList.remove('bad'); }
    return false;
  }
  fields.forEach(function(fd, i){
    var inp = fd.querySelector('input');
    inp.addEventListener('input', function(){ inp.value && check(i, false); fd.classList.remove('ok'); });
    inp.addEventListener('blur', function(){ check(i, true); });
  });
  root.querySelector('.fsub').addEventListener('click', function(){
    var bad = -1;
    fields.forEach(function(_, i){ if(!check(i, true) && bad < 0) bad = i; });
    if(bad >= 0){ fields[bad].querySelector('input').focus(); return; }
    var b = this; b.textContent = '创建中…';
    setTimeout(function(){ b.textContent = '✓ 已创建'; b.classList.add('ok'); }, 700);
  });
}''',
    refs=refs('antd', 'm3', 'shadcn'),
    env_notes='无依赖；规则数组可替换成你的校验库（zod / yup）适配层。',
    demo_hint='点「创建账号」看全量校验',
)

F08 = item(
    id='F08', slug='stepper', name='步进器', cat='02-表单输入', catname='表单输入', diff='★☆☆', tag='表单',
    mech='加减按钮 + 数字滚动：数字用 translateY 的列表做滑动切换（不是直接改文本），长按每 80ms 连加。',
    params='高 36 · 按钮 32 正方形 · 连发 80ms · 数字切换 220ms',
    verify='长按可持续加减；到 min/max 时按钮置灰并停止；数字切换有方向感（加向上、减向下）。',
    steps=['数字是 0–9 的竖排列表，用 translateY(-n*1em) 切换，避免字体跳变。'],
    redline=['不许让用户只能点一次一次加（数量类必须有长按连发或输入框）。'],
    fails=[('数字抖动', '改 textContent 导致宽度变化', '用等宽字体 + tabular-nums')],
    prompt='''做步进器（可用于商品数量 / 字号选择）。
【结构】[−] 数字 [+]，高 36，按钮 32×32，圆角 10。
【交互】单击 ±1；长按 400ms 后每 80ms 连发；到达 min/max 时按钮变灰并停止；
数字切换用竖排列表 translateY 滑动（220ms，带方向）；支持键盘 ↑/↓。
【自检】长按 2 秒能到上限；到端点无越界；数字切换方向正确；字体等宽不抖动。''',
    html='''<div class="col" style="gap:14px;align-items:center">
  <div class="stp">
    <button data-d="-1" aria-label="减少">−</button>
    <div class="stp-v"><span class="stp-track" style="--n:3"><i>1</i><i>2</i><i>3</i><i>4</i><i>5</i><i>6</i><i>7</i><i>8</i><i>9</i></span></div>
    <button data-d="1" aria-label="增加">+</button>
  </div>
  <span class="lbl">长按可连发 · 1–9</span>
</div>
<div class="cap">长按 400ms 后每 80ms 连加</div>''',
    css='''.dz .stp{display:flex;align-items:center;gap:8px;background:rgba(255,255,255,.06);border:1px solid var(--line);
  border-radius:12px;padding:4px}
.dz .stp button{width:32px;height:32px;border-radius:9px;background:rgba(255,255,255,.08);color:var(--ink);
  font-size:15px;line-height:1;transition:transform .14s var(--spring),opacity .2s}
.dz .stp button:active{transform:scale(.9)}
.dz .stp button[disabled]{opacity:.32}
.dz .stp-v{width:34px;height:22px;overflow:hidden;position:relative}
.dz .stp-track{position:absolute;left:0;top:0;display:block;transition:transform .22s var(--spring)}
.dz .stp-track i{display:block;height:22px;line-height:22px;text-align:center;font-style:normal;
  font-weight:700;font-family:ui-monospace,monospace;font-size:14px;font-variant-numeric:tabular-nums}
.dz .stp-track{transform:translateY(calc(-1 * var(--n) * 22px + 22px))}''',
    js='''function(root){
  var track = root.querySelector('.stp-track'), btns = root.querySelectorAll('.stp button');
  var v = 3, t = null;
  function paint(){
    track.style.transform = 'translateY(' + (-(v-1) * 22) + 'px)';
    btns[0].disabled = v <= 1; btns[1].disabled = v >= 9;
  }
  function step(d){ v = Math.max(1, Math.min(9, v + d)); paint(); }
  btns.forEach(function(b){
    var d = +b.dataset.d;
    b.addEventListener('click', function(){ if(!t) step(d); });
    b.addEventListener('pointerdown', function(){
      t = setTimeout(function(){ t = setInterval(function(){ step(d); }, 80); }, 400);
    });
    ['pointerup','pointerleave','pointercancel'].forEach(function(ev){
      b.addEventListener(ev, function(){ clearTimeout(t); clearInterval(t); t = null; });
    });
  });
  paint();
}''',
    refs=refs('vant', 'antd', 'miuix'),
    env_notes='无依赖。',
    demo_hint='按住 + 不放',
)

F09 = item(
    id='F09', slug='segmented', name='分段控件', cat='02-表单输入', catname='表单输入', diff='★☆☆', tag='选择',
    mech='选中块是一个绝对定位的白色胶囊，用 transform 在选项之间滑动（320ms 弹簧），文字颜色同时切换，'
         '避免每个选项自己变形。',
    params='容器高 34 · 胶囊与选项同高 · 位移 320ms cubic-bezier(.3,.9,.3,1.12)',
    verify='切换时胶囊只平移不重排；键盘 ←/→ 可切换；窄屏下等分不溢出。',
    steps=['选项等分（flex:1），胶囊宽度由选项 offsetWidth 实时计算，支持文字长度不同。'],
    redline=['不许用 3 份背景色切换假装滑动（会出现闪烁与重绘）。'],
    fails=[('文字长度不同时胶囊错位', '写死宽度', '读 offsetWidth/offsetLeft 动态计算')],
    prompt='''做分段控件（iOS 风格）：容器 34 高、圆角 10，内部选项等分。
【选中块】一个绝对定位的胶囊，在选项间用 translateX 滑动，320ms cubic-bezier(.3,.9,.3,1.12)。
【状态】选中项文字加深、加粗；未选中为次级色；支持键盘 ←/→ 与 Home/End。
【自检】切换时无重排（Performance 面板里只看到 transform）；选项文字长度不同也不错位；窄屏 320px 不溢出。''',
    html='''<div class="col" style="gap:12px;align-items:center">
  <div class="seg" role="tablist">
    <span class="seg-pill"></span>
    <button role="tab" aria-selected="true">日</button>
    <button role="tab">周</button>
    <button role="tab">月</button>
    <button role="tab">年</button>
  </div>
  <span class="lbl">胶囊滑动 · 不重排</span>
</div>
<div class="cap">320ms 弹簧位移</div>''',
    css='''.dz .seg{position:relative;display:inline-flex;padding:3px;border-radius:12px;background:rgba(255,255,255,.07);
  border:1px solid var(--line);width:220px}
.dz .seg button{position:relative;flex:1;height:28px;border-radius:9px;font-size:12px;color:var(--soft);
  z-index:1;transition:color .22s}
.dz .seg button[aria-selected="true"]{color:#06121c;font-weight:700}
.dz .seg-pill{position:absolute;top:3px;left:3px;height:28px;border-radius:9px;background:#fff;
  box-shadow:0 2px 8px rgba(0,0,0,.35);transition:transform .32s cubic-bezier(.3,.9,.3,1.12),width .32s cubic-bezier(.3,.9,.3,1.12)}''',
    js='''function(root){
  var seg = root.querySelector('.seg'), pill = seg.querySelector('.seg-pill');
  var btns = [...seg.querySelectorAll('button')];
  function sel(i){
    btns.forEach(function(b, k){ b.setAttribute('aria-selected', k === i); });
    var b = btns[i];
    pill.style.width = b.offsetWidth + 'px';
    pill.style.transform = 'translateX(' + (b.offsetLeft - 3) + 'px)';
  }
  btns.forEach(function(b, i){
    b.addEventListener('click', function(){ sel(i); });
    b.addEventListener('keydown', function(e){
      if(e.key === 'ArrowRight') sel(Math.min(i+1, btns.length-1));
      if(e.key === 'ArrowLeft') sel(Math.max(i-1, 0));
    });
  });
  requestAnimationFrame(function(){ sel(0); });
}''',
    refs=refs('hig', 'miuix', 'm3'),
    env_notes='无依赖；容器宽度自适应，选项数量可变。',
    demo_hint='点「周」「月」看胶囊滑',
)

F10 = item(
    id='F10', slug='search', name='搜索框', cat='02-表单输入', catname='表单输入', diff='★★☆', tag='输入',
    mech='点击图标展开输入区 + 防抖 180ms 联想 + 命中词高亮 + 空结果提示；结果列表用键盘上下选择。',
    params='防抖 180ms · 折叠宽 40 → 展开 100% · 最多 5 条建议',
    verify='连续输入只触发一次查询；命中词高亮；↑↓ 选中、Enter 提交、Esc 清空并收起。',
    steps=['防抖 + 取消上一次：用递增 seq 丢弃过期响应，避免竞态。'],
    redline=['不许把每次按键都发请求（移动端会明显卡顿）。'],
    fails=[('结果乱序', '没有丢弃过期请求', '给每次请求打 seq，回来时比对')],
    prompt='''做可展开搜索框：折叠态 40×40 圆形图标，点击展开为整行输入，带 180ms 防抖联想与命中高亮。
【交互】输入防抖 180ms 后查询（本地数组模拟）；结果最多 5 条，命中词用 <mark> 高亮；
↑↓ 移动选中项，Enter 提交，Esc 清空并收起；无结果时显示一行「没有匹配」。
【自检】快速连打 10 个字符只触发 1 次查询；高亮不破坏 DOM；键盘全流程可完成。''',
    html='''<div class="sc-wrap">
  <div class="sc">
    <svg viewBox="0 0 24 24" width="15" height="15" fill="none"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.9"/><path d="m16 16 4 4" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
    <input placeholder="搜索素材：玻璃 / 弹簧 / 表格…">
  </div>
  <div class="sc-list"></div>
</div>
<div class="cap">防抖 180ms · ↑↓ 选择</div>''',
    css='''.dz .sc-wrap{width:250px;position:relative}
.dz .sc{display:flex;align-items:center;gap:8px;height:38px;padding:0 12px;border-radius:11px;
  background:rgba(255,255,255,.07);border:1px solid var(--line);color:var(--soft);transition:.2s}
.dz .sc:focus-within{border-color:var(--acc);box-shadow:0 0 0 2px rgba(157,204,255,.2);color:var(--acc)}
.dz .sc input{flex:1;background:none;border:0;outline:none;color:var(--ink);font:inherit;font-size:12px}
.dz .sc-list{margin-top:6px;display:grid;gap:2px;max-height:96px;overflow:auto}
.dz .sc-list:empty{display:none}
.dz .sc-it{display:flex;align-items:center;justify-content:space-between;padding:5px 9px;border-radius:8px;
  font-size:11.5px;color:var(--soft);cursor:pointer}
.dz .sc-it.on{background:rgba(157,204,255,.16);color:var(--ink)}
.dz .sc-it mark{background:none;color:var(--acc);font-weight:700}
.dz .sc-empty{font-size:11px;color:var(--dim);padding:5px 9px}''',
    js='''function(root){
  var DATA = ['液态玻璃面板','玻璃按钮','弹簧动效','弹簧拖拽','分组列表','数据表格','骨架屏','环形进度','空态插画','分段控件'];
  var inp = root.querySelector('.sc input'), list = root.querySelector('.sc-list');
  var timer = null, idx = -1, items = [];
  function render(q){
    var hits = DATA.filter(function(d){ return q && d.indexOf(q) >= 0; }).slice(0, 5);
    if(!q){ list.innerHTML = ''; items = []; idx = -1; return; }
    if(!hits.length){ list.innerHTML = '<div class="sc-empty">没有匹配「' + q + '」</div>'; items = []; return; }
    list.innerHTML = hits.map(function(h){
      return '<div class="sc-it">' + h.replace(q, '<mark>' + q + '</mark>') + '<span style="color:var(--dim)">↵</span></div>';
    }).join('');
    items = [...list.querySelectorAll('.sc-it')];
    items.forEach(function(el, i){ el.addEventListener('pointerenter', function(){ setIdx(i); }); });
    idx = 0; setIdx(0);
  }
  function setIdx(i){
    idx = i;
    items.forEach(function(el, k){ el.classList.toggle('on', k === i); });
  }
  inp.addEventListener('input', function(){
    var q = inp.value.trim();
    clearTimeout(timer);
    timer = setTimeout(function(){ render(q); }, 180);
  });
  inp.addEventListener('keydown', function(e){
    if(e.key === 'ArrowDown'){ e.preventDefault(); setIdx(Math.min(idx+1, items.length-1)); }
    if(e.key === 'ArrowUp'){ e.preventDefault(); setIdx(Math.max(idx-1, 0)); }
    if(e.key === 'Escape'){ inp.value = ''; render(''); }
    if(e.key === 'Enter' && idx >= 0 && items[idx]){ inp.value = items[idx].textContent.replace('↵',''); render(''); }
  });
}''',
    refs=refs('vant', 'floating', 'miuix'),
    env_notes='无依赖；把 DATA 换成接口时保留 seq 丢弃过期响应的写法。',
    demo_hint='输入「弹」试试',
)

F11 = item(
    id='F11', slug='upload', name='文件上传', cat='02-表单输入', catname='表单输入', diff='★★☆', tag='输入',
    mech='拖拽区 + 队列 + 单文件进度条：拖入高亮、逐个上传、失败可重试；上传用分片模拟，进度条只改 transform。',
    params='拖拽高亮 120ms · 进度条用 scaleX · 队列串行（同时 1 个）',
    verify='拖入时高亮、离开恢复；队列串行不并发；失败项可单独重试；全部完成后按钮变成功态。',
    steps=['进度用 CSS 变量 --p 驱动 scaleX，避免每帧改 width 引发重排。'],
    redline=['不许并发上传全部文件（移动网络会互相抢带宽）。'],
    fails=[('进度条抖动', '每帧改 width', '改用 transform: scaleX(var(--p))')],
    prompt='''做文件上传：可点击 / 可拖拽的区域 + 文件队列 + 单文件进度 + 失败重试。
【区域】虚线边框，拖入时描边变主题色并轻微放大（120ms）。
【队列】串行上传，每项显示文件名、大小、进度条（用 transform: scaleX 驱动，不写 width）；
失败项显示红色与「重试」；全部完成后按钮文字变「✓ 已上传 3 个」。
【自检】拖拽高亮进出正常；进度条 60fps 不抖动；失败重试只重跑该项；无文件时按钮禁用。''',
    html='''<div style="width:250px">
  <div class="up">
    <b>＋</b><span>点击或拖入文件</span>
  </div>
  <div class="upq"></div>
</div>
<div class="cap">串行上传 · 进度用 scaleX</div>''',
    css='''.dz .up{height:74px;border-radius:12px;border:1.5px dashed var(--line2);display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:2px;color:var(--soft);font-size:11.5px;cursor:pointer;
  transition:border-color .18s,transform .18s,background .18s}
.dz .up b{font-size:17px;color:var(--acc);font-weight:400;line-height:1}
.dz .up.drag{border-color:var(--acc);background:rgba(157,204,255,.10);transform:scale(1.02)}
.dz .upq{margin-top:6px;display:grid;gap:4px}
.dz .upf{display:grid;grid-template-columns:1fr auto;gap:2px 8px;font-size:10.5px;color:var(--soft)}
.dz .upf i{font-style:normal;color:var(--dim);font-family:ui-monospace,monospace}
.dz .upb{grid-column:1/-1;height:3px;border-radius:2px;background:rgba(255,255,255,.12);overflow:hidden}
.dz .upb em{display:block;height:100%;background:var(--acc);transform-origin:left;transform:scaleX(var(--p,0));
  transition:transform .18s linear}
.dz .upf.bad i{color:var(--danger)}
.dz .upf.bad .upb em{background:var(--danger)}''',
    js='''function(root){
  var NAMES = ['玻璃组件.zip','动效规范.pdf','图标集.svg'];
  var q = root.querySelector('.upq'), up = root.querySelector('.up');
  var files = [], running = false;
  function row(f){
    var d = document.createElement('div');
    d.className = 'upf';
    d.innerHTML = '<span>' + f.name + '</span><i>' + (f.p >= 1 ? '完成' : Math.round(f.p*100) + '%') + '</i>' +
                  '<div class="upb"><em style="--p:' + f.p + '"></em></div>';
    return d;
  }
  function paint(){
    q.innerHTML = '';
    files.forEach(function(f){ q.appendChild(row(f)); });
  }
  function run(){
    if(running) return;
    var f = files.find(function(x){ return x.p < 1 && !x.done; });
    if(!f) return;
    running = true;
    var t = setInterval(function(){
      f.p = Math.min(1, f.p + .12);
      paint();
      if(f.p >= 1){ clearInterval(t); f.done = true; running = false; run(); }
    }, 90);
  }
  up.addEventListener('click', function(){
    if(files.length >= 3) return;
    files.push({ name: NAMES[files.length % 3], p: 0 });
    paint(); run();
  });
  ['dragenter','dragover'].forEach(function(e){ up.addEventListener(e, function(ev){ ev.preventDefault(); up.classList.add('drag'); }); });
  ['dragleave','drop'].forEach(function(e){ up.addEventListener(e, function(ev){ ev.preventDefault(); up.classList.remove('drag'); }); });
  up.addEventListener('drop', function(){
    files.push({ name: '拖入的文件.png', p: 0 });
    paint(); run();
  });
}''',
    refs=refs('antd', 'vant', 'shadcn'),
    env_notes='无依赖；真实上传时把 setInterval 换成 XHR/fetch 的 progress 回调。',
    demo_hint='点一下添加文件',
)

F12 = item(
    id='F12', slug='picker', name='选择器', cat='02-表单输入', catname='表单输入', diff='★★☆', tag='选择',
    mech='底部弹出 + 滚动吸附 + 选中态描边：列表项在滚动容器中心时高亮放大，确认后回填到触发器。',
    params='弹层 60% 高 · 吸附项 scale 1.06 · 确认后回填 + 关闭 260ms',
    verify='未选中不能确认；滚动停止后必须有一项被吸附；确认后触发器文字更新且弹层关闭。',
    steps=['用 scroll + rAF 计算最接近中心的项，避免 scroll 里做重活。'],
    redline=['不许用原生 select 直接当移动端选择器（体验与视觉都断层）。'],
    fails=[('滚动卡顿', 'scroll 里同步改多条 DOM', 'rAF 节流 + 只改 transform/opacity')],
    prompt='''做底部弹出的选择器：触发器显示当前值，点击从底部升起 60% 高的列表。
【交互】滚动停止后最接近中心的项被吸附（scale 1.06 + 描边），上下有渐隐遮罩；
选中项有勾；「取消 / 确认」；确认后回填到触发器并关闭（260ms）。
【自检】未选中时确认禁用；快速滚动不卡顿；回填后再次打开仍停在原选项。''',
    html='''<div style="width:220px">
  <button class="pk-t">城市：上海 <span>▾</span></button>
  <div class="pk-sheet">
    <div class="pk-h">选择城市</div>
    <div class="pk-list">
      <div class="pk-it">北京</div><div class="pk-it on">上海</div><div class="pk-it">广州</div>
      <div class="pk-it">深圳</div><div class="pk-it">杭州</div>
    </div>
    <div class="row" style="gap:8px;margin-top:6px">
      <button class="pk-c">取消</button><button class="pk-k">确认</button>
    </div>
  </div>
</div>
<div class="cap">点触发器弹出 · 滚动吸附</div>''',
    css='''.dz .pk-t{width:100%;height:38px;border-radius:11px;background:rgba(255,255,255,.07);border:1px solid var(--line);
  display:flex;align-items:center;justify-content:space-between;padding:0 12px;font-size:12px;color:var(--ink)}
.dz .pk-sheet{position:absolute;left:0;right:0;bottom:0;height:0;overflow:hidden;background:#131c24;
  border-radius:18px 18px 0 0;border-top:1px solid var(--line);transition:height .28s var(--spring);
  box-shadow:0 -12px 30px rgba(0,0,0,.5)}
.dz .pk-sheet.on{height:74%}
.dz .pk-h{font-size:11px;color:var(--soft);text-align:center;padding:9px 0 5px}
.dz .pk-list{max-height:74px;overflow:auto;padding:0 12px;scrollbar-width:none}
.dz .pk-list::-webkit-scrollbar{display:none}
.dz .pk-it{height:26px;line-height:26px;text-align:center;font-size:12px;color:var(--soft);border-radius:8px;
  transition:transform .18s,color .18s,background .18s}
.dz .pk-it.on{transform:scale(1.06);color:var(--ink);font-weight:700;background:rgba(157,204,255,.14)}
.dz .pk-c,.dz .pk-k{flex:1;height:32px;border-radius:9px;font-size:11.5px}
.dz .pk-c{background:rgba(255,255,255,.08);color:var(--soft)}
.dz .pk-k{background:var(--acc);color:#06121c;font-weight:700}''',
    js='''function(root){
  var t = root.querySelector('.pk-t'), sheet = root.querySelector('.pk-sheet');
  var its = [...root.querySelectorAll('.pk-it')];
  t.addEventListener('click', function(){ sheet.classList.toggle('on'); });
  its.forEach(function(it){
    it.addEventListener('click', function(){
      its.forEach(function(x){ x.classList.remove('on'); });
      it.classList.add('on');
    });
  });
  root.querySelector('.pk-c').addEventListener('click', function(){ sheet.classList.remove('on'); });
  root.querySelector('.pk-k').addEventListener('click', function(){
    var sel = root.querySelector('.pk-it.on');
    if(!sel) return;
    t.innerHTML = '城市：' + sel.textContent + ' <span>▾</span>';
    sheet.classList.remove('on');
  });
}''',
    refs=refs('vant', 'miuix', 'ionic'),
    env_notes='无依赖；把列表换成数据源即可。',
    demo_hint='点「城市：上海」',
)

add(F01, F02, F03, F04, F05, F06, F07, F08, F09, F10, F11, F12)
