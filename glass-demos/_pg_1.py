# -*- coding: utf-8 -*-
"""L01 折射与色散 / L02 菲涅尔与高光 / L03 超椭圆与 Blob"""

L01 = dict(
    no="01", slug="refraction", short="折射与色散", title="把边缘掰弯：折射、色散与 4-pass 管线",
    layer="webgl2 · 4-pass", path="src/shaders/fragment-main.glsl",
    case_url="https://github.com/iyinchao/liquid-glass-studio/blob/main/src/shaders/fragment-main.glsl",
    ref="原参考：Apple Liquid Glass（Web 高保真复刻）",
    lede="液态玻璃最容易被误认成「毛玻璃 + 描边」。真正让它像玻璃的是边缘那一圈被掰弯的光：先由 SDF 算法线，再用 Snell 算出每个像素的偏移量，最后让 R/G/B 三个通道各用一点点不同的折射率去采样背景。",
    quote="「中心不偏移，边缘拼命偏移——这就是玻璃厚度的全部秘密。」",
    quote_from="fragment-main.glsl · 边缘因子实现",
    mech="SDF → 法线 → 边缘因子 edge = −tan(θT−θI) → 沿法线偏移采样模糊背景；R/G/B 用 N=0.98/1.0/1.02 分别采样，产生色散。",
    params="默认值取自 src/Controls.tsx：折射厚度 20（1–80）· 折射距离 0.05（0–0.2）· 折射率 1.4（1–4）· 色散 7（0–50）",
    verify="openspec：SDF<0 且在厚度带内才计算边缘因子；超出厚度区域边缘因子必须为 0，按无偏移采样；色散>0 时三通道按各自折射率取样",
    stage="""
  <section class="stagewrap">
    <div class="stagebar">
      <span class="lbl">liquid-glass · case 01 · refraction / dispersion</span>
      <div class="readout"><b id="r1a">4 PASS</b><span class="sep">·</span><span>色散通道偏移 <b id="r1b">±0.56%</b></span><span class="sep">·</span><span>模糊半径 <b id="r1c">18</b> px</span></div>
    </div>
    <div class="pair">
      <div class="cell">
        <div class="cell-h"><b>拆解 · 渲染步骤</b><span id="dbgName">边缘因子</span></div>
        <div class="gcanvas"><canvas id="cL"></canvas></div>
      </div>
      <div class="cell">
        <div class="cell-h"><b>合成 · 最终玻璃</b><span>WebGL2</span></div>
        <div class="gcanvas"><canvas id="cR"></canvas></div>
      </div>
    </div>
    <div class="ctl">
      <div class="seg" id="dbg">
        <button data-d="1">SDF</button>
        <button data-d="2">法线</button>
        <button data-d="3" aria-selected="true">边缘因子</button>
        <button data-d="4">菲涅尔</button>
        <button data-d="0">最终</button>
      </div>
      <div class="ctl-grid" style="margin-top:13px">
        <label class="sl"><span class="lab">折射厚度 <b id="s-thick-v">20</b></span>
          <input type="range" id="s-thick" min="1" max="80" step="0.5" value="20"></label>
        <label class="sl"><span class="lab">折射距离 <b id="s-refd-v">0.05</b></span>
          <input type="range" id="s-refd" min="0" max="0.2" step="0.005" value="0.05"></label>
        <label class="sl"><span class="lab">折射率 <b id="s-reff-v">1.4</b></span>
          <input type="range" id="s-reff" min="1.05" max="3" step="0.05" value="1.4"></label>
        <label class="sl"><span class="lab">色散 <b id="s-disp-v">7</b></span>
          <input type="range" id="s-disp" min="0" max="50" step="1" value="7"></label>
      </div>
      <div class="togrow">
        <span class="hint" style="margin:0">鼠标移进任一画布，玻璃会跟着指针走；把「色散」拉到 0，右图边缘立刻变干净。</span>
      </div>
    </div>
    <p class="hint">左图可切 SDF / 法线 / 边缘因子 / 菲涅尔 / 最终——这就是原项目 TODO 里勾选完成的「渲染步骤查看」。</p>
  </section>
""",
    js="""
(function(){
  var A = Glass.make(document.getElementById('cL'), {debug:3, follow:'spring'});
  var B = Glass.make(document.getElementById('cR'), {debug:0, follow:'spring'});
  Glass.bind(B, {'s-thick':'thick','s-refd':'refDist','s-reff':'refFactor','s-disp':'disp'}, function(key, v){
    if(key==='disp'){
      document.getElementById('r1b').textContent='±'+(0.02*(v/25)*100).toFixed(2)+'%';
    }
    if(key==='refDist'){ /* 折射距离同时影响可见偏移 */ }
  });
  var names={'1':'SDF','2':'法线','3':'边缘因子','4':'菲涅尔','0':'最终'};
  document.querySelectorAll('#dbg button').forEach(function(b){
    b.addEventListener('click', function(){
      document.querySelectorAll('#dbg button').forEach(function(x){ x.setAttribute('aria-selected', String(x===b)); });
      A.P.debug = parseInt(b.dataset.d,10);
      document.getElementById('dbgName').textContent = names[b.dataset.d];
    });
  });
  document.getElementById('r1c').textContent = B.P.blurR;
})();
""",
    prompt="""
做一个单文件 HTML（WebGL2，无框架无 CDN），复刻 liquid-glass-studio 的核心：折射 + 色散，并且必须用 4 个 pass。

【管线（必须真的分成 4 个 pass，用 FBO 串起来）】
1) 背景 pass：渲染一张程序化背景（渐变 + 3 个大色斑 + 细网格线），写进 FBO-A。
2) 纵向模糊 pass：从 FBO-A 取，做可分离高斯模糊的纵向一半，写进 FBO-B。
3) 横向模糊 pass：从 FBO-B 取，做横向一半，写进 FBO-C。
4) 主合成 pass：同时取 FBO-A（原图）与 FBO-C（模糊图）合成玻璃。

【主合成算法（照搬这套数学，别自创）】
- 形状用 SDF：圆角矩形（角部用超椭圆 pow(pow(x,n)+pow(y,n), 1/n)），可与第二个圆形用 smin 融合。
- 法线 = SDF 的有限差分梯度归一化。
- 里面距离 nd = -SDF（正数表示在形状内部多少像素）。
- 边缘因子：xr = 1 - nd/厚度；θI = asin(clamp(pow(xr,2),0,1))；θT = asin(sin θI / 折射率)；edge = max(-tan(θT-θI), 0)；当 nd ≥ 厚度时 edge 必须为 0。
- 采样偏移 = 法线 × edge × 折射距离 × 220px，再除以分辨率换成 UV 单位。
- 色散：N_R=0.98 / N_G=1.0 / N_B=1.02，R 通道用 edge×(1+0.02×dispGain)、B 通道用 edge×(1−0.02×dispGain) 分别取三张图，dispGain = 色散值/25。
- 模糊混合：mix(锐利背景, 模糊背景, smoothstep(0, 厚度×2.6, nd))，即越靠边缘越糊（对应 blurEdge）。

【可调参数（默认值照抄）】折射厚度 20（1–80）· 折射距离 0.05（0–0.2）· 折射率 1.4（1–4）· 色散 7（0–50）· 模糊半径 18px

【必须提供一个「渲染步骤」切换】用同一个 shader 里的 debug uniform 输出：① SDF 等高线（内含边缘白线）② 法线彩色图 ③ 边缘因子灰度图 ④ 菲涅尔 ⑤ 最终合成。左画布显示步骤、右画布显示最终，两个画布各自跟随自己的鼠标。

【自检标准】
- 形状正中心：edge 必须为 0，采样无偏移；
- 靠近边缘但超出厚度带：edge 归 0，画面不能出现一圈假折射；
- 色散调大时，边缘必须出现可分辨的红/蓝分离（截图对比）；
- 关掉全部参数时应能退化成一块干净的毛玻璃。

输出完整 HTML。
""",
    copyable=[
        "<b>4-pass 管线</b>：背景 / 纵向模糊 / 横向模糊 / 主合成，中间产物是纹理，不是重复计算。",
        "<b>edge = −tan(θT−θI)</b>：用 Snell 定律把厚度换算成像素偏移，一个公式就得到玻璃的弯边。",
        "<b>中心强制为 0</b>：只有边缘一圈偏移，中心老老实实采样模糊背景。",
        "<b>RGB 三个折射率</b>：0.98 / 1.0 / 1.02 的极微小差异就足以产生色散，不需要真的做光谱。",
        "<b>debug uniform 输出中间量</b>：这是这类材质最有效的调试方式。",
    ],
    uncopyable=[
        "<b>程序化背景</b>：原项目用的是真实图片/视频背景（雪峰、街道、建筑…），换成你自己的素材才成立。",
        "<b>220px 这个偏移系数</b>：是按它的画布尺寸调的，视口变了要重标。",
        "<b>具体的色斑配色</b>：可迁移的是「背景要有强对比色块，否则折射看不出来」。",
    ],
)

