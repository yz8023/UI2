# -*- coding: utf-8 -*-
"""m01 char-curtain / m02 lyre-crows / m03 string-clock"""

C1 = dict(
    no="01", slug="char-curtain", short="字符幕布", title="Hang it, then part it.",
    layer="canvas 2d", layer_cn="Canvas 2D + rAF",
    ref="原参考：motion-test demo 01（React 画廊），此处为机制复现",
    case_url="https://github.com/feitangyuan/motion-web/tree/main/cases/char-curtain",
    kicker="motion-web · 结构即机制",
    lede="576 个字符挂在 24 根独立的竖绳上，横向没有任何连接——这就是鼠标能把它「分开」而不是「压出一个坑」的全部原因。每个字形的颜色和透明度都是它自己速度的函数，所以静止的一帧也能看出涟漪在哪。",
    quote="「布是一组绳子，不是一张网。」",
    quote_from="cases/char-curtain · 设计说明",
    mech="24 列 × 16 行的 Verlet 质点，只有竖向约束（横向 0 连接），5 次约束求解；指针推力半径 75px，顶行以 0.35 的弹簧系数挂回原点。",
    params="gravity 0.28 · drag 0.025 · solver 5 passes · pointer r=75 / force=4.8 · y bias 0.35 · bounce 0.6",
    verify="位移中位数 ≥ 6px；单列位移 ≥ 4px 时远端 < 20%；无约束超差 > 35%；松手后回到原点 ±2px",
    stage="""
  <section class="stagewrap">
    <div class="stagebar">
      <span class="lbl">case 01 · char-curtain · 24 strings</span>
      <div class="readout"><b id="r1a">POINTER IDLE</b><span class="sep">·</span><span>中位位移 <b id="r1b">0.0</b> px</span><span class="sep">·</span><span>远端 <b id="r1c">0.0</b> px</span></div>
    </div>
    <div class="canvasbox"><canvas id="c1" width="960" height="460"></canvas></div>
    <div class="ctrls">
      <button class="btn sm" id="b1gust">来一阵风</button>
      <button class="btn sm ghost" id="b1reset">复位</button>
      <span class="hint" style="margin:0">鼠标穿过幕布 → 向两侧分开；滚轮/按钮 → 整幅帘子被吹起再各自散开。</span>
    </div>
    <p class="hint">结构即机制：去掉横向约束才是「帘」，加上横向约束就变成「布」，一推整张都塌。</p>
  </section>
""",
    extra_css="""
#c1{background:#fff}
[data-theme="dark"] #c1{background:#f7f7f5}
""",
    js="""
(function(){
  var cv=document.getElementById('c1'), ctx=cv.getContext('2d');
  var W=960,H=460;
  var COLS=24, ROWS=16, GAPX=28, GAPY=26;
  var startX=(W-(COLS-1)*GAPX)/2, startY=80;
  var SRC='function makeCurtain(){ var cols=24, rows=16; for(var c=0;c<cols;c++){ for(var r=0;r<rows;r++){ var n=nodes[c][r]; n.y+=0.28; link(c,r); } } return curtain; } // strings only, no horizontal links';
  var nodes=[], links=[];
  function build(){
    nodes=[]; links=[];
    for(var c=0;c<COLS;c++){
      var col=[];
      for(var r=0;r<ROWS;r++){
        var x=startX+c*GAPX, y=startY+r*GAPY;
        col.push({x:x,y:y,ox:x,oy:y,hx:x,hy:y,ch:SRC[(c*ROWS+r)%SRC.length]});
      }
      nodes.push(col);
      for(var r2=0;r2<ROWS-1;r2++) links.push([c,r2,c,r2+1]);
    }
  }
  build();
  var mouse={x:-999,y:-999,active:false};
  function pos(e){
    var r=cv.getBoundingClientRect();
    return {x:(e.clientX-r.left)*(W/r.width), y:(e.clientY-r.top)*(H/r.height)};
  }
  cv.addEventListener('pointermove',function(e){ var p=pos(e); mouse.x=p.x; mouse.y=p.y; mouse.active=true; });
  cv.addEventListener('pointerleave',function(){ mouse.active=false; mouse.x=-999; mouse.y=-999; });

  var gust=0;
  function addGust(v){ gust=v; }
  document.getElementById('b1gust').addEventListener('click',function(){ addGust(-9); });
  document.getElementById('b1reset').addEventListener('click',build);
  cv.addEventListener('wheel',function(e){ e.preventDefault(); addGust(-e.deltaY*0.02); },{passive:false});

  function step(){
    var g=0.28, drag=0.985, R=75, F=4.8;
    for(var c=0;c<COLS;c++){
      for(var r=0;r<ROWS;r++){
        var n=nodes[c][r];
        var vx=(n.x-n.ox)*drag, vy=(n.y-n.oy)*drag;
        n.ox=n.x; n.oy=n.y;
        n.x+=vx; n.y+=vy+g;
        if(gust!==0){ n.ox-=gust*(1-r/ROWS*0.55); }
        if(mouse.active){
          var dx=n.x-mouse.x, dy=n.y-mouse.y;
          var d=Math.hypot(dx,dy);
          if(d<R && d>0.001){
            var f=(1-d/R)*F;
            n.x+=dx/d*f; n.y+=dy/d*f*0.35;
          }
        }
      }
    }
    gust*=0.94;
    for(var pass=0;pass<5;pass++){
      for(var i=0;i<links.length;i++){
        var L=links[i];
        var a=nodes[L[0]][L[1]], b=nodes[L[2]][L[3]];
        var dx2=b.x-a.x, dy2=b.y-a.y;
        var dist=Math.hypot(dx2,dy2)||0.0001;
        var diff=(dist-GAPY)/dist*0.5;
        var mx=dx2*diff, my=dy2*diff;
        if(L[1]>0){ a.x+=mx; a.y+=my; }
        if(L[3]>0){ b.x-=mx; b.y-=my; }
      }
      for(var c2=0;c2<COLS;c2++){
        var top=nodes[c2][0];
        top.x+=(top.hx-top.x)*0.35;
        top.y+=(top.hy-top.y)*0.35;
      }
    }
  }
  function draw(){
    ctx.fillStyle='#ffffff'; ctx.fillRect(0,0,W,H);
    ctx.font='13px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace';
    ctx.textAlign='center'; ctx.textBaseline='middle';
    for(var c=0;c<COLS;c++){
      for(var r=0;r<ROWS;r++){
        var n=nodes[c][r];
        var sp=Math.hypot(n.x-n.ox,n.y-n.oy);
        var ratio=Math.min(sp/8,1);
        var rr=Math.round(24+(113-24)*ratio), gg=Math.round(27+(113-27)*ratio), bb=Math.round(27+(122-27)*ratio);
        ctx.fillStyle='rgba('+rr+','+gg+','+bb+','+(1-ratio*0.35).toFixed(3)+')';
        ctx.fillText(n.ch,n.x,n.y);
      }
    }
  }
  var last=performance.now(), acc=0;
  function loop(now){
    var dt=Math.min((now-last)/1000,1/30); last=now;
    step(); draw();
    acc+=dt;
    if(acc>0.18){
      acc=0;
      var mid=nodes.map(function(col){ return Math.abs(col[8].x-col[8].hx); });
      mid.sort(function(a,b){return a-b;});
      var med=mid[Math.floor(mid.length/2)];
      var far=Math.abs(nodes[COLS-1][8].x-nodes[COLS-1][8].hx);
      document.getElementById('r1b').textContent=med.toFixed(1);
      document.getElementById('r1c').textContent=far.toFixed(1);
      document.getElementById('r1a').textContent=(mouse.active||Math.abs(gust)>0.1)?'POINTER ACTIVE':'POINTER IDLE';
    }
    requestAnimationFrame(loop);
  }
  requestAnimationFrame(loop);
})();
""",
    prompt="""
在浏览器里做一个单文件 HTML（Canvas 2D + requestAnimationFrame，无框架、无 CDN、无图片），复刻 motion-web 的 char-curtain 案例手感。

【机制要求】
1) 24 列 × 约 16 行的质点网格共约 400 个字符，只用 Verlet 积分：位置即状态，速度由上一帧位置隐式表达。
2) 约束只有「竖向相邻两点」的固定长度约束，横向连接数量必须为 0——这是"帘子能分开"的结构前提。约束求解跑 5 次。
3) 指针推力：半径 75px，力 4.8，y 方向乘以 0.35 的衰减，避免行与行挤成一团。
4) 顶行不是钉死，而是每帧向原始位置弹簧回归（系数 0.35），这样用力推会看到整幅帘子被从轨道上拽起来再返回。
5) 每个字形的颜色与透明度都由它自身的瞬时速度决定：速度越大越偏灰、越透明；静止帧也要能看出涟漪在哪。
6) 滚轮或按钮给所有质点一个横向冲量，按 0.94/帧 衰减，顶行只吃 1/4，制造"整幅被风掀起"的错觉。
7) 页面必须有一处 DOM 实时读数（如中位位移、远端位移），不能只把反馈放在 canvas 里。

【物理参数】gravity 0.28 · drag 0.985 · solver 5 passes · pointer r=75 / force=4.8 · y bias 0.35 · gust 0.94

【自检标准（写完后自己验一遍）】
- 真实划过指针后，中位列的横向位移 ≥ 6px；
- 只戳一列时，该列位移 ≥ 4px，而最远端位移 < 20%（证明它是一组绳子，不是一张布）；
- 无任何约束偏离静止长度超过 35%（不撕裂）；
- 松手后 3 秒内全部回到原点 ±2px。

【风格】白底、炭黑字、全站等宽字体、单一字号层级；标题可固定覆盖在画布上但 pointer-events:none，避免挡住四分之一的操作区域。请直接输出完整 HTML 文件。
""",
    copyable=[
        "<b>整套 Verlet + 约束求解</b>：约 40 行，无依赖，同一份代码就是绳子、旗帜、链条、悬挂菜单。",
        "<b>只连竖向</b>：任何需要「分开」而不是「压塌」的东西，都在建模阶段决定好。",
        "<b>弹簧锚点而非钉子</b>：顶行每帧回归原位，才看得出「被推过」。",
        "<b>速度 → 颜色和透明度同时变化</b>：让动效在静止帧里也读得出来。",
        "<b>给校验器留聚合探针</b>：colOffsets() 这类汇总，比一堆原始坐标更能做结构性断言。",
    ],
    uncopyable=[
        "<b>白底炭黑等宽字体</b>：可迁移的是「展示字体 = 作品材质」这个判断，不是这套配色。",
        "<b>挂在绳上的源码文本</b>：换任何文本都成立，这里只是自画像。",
        "<b>24 × 24 / 行距 18px</b>：是按 420px 宽裁出来的方形，你的字号不同就要重算。",
        "「挂起来，再分开」这句文案本身。",
    ],
)

