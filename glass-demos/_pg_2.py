# -*- coding: utf-8 -*-
"""L04 模糊管线与阴影 / L05 弹簧跟随 / L06 渲染步骤查看"""

L04 = dict(
    no="04", slug="blur-pipeline", short="模糊管线与阴影", title="31 个像素×2 次取样：模糊也要讲究顺序",
    layer="webgl2 · pass 2–3", path="src/shaders/fragment-vblur.glsl",
    case_url="https://github.com/iyinchao/liquid-glass-studio/tree/main/src/shaders",
    ref="原参考：Apple Liquid Glass（毛玻璃基底）",
    lede="模糊在液态玻璃里不是滤镜，而是提前算好的两张纹理：先纵向、再横向。这样 31 次取样就能得到 31×31 的高斯核效果，否则要 961 次。左图是「不做模糊」的玻璃，右图加了模糊、染色和投影——差距主要来自投影，而不是模糊。",
    quote="「可分离卷积：两次一维，等于一次二维。」",
    quote_from="vblur / hblur 两个 shader 文件",
    mech="模糊半径 r → sigma = r/3 → 取 ±15 个偏移（共 31 个）按高斯权重加权；纵向输出传给横向，横向输出给主合成。",
    params="模糊半径 1–200（默认 18px）· blurEdge 开 · 阴影 expand 25 / factor 15 / pos (0,−10) · tint rgba(255,255,255,0)",
    verify="openspec：blurRadius 必须通过两趟一维卷积实现（不得单趟二维）；blurEdge=true 时模糊强度随离边缘距离衰减；阴影为形状向外扩张后的偏移软阴影",
    stage="""
  <section class="stagewrap">
    <div class="stagebar">
      <span class="lbl">liquid-glass · case 04 · blur / shadow / tint</span>
      <div class="readout"><b id="r4a">18 px</b><span class="sep">·</span><span>每趟取样 <b id="r4b">31</b></span><span class="sep">·</span><span>阴影 <b id="r4c">15%</b></span></div>
    </div>
    <div class="pair">
      <div class="cell">
        <div class="cell-h"><b>关掉模糊 / 阴影 / 染色</b><span>只剩折射</span></div>
        <div class="gcanvas"><canvas id="cL"></canvas></div>
      </div>
      <div class="cell">
        <div class="cell-h"><b>打开全部 · blurEdge</b><span>默认参数</span></div>
        <div class="gcanvas"><canvas id="cR"></canvas></div>
      </div>
    </div>
    <div class="ctl">
      <div class="ctl-grid">
        <label class="sl"><span class="lab">模糊半径 <b id="s-br-v">18</b></span>
          <input type="range" id="s-br" min="1" max="60" step="0.5" value="18"></label>
        <label class="sl"><span class="lab">阴影扩散 <b id="s-se-v">25</b></span>
          <input type="range" id="s-se" min="0" max="80" step="1" value="25"></label>
        <label class="sl"><span class="lab">阴影浓度 <b id="s-sf-v">15</b></span>
          <input type="range" id="s-sf" min="0" max="60" step="1" value="15"></label>
        <label class="sl"><span class="lab">染色 alpha <b id="s-ta-v">0</b></span>
          <input type="range" id="s-ta" min="0" max="40" step="1" value="0"></label>
      </div>
      <div class="togrow">
        <label class="switch" id="sw4" role="switch" aria-checked="true"><span class="track"><span class="knob"></span></span>blurEdge（边缘更糊，中心更清）</label>
        <button class="btn sm" id="b4tint">加一点冷色染色</button>
      </div>
    </div>
    <p class="hint">把「撕裂感」拉出来：模糊半径调到 60 时，边缘的光晕会明显跑出形状边界——因为它采样的就是玻璃外围的背景。</p>
  </section>
""",
    js="""
(function(){
  var A = Glass.make(document.getElementById('cL'), {debug:0, blurR:0, shadowFactor:0, tintA:0, blurEdge:0});
  var B = Glass.make(document.getElementById('cR'), {debug:0});
  Glass.bind(B, {'s-br':'blurR','s-se':'shadowExpand','s-sf':'shadowFactor','s-ta':'tintA'}, function(key,v){
    if(key==='blurR') document.getElementById('r4a').textContent = (Math.round(v))+' px';
    if(key==='shadowFactor') document.getElementById('r4c').textContent = Math.round(v)+'%';
  });
  document.getElementById('b4tint').addEventListener('click',function(){
    var on = B.P.tint[3] < 0.1;
    B.P.tint = on ? [0.55,0.78,1.0,0.16] : [1,1,1,0];
    document.getElementById('s-ta').value = Math.round(B.P.tint[3]*100);
    document.getElementById('s-ta-v').textContent = Math.round(B.P.tint[3]*100);
    this.textContent = on?'去掉染色':'加一点冷色染色';
  });
  var sw=document.getElementById('sw4');
  sw.addEventListener('click',function(){
    var on = sw.getAttribute('aria-checked')==='true';
    sw.setAttribute('aria-checked', on?'false':'true');
    B.P.blurEdge = on?0:1;
  });
})();
""",
    prompt="""
做一个单文件 HTML（WebGL2），把液态玻璃的「模糊 + 阴影 + 染色」单独拎出来做对比，左右两块画布。

【必须真的用两趟一维卷积（这是重点）】
1) 模糊半径 r（默认 18，范围 1–200，滑杆实际给 1–60）→ sigma = max(r/3, 0.0001)。
2) 核宽固定 ±15（共 31 个采样点），权重 w[i] = exp(-0.5·(i/3)²) 归一化；纵向一趟写进 FBO，横向一趟从该 FBO 取样。
3) 对比页要能显示「每趟取样数 31」这个读数，说明为什么不是 961。
4) blurEdge 开关：开启时模糊程度随「离边缘距离」变化——中心用较锐的背景、边缘用最糊的背景，用 mix(sharp, blurred, smoothstep(0, radius×2.6, edgeDist)) 实现；关闭时整块均匀模糊。

【阴影】
5) 阴影不是 CSS box-shadow：把 SDF 向外偏移 shadowExpand（默认 25px）再软化，乘以 shadowFactor/100（默认 15%），并整体沿 shadowPos 偏移 (0, −10)，绘制在玻璃之前。

【染色】
6) tint 为 rgba(255,255,255,tintA/100)，叠加在合成结果上；默认 alpha = 0（完全无色）。给一个按钮切到淡蓝 tint，直观看到染色。

【对比与交互】
- 左画布：blurRadius=0、shadowFactor=0、tint=0，作为「只剩折射」的基准。
- 右画布：默认参数，滑杆实时生效；两个画布都跟随各自鼠标做弹簧移动。

【自检标准】
- 把模糊半径从 1 拉到 60，背景必须出现清晰可辨的糊化梯度；
- 关掉阴影后玻璃应该「浮不起来」，打开后底部必须有偏移的软阴影；
- blurEdge 关闭时四角与中心的模糊程度必须一致。

输出完整 HTML。
""",
    copyable=[
        "<b>可分离卷积</b>：2×31 次取样代替 961 次，是所有实时模糊的默认做法。",
        "<b>sigma = r/3 + 固定 31 个 tap</b>：半径变化不用重建核，只改 sigma，性能稳定。",
        "<b>blurEdge</b>：中心清、边缘糊，是「玻璃有厚度」的第二个来源（第一个是折射）。",
        "<b>阴影用 SDF 扩张</b>：不用真的做 blur pass，偏移 SDF 就够了，且形状永远对齐。",
    ],
    uncopyable=[
        "<b>25/15/10 这组阴影参数</b>：深色背景专用，浅色背景要重调。",
        "<b>tint 默认全透明</b>：颜色是品牌选择，不是机制。",
        "<b>31 个 tap</b>：移动端可降到 15 个 tap，视觉差异很小。",
    ],
)