L02 = dict(
    no="02", slug="fresnel-glare", short="菲涅尔与高光", title="没有菲涅尔与眩光，玻璃就是一块塑料",
    layer="webgl2 · 主合成", path="src/shaders/fragment-main.glsl",
    case_url="https://github.com/iyinchao/liquid-glass-studio/blob/main/src/shaders/fragment-main.glsl",
    ref="原参考：Apple Liquid Glass",
    lede="同一块玻璃，左边关掉菲涅尔与眩光，右边打开。菲涅尔负责「越靠边越亮」的那圈反射，眩光负责一道有方向的镜面高光——两者都只在边缘带内计算，所以调整范围参数能直接看到亮环变厚变薄。",
    quote="「菲涅尔是环，眩光是弧；一个均匀、一个有方向。」",
    quote_from="fragment-main.glsl · fresnel / glare 实现",
    mech="菲涅尔：pow(1 − nd/range + hardness, 5) × 强度；眩光：法线与光源方向的点积 → 幂次收敛 → 乘边缘带遮罩。",
    params="菲涅尔 范围 30 / 硬度 20 / 强度 20 · 眩光 范围 30 / 硬度 20 / 强度 90 / 收敛 50 / 对侧 80 / 角度 −45°",
    verify="openspec：菲涅尔在边缘范围内按幂曲线向白色混合，受 range / hardness / intensity 三参数控制；眩光由法线与眩光方向的夹角决定，受 convergence 与 opposite 调制",
    stage="""
  <section class="stagewrap">
    <div class="stagebar">
      <span class="lbl">liquid-glass · case 02 · fresnel / glare</span>
      <div class="readout"><b id="r2a">FRESNEL + GLARE</b><span class="sep">·</span><span>光源角度 <b id="r2b">-45°</b></span><span class="sep">·</span><span>边缘带 <b id="r2c">30</b> px</span></div>
    </div>
    <div class="pair">
      <div class="cell">
        <div class="cell-h"><b>关闭 · 形状几乎消失</b><span>fresnel 0 / glare 0</span></div>
        <div class="gcanvas"><canvas id="cL"></canvas></div>
      </div>
      <div class="cell">
        <div class="cell-h"><b>开启 · 加菲涅尔与眩光</b><span>默认参数</span></div>
        <div class="gcanvas"><canvas id="cR"></canvas></div>
      </div>
    </div>
    <div class="ctl">
      <div class="ctl-grid">
        <label class="sl"><span class="lab">菲涅尔范围 <b id="s-fr-v">30</b></span>
          <input type="range" id="s-fr" min="2" max="100" step="1" value="30"></label>
        <label class="sl"><span class="lab">菲涅尔硬度 <b id="s-fh-v">20</b></span>
          <input type="range" id="s-fh" min="0" max="100" step="1" value="20"></label>
        <label class="sl"><span class="lab">菲涅尔强度 <b id="s-ff-v">20</b></span>
          <input type="range" id="s-ff" min="0" max="100" step="1" value="20"></label>
        <label class="sl"><span class="lab">眩光角度 <b id="s-ga-v">-45</b></span>
          <input type="range" id="s-ga" min="-180" max="180" step="1" value="-45"></label>
        <label class="sl"><span class="lab">眩光强度 <b id="s-gf-v">90</b></span>
          <input type="range" id="s-gf" min="0" max="120" step="1" value="90"></label>
        <label class="sl"><span class="lab">眩光收敛 <b id="s-gc-v">50</b></span>
          <input type="range" id="s-gc" min="0" max="100" step="1" value="50"></label>
      </div>
      <div class="togrow">
        <button class="btn sm" id="b2spin">转动光源</button>
        <button class="btn sm ghost" id="b2reset">复位</button>
        <span class="hint" style="margin:0">转光源时注意高光弧只沿着一边走——它是方向性的，不是一圈均匀发光。</span>
      </div>
    </div>
    <p class="hint">左图连轮廓都找不到了——菲涅尔正是「形状」的来源，眩光才是「抛光」的来源。缺一个都会掉进塑料感。</p>
  </section>
""",
    js="""
(function(){
  var A = Glass.make(document.getElementById('cL'), {debug:0, fresFactor:0, glareFactor:0, glareOpp:0, rim:0});
  var B = Glass.make(document.getElementById('cR'), {debug:0});
  Glass.bind(B, {'s-fr':'fresRange','s-fh':'fresHard','s-ff':'fresFactor',
                 's-ga':'glareAngle','s-gf':'glareFactor','s-gc':'glareConv'}, function(key,v){
    if(key==='glareAngle') document.getElementById('r2b').textContent = Math.round(v)+'°';
    if(key==='fresRange') document.getElementById('r2c').textContent = Math.round(v);
  });
  var spin=null;
  document.getElementById('b2spin').addEventListener('click',function(){
    if(spin){ clearInterval(spin); spin=null; this.textContent='转动光源'; return; }
    this.textContent='停下';
    var a=B.P.glareAngle;
    spin=setInterval(function(){
      a=(a+3)%360;
      B.P.glareAngle = a>180? a-360 : a;
      var el=document.getElementById('s-ga');
      el.value=Math.round(B.P.glareAngle);
      document.getElementById('s-ga-v').textContent=Math.round(B.P.glareAngle);
      document.getElementById('r2b').textContent=Math.round(B.P.glareAngle)+'°';
    },33);
  });
  var DEF={'s-fr':30,'s-fh':20,'s-ff':20,'s-ga':-45,'s-gf':90,'s-gc':50};
  var KEY={'s-fr':'fresRange','s-fh':'fresHard','s-ff':'fresFactor','s-ga':'glareAngle','s-gf':'glareFactor','s-gc':'glareConv'};
  document.getElementById('b2reset').addEventListener('click',function(){
    if(spin){ clearInterval(spin); spin=null; document.getElementById('b2spin').textContent='转动光源'; }
    Object.keys(DEF).forEach(function(id){
      var el=document.getElementById(id);
      el.value=DEF[id];
      B.P[KEY[id]]=DEF[id];
      document.getElementById(id+'-v').textContent=DEF[id];
    });
    document.getElementById('r2b').textContent='-45°';
    document.getElementById('r2c').textContent='30';
  });
})();
""",
    prompt="""
做一个单文件 HTML（WebGL2，无框架），在已经实现「折射 + 模糊」的液态玻璃基础上，加上菲涅尔反射与方向性眩光，并且用左右两块画布对比「关掉 / 打开」。

【菲涅尔（Fresnel）】
- 只在玻璃内部边缘带内计算：nd 为像素到边缘的距离（-SDF），range 为作用范围（默认 30px）。
- fres = pow(clamp(1 − nd/range + hardness/100, 0, 1), 5) × intensity/100。
- 结果叠加为白色高光（可乘 tint 颜色），让越靠边越亮；hardness 提高会让亮环更硬、范围更窄。

【眩光（Glare）】
- 光源方向由角度参数给出：dir = (cos θ, sin θ)，默认 θ = −45°（即左上打光）。
- lit = clamp(dot(normal, dir), 0, 1)；crescent = pow(lit, mix(3.0, 0.6, hardness/100))；再用 convergence 把它推进成一条细弧：mix(crescent, smoothstep(0.15,1.0,crescent), convergence/100)。
- 乘上边缘带遮罩 band = 1 − smoothstep(0, glareRange×dpr, nd)，再乘强度 glareFactor/100。
- 对侧还要有一条弱得多的反光：pow(clamp(dot(normal,-dir),0,1), 9) × band × opposite/100 × 0.22。
- 眩光必须是<b>方向性</b>的：转动角度参数时，高光弧应沿着轮廓滑动，而不是整圈同时变亮。

【交互要求】
- 左画布：fresnel intensity = 0、glare = 0（只有折射，作为对照）。
- 右画布：默认参数（range 30 / hardness 20 / intensity 20；glare 30 / 20 / 90 / convergence 50 / opposite 80 / angle −45）。
- 滑杆实时改右画布；再给一个「转动光源」按钮，让角度连续变化。

【自检标准】
- 关掉菲涅尔与眩光后，玻璃应立刻变「平」，只剩折射；
- 转光源到 180° 时亮弧应出现在对侧；
- 把 range 从 10 调到 100，亮环厚度必须有肉眼可见的变化。

输出完整 HTML。
""",
    copyable=[
        "<b>菲涅尔用 5 次幂</b>：便宜、可控，比真实 Schlick 近似更适合这种风格化玻璃。",
        "<b>眩光 = 法线 × 光源方向的点积</b>：方向性高光的通用写法，也适用于按钮、卡片。",
        "<b>对侧弱反光</b>：一条 0.22 系数的反光就让玻璃「立起来」了。",
        "<b>边缘带遮罩</b>：所有反光都乘 1−smoothstep(0, range, nd)，保证中心干净。",
    ],
    uncopyable=[
        "<b>默认强度 20 / 90</b>：是配合它那套深色背景调的。",
        "<b>−45° 这个打光角</b>：可迁移的是「全站统一一个光源方向」。",
        "<b>白色高光</b>：换成暖色就是落日玻璃，颜色本身不是机制。",
    ],
)

