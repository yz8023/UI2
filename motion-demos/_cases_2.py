# -*- coding: utf-8 -*-
"""m04 press-stack / m05 wheel-rail / m06 toy-flipbook / m07 ink-crowd"""

C4 = dict(
    no="04", slug="press-stack", short="粘性堆叠", title="原生滚动，屏与屏互相压上去。",
    layer="dom + css", layer_cn="DOM + position: sticky",
    ref="原参考：refs/4-side-b.mp4（@LexnLin，无线上站）",
    case_url="https://github.com/feitangyuan/motion-web/tree/main/cases/press-stack",
    kicker="motion-web · 与 wheel-rail 相反的答案",
    lede="上一个案例（wheel-rail）劫持滚轮、平移一条轨道；这一页反过来：原生滚动一根不动，每一屏用 position: sticky 自己钉住，下一屏从下面骑上来盖住它。同一份需求，两种解法。",
    quote="「劫持滚轮能算任意进度，但换不来钉住；粘性堆叠白拿钉住，却要从文档里把进度读回来。」",
    quote_from="cases/press-stack · 设计说明",
    mech="原生滚动 + 每屏 position: sticky; top:0；用滚动位置反算每一屏的进度，驱动文字擦除（clip-path）与封面缩放。",
    params="四块土地色 #e9ebee / #11151c / #2f5570 / #c3ccd3 · 唯一暖色 #e08a3c · 屏高 = 容器高 · 擦除进度 0→1 映射到 30%~70% 屏",
    verify="每屏都必须真正钉住（不跟随滚动位移）· 文字擦除必须由滚动位置驱动而非计时器 · 不能拉外链位图",
    stage="""
  <section class="stagewrap">
    <div class="stagebar">
      <span class="lbl">case 04 · press-stack · 4 screens</span>
      <div class="readout"><b id="r4a">SCREEN 1 / 4</b><span class="sep">·</span><span>屏内进度 <b id="r4b">0%</b></span><span class="sep">·</span><span>容器 scrollTop <b id="r4c">0</b></span></div>
    </div>
    <div class="stackscroll" id="st4"></div>
    <div class="ctrls">
      <span class="hint" style="margin:0">在这个窗口里向下滚：每一屏会先钉住，下一屏再压上来。文字是「擦」出来的，不是淡入。</span>
    </div>
    <p class="hint">注意：页面主滚动条完全没动 —— 滚动发生在这个容器内部，进度靠 scrollTop 反算。</p>
  </section>
""",
    extra_css="""
.stackscroll{height:420px;overflow:auto;border-radius:14px;position:relative;
  box-shadow:inset 0 0 0 1px var(--line);overscroll-behavior:contain;scrollbar-width:thin}
.scr{height:420px;position:sticky;top:0;display:grid;place-items:center;overflow:hidden;
  will-change:transform}
.scr .inner{width:100%;height:100%;padding:26px 30px;display:grid;grid-template-columns:1fr auto;
  align-items:center;gap:18px;position:relative}
.scr .idx{position:absolute;left:30px;top:22px;font-size:10.5px;letter-spacing:.18em;opacity:.55}
.scr h4{font-size:clamp(24px,3.6vw,38px);line-height:1.18;letter-spacing:-.03em;margin:0;
  clip-path:inset(0 calc(100% - var(--wipe,0%)) 0 0);transition:clip-path .06s linear}
.scr p{font-size:12.5px;opacity:.62;margin-top:10px;max-width:34ch;line-height:1.7}
.sleeve{width:150px;height:150px;border-radius:4px;position:relative;flex:0 0 auto;
  transform:scale(var(--sc,1));transition:transform .06s linear}
.sleeve::before{content:"";position:absolute;inset:10px;border-radius:50%;
  background:repeating-radial-gradient(circle at 50% 50%,rgba(0,0,0,.55) 0 1px,transparent 1px 4px),
             radial-gradient(circle at 50% 50%,#1b1b1b 0 18%,transparent 19%)}
.sleeve::after{content:"";position:absolute;inset:0;border-radius:4px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.12)}
.scr .hintbar{position:absolute;right:30px;bottom:20px;font-size:10.5px;letter-spacing:.14em;opacity:.5}
.scr.s0{background:#e9ebee;color:#11151c}
.scr.s1{background:#11151c;color:#e9ebee}
.scr.s2{background:#2f5570;color:#e9ebee}
.scr.s3{background:#c3ccd3;color:#11151c}
.scr .accent{color:#e08a3c}
@media (max-width:640px){.sleeve{width:96px;height:96px}.scr .inner{padding:20px}}
""",
    js="""
(function(){
  var host=document.getElementById('st4');
  var data=[
    {i:'01 / 04',h:'原生滚动<br>不劫持',p:'这一屏钉住，下一屏压上来。滚动条属于浏览器，进度靠 scrollTop 反算。',s:'s0',acc:'不劫持'},
    {i:'02 / 04',h:'<span class="accent">sticky</span> 换来的<br>是免费钉住',p:'position: sticky 在被 transform 的祖先里会失效 —— 这是它唯一的代价。',s:'s1',acc:'钉住'},
    {i:'03 / 04',h:'文字是<br><span class="accent">擦</span>出来的',p:'clip-path: inset() 由滚动进度驱动，往回滚文字会退回未擦除状态。',s:'s2',acc:'擦除'},
    {i:'04 / 04',h:'封面用<br>画布画出来',p:'四个唱片套全部是加载时用 CSS 渐变画的，页面不拉任何位图。',s:'s3',acc:'零位图'}
  ];
  host.innerHTML=data.map(function(d){
    return '<section class="scr '+d.s+'"><div class="inner">'+
      '<div><div class="idx">'+d.i+'</div><h4>'+d.h+'</h4><p>'+d.p+'</p></div>'+
      '<div class="sleeve"></div>'+
      '<div class="hintbar">'+d.acc+'</div>'+
    '</div></section>';
  }).join('');

  var screens=[].slice.call(host.querySelectorAll('.scr'));
  var rA=document.getElementById('r4a'), rB=document.getElementById('r4b'), rC=document.getElementById('r4c');
  var H=host.clientHeight;
  function update(){
    var st=host.scrollTop;
    rC.textContent=Math.round(st);
    screens.forEach(function(s,i){
      var p=(st - i*H)/H;
      p=Math.max(0,Math.min(1,p));
      /* 擦除由「上一屏的进度」驱动：新屏压上来时文字才被擦出来 */
      var enter=i===0?1:Math.max(0,Math.min(1,(st-(i-1)*H)/H));
      s.style.setProperty('--wipe',(enter*130).toFixed(1)+'%');
      s.style.setProperty('--sc',(1-p*0.12).toFixed(3));
      s.style.transform='translateY('+(-p*8).toFixed(1)+'px)';
      s.style.opacity=(1-p*0.32).toFixed(2);
    });
    var idx=Math.min(screens.length-1,Math.round(st/H));
    rA.textContent='SCREEN '+(idx+1)+' / '+screens.length;
    var p=(st - idx*H)/H; p=Math.max(0,Math.min(1,p));
    rB.textContent=Math.round(p*100)+'%';
  }
  var ticking=false;
  host.addEventListener('scroll',function(){
    if(ticking) return;
    ticking=true; requestAnimationFrame(function(){ update(); ticking=false; });
  });
  window.addEventListener('resize',function(){ H=host.clientHeight; update(); });
  update();
})();
""",
    prompt="""
做一个单文件 HTML（无框架、无外链图片），复刻 motion-web 的 press-stack：一个用原生滚动 + position: sticky 的「屏堆叠」落地页。

【机制要求】
1) 页面里有一个固定高度（约 420px）的滚动容器；容器内放 4 个「屏」，每屏高度 = 容器高度。
2) 每一屏使用 position: sticky; top: 0 自己钉住，下一屏从下方骑上来覆盖它，形成堆叠。
3) 不要劫持滚轮、不要 preventDefault、不要用 scroll-snap 模拟——必须是原生滚动。
4) 每屏的内容进度由 scrollTop 反算：p = (scrollTop - i*屏高) / 屏高，并驱动两个效果：
   a. 标题用 clip-path: inset(0 calc(100% - wipe) 0 0) 被「擦」出来（wipe 从 0 到 130%，留一点过冲）；
   b. 右侧唱片封套随进度轻微缩小（scale 1 → 0.88）并淡出。
   进度必须每帧从滚动位置读，不能改成定时器动画。
5) 唱片封套的纹理完全用 CSS 渐变 / conic-gradient 画出来，不许外链任何位图。
6) DOM 里给三个读数：当前第几屏、该屏进度百分比、容器 scrollTop，便于自动化验证。
7) 在页面注释里写清楚：sticky 在被 transform 的祖先内会失效，如果外层必须做动画，就要像 wheel-rail 那样改成劫持轨道方案。

【配色】四块「土地」：#e9ebee / #11151c / #2f5570 / #c3ccd3，全站唯一暖色 #e08a3c 只用于强调词。

【自检标准】
- 滚动时每屏必须真的钉住（用 getBoundingClientRect 观察其 top 恒为 0）；
- 往回滚，文字必须退回未擦除状态（证明是 scrub 而不是一次性触发）；
- 全站 0 张位图请求。

输出完整 HTML。
""",
    copyable=[
        "<b>原生滚动 + sticky</b>：不劫持输入，钉住是白拿的，代价是被 transform 的祖先生效范围。",
        "<b>进度反算</b>：p = (scrollTop − i·H) / H，一个公式驱动所有揭示。",
        "<b>clip-path 擦除</b>：比淡入更有「内容被写出来」的感觉，且可回退。",
        "<b>画出来的封面</b>：CSS 渐变足够替代位图时，就不要拉图片。",
    ],
    uncopyable=[
        "<b>四块土地色的具体色值</b>：可迁移的是「一明一暗两块 + 一个饱和块 + 一个灰调」。",
        "<b>唱片主题</b>：换成任何产品都成立。",
        "<b>4 屏 / 420px</b>：按你实际的内容量与视口高度重算。",
    ],
)