L05 = dict(
    no="05", slug="spring-follow", short="弹簧跟随", title="玻璃为什么不能直接跟着鼠标走",
    layer="react-spring · controller", path="src/hooks/useGlassController",
    case_url="https://github.com/iyinchao/liquid-glass-studio",
    ref="原参考：@react-spring/web 的 useSpring 控制器",
    lede="直接设 transform 是「瞬移」：指针动 1px 玻璃就动 1px，看起来像贴纸。原项目用 spring 控制器把指针位置当目标值，位置有惯性和过冲，于是玻璃会「追」鼠标。三块画布分别是 none / lerp / spring——差别一眼可见。",
    quote="「弹簧不是装饰，它是材质的一部分：玻璃有质量。」",
    quote_from="useGlassController · velocity 追踪",
    mech="目标值 = 指针位置；每帧 v += (target−x)·k·dt，v *= damping，x += v。k/damping 决定软硬，velocity 同时用来驱动尺寸挤压。",
    params="跟随模式 none / lerp / spring · 刚度 k = 0.22（默认）· 阻尼 = 0.72 · 尺寸回弹 springSizeFactor = 0.4",
    verify="指针离开画布后形状必须回到静止位；spring 模式下快速甩动必须出现过冲（overshoot）；lerp 模式不得过冲",
    stage="""
  <section class="stagewrap">
    <div class="stagebar">
      <span class="lbl">liquid-glass · case 05 · follow physics</span>
      <div class="readout"><b id="r5a">SPRING</b><span class="sep">·</span><span>速度 <b id="r5b">0.0</b></span><span class="sep">·</span><span>过冲 <b id="r5c">0.0</b> px</span></div>
    </div>
    <div class="trio">
      <div class="cell">
        <div class="cell-h"><b>none · 瞬移</b><span>0 帧延迟</span></div>
        <div class="gcanvas short"><canvas id="cA"></canvas></div>
      </div>
      <div class="cell">
        <div class="cell-h"><b>lerp · 线性插值</b><span>不会过冲</span></div>
        <div class="gcanvas short"><canvas id="cB"></canvas></div>
      </div>
      <div class="cell">
        <div class="cell-h"><b>spring · 弹簧</b><span>会过冲</span></div>
        <div class="gcanvas short"><canvas id="cC"></canvas></div>
      </div>
    </div>
    <div class="ctl">
      <div class="ctl-grid">
        <label class="sl"><span class="lab">弹簧刚度 k <b id="s-k-v">0.22</b></span>
          <input type="range" id="s-k" min="0.05" max="0.6" step="0.01" value="0.22"></label>
        <label class="sl"><span class="lab">阻尼 <b id="s-d-v">0.72</b></span>
          <input type="range" id="s-d" min="0.55" max="0.95" step="0.01" value="0.72"></label>
        <label class="sl"><span class="lab">尺寸回弹 <b id="s-ss-v">0.4</b></span>
          <input type="range" id="s-ss" min="0" max="1" step="0.02" value="0.4"></label>
        <label class="sl"><span class="lab">玻璃宽度 <b id="s-sw-v">230</b></span>
          <input type="range" id="s-sw" min="140" max="300" step="2" value="230"></label>
      </div>
      <div class="togrow">
        <button class="btn sm" id="b5shake">甩一下</button>
        <span class="hint" style="margin:0">点「甩一下」会把指针目标值瞬移到对角，三块画布的反应差别最明显：左边直接跳，中间匀速滑，右边冲过头再回来。</span>
      </div>
    </div>
    <p class="hint">读数里的「过冲」是三块画布中 spring 的最大越界距离；刚度越高、阻尼越低，过冲越明显（k 很小时弹簧被自己压住，反而不冲）。</p>
  </section>
""",
    extra_css=".trio{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}@media(max-width:900px){.trio{grid-template-columns:1fr}}",
    js="""
(function(){
  var OPT = {shapeW:230, shapeH:170, radius:75, idle:false};
  var A = Glass.make(document.getElementById('cA'), Object.assign({follow:'none'},   OPT));
  var B = Glass.make(document.getElementById('cB'), Object.assign({follow:'lerp'},   OPT));
  var C = Glass.make(document.getElementById('cC'), Object.assign({follow:'spring'}, OPT));
  var kB=document.getElementById('r5b'), kC=document.getElementById('r5c'), kA=document.getElementById('r5a');
  /* 滑杆给的是「手感系数」，换算成弹簧常数：stiff = k×800，damp = -ln(每帧保留率)×60 */
  Glass.bind(C, {'s-k':'stiff','s-d':'damp','s-ss':'sizeSpring','s-sw':'shapeW'}, function(key,v){
    if(key==='stiff'){ var st=v*800; C.P.stiff=st; B.P.stiff=st; }
    if(key==='damp'){ var dp=-Math.log(v)*60; C.P.damp=dp; B.P.damp=dp; }
    if(key==='shapeW'){ A.P.shapeW = v; B.P.shapeW = v; }
    if(key==='stiff') document.getElementById('r5a').textContent = v<0.12?'SOFT':(v>0.4?'STIFF':'SPRING');
  });
  var flip = 1;
  document.getElementById('b5shake').addEventListener('click',function(){
    flip = -flip;
    [A,B,C].forEach(function(g){
      if(!g) return;
      var w=g.canvas.clientWidth, h=g.canvas.clientHeight, d=g.dpr||1;
      g.target.x = flip * w * 0.28 * d;
      g.target.y = flip * h * 0.22 * d;
    });
    B.overshoot = 0; C.overshoot = 0;
  });
  setInterval(function(){
    if(!C) return;
    var d=C.dpr||1;
    kB.textContent = (Math.hypot(C.vel.x,C.vel.y)/d/1000).toFixed(2);
    kC.textContent = (C.overshoot/d).toFixed(1);
    kA.textContent = C.P.stiff<0.12?'SOFT':(C.P.stiff>0.4?'STIFF':'SPRING');
  },120);
})();
""",
    prompt="""
做一个单文件 HTML（WebGL2），用同一个液态玻璃 shader 渲染三块画布，只改「跟随物理」，并排对比 none / lerp / spring。

【三种跟随模式（必须真的三种，且共用一套渲染）】
1) none：形状中心 = 指针位置，零延迟。
2) lerp：每帧 x += (target − x) × 0.28；永不过冲。
3) spring：v += (target − x) × k × dt × 60；v ×= damp；x += v × dt × 60。默认 k=0.22、damp=0.72，都必须可调（k 0.05–0.6，damp 0.55–0.95）。

【尺寸回弹】
4) 用弹簧的速度驱动形状轻微缩放：scale = 1 + clamp(|v|,0,1)×sizeSpring×0.06。sizeSpring 默认 0.4，可调到 0 关闭。这样快速甩动时玻璃会像果冻一样被拉扯。

【交互】
5) 三块画布各自跟随自己的指针；指针离开画布后，形状用同一套物理回到画布中心（不能瞬间归位）。
6) 一个「甩一下」按钮：把三块画布的指针目标瞬移到对角，用来对比反应差异。
7) 读数显示 spring 那块的当前速度与最大过冲距离（px），每 120ms 刷新。

【自检标准】
- spring 模式在「甩一下」之后必须出现可见过冲（数值 > 1px），lerp 的过冲读数必须是 0；
- k 从 0.05 调到 0.6，跟随手感必须从「很软很滞后」变成「很硬几乎跟手」；
- 指针移出画布后三块都必须平滑回到中心，不能闪跳。

输出完整 HTML。
""",
    copyable=[
        "<b>三种模式共用一套渲染</b>：物理只是喂给 shader 的一组位置/缩放，渲染管线不用动。",
        "<b>velocity 顺手驱动缩放</b>：一个速度值同时做出跟随与果冻感，不用额外的动画。",
        "<b>回到中心也用同一套物理</b>：避免「移出即瞬移」的廉价感。",
        "<b>把过冲做成读数</b>：参数的作用立刻可验证。",
    ],
    uncopyable=[
        "<b>k=0.22 / damp=0.72</b>：这是它配合 react-spring 默认 mass/tension 标出来的手感值。",
        "<b>sizeSpring 的具体弧度</b>：不同画布尺寸需要按比例缩放。",
        "<b>「甩一下」这种演示按钮</b>：是给观众看的，产品里不会有。",
    ],
)