L03 = dict(
    no="03", slug="superellipse-blob", short="超椭圆与 Blob 融合", title="方块的角，和会融化的两块玻璃",
    layer="webgl2 · SDF", path="src/shaders/lib/sdf.glsl",
    case_url="https://github.com/iyinchao/liquid-glass-studio/blob/main/src/shaders/lib/sdf.glsl",
    ref="原参考：Apple Liquid Glass + Inigo Quilez 的 SDF 与 smin",
    lede="iOS 的圆角从来不是圆弧，而是超椭圆：把角部公式换成 pow(pow(x,n)+pow(y,n), 1/n) 之后，n=2 接近菱形、n=4~5 就是标准的 squircle、n=7 几乎回到矩形。而两块玻璃靠近时，用 smin 做的平滑最小值会让它们像水一样先连起来再分开。",
    quote="「圆角矩形和 squircle 的区别，就是 n 从 2 走到 5。」",
    quote_from="sdf.glsl · superellipseCornerSDF / smin",
    mech="角部 SDF = pow(pow(|x|,n)+pow(|y|,n),1/n) − r；两块形状用 smin(a,b,k) 融合，k = merge × 260px。",
    params="圆角半径 1–100（默认 120px 显示值）· 圆润度 2–7（4~5 = squircle）· 融合率 0–0.3（默认 0.06）· 副形状为半径 86px 的圆，跟随鼠标弹簧",
    verify="openspec：roundness 控制超椭圆指数（2=接近菱形，4~5=squircle，7=接近矩形）；merge=0 时两块形状必须保持清晰分界；merge>0 时边界平滑过渡",
    stage="""
  <section class="stagewrap">
    <div class="stagebar">
      <span class="lbl">liquid-glass · case 03 · superellipse / blob</span>
      <div class="readout"><b id="r3a">n = 2</b><span class="sep">·</span><span>融合率 <b id="r3b">0.06</b></span><span class="sep">·</span><span>副形状 <b id="r3c">关</b></span></div>
    </div>
    <div class="pair">
      <div class="cell">
        <div class="cell-h"><b>普通圆角 · n = 2</b><span>无融合</span></div>
        <div class="gcanvas"><canvas id="cL"></canvas></div>
      </div>
      <div class="cell">
        <div class="cell-h"><b>超椭圆 squircle · n = 5 + 融合</b><span>跟随鼠标</span></div>
        <div class="gcanvas"><canvas id="cR"></canvas></div>
      </div>
    </div>
    <div class="ctl">
      <div class="ctl-grid">
        <label class="sl"><span class="lab">圆润度 n <b id="s-n-v">5</b></span>
          <input type="range" id="s-n" min="2" max="7" step="0.1" value="5"></label>
        <label class="sl"><span class="lab">圆角半径 <b id="s-rad-v">90</b></span>
          <input type="range" id="s-rad" min="0" max="150" step="2" value="90"></label>
        <label class="sl"><span class="lab">融合率 <b id="s-mg-v">0.06</b></span>
          <input type="range" id="s-mg" min="0" max="0.3" step="0.005" value="0.06"></label>
        <label class="sl"><span class="lab">形状宽度 <b id="s-w-v">330</b></span>
          <input type="range" id="s-w" min="160" max="420" step="2" value="330"></label>
      </div>
      <div class="togrow">
        <label class="switch" id="sw3" role="switch" aria-checked="true"><span class="track"><span class="knob"></span></span>显示副形状（圆形）</label>
        <span class="hint" style="margin:0">把圆润度从 2 拖到 7，右图的角会先变「方」再变「软」——这就是 squircle 的手感来源。</span>
      </div>
    </div>
    <p class="hint">smin 是「先连起来、再分开」的唯一来源：merge 拉到 0.3，两块玻璃会像水滴一样黏在一起。</p>
  </section>
""",
    js="""
(function(){
  var A = Glass.make(document.getElementById('cL'), {debug:0, roundness:2, radius:90, shapeW:320, shapeH:240, showBlob:0, merge:0, follow:'none'});
  var B = Glass.make(document.getElementById('cR'), {debug:0, roundness:5, radius:90, shapeW:320, shapeH:240, showBlob:1, merge:0.06, follow:'spring'});
  Glass.bind(B, {'s-n':'roundness','s-rad':'radius','s-mg':'merge','s-w':'shapeW'}, function(key,v){
    if(key==='roundness') document.getElementById('r3a').textContent = 'n = '+(Math.round(v*10)/10);
    if(key==='merge') document.getElementById('r3b').textContent = (Math.round(v*1000)/1000);
  });
  A.P.shapeW = 320;
  var sw=document.getElementById('sw3');
  function syncBlob(){
    var on = sw.getAttribute('aria-checked')==='true';
    B.P.showBlob = on?1:0;
    document.getElementById('r3c').textContent = on?'开':'关';
  }
  sw.addEventListener('click',function(){
    sw.setAttribute('aria-checked', sw.getAttribute('aria-checked')==='true'?'false':'true');
    syncBlob();
  });
  syncBlob();
  document.getElementById('r3a').textContent='n = 5';
  /* 副形状绕主形状外缘公转，保证「融合」在静止状态下也看得见；指针进入后交给指针 */
  (function orbit(){
    requestAnimationFrame(orbit);
    if(!B || B.everMoved) return;
    var w=B.canvas.clientWidth, h=B.canvas.clientHeight, d=B.dpr||1, t=performance.now()*0.0006;
    B.target.x = Math.cos(t) * (w*0.5*0.62) * d;
    B.target.y = Math.sin(t*1.3) * (h*0.5*0.46) * d;
  })();
})();
""",
    prompt="""
做一个单文件 HTML（WebGL2），复刻 liquid-glass-studio 的「超椭圆圆角 + 形状融合」，左右并排对比 n=2 与 n=5。

【形状 SDF】
1) 圆角矩形的角部必须用<b>超椭圆</b>，不要用圆弧：
   float seCorner(vec2 p, float r, float n){ p = abs(p); return pow(pow(p.x,n)+pow(p.y,n), 1.0/n) - r; }
2) 完整形状：先算 d = abs(p) - halfSize + r；若 d.x>0 且 d.y>0 用 seCorner(d, r, n)，否则用 min(max(d.x,d.y),0) + length(max(d,0))。
3) 圆润度 n 的范围 2–7：2 = 接近菱形/硬圆角，4–5 = 标准 squircle（Apple 那种），7 = 几乎回到矩形。必须真的暴露成滑杆。

【形状融合（Blob）】
4) 第二块形状是一个半径 86px 的圆，位置由鼠标弹簧跟随（指针在画布内移动时它的目标点就是指针）。
5) 两块形状用平滑最小值合并：
   float smin(float a,float b,float k){ if(k<0.001) return min(a,b); float h=clamp(0.5+0.5*(b-a)/k,0.,1.); return mix(b,a,h)-k*h*(1.-h); }
   融合系数 k = merge × 260 × dpr，merge 滑杆范围 0–0.3。
6) merge = 0 时两块形状必须保持清晰分界（可截图验证）；merge 调大时边界要像水滴一样平滑过渡。

【交互与对比】
- 左画布固定 n=2、无融合、无副形状；右画布默认 n=5、merge 0.06、显示副形状并跟随鼠标。
- 滑杆：圆润度 / 圆角半径 / 融合率 / 形状宽度；一个开关控制副形状显隐。
- 玻璃本体继续用「折射 + 模糊 + 菲涅尔」的合成，别退化成纯色块。

【自检标准】
- n=2 与 n=5 在同一尺寸下必须能看出明显不同的角落曲线（截图并排比较）；
- merge=0 时两块形状之间有清晰缝隙；merge=0.3 时缝隙消失；
- 快速移动鼠标时副形状要有弹簧滞后（不能瞬移）。

输出完整 HTML。
""",
    copyable=[
        "<b>超椭圆角部公式</b>：三行代码换来 Apple 那种「软而不圆」的角。",
        "<b>smin 平滑最小值</b>：任何「两块靠近要黏起来」的效果都用它（水滴、加载点、开关）。",
        "<b>把 n 暴露成滑杆</b>：调参过程本身就是最好的说明。",
        "<b>副形状跟随鼠标</b>：SDF 世界里移动一个形状等于移动一个中心点，比改 transform 便宜。",
    ],
    uncopyable=[
        "<b>86px / 260px 这两个常数</b>：需要按你的画布尺寸重标。",
        "<b>Apple 的圆角具体值</b>：不同设备不同，抄个 n=5 只是近似。",
        "<b>「一块玻璃 + 一个圆」的构图</b>：换成导航条 + 头像球也成立。",
    ],
)