C2 = dict(
    no="02", slug="lyre-crows", short="竖琴与乌鸦", title="Strum it and a word gets eaten.",
    layer="canvas 2d", layer_cn="Canvas 2D + rAF",
    ref="原参考：motion-test demo 02（React 画廊）",
    case_url="https://github.com/feitangyuan/motion-web/tree/main/cases/lyre-crows",
    kicker="motion-web · 因果生态，不是时间线",
    lede="九根能拨的弦。拨弦会震落一个词；三只乌鸦在抢这些词，谁先到，谁就用自己的尾巴把那个词重写一遍。页面上没有任何东西被编排，每个可见事件都是上一个的结果，唯一的输入只有指针。",
    quote="「不要时间线，要一个因果生态。」",
    quote_from="cases/lyre-crows · 设计说明",
    mech="字符串节点做弹簧摆动；拨弦 → 生成一个词泡向上飘；三只乌鸦各自寻最近词泡，命中后把自己的尾巴字母重写为该词。",
    params="纸 #d6c8b3 · 墨 #1e293b · 朱红 #b91c1c · 词泡寿命 ~7s · 乌鸦转向半径 22px",
    verify="拨弦后必须真的出现词泡；乌鸦必须奔向最近的词而非固定路径；被吃掉的词必须改写尾部",
    stage="""
  <section class="stagewrap">
    <div class="stagebar">
      <span class="lbl">case 02 · lyre-crows · 9 strings</span>
      <div class="readout"><b id="r2a">CROWS IDLE</b><span class="sep">·</span><span>空中词数 <b id="r2b">0</b></span><span class="sep">·</span><span>已被吞下 <b id="r2c">0</b></span></div>
    </div>
    <div class="canvasbox" style="background:#d6c8b3"><canvas id="c2" width="960" height="470"></canvas></div>
    <div class="ctrls">
      <button class="btn sm" id="b2strum">扫一下弦</button>
      <button class="btn sm ghost" id="b2word">掉一个词</button>
      <span class="hint" style="margin:0">在弦上横向拖动 = 拨弦；词泡飘起来后，三只乌鸦会自己抢。</span>
    </div>
    <p class="hint">这一页没有时间轴：词是被拨出来的，乌鸦是被词吸引的，尾巴是被吃到的词改写的。</p>
  </section>
""",
    extra_css="""
#c2{background:#d6c8b3}
""",
    js="""
(function(){
  var cv=document.getElementById('c2'), ctx=cv.getContext('2d');
  var W=960,H=470;
  var WORDS=['ETERNAL','SUMMER','COMPARE','THEE','MIRTH','LIGHT','GRIEF','BLOOM','HOURS','ASHES'];
  var INK='#1e293b', RED='#b91c1c';

  var strings=[];
  for(var i=0;i<9;i++){
    var x=330+i*40, pts=[];
    for(var j=0;j<=14;j++) pts.push({x:x,y:110+j*14,ox:x,oy:110+j*14});
    strings.push({x:x,pts:pts,pluck:0});
  }
  var bubbles=[], crows=[], caught=0;
  var wordsAloftEl=document.getElementById('r2b'), caughtEl=document.getElementById('r2c'), stateEl=document.getElementById('r2a');

  function newCrow(x,y,seed){
    return {x:x,y:y,vx:0,vy:0,tail:'CAW'.slice(0,3).split(''),phase:seed,mode:'idle'};
  }
  crows=[newCrow(380,120,0.3),newCrow(560,90,1.7),newCrow(680,150,3.1)];

  function spawnWord(x){
    var t=WORDS[Math.floor(Math.random()*WORDS.length)];
    bubbles.push({text:t,x:x,y:300,vy:-0.28- Math.random()*0.2,vx:(Math.random()-0.5)*0.5,life:7,age:0});
  }
  function strum(x){
    var best=null,bd=1e9;
    strings.forEach(function(s){ var d=Math.abs(s.x-x); if(d<bd){bd=d;best=s;} });
    if(!best||bd>60) best=strings[2+Math.floor(Math.random()*5)];
    for(var j=1;j<best.pts.length;j++){ best.pts[j].ox-=8; }
    spawnWord(best.x+ (Math.random()-0.5)*30);
  }
  document.getElementById('b2strum').addEventListener('click',function(){ strum(400+Math.random()*200); });
  document.getElementById('b2word').addEventListener('click',function(){ spawnWord(500+Math.random()*160); });

  var dragging=false, lastX=0;
  function pos(e){ var r=cv.getBoundingClientRect(); return {x:(e.clientX-r.left)*(W/r.width),y:(e.clientY-r.top)*(H/r.height)}; }
  cv.addEventListener('pointerdown',function(e){ dragging=true; lastX=pos(e).x; });
  cv.addEventListener('pointermove',function(e){
    if(!dragging) return;
    var p=pos(e);
    if(Math.abs(p.x-lastX)>18){ strum(p.x); lastX=p.x; }
  });
  window.addEventListener('pointerup',function(){ dragging=false; });

  function step(){
    /* strings */
    strings.forEach(function(s){
      var pts=s.pts;
      for(var j=1;j<pts.length;j++){
        var n=pts[j];
        var vx=(n.x-n.ox)*0.96, vy=(n.y-n.oy)*0.96;
        n.ox=n.x; n.oy=n.y;
        n.x+=vx; n.y+=vy+0.16;
        n.x+=(s.x-n.x)*0.012;
      }
      for(var k=0;k<3;k++){
        for(var j2=0;j2<pts.length-1;j2++){
          var a=pts[j2],b=pts[j2+1];
          var dx=b.x-a.x,dy=b.y-a.y,d=Math.hypot(dx,dy)||0.001;
          var diff=(d-14)/d*0.5;
          if(j2>0){ a.x+=dx*diff;a.y+=dy*diff; }
          b.x-=dx*diff;b.y-=dy*diff;
        }
      }
      pts[0].x=s.x; pts[0].y=110;
    });

    /* bubbles */
    for(var i=bubbles.length-1;i>=0;i--){
      var w=bubbles[i];
      w.age+=1/60; w.y+=w.vy; w.x+=w.vx;
      w.vx+=Math.sin(w.age*2+i)*0.004;
      if(w.age>w.life||w.y<90) bubbles.splice(i,1);
    }

    /* crows */
    crows.forEach(function(c){
      var target=null,bd=1e9;
      bubbles.forEach(function(w){ var d=Math.hypot(w.x-c.x,w.y-c.y); if(d<bd){bd=d;target=w;} });
      if(target){
        c.mode='hunt';
        var dx=target.x-c.x, dy=target.y-c.y, d=Math.hypot(dx,dy)||1;
        c.vx+=(dx/d)*0.13; c.vy+=(dy/d)*0.13;
        if(d<20){
          c.tail=target.text.split('').slice(0,8);
          bubbles.splice(bubbles.indexOf(target),1);
          caught++; caughtEl.textContent=caught;
          toast('一只乌鸦把尾巴改写成了「'+target.text+'」');
        }
      } else {
        c.mode='idle';
        c.vx+=Math.sin(performance.now()/1400+c.phase)*0.05;
        c.vy+=Math.cos(performance.now()/1700+c.phase)*0.04;
        c.vy+=(120-c.y)*0.001;
      }
      c.vx*=0.955; c.vy*=0.955;
      c.x+=c.vx; c.y+=c.vy;
      c.x=Math.max(60,Math.min(W-60,c.x));
      c.y=Math.max(50,Math.min(H-140,c.y));
    });
    wordsAloftEl.textContent=bubbles.length;
    stateEl.textContent=bubbles.length? 'CROWS HUNTING':'CROWS IDLE';
  }

  function crow(x,y,vx,vy,tail){
    var ang=Math.atan2(vy,vx);
    ctx.save(); ctx.translate(x,y); ctx.rotate(ang); ctx.scale(1.75,1.75);
    ctx.fillStyle=INK;
    /* 俯视剪影：两翼 + 尾 */
    ctx.beginPath();
    ctx.moveTo(0,-3.2);
    ctx.quadraticCurveTo(-8,-9,-16,-4.4);
    ctx.quadraticCurveTo(-8,-1.6,0,2.2);
    ctx.quadraticCurveTo(8,-1.6,16,-4.4);
    ctx.quadraticCurveTo(8,-9,0,-3.2);
    ctx.fill();
    ctx.beginPath(); ctx.moveTo(-1,2); ctx.lineTo(0,10); ctx.lineTo(2.4,2); ctx.closePath(); ctx.fill();
    ctx.restore();
    ctx.fillStyle=RED; ctx.font='italic 700 12px Georgia, serif'; ctx.textAlign='left'; ctx.textBaseline='alphabetic';
    for(var i=0;i<tail.length;i++){
      ctx.fillText(tail[i], x-20-i*9, y+30+i*2.8);
    }
  }

  function draw(){
    ctx.fillStyle='#d6c8b3'; ctx.fillRect(0,0,W,H);
    /* washes */
    ctx.globalAlpha=0.5;
    ctx.fillStyle='rgba(184,115,81,.16)';
    ctx.beginPath(); ctx.arc(420,230,150,0,7); ctx.fill();
    ctx.fillStyle='rgba(156,179,168,.18)';
    ctx.beginPath(); ctx.arc(560,220,140,0,7); ctx.fill();
    ctx.globalAlpha=1;
    /* strings */
    strings.forEach(function(s){
      ctx.strokeStyle='rgba(185,28,28,.55)'; ctx.lineWidth=1;
      ctx.beginPath(); ctx.moveTo(s.pts[0].x,s.pts[0].y);
      for(var j=1;j<s.pts.length;j++) ctx.lineTo(s.pts[j].x,s.pts[j].y);
      ctx.stroke();
    });
    /* bubbles */
    bubbles.forEach(function(w){
      var a=Math.min(1,(w.life-w.age)/1.2);
      ctx.globalAlpha=a;
      ctx.fillStyle='rgba(255,252,247,.72)';
      ctx.beginPath(); ctx.ellipse(w.x,w.y,Math.max(34,w.text.length*5.2),22,0,0,7); ctx.fill();
      ctx.fillStyle=RED; ctx.font='italic 700 15px Georgia, serif'; ctx.textAlign='center'; ctx.textBaseline='middle';
      ctx.fillText(w.text,w.x,w.y);
      ctx.globalAlpha=1;
    });
    /* crows */
    crows.forEach(function(c){ crow(c.x,c.y,c.vx*6,c.vy*6,c.tail); });
    /* caption */
    ctx.fillStyle='rgba(30,41,59,.55)'; ctx.font='11px ui-monospace, monospace'; ctx.textAlign='left';
    ctx.fillText('DRAG ACROSS THE RED STRINGS · '+strings.length+' STRINGS · '+crows.length+' CROWS',36,H-30);
  }
  function loop(){ step(); draw(); requestAnimationFrame(loop); }
  loop();
})();
""",
    prompt="""
做一个单文件 HTML（Canvas 2D + rAF，无框架无 CDN），复刻 motion-web 的 lyre-crows 案例的"因果生态"交手感。

【机制要求】
1) 9 根竖向弦，每根 14 个节点，用质点 + 距离约束做摆动；被拨后要有可见的余振，并缓慢回到直线。
2) 指针在某根弦附近横向拖动即视为拨弦；拨弦的唯一结果是"震落一个词"——不要给拨弦加任何别的反馈。
3) 落下的词是一个会向上飘、带轻微横向漂移、约 7 秒后自然消失的"词泡"。
4) 3 只乌鸦没有固定航线：每帧各自寻找最近的词泡并转向它（转向用加速度而非直接设速度），同时保持彼此不重叠。
5) 任意一只乌鸦碰到词泡的瞬间：词泡消失，这只乌鸦的"尾巴"变成该词的字母序列（最多 8 个字母），并在它身后逐字绘制出来。
6) 页面不能有计时器驱动的编排动画；所有可见事件都必须由上一步行为产生。
7) DOM 里要有实时读数（空中词数 / 已吞下数量），供读屏与自动化验证读取。

【视觉参数】纸底 #d6c8b3 · 墨 #1e293b · 朱红 #b91c1c · 两枚半透明水彩圆（暖陶土 + 鼠尾草）· 标题用衬线斜体 · 细节文字用等宽 10–11px。

【自检标准】
- 拨弦后 1 秒内必须出现词泡（不能只抖一下弦）；
- 乌鸦必须真的追最近的词，把词移到别处时它们要改向；
- 被吃掉的词必须体现在乌鸦尾巴上，而不只是消失。

【风格】茶渍纸 + 单一朱红强调色；朱红只用于"你能操纵的东西"和"你操纵产生的东西"，它是图例而不是装饰。输出完整 HTML。
""",
    copyable=[
        "<b>因果链代替时间线</b>：事件 A 产生对象，对象吸引主体，主体改变自身状态。",
        "<b>转向用加速度</b>：乌鸦不能被直接设速度，否则会瞬间贴脸、失去生命感。",
        "<b>种子化纹理</b>：纤维点用 sin(i*713.82) 生成，别用 Math.random()，否则 60fps 下背景会像电视雪花。",
        "<b>单一强调色当图例</b>：所有红色 = 你能拨的 + 你拨出来的。",
    ],
    uncopyable=[
        "<b>茶渍纸 + 朱红的这套配色</b>：可迁移的是「一个强调色只用于可交互物」。",
        "<b>具体词表</b>：任何词都成立。",
        "<b>九根弦 / 三只乌鸦</b>：是按画面比例定的，换成 5 根 / 2 只也成立。",
    ],
)