C5 = dict(
    no="05", slug="wheel-rail", short="滚轮轨道", title="滚轮被劫持，文档一步没动。",
    layer="dom + css", layer_cn="DOM + rAF",
    ref="原参考：blink.trade（实测）；本页为机制复现",
    case_url="https://github.com/feitangyuan/motion-web/tree/main/cases/wheel-rail",
    kicker="motion-web · 交互动效 = 滚轮与指针产生",
    lede="整页编排只由两个输入驱动：滚轮和指针。没有任何东西按计时器播放，页面加载时也不动。鼠标放下，页面是静的；移动它，每一层以不同幅度位移；转滚轮，一条轨道平移，而文档本身从不滚动。",
    quote="「交互动效，是由鼠标滚轮或鼠标移动产生的运动。会自己漂的页面是屏保。」",
    quote_from="cases/wheel-rail · 设计说明",
    mech="滚轮 preventDefault 后累加进 target，轨道用 1−exp(−k·dt) 缓动；三层视差各不同幅度；每个词的低位升起由轨道进度驱动；雷达扫描用独立时钟 3.95s/圈。",
    params="follow k=6.2 · 视差 far 69.5px / near 9.9px（≈7×）· 词升 8px、错开 0.55/n · 扫描 3.95s · 文档 scrollY 恒为 0",
    verify="滚轮必须被 cancel（defaultPrevented）· 40ms 后距目标 ≥ 数百 px（有惯性）· 三层视差幅度必须不同 · 静置 1.5s 后仍有元素在动",
    stage="""
  <section class="stagewrap">
    <div class="stagebar">
      <span class="lbl">case 05 · wheel-rail · scrollY = 0</span>
      <div class="readout"><b id="r5a">scrollY 0</b><span class="sep">·</span><span>rail <b id="r5b">0</b> px</span><span class="sep">·</span><span>距目标 <b id="r5c">0</b> px</span></div>
    </div>
    <div class="railview" id="rv5">
      <div class="hairline" id="hl5"></div>
      <div class="plane far" id="pl5f"></div>
      <div class="plane mid" id="pl5m"></div>
      <div class="radar" id="rd5"><i></i></div>
      <div class="rail" id="rail5">
        <div class="act"><div class="words" data-stagger="0">形状<br>先于<br>色彩</div><div class="card">近景卡片 · 视差最大</div></div>
        <div class="act"><div class="words" data-stagger="1">滚轮<br>不是<br>滚动条</div><div class="card">轨道平移 · 文档不动</div></div>
        <div class="act"><div class="words" data-stagger="2">每个词<br>都从<br>下方升起</div><div class="card">8px 升起 · 错开 0.55/n</div></div>
        <div class="act"><div class="words" data-stagger="3">回到<br>开始<br>就退回去</div><div class="card">往回滚 = 反向播放</div></div>
      </div>
      <div class="railhint">把指针移到画面里 · 转动滚轮（页面不会滚动）</div>
    </div>
    <div class="ctrls">
      <button class="btn sm" id="b5next">下一段</button>
      <button class="btn sm ghost" id="b5reset">回到起点</button>
      <span class="hint" style="margin:0">指针在画面上移动时，三层视差会以不同幅度跟随；右上角的扫描由它自己的时钟驱动。</span>
    </div>
    <p class="hint">这是「劫持派」：能算任意进度，但没有钉住；press-stack 是另一派，白拿钉住但从文档读进度。</p>
  </section>
""",
    extra_css="""
.railview{position:relative;height:400px;border-radius:14px;overflow:hidden;background:#edecEB;
  box-shadow:inset 0 0 0 1px var(--line);cursor:crosshair}
[data-theme="dark"] .railview{background:#151515}
.rail{position:absolute;inset:0;display:flex;width:400%;will-change:transform}
.act{width:25%;flex:0 0 25%;position:relative;display:flex;align-items:center;padding:0 40px}
.act .words{font-size:clamp(26px,4.2vw,46px);line-height:1.12;letter-spacing:-.035em;color:#272424;font-weight:600}
[data-theme="dark"] .act .words{color:#eceae7}
.act .words span{display:inline-block;transform:translateY(8px);opacity:0}
.act .card{position:absolute;right:44px;bottom:64px;background:#fbfcfd;border-radius:10px;padding:12px 14px;
  font-size:11.5px;color:#3f3c3a;box-shadow:0 10px 30px rgba(0,0,0,.09);max-width:180px}
[data-theme="dark"] .act .card{background:#20201e;color:#cfcdc8}
.plane{position:absolute;pointer-events:none;will-change:transform}
.plane.far{left:6%;top:8%;width:220px;height:220px;border-radius:50%;
  background:radial-gradient(circle at 40% 40%,rgba(221,110,54,.30),rgba(221,110,54,0) 68%)}
.plane.mid{right:16%;top:20%;width:130px;height:130px;border-radius:50%;
  background:radial-gradient(circle at 50% 50%,rgba(154,169,102,.34),rgba(154,169,102,0) 70%)}
.hairline{position:absolute;inset:0;pointer-events:none;opacity:.55}
.hairline i{position:absolute;top:0;bottom:0;width:1px;background:#dcd9d5;transform:scaleY(0);transform-origin:top;
  transition:transform .5s cubic-bezier(.215,.61,.355,1)}
[data-theme="dark"] .hairline i{background:#2b2b28}
.radar{position:absolute;right:34px;top:30px;width:120px;height:120px;border-radius:50%;
  box-shadow:inset 0 0 0 1px rgba(39,36,36,.16);pointer-events:none}
.radar i{position:absolute;inset:0;border-radius:50%;
  background:conic-gradient(from 0deg,rgba(151,171,116,.55),rgba(151,171,116,0) 70deg,transparent 360deg);
  animation:spin 3.95s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.railhint{position:absolute;left:40px;bottom:22px;font-size:10.5px;letter-spacing:.16em;color:#8a8683}
""",
    js="""
(function(){
  var view=document.getElementById('rv5'), rail=document.getElementById('rail5');
  var far=document.getElementById('pl5f'), mid=document.getElementById('pl5m');
  var rA=document.getElementById('r5a'), rB=document.getElementById('r5b'), rC=document.getElementById('r5c');
  var maxX=0, target=0, cur=0, last=performance.now();
  var acts=rail.querySelectorAll('.act');

  /* 竖线网格：加载时画下来，之后随指针起伏 */
  var hl=document.getElementById('hl5');
  for(var i=0;i<11;i++){
    var d=document.createElement('i');
    d.style.left=(6+i*8.6)+'%';
    d.style.transitionDelay=(i*60)+'ms';
    hl.appendChild(d);
  }
  setTimeout(function(){ hl.querySelectorAll('i').forEach(function(x){ x.style.transform='scaleY(1)'; }); },120);

  function layout(){
    maxX=Math.max(0, rail.scrollWidth - view.clientWidth);
    target=Math.min(target,maxX);
  }
  window.addEventListener('resize',layout); layout();

  view.addEventListener('wheel',function(e){
    e.preventDefault();
    target=Math.max(0,Math.min(maxX,target + e.deltaY*1.15 + e.deltaX*0.6));
  },{passive:false});

  document.getElementById('b5next').addEventListener('click',function(){
    target=Math.min(maxX,target+view.clientWidth);
  });
  document.getElementById('b5reset').addEventListener('click',function(){ target=0; });

  var px=0, py=0, tx=0, ty=0;
  view.addEventListener('pointermove',function(e){
    var r=view.getBoundingClientRect();
    tx=((e.clientX-r.left)/r.width-0.5)*2;
    ty=((e.clientY-r.top)/r.height-0.5)*2;
  });
  view.addEventListener('pointerleave',function(){ tx=0; ty=0; });

  var words=[].slice.call(rail.querySelectorAll('.words'));
  words.forEach(function(w){
    var txt=w.innerHTML.split('<br>');
    w.innerHTML=txt.map(function(t){ return '<span>'+t+'</span>'; }).join('<br>');
  });

  function frame(now){
    var dt=Math.min((now-last)/1000,1/30); last=now;
    /* 帧率无关缓动 */
    cur += (target-cur)*(1-Math.exp(-6.2*dt));
    rail.style.transform='translate3d('+(-cur).toFixed(2)+'px,0,0)';

    px += (tx-px)*(1-Math.exp(-4.2*dt));
    py += (ty-py)*(1-Math.exp(-4.2*dt));
    far.style.transform='translate3d('+(px*-69.5).toFixed(1)+'px,'+(py*-34).toFixed(1)+'px,0)';
    mid.style.transform='translate3d('+(px*-30).toFixed(1)+'px,'+(py*-16).toFixed(1)+'px,0)';

    /* 每个词的升起由它在轨道里的位置驱动 */
    acts.forEach(function(act,i){
      var p=((cur - i*view.clientWidth)/(view.clientWidth));
      p=Math.max(0,Math.min(1,p));
      var spans=act.querySelectorAll('.words span');
      spans.forEach(function(s,k){
        /* 第一屏（p 恒为 0）直接给足，保证落地不是空白页 */
        var base=(i===0)?1:0;
        var local=Math.max(0,Math.min(1,(p*(spans.length+1)-k)/1.2));
        local=Math.max(base,local);
        s.style.opacity=local.toFixed(3);
        s.style.transform='translateY('+((1-local)*8).toFixed(2)+'px)';
      });
      var card=act.querySelector('.card');
      var cp=Math.max(0,Math.min(1,p*1.4));
      card.style.opacity=(0.35+cp*0.65).toFixed(2);
      card.style.transform='translateY('+((1-cp)*18).toFixed(1)+'px)';
    });

    rA.textContent='scrollY '+window.scrollY;
    rB.textContent=Math.round(cur);
    rC.textContent=Math.round(target-cur);
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
  requestAnimationFrame(function(){ /* 首帧后校正 maxX */ setTimeout(layout,50); });
})();
""",
    prompt="""
做一个单文件 HTML（DOM + rAF，无框架），复刻 motion-web 的 wheel-rail：一个由滚轮和指针驱动的整屏落地页。

【机制要求】
1) 页面本身不能滚动（document 的 scrollHeight - innerHeight = 0，window.scrollY 恒为 0）。
2) 在一个固定视口大小的容器里放一条横向「轨道」，轨道里有 4 段内容（每段 100% 宽）。
3) 滚轮事件必须绑定 {passive:false} 并 preventDefault()，把 deltaY 累加进一个 target；轨道位置用帧率无关的缓动接近它：
   cur += (target - cur) * (1 - Math.exp(-6.2 * dt));
   不要用 cur += (target-cur)*0.1，否则 120Hz 屏幕上快一倍。
4) 三层视差：远景光斑、中景圆、近景卡片，各自对指针位移做不同幅度跟随（远景约 69px，近景约 10px，量级明显不同），并共享一个滞后常数。
5) 每一段里的大标题按「每个词一个 span」，其 translateY(8px) → 0 与 opacity 0 → 1 由轨道位置驱动，同段内按 0.55/n 错开；往回滚动要能原样退回去（scrub，不能用一次性 transitionend 触发）。
6) 除滚轮和指针外，允许且仅允许一个「不是输入驱动」的元素：一圈雷达扫描（柔和锥形渐变 + 独立 3.95s 时钟）。
7) 背景要有一层细竖线网格：加载时自上而下画下来，之后靠近指针的竖线会微微上浮。
8) DOM 要有实时读数：window.scrollY（用于证明没滚动）、轨道当前位移、距目标差值。
9) 注意触控板惯性：滚轮事件在手指离开后还会持续约 1 秒，必要时加累加阈值与冷却。

【配色（实测自参考站）】底 rgb(237,236,235) · 墨 rgb(39,36,36) · 暖色强调 rgb(221,110,54) 只出现在 12 个元素上 · 橄榄 rgb(154,169,102) · 提亮面 rgb(251,252,253) · 发丝线 rgb(220,217,213)。

【自检标准】
- 滚轮事件必须被取消（defaultPrevented = true）；
- 一次滚动后 40ms，轨道应仍距目标数百 px（证明有惯性），900ms 后差距 < 5px；
- 三层视差在角到角扫过时的位移比例应 ≥ 5×；
- 指针离开 1.5 秒后，仍应有若干个元素在动（扫描），但不应该有布局在漂。

输出完整 HTML。
""",
    copyable=[
        "<b>1 − exp(−k·dt) 缓动</b>：同一份代码在 60 / 120Hz 上手感一致。",
        "<b>滚轮劫持 + target 累加</b>：任意进度、可回退，适合叙事型页面。",
        "<b>三层视差共享滞后常数、不同幅度</b>：幅度相同就成了一个平面在滑。",
        "<b>保留一个非输入驱动的元素（扫描）</b>：页面在没人碰时也有生命，但不会「自己在漂」。",
        "<b>竖线网格 + 接近度响应</b>：二十来个元素就撑起了密度感。",
    ],
    uncopyable=[
        "<b>blink.trade 的具体配色与字体</b>：可迁移的是「暖色只花一次」。",
        "<b>4 段文案结构</b>：换成你的产品叙事。",
        "<b>69.5 / 9.9 这组像素值</b>：是 1440×900 下量出来的，视口变了要重测。",
    ],
)