L06 = dict(
    no="06", slug="render-steps", short="渲染步骤查看", title="把 4 个 pass 一层层剥开",
    layer="webgl2 · STEP 0–7", path="src/components/StepViewer",
    case_url="https://github.com/iyinchao/liquid-glass-studio",
    ref="原参考：项目自带的 STEP 0–7 渲染步骤面板",
    lede="原项目最值得抄的不是玻璃，而是这个面板：STEP 按钮把管线切成 8 个可观察的中间态——原始背景、纵向模糊、横向模糊、SDF、法线、边缘因子、菲涅尔+眩光、最终合成。它把「黑盒 shader」变成可检查的流水线。",
    quote="「能看见中间步骤的渲染器，才调得动参数。」",
    quote_from="STEP 0–7 设计",
    mech="同一套 4-pass 管线，每个 pass 结束后把中间纹理按 debug 值直接输出到屏幕；主合成 pass 用 uniform 选择输出哪一项中间量。",
    params="STEP 0 背景 · 1 纵向模糊 · 2 横向模糊 · 3 SDF · 4 法线 · 5 边缘因子 · 6 菲涅尔+眩光 · 7 最终",
    verify="每个 STEP 必须来自真实中间纹理（不是重新计算一遍），且 STEP 7 必须与正常渲染逐像素一致",
    stage="""
  <section class="stagewrap">
    <div class="stagebar">
      <span class="lbl">liquid-glass · case 06 · step viewer</span>
      <div class="readout"><b id="r6a">STEP 7 · 最终合成</b><span class="sep">·</span><span>pass <b id="r6b">4 / 4</b></span></div>
    </div>
    <div class="cell" style="padding:10px">
      <div class="gcanvas tall"><canvas id="cS"></canvas></div>
      <div class="steps" id="steps6">
        <button data-d="10">0<br><span>背景</span></button>
        <button data-d="11">1<br><span>纵向模糊</span></button>
        <button data-d="12">2<br><span>横向模糊</span></button>
        <button data-d="1">3<br><span>SDF</span></button>
        <button data-d="2">4<br><span>法线</span></button>
        <button data-d="3">5<br><span>边缘因子</span></button>
        <button data-d="6">6<br><span>菲涅尔+眩光</span></button>
        <button data-d="0" aria-selected="true">7<br><span>最终</span></button>
      </div>
    </div>
    <div class="ctl">
      <div class="ctl-grid">
        <label class="sl"><span class="lab">播放速度 <b id="s-sp-v">1.0×</b></span>
          <input type="range" id="s-sp" min="0.2" max="3" step="0.1" value="1"></label>
        <label class="sl"><span class="lab">背景模式 <b id="s-bm-v">色斑</b></span>
          <input type="range" id="s-bm" min="0" max="1" step="1" value="0"></label>
      </div>
      <div class="togrow">
        <button class="btn sm" id="b6play">自动播放步骤</button>
        <button class="btn sm ghost" id="b6prev">上一步</button>
        <button class="btn sm ghost" id="b6next">下一步</button>
      </div>
    </div>
    <p class="hint">STEP 0–2 是「纹理流」，STEP 3–6 是「几何量」，STEP 7 才把它们乘在一起。看一遍就知道每个参数到底作用在哪一层。</p>
  </section>
""",
    extra_css="""
.steps{display:grid;grid-template-columns:repeat(8,1fr);gap:6px;margin-top:9px}
.steps button{padding:7px 4px;border-radius:8px;border:1px solid var(--line);background:var(--card);color:var(--ink-3);
  font-size:10.5px;line-height:1.25;cursor:pointer;font-family:ui-monospace,Menlo,monospace}
.steps button span{font-family:inherit;font-size:10px}
.steps button[aria-selected="true"]{background:var(--ink);color:#fff;border-color:transparent}
@media(max-width:760px){.steps{grid-template-columns:repeat(4,1fr)}}
""",
    js="""
(function(){
  var S = Glass.make(document.getElementById('cS'), {debug:0, follow:'spring', shapeW:460, shapeH:300, radius:130});
  var order=[10,11,12,1,2,3,6,0];
  var names={10:'背景',11:'纵向模糊',12:'横向模糊',1:'SDF',2:'法线',3:'边缘因子',6:'菲涅尔+眩光',0:'最终合成'};
  var idx=7, timer=null;
  function select(d){
    S.P.debug=d;
    idx=order.indexOf(d);
    document.querySelectorAll('#steps6 button').forEach(function(b){ b.setAttribute('aria-selected', String(parseInt(b.dataset.d,10)===d)); });
    document.getElementById('r6a').textContent='STEP '+idx+' · '+names[d];
    document.getElementById('r6b').textContent=(d===10?1:(d===11||d===12?2:(d===0?4:3)))+' / 4';
  }
  document.querySelectorAll('#steps6 button').forEach(function(b){
    b.addEventListener('click',function(){ select(parseInt(b.dataset.d,10)); });
  });
  document.getElementById('b6next').addEventListener('click',function(){ select(order[(idx+1)%8]); });
  document.getElementById('b6prev').addEventListener('click',function(){ select(order[(idx+7)%8]); });
  document.getElementById('b6play').addEventListener('click',function(){
    if(timer){ clearInterval(timer); timer=null; this.textContent='自动播放步骤'; return; }
    this.textContent='暂停';
    var sp=parseFloat(document.getElementById('s-sp').value);
    timer=setInterval(function(){ select(order[(idx+1)%8]); }, 1200/parseFloat(document.getElementById('s-sp').value));
  });
  document.getElementById('s-sp').addEventListener('input',function(){
    var v=parseFloat(this.value);
    document.getElementById('s-sp-v').textContent=v.toFixed(1)+'×';
    if(timer){ clearInterval(timer); timer=setInterval(function(){ select(order[(idx+1)%8]); },1200/v); }
  });
  document.getElementById('s-bm').addEventListener('input',function(){
    var v=parseInt(this.value,10);
    S.P.bgMode=v;
    document.getElementById('s-bm-v').textContent=v?'条纹':'色斑';
  });
})();
""",
    prompt="""
做一个单文件 HTML（WebGL2），实现一个液态玻璃的「渲染步骤查看器」：同一套 4-pass 管线，把每个中间态都能单独显示出来。

【管线】
1) pass 1：程序化背景 → texBG。
2) pass 2：texBG 纵向高斯 → texV。
3) pass 3：texV 横向高斯 → texH。
4) pass 4：主合成，同时采样 texBG 与 texH，输出 SDF / 法线 / 边缘因子 / 菲涅尔 / 眩光 的具体贡献。

【STEP 0–7 必须对应真实中间纹理或真实 uniform 分支】
- STEP 0 原始背景：直接输出 texBG（不重算背景）。
- STEP 1 纵向模糊：输出 texV。
- STEP 2 横向模糊：输出 texH（此时画面应明显「横向拉丝后再糊」，与 STEP 1 肉眼可分辨）。
- STEP 3 SDF：输出 clamp(-sdf/40, 0, 1) 的灰度，形状内部为白，并叠一条边缘等高线。
- STEP 4 法线：输出 normal×0.5+0.5 的 RGB。
- STEP 5 边缘因子：输出 edge 的灰度（中心必须为纯黑）。
- STEP 6 菲涅尔+眩光：只输出这两项叠加的白色高光（黑底）。
- STEP 7 最终：完整合成，必须与正常渲染逐像素一致。

【交互】
- 8 个 STEP 按钮，另加上一步/下一步/自动播放（速度 0.2×–3×，可调）。
- 背景模式可在「色斑 / 条纹」之间切换，用来验证 STEP 1 与 STEP 2 的方向差异。
- 玻璃继续跟随鼠标（spring），这样任何 STEP 下都能看到形状在动。
- 显示当前是第几个 pass（1/4 … 4/4）。

【自检标准】
- STEP 1 与 STEP 2 必须能看出模糊方向不同（截图对比）；
- STEP 5 中心为纯黑、边缘为亮环；
- 自动播放到 STEP 7 时画面必须与默认渲染完全一致（做一个像素对比开关更好）。

输出完整 HTML。
""",
    copyable=[
        "<b>debug uniform 直出中间态</b>：一个 int 参数切换 8 种输出，不用 8 套 shader。",
        "<b>STEP 分两类</b>：纹理流（0–2）与几何量（3–6），这个分类本身就能教会读者管线结构。",
        "<b>自动播放 + 速度控制</b>：静态截图讲不清「顺序」，播放可以。",
        "<b>pass 计数读数</b>：随时知道自己站在管线的哪一层。",
    ],
    uncopyable=[
        "<b>它的 STEP 具体配色</b>：灰度/SDF 着色是调试惯例，不必照抄色阶。",
        "<b>背景素材</b>：原项目可以传图和视频，这里必须程序化生成。",
        "<b>面板 UI 布局</b>：可迁移的是「8 个正交切面」，不是那排按钮的样子。",
    ],
)