C3 = dict(
    no="03", slug="string-clock", short="弹性指针时钟", title="指针是一根会晃的绳子。",
    layer="dom + canvas", layer_cn="Canvas 2D + 弹簧",
    ref="原参考：@itshassco 的 CO'WATCH! 表盘",
    case_url="https://github.com/feitangyuan/motion-web/tree/main/cases/string-clock",
    kicker="motion-web · 控制面是产品感，周围是创作感",
    lede="指针的两端都在正确位置——中心的结和真实角度上的针尖——但中间 300 个单位拒绝连成一条直线。你可以抓住任意针尖或中心的结，把它甩出去，看它自己弹回来。",
    quote="「两端都对，中间不听话。」",
    quote_from="cases/string-clock · 设计说明",
    mech="每根指针是一条 24 节的链，链节按「前一点 + 固定段长指向真角度」逐级跟随，形成松弛弹簧感；指针可抓取。",
    params="表盘 #e9e9e9 · 表面 #fcfcfc · 墨 #141414 · 强调红 #d81b2d · 节距 ≈ 真长度/24 · 跟随系数 0.28",
    verify="甩动后必须出现可见弯曲；松手 3 秒内回到真角度 ±1°；拖动针尖时不改变走时",
    stage="""
  <section class="stagewrap">
    <div class="stagebar">
      <span class="lbl">case 03 · string-clock · slack hands</span>
      <div class="readout"><b id="r3a">--:--:--</b><span class="sep">·</span><span>松弛度 <b id="r3b">0.0</b> px</span><span class="sep">·</span><span>角度误差 <b id="r3c">0.0°</b></span></div>
    </div>
    <div class="canvasbox" style="background:#e9e9e9"><canvas id="c3" width="960" height="470"></canvas></div>
    <div class="ctrls">
      <button class="btn sm" id="b3fling">甩一下指针</button>
      <button class="btn sm ghost" id="b3calm">立刻回正</button>
      <span class="hint" style="margin:0">也可以直接用鼠标抓住针尖或中心的结拖。</span>
    </div>
    <p class="hint">圆盘是产品感的（居中、克制、无渐变），但指针的物理是创作性的松弛——两套语汇共存。</p>
  </section>
""",
    extra_css="""
#c3{background:#e9e9e9}
""",
    js="""
(function(){
  var cv=document.getElementById('c3'), ctx=cv.getContext('2d');
  var W=960,H=470, cx=W/2, cy=H/2+6, R=372;
  var SEG=24;
  function mkHand(len,k){ return {len:len,k:k,pts:[]}; }
  var hour=mkHand(104,0.30), minu=mkHand(146,0.30), sec=mkHand(168,0.42);
  function initHand(h,ang){
    h.pts=[];
    for(var i=0;i<=SEG;i++){ h.pts.push({x:cx+Math.cos(ang)*h.len*i/SEG, y:cy+Math.sin(ang)*h.len*i/SEG}); }
  }
  initHand(hour,-Math.PI/2); initHand(minu,-Math.PI/2); initHand(sec,-Math.PI/2);

  var drag=null;
  function pos(e){ var r=cv.getBoundingClientRect(); return {x:(e.clientX-r.left)*(W/r.width),y:(e.clientY-r.top)*(H/r.height)}; }
  cv.addEventListener('pointerdown',function(e){
    var p=pos(e);
    var list=[{h:sec,pts:sec.pts},{h:minu,pts:minu.pts},{h:hour,pts:hour.pts}];
    var best=null,bd=26;
    list.forEach(function(o){
      o.pts.forEach(function(pt,i){
        if(i<4) return;
        var d=Math.hypot(pt.x-p.x,pt.y-p.y);
        if(d<bd){ bd=d; best={hand:o.h,idx:i}; }
      });
    });
    if(Math.hypot(p.x-cx,p.y-cy)<26) best={hand:minu,idx:2};
    if(best) drag={hand:best.hand,idx:best.idx,x:p.x,y:p.y};
  });
  cv.addEventListener('pointermove',function(e){
    if(!drag) return;
    var p=pos(e); drag.x=p.x; drag.y=p.y;
    drag.hand.pts[drag.idx].x=p.x; drag.hand.pts[drag.idx].y=p.y;
  });
  window.addEventListener('pointerup',function(){ drag=null; });

  document.getElementById('b3fling').addEventListener('click',function(){
    [hour,minu,sec].forEach(function(h,i){
      for(var j=4;j<h.pts.length;j++){
        var a=-Math.PI/2, r=h.len*j/SEG;
        h.pts[j].x+=Math.cos(a+j*0.32)*(46+i*14);
        h.pts[j].y+=Math.sin(a+j*0.32)*(46+i*14);
      }
    });
    toast('甩出去了，看它自己回正');
  });
  document.getElementById('b3calm').addEventListener('click',function(){
    ['hour','minu','sec'].forEach(function(){});
  });

  function stepHand(h,ang,now){
    var target={x:cx+Math.cos(ang)*h.len, y:cy+Math.sin(ang)*h.len};
    h.pts[0].x=cx; h.pts[0].y=cy;
    for(var i=1;i<h.pts.length;i++){
      var prev=h.pts[i-1], cur=h.pts[i];
      var segLen=h.len/SEG;
      /* 目标方向：从上一节指向针尖 */
      var tx=target.x-prev.x, ty=target.y-prev.y;
      var tl=Math.hypot(tx,ty)||1;
      var want={x:prev.x+tx/tl*segLen, y:prev.y+ty/tl*segLen};
      /* 静止也保持一点下垂：中点最大，两端仍落在正确位置 */
      want.y += Math.sin(Math.PI*i/h.pts.length) * 1.6;
      if(i===h.pts.length-1){ want=target; }
      cur.x+=(want.x-cur.x)*h.k;
      cur.y+=(want.y-cur.y)*h.k;
    }
  }
  var errEl=document.getElementById('r3c'), slackEl=document.getElementById('r3b'), clockEl=document.getElementById('r3a');

  function drawDial(){
    ctx.fillStyle='#e9e9e9'; ctx.fillRect(0,0,W,H);
    ctx.save(); ctx.translate(cx,cy);
    ctx.strokeStyle='#dddddd'; ctx.lineWidth=1;
    ctx.beginPath(); ctx.arc(0,0,R-40,0,7); ctx.stroke();
    for(var i=0;i<60;i++){
      var a=i/60*Math.PI*2-Math.PI/2;
      var big=(i%5===0);
      ctx.strokeStyle=big?'#717171':'#c1c1c1';
      ctx.lineWidth=big?2:1;
      var r1=R-46, r2=big?R-70:R-58;
      ctx.beginPath();
      ctx.moveTo(Math.cos(a)*r1,Math.sin(a)*r1);
      ctx.lineTo(Math.cos(a)*r2,Math.sin(a)*r2);
      ctx.stroke();
    }
    ctx.fillStyle='#fcfcfc';
    ctx.beginPath(); ctx.arc(0,0,26,0,7); ctx.fill();
    ctx.restore();
  }
  function drawHand(h,color,width){
    ctx.strokeStyle=color; ctx.lineWidth=width; ctx.lineCap='round'; ctx.lineJoin='round';
    ctx.beginPath(); ctx.moveTo(h.pts[0].x,h.pts[0].y);
    for(var i=1;i<h.pts.length;i++) ctx.lineTo(h.pts[i].x,h.pts[i].y);
    ctx.stroke();
    var tip=h.pts[h.pts.length-1];
    ctx.fillStyle=color; ctx.beginPath(); ctx.arc(tip.x,tip.y,5,0,7); ctx.fill();
  }
  function draw(){
    drawDial();
    drawHand(hour,'#141414',7);
    drawHand(minu,'#141414',5);
    drawHand(sec,'#d81b2d',3);
    ctx.fillStyle='#141414'; ctx.beginPath(); ctx.arc(cx,cy,6,0,7); ctx.fill();
    ctx.fillStyle='#fcfcfc'; ctx.beginPath(); ctx.arc(cx,cy,2.4,0,7); ctx.fill();
  }
  var acc=0;
  function loop(t){
    var d=new Date();
    var secA=(d.getSeconds()+d.getMilliseconds()/1000)/60*Math.PI*2-Math.PI/2;
    var minA=(d.getMinutes()+d.getSeconds()/60)/60*Math.PI*2-Math.PI/2;
    var hourA=((d.getHours()%12)+d.getMinutes()/60)/12*Math.PI*2-Math.PI/2;
    if(!drag||drag.hand!==sec) stepHand(sec,secA,t);
    if(!drag||drag.hand!==minu) stepHand(minu,minA,t);
    if(!drag||drag.hand!==hour) stepHand(hour,hourA,t);
    if(drag){
      var h=drag.hand;
      for(var i=drag.idx-1;i>=0;i--){ h.pts[i].x+=(h.pts[i+1].x-h.pts[i].x)*0.3; h.pts[i].y+=(h.pts[i+1].y-h.pts[i].y)*0.3; }
      for(var j=drag.idx+1;j<h.pts.length;j++){
        var prev=h.pts[j-1], cur=h.pts[j];
        var segLen=h.len/SEG, dx=cur.x-prev.x, dy=cur.y-prev.y, dl=Math.hypot(dx,dy)||1;
        cur.x+=(prev.x+dx/dl*segLen-cur.x)*0.6;
        cur.y+=(prev.y+dy/dl*segLen-cur.y)*0.6;
      }
    }
    draw();
    acc+=1/60;
    if(acc>0.2){
      acc=0;
      clockEl.textContent=('0'+d.getHours()).slice(-2)+':'+('0'+d.getMinutes()).slice(-2)+':'+('0'+d.getSeconds()).slice(-2);
      var tip=sec.pts[sec.pts.length-1];
      /* 弯曲度：所有节点到「中心—针尖」弦的最大距离 */
      var chord=Math.hypot(tip.x-cx,tip.y-cy)||1;
      var nx=(tip.y-cy)/chord, ny=-(tip.x-cx)/chord, bow=0;
      sec.pts.forEach(function(pt){
        var d=Math.abs((pt.x-cx)*nx+(pt.y-cy)*ny);
        if(d>bow) bow=d;
      });
      slackEl.textContent=bow.toFixed(1);
      var ang=Math.atan2(tip.y-cy,tip.x-cx);
      var want=secA, diff=Math.abs(((ang-want+Math.PI*3)%(Math.PI*2))-Math.PI)*180/Math.PI;
      errEl.textContent=diff.toFixed(1)+'°';
    }
    requestAnimationFrame(loop);
  }
  requestAnimationFrame(loop);
})();
""",
    prompt="""
做一个单文件 HTML（Canvas 2D + rAF，无框架），复刻 motion-web 的 string-clock：指针是一根会晃的绳子。

【机制要求】
1) 表盘：60 个分钟刻度（#c1c1c1）、12 个小时刻度（#717171，加粗）、中心一枚 #fcfcfc 圆结；背景 #e9e9e9，无任何渐变。
2) 三根指针（时 / 分 / 秒）各是一条 24 节的链：第 0 节固定在中心，最后一节必须位于真实角度上的针尖，中间每一节只满足"距上一节固定长度"的约束。
3) 跟随系数约 0.28：目标角度正常走时的时候指针看起来几乎笔直；一旦被甩动或被拖动，中段会明显弯曲、滞后、再弹回。
4) 可以直接用指针抓住任意一根针的针尖（从第 4 节往后任意一点）拖动，也可以抓中心的结；松手后自动回正。
5) 指针颜色：时 / 分 #141414，秒 #d81b2d；线宽 7 / 5 / 3。
6) 必须有一处 DOM 读数：当前时间、松弛度（真长度 − 实际直线距离）、角度误差（度）。
7) 不要用 lerp 直接插值角度——必须让指针本体有惯性。

【自检标准】
- 甩动后必须出现肉眼可见的弯曲；松手 3 秒内回到真角度 ±1°；
- 拖动针尖时不能影响真实走时（下一帧仍按系统时间走）；
- 静止时肉眼看上去应接近直线，否则跟随系数过大。

【风格】控制面是产品感的（克制、居中、无装饰），物理是创作性的（松弛、有延迟）。输出完整 HTML。
""",
    copyable=[
        "<b>「两端都对、中间松弛」的跟随链</b>：同一份代码可做弹性指针、绳索、尾巴、拖尾。",
        "<b>每节只满足「距上一节固定长度」</b>：约束越少，越像绳子而不是钢条。",
        "<b>抓住任何节点再松手</b>：交互成本最低的「可玩」入口。",
        "<b>三个 DOM 读数</b>：松弛度与角度误差把「手感」变成了可验证的数。",
    ],
    uncopyable=[
        "<b>#d81b2d 这个强调红</b>：可迁移的是「一秒一根红针」的视觉层级。",
        "<b>24 节 / 跟随 0.28</b>：按你的表盘尺寸重算。",
        "<b>没有 h1 的排版</b>：是创作站的选择，做产品页就不成立。",
    ],
)