C6 = dict(
    no="06", slug="toy-flipbook", short="翻页动画玩具", title="用鼠标转动的翻页动画。",
    layer="rAF + 预渲染", layer_cn="Canvas 2D + 预渲染帧",
    ref="原参考：inflatable-chrome-toystudio（TOYBOX）",
    case_url="https://github.com/feitangyuan/motion-web/tree/main/cases/toy-flipbook",
    kicker="motion-web · 无渲染器的旋转",
    lede="它不是 3D 模型，也不是视频：四个预渲染的偏航姿态，像翻页动画一样硬切，还刻意踩在一个抖动的停格时钟上。转得快一点，桌上的玩具会被踢飞出去。",
    quote="「没有渲染器的深度旋转：四张预渲染图，硬切。」",
    quote_from="cases/toy-flipbook · 设计说明",
    mech="指针/滚轮产生角速度 → 角度积分 → 按 12Hz 停格时钟量化成 4 个姿态硬切；|ω| 超过阈值时桌面玩具被踢飞，落地做 squash 且冲击量衰减 ~10 帧。",
    params="4 姿态 · 停格 12Hz · 阻尼 0.94/帧 · 踢飞阈值 |ω|>2.2 · 撞击后 squash 持续约 10 帧 · 地面 #f3efe8→#e9e3d8 · 强调 #dcc8ef / #ffe94d",
    verify="姿态必须硬切（不得插值）· 快转时玩具必须被踢飞并落地回弹 · squash 不能只持续 1 帧",
    stage="""
  <section class="stagewrap">
    <div class="stagebar">
      <span class="lbl">case 06 · toy-flipbook · 4 poses / 12Hz</span>
      <div class="readout"><b id="r6a">POSE F0</b><span class="sep">·</span><span>角速度 <b id="r6b">0.0</b></span><span class="sep">·</span><span>被踢飞 <b id="r6c">0</b></span></div>
    </div>
    <div class="canvasbox" style="background:#f3efe8"><canvas id="c6" width="960" height="470"></canvas></div>
    <div class="ctrls">
      <button class="btn sm" id="b6spin">使劲转一下</button>
      <button class="btn sm ghost" id="b6reset">复位</button>
      <span class="hint" style="margin:0">在画面上左右拖动 = 转动机器；转得快，桌上的玩具会被踢出去。</span>
    </div>
    <p class="hint">注意角速度越快，中段越容易「跳帧」——那 4 张姿态是硬切的，不是插值出来的。</p>
  </section>
""",
    extra_css="""
#c6{background:#f3efe8}
""",
    js="""
(function(){
  var cv=document.getElementById('c6'), ctx=cv.getContext('2d');
  var W=960,H=470;
  var GROUND1='#f3efe8', GROUND2='#e9e3d8';
  var INK='#17150f', PAPER='#e7e2d6', LILAC='#dcc8ef', MINT='#cde6d4', MARK='#ffe94d';

  /* 预渲染四个偏航姿态（离屏画布） */
  var POSES=[];
  function makePose(k){
    var c=document.createElement('canvas'); c.width=260; c.height=200;
    var g=c.getContext('2d');
    var yaw=[1,0.72,0.42,0.72][k];       /* 横向压缩比 = 假装的偏航 */
    var skew=[0,6,0,-6][k];
    g.translate(130,110);
    g.transform(yaw,0,skew/200,1,0,0);
    /* 机身 */
    g.fillStyle=PAPER; g.strokeStyle=INK; g.lineWidth=3;
    roundRect(g,-92,-56,184,112,18); g.fill(); g.stroke();
    /* 屏幕 */
    g.fillStyle=MINT; roundRect(g,-72,-40,96,72,10); g.fill(); g.stroke();
    g.fillStyle=INK; g.font='700 11px ui-monospace, monospace';
    g.fillText('TOYBOX',-66,-24);
    g.fillStyle='rgba(23,21,15,.25)'; roundRect(g,-66,-14,70,34,6); g.fill();
    /* 旋钮 */
    g.fillStyle=LILAC; roundRect(g,36,-34,44,44,22); g.fill(); g.stroke();
    g.fillStyle=MARK; roundRect(g,46,-4,30,30,15); g.fill(); g.stroke();
    g.fillStyle=INK; g.beginPath(); g.arc(57,10,4,0,7); g.fill();
    g.beginPath(); g.arc(66,10,4,0,7); g.fill();
    return c;
  }
  function roundRect(g,x,y,w,h,r){
    g.beginPath();
    g.moveTo(x+r,y); g.arcTo(x+w,y,x+w,y+h,r); g.arcTo(x+w,y+h,x,y+h,r);
    g.arcTo(x,y+h,x,y,r); g.arcTo(x,y,x+w,y,r); g.closePath();
  }
  for(var i=0;i<4;i++) POSES.push(makePose(i));

  var yaw=0, omega=0, stepClock=0, poseIdx=0;
  var toys=[], kicked=0;
  function resetToys(){
    toys=[];
    for(var i=0;i<5;i++){
      toys.push({x:120+i*170, y:388-Math.random()*8, vx:0, vy:0,
        kind:i, rot:(Math.random()-0.5)*0.4, impact:0, flying:false, sq:0});
    }
    kicked=0;
  }
  resetToys();

  var dragging=false, lastX=0;
  function pos(e){ var r=cv.getBoundingClientRect(); return {x:(e.clientX-r.left)*(W/r.width), y:(e.clientY-r.top)*(H/r.height)}; }
  cv.addEventListener('pointerdown',function(e){ dragging=true; lastX=pos(e).x; });
  cv.addEventListener('pointermove',function(e){
    if(!dragging) return;
    var p=pos(e), d=p.x-lastX; lastX=p.x;
    omega += d*0.06;
    omega=Math.max(-16,Math.min(16,omega));
  });
  window.addEventListener('pointerup',function(){ dragging=false; });
  cv.addEventListener('wheel',function(e){ e.preventDefault(); omega += e.deltaY*0.05; },{passive:false});
  document.getElementById('b6spin').addEventListener('click',function(){ omega=11; });
  document.getElementById('b6reset').addEventListener('click',function(){ omega=0; yaw=0; resetToys(); });

  var rA=document.getElementById('r6a'), rB=document.getElementById('r6b'), rC=document.getElementById('r6c');

  function step(dt){
    yaw += omega*dt*60;
    omega *= 0.955;
    /* 停格时钟：12Hz 量化姿态 —— 硬切，不插值 */
    stepClock += dt;
    if(stepClock > 1/12){
      stepClock = 0;
      var raw=((yaw%360)+360)%360;
      var idx=Math.floor(raw/90)%4;
      if(idx!==poseIdx){ poseIdx=idx; }
      /* 快速旋转时踢飞玩具 */
      if(Math.abs(omega)>2.2){
        toys.forEach(function(t){
          if(!t.flying && Math.random()<0.06){
            t.flying=true; t.vx=(Math.random()-0.5)*9 + Math.sign(omega)*4;
            t.vy=-6-Math.random()*5; t.vr=(Math.random()-0.5)*0.7;
            kicked++;
          }
        });
      }
    }
    /* 玩具物理 */
    toys.forEach(function(t){
      if(t.flying){
        t.vy+=0.45; t.x+=t.vx; t.y+=t.vy; t.rot+=t.vr;
        t.vx*=0.995;
        if(t.y>404 && t.vy>0){
          if(Math.abs(t.vy)>3){
            t.y=404; t.vy*=-0.42; t.vx*=0.7; t.impact=1; t.sq=1;
          } else {
            t.y=404; t.vy=0; t.vx*=0.86; t.flying=false; t.impact=0.6; t.sq=1;
          }
        }
        if(t.y>460||t.x<40||t.x>W-40){ t.x=Math.max(60,Math.min(W-60,t.x)); t.y=404; t.flying=false; }
      }
      t.impact*=0.90;                 /* 冲击量衰减 ~10 帧 */
      t.sq += (t.impact - t.sq)*0.35;
    });
  }

  function drawToy(t){
    var s=1, sy=1;
    if(t.sq>0.02){ sy=1-t.sq*0.34; s=1+t.sq*0.2; }
    ctx.save();
    ctx.translate(t.x,t.y);
    ctx.rotate(t.rot);
    ctx.scale(s,sy);
    ctx.strokeStyle=INK; ctx.lineWidth=2.5; ctx.fillStyle=[LILAC,MINT,PAPER,MARK,'#dcc8ef'][t.kind];
    if(t.kind===0){ ctx.beginPath(); ctx.arc(0,0,14,0,7); ctx.fill(); ctx.stroke(); }
    if(t.kind===1){ roundRect(ctx,-15,-12,30,24,6); ctx.fill(); ctx.stroke(); }
    if(t.kind===2){ ctx.beginPath(); ctx.moveTo(0,-15); ctx.lineTo(14,12); ctx.lineTo(-14,12); ctx.closePath(); ctx.fill(); ctx.stroke(); }
    if(t.kind===3){ roundRect(ctx,-6,-16,12,32,6); ctx.fill(); ctx.stroke(); }
    if(t.kind===4){ ctx.beginPath(); ctx.arc(8,0,11,0,7); ctx.arc(-8,0,11,0,7); ctx.fill(); ctx.stroke(); }
    ctx.restore();
  }

  function draw(){
    var grad=ctx.createRadialGradient(W/2,-120,80,W/2,120,900);
    grad.addColorStop(0,GROUND1); grad.addColorStop(1,GROUND2);
    ctx.fillStyle=grad; ctx.fillRect(0,0,W,H);
    ctx.fillStyle='rgba(23,21,15,.10)';
    ctx.beginPath(); ctx.ellipse(W/2,404,190,16,0,0,7); ctx.fill();
    toys.forEach(drawToy);
    var p=POSES[poseIdx];
    var jitter=(Math.sin(stepClock*60)*1.2);
    ctx.drawImage(p, W/2-130, 170+jitter, 260, 200);
    ctx.fillStyle=INK; ctx.textAlign='left';
    ctx.font='700 42px "Segoe UI", sans-serif';
    ctx.fillText('TOY', 44, 86);
    ctx.fillStyle=LILAC; roundRect(ctx,44,96,150,44,22); ctx.fill();
    ctx.fillStyle=INK; ctx.font='700 40px "Segoe UI", sans-serif';
    ctx.fillText('STUDIO', 52, 130);
    ctx.font='11px ui-monospace, monospace'; ctx.fillStyle='rgba(23,21,15,.55)';
    ctx.fillText('DRAG TO SPIN · 4 PRE-RENDERED POSES · 12Hz CUT', 44, H-30);
    ctx.fillStyle=MARK; roundRect(ctx,W-150,H-52,106,28,14); ctx.fill();
    ctx.fillStyle=INK; ctx.font='700 10px ui-monospace, monospace';
    ctx.fillText('STOP-MOTION', W-140, H-33);
  }

  var last=performance.now();
  function loop(now){
    var dt=Math.min((now-last)/1000,1/30); last=now;
    step(dt); draw();
    rA.textContent='POSE F'+poseIdx;
    rB.textContent=omega.toFixed(1);
    rC.textContent=kicked;
    requestAnimationFrame(loop);
  }
  requestAnimationFrame(loop);
})();
""",
    prompt="""
做一个单文件 HTML（Canvas 2D + rAF），复刻 motion-web 的 toy-flipbook：一个"不用 3D 渲染器也能转"的 Studio 首屏。

【机制要求】
1) 中心是一台手持游戏机，只有 4 张预渲染的偏航姿态图（用离屏 canvas 在加载时画好，不要外链图片）；旋转时在这 4 张图之间硬切，禁止任何角度插值或补间。
2) 硬切必须踩在一个"停格时钟"上：约 12Hz，每 1/12 秒才允许切换一次姿态，制造手绘翻页动画的顿挫感。
3) 输入：指针水平拖动 + 滚轮，都作用于角速度 omega（带阻尼 0.955/帧），角度用积分累加，不用绝对位置映射。
4) 桌面有 5 个小玩具（圆形、方块、三角、胶囊、双圆），初始静置；当 |omega| > 2.2 时，每个停格时刻有约 6% 概率把一个玩具踢飞（给初速度，受重力，落地回弹）。
5) 落地必须有 squash & stretch：冲击量 impact 从 1 开始每帧衰减 0.90（约 10 帧），缩放按 impact 插值——只持续 1 帧的形变等于没有。
6) 页面整体基调：暖白渐变地面、纸色机身、紫丁香与薄荷两个强调块（各只出现一次）、黄色标签一处。
7) DOM 读数：当前姿态 F0–F3、角速度、被踢飞数量。

【自检标准】
- 慢速拖动时应看到姿态在 4 张之间硬切（可用连续截图验证没有中间态）；
- 快速旋转时至少有 1 个玩具被踢飞并落地回弹；
- 落地后至少 3~4 帧能观察到形变（squash 不能一闪而过）。

输出完整 HTML。
""",
    copyable=[
        "<b>4 张预渲染帧 + 硬切</b>：没有渲染器也能做出「深度旋转」的重手感，代价是姿态有限。",
        "<b>停格时钟（12Hz）</b>：把「不够流畅」变成风格，比补间更有个性。",
        "<b>角速度而不是绝对角度</b>：拖动手感立刻变得有惯性。",
        "<b>impact 衰减 ~10 帧后再插值形变</b>：保证 squash 真的看得见。",
    ],
    uncopyable=[
        "<b>紫丁香 + 薄荷 + 黄标签这套配色</b>：可迁移的是「两个强调色各用一次」。",
        "<b>TOYBOX 这个词和玩具造型</b>：换成你的产品与实物。",
        "<b>4 张姿态</b>：依据你的素材量，8 张 45° 会更顺。",
    ],
)

C7 = dict(
    no="07", slug="ink-crowd", short="手绘 3D", title="把「手绘 3D」画成它自己讲的样子。",
    layer="webgl2（本页 canvas 2d 近似）", layer_cn="Canvas 2D 近似 WebGL2 管线",
    ref="原参考：ink-crowd.vercel.app（@pallavmac 的浏览器游戏）",
    case_url="https://github.com/feitangyuan/motion-web/tree/main/cases/ink-crowd",
    kicker="motion-web · 渲染层是设计决策",
    lede="原案例是手写 WebGL2：实例化胶囊 → 深度纹理 → 只在深度不连续处描边 → 叠 11Hz 的「沸腾」抖动与颗粒。这一页用 Canvas 2D 复现同一套可见机制：轮廓只出现在整体的外缘而不是每一块的接缝上，线条每 1/11 秒轻轻抖一下，贴图感来自颗粒而不是渐变。",
    quote="「先用 DOM 写的页面，永远长成 div。」",
    quote_from="cases/ink-crowd · 设计说明",
    mech="胶囊骨架投影 → 外扩描边 + 白色回填吃掉内部接缝（近似深度断点描边）→ 11Hz boil 抖动 → 二值调色板 + 颗粒。",
    params="boil 11Hz · 描边 2.7px · 颗粒 0.012 · 调色板二值：79% 白 / 16.5% 黑 · 每帧 95% 变化、无周期性停顿",
    verify="必须声明渲染层 · 描边只出现在整体外缘（不出现内部接缝）· boil 必须按 11Hz 量化而非每帧随机",
    stage="""
  <section class="stagewrap">
    <div class="stagebar">
      <span class="lbl">case 07 · ink-crowd · boil 11Hz</span>
      <div class="readout"><b id="r7a">STEP 0</b><span class="sep">·</span><span>偏航 <b id="r7b">0°</b></span><span class="sep">·</span><span>形体 <b id="r7c">0</b></span></div>
    </div>
    <div class="canvasbox" style="background:#fff"><canvas id="c7" width="960" height="470"></canvas></div>
    <div class="ctrls">
      <label class="switch" id="sw7" role="switch" aria-checked="true"><span class="track"><span class="knob"></span></span>开启 boil（11Hz）</label>
      <button class="btn sm ghost" id="b7reset">回正</button>
      <span class="hint" style="margin:0">在画面上左右移动鼠标 → 角色转向；关掉 boil 立刻能看到「数码味」回来。</span>
    </div>
    <p class="hint">原版是 WebGL2 的两次 pass（颜色 + 视图法线 + 深度，再在深度断点处画线）；这里用「外扩描边 + 回填」近似同一视觉：内部接缝被吃掉，只留外缘。</p>
  </section>
""",
    extra_css="""
#c7{background:#fff}
""",
    js="""
(function(){
  var cv=document.getElementById('c7'), ctx=cv.getContext('2d');
  var W=960,H=470;
  var boilOn=true, yaw=0, targetYaw=0, step=0, lastStep=0;
  var rA=document.getElementById('r7a'), rB=document.getElementById('r7b'), rC=document.getElementById('r7c');

  var rig=[
    {x:0,y:-40,z:0,r:34,l:70,a:0,tag:'body'},
    {x:0,y:-96,z:0,r:26,l:26,a:0,tag:'head'},
    {x:-46,y:-52,z:6,r:13,l:56,a:-0.5,tag:'armL'},
    {x:46,y:-52,z:6,r:13,l:56,a:0.5,tag:'armR'},
    {x:-20,y:10,z:0,r:15,l:60,a:0.12,tag:'legL'},
    {x:20,y:10,z:0,r:15,l:60,a:-0.12,tag:'legR'},
    {x:0,y:-124,z:0,r:5,l:18,a:0,tag:'antenna'}
  ];

  function project(p, cy){
    var rx = p.x*Math.cos(yaw) - p.z*Math.sin(yaw);
    var rz = p.x*Math.sin(yaw) + p.z*Math.cos(yaw);
    var persp = 1/(1+rz/600);
    return {x: W/2 + rx*persp, y: cy + p.y*persp, r: p.r*persp*persp, l: p.l*persp, a:p.a, z:rz};
  }
  function boil(i){ return boilOn ? Math.sin((step*7.3+i*3.1))*0.9 : 0; }

  function capsulePath(g,x1,y1,x2,y2,r){
    var a=Math.atan2(y2-y1,x2-x1);
    g.beginPath();
    g.arc(x1,y1,r,a+Math.PI/2,a-Math.PI/2);
    g.arc(x2,y2,r,a-Math.PI/2,a+Math.PI/2);
    g.closePath();
  }
  function drawCapsule(g,cp,extra){
    var dx=Math.cos(cp.a)*cp.l/2, dy=Math.sin(cp.a)*cp.l/2;
    capsulePath(g, cp.x-dx, cp.y-dy, cp.x+dx, cp.y+dy, cp.r+extra);
    g.fill();
  }

  var grain=[];
  for(var i=0;i<420;i++){
    grain.push({x:Math.abs(Math.sin(i*713.82))*W, y:Math.abs(Math.cos(i*313.41))*H,
      a:0.05+Math.abs(Math.sin(i*97.7))*0.16});
  }

  function draw(){
    ctx.fillStyle='#fff'; ctx.fillRect(0,0,W,H);
    var cy=250;
    var shapes=rig.map(function(p,i){
      var q=project(p,cy);
      return {x:q.x+boil(i*2), y:q.y+boil(i*2+1), r:q.r, l:q.l, a:q.a+(i>1?boil(i)*0.004:0)};
    });

    /* pass 1：整体外扩出墨色；pass 2：白色回填 → 内部接缝消失，只留外缘 */
    ctx.fillStyle='#0a0a0a';
    shapes.forEach(function(c){ drawCapsule(ctx,c,1.9); });
    ctx.fillStyle='#fff';
    shapes.forEach(function(c){ drawCapsule(ctx,c,0); });

    /* 脸 */
    var hq=shapes[1];
    ctx.fillStyle='#0a0a0a';
    ctx.beginPath(); ctx.ellipse(hq.x-9,hq.y-3,2.6,3.6,0,0,7); ctx.fill();
    ctx.beginPath(); ctx.ellipse(hq.x+9,hq.y-3,2.6,3.6,0,0,7); ctx.fill();
    ctx.strokeStyle='#0a0a0a'; ctx.lineWidth=1.8; ctx.lineCap='round';
    ctx.beginPath(); ctx.arc(hq.x,hq.y+4,5,0.25*Math.PI,0.75*Math.PI); ctx.stroke();
    var aq=shapes[6];
    ctx.beginPath(); ctx.arc(aq.x,aq.y-aq.l/2-4,4.4,0,7); ctx.fill();
    /* 手：两只空心小圆 */
    [2,3].forEach(function(i){
      var c=shapes[i];
      var ex=c.x+Math.cos(c.a)*c.l/2, ey=c.y+Math.sin(c.a)*c.l/2;
      ctx.fillStyle='#fff'; ctx.strokeStyle='#0a0a0a'; ctx.lineWidth=2.2;
      ctx.beginPath(); ctx.arc(ex,ey,5.4,0,7); ctx.fill(); ctx.stroke();
    });

    /* 地面：粗描边椭圆 */
    ctx.strokeStyle='#0a0a0a'; ctx.lineWidth=2.7;
    ctx.beginPath();
    ctx.ellipse(W/2+boil(31), 372+boil(32), 96+boil(33), 15+boil(34), 0, 0, 7);
    ctx.stroke();

    /* 颗粒 */
    ctx.fillStyle='#0a0a0a';
    grain.forEach(function(g){ ctx.globalAlpha=g.a; ctx.fillRect(g.x,g.y,1.6,1.6); });
    ctx.globalAlpha=1;

    ctx.fillStyle='rgba(10,10,10,.45)';
    ctx.font='10px ui-monospace, monospace'; ctx.textAlign='left';
    ctx.fillText('BOIL '+(boilOn?'11Hz':'OFF')+' · OUTLINE ONLY ON SILHOUETTE BREAKS · 79% WHITE / 16.5% BLACK', 34, H-24);

    rC.textContent=shapes.length;
  }

  var last=performance.now(), drag=false, lastX=0;
  function px(e){ var r=cv.getBoundingClientRect(); return (e.clientX-r.left)*(W/r.width); }
  cv.addEventListener('pointerdown',function(e){ drag=true; lastX=px(e); });
  cv.addEventListener('pointermove',function(e){
    var x=px(e);
    if(drag){ targetYaw += (x-lastX)*0.012; lastX=x; }
    else { targetYaw = (x/W-0.5)*1.2; }
  });
  window.addEventListener('pointerup',function(){ drag=false; });
  document.getElementById('b7reset').addEventListener('click',function(){ targetYaw=0; });
  var sw=document.getElementById('sw7');
  sw.addEventListener('click',function(){ boilOn=!boilOn; sw.setAttribute('aria-checked',String(boilOn)); });
  document.addEventListener('keydown',function(e){
    if(e.key==='ArrowLeft') targetYaw-=0.2;
    if(e.key==='ArrowRight') targetYaw+=0.2;
  });

  function loop(now){
    var dt=Math.min((now-last)/1000,1/30); last=now;
    yaw += (targetYaw-yaw)*(1-Math.exp(-5*dt));
    if(now-lastStep > 1000/11){ lastStep=now; step++; }
    draw();
    rA.textContent='STEP '+step;
    rB.textContent=Math.round(yaw*180/Math.PI)+'°';
    requestAnimationFrame(loop);
  }
  requestAnimationFrame(loop);
})();
""",
    prompt="""
做一个单文件 HTML，复刻 motion-web 的 ink-crowd「手绘 3D」质感。首选 WebGL2（手写、无框架、无 CDN）；如果环境不支持，用 Canvas 2D 近似，但必须保留下面三项可见机制。

【机制要求】
1) 角色由若干个「胶囊」组成（身体、头、双臂、双腿、天线），有真实的三维位置、半径、长度、朝向；相机做简单偏航旋转 + 一点透视。
2) 描边只出现在整体的外缘：原版靠深度纹理做深度不连续检测，内部接缝一律不描；如果你在 2D 里实现，用「所有形体先外扩 2px 填墨色、再原尺寸填白」的两遍画法达到同样效果。绝不要给每个胶囊各画一圈完整黑边（那是卡通渲染，不是这个案例）。
3) 「沸腾」：所有控制点每 1/11 秒才更新一次抖动量（±1px，用 step 索引参与相位），而不是每帧随机——每帧随机会变成噪点，11Hz 量化才有手绘呼吸感。
4) 调色板二值：约 79% 白 + 16.5% 黑，没有灰色、没有渐变；地面阴影是黑色粗描边的椭圆，不是投影。
5) 叠加轻微颗粒（强度约 0.012，种子化固定位置），让白底不是死白。
6) 交互只有一个：指针左右移动 = 角色转向；关掉 boil 应立刻能看出「数码味」回来。
7) DOM 读数：boil step 索引、当前偏航角、形体数量。

【关键参数】boil 11Hz · 描边 2.7px · 颗粒 0.012 · 二值调色板 · 深度不连续阈值由你定但必须只在断点画线
【自检标准】
- 截图上只出现整体外缘、不出现内部接缝；
- 静止时仍有 11Hz 的轻微抖动，但轮廓结构不变（不是闪烁）；
- 关掉 boil 后画面立刻「死」下来，证明 boil 是唯一的高频变化源。

输出完整 HTML（若用 WebGL2，把两个 pass 的着色器写在同一个字符串模板里，并在注释里标明每个 uniform 的作用）。
""",
    copyable=[
        "<b>先问渲染层</b>：DOM / Canvas / WebGL 是设计决策，不是实现细节。",
        "<b>只在深度断点描边</b>：比卡通描边省一半线条，还更像手绘；2D 里可用「外扩 + 回填」等效。",
        "<b>11Hz 量化的 boil</b>：抖动频率低于帧率才有呼吸感。",
        "<b>二值调色板 + 颗粒</b>：颗粒替代渐变，是「贴图感」的真正来源。",
    ],
    uncopyable=[
        "<b>ink-crowd 的角色造型与黑白二值</b>：可迁移的是「二值 + 颗粒 + 外缘描边」。",
        "<b>boil 0.011 / freq 2.2 这组偏置</b>：是原 bundle 里的常量，要按你的形体尺寸重调。",
        "<b>完整的两 pass 管线</b>：如果你只在 2D 里用外缘近似，就别声称有深度纹理。",
    ],
)
