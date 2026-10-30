# -*- coding: utf-8 -*-
"""页面 03、04：大厂质感 5 招 / AI 界面 5 个隐藏细节"""

P03 = dict(
    no="03", short="大厂质感 5 招", title="扒了大厂源码，高级感全在这 5 招",
    bvid="BV19gn96oEGt", dur="02:57", date="2026-10-26",
    kicker="Bilibili · KD一对A · 视觉质感 · Vibe coding",
    lede="用 AI 堆出来的界面为什么总有一股塑料味？把这 5 个细节摆在一起对比，你会发现问题不在配色，而在「分层、字重、打字、数字、动效」这五件小事上。",
    tag1="微对比分层", tag2="流式打字 / 弹簧动效",
    quote="「不画边框，靠 <b>1%~3% 的亮度差</b>分层；暗色模式把字重悄悄降一档；拖拽要过阻尼，点赞要欠阻尼。」",
    demos="""
  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 01</span>
      <div><h2>分层：画边框，还是用 1% 的亮度差</h2>
      <p>同一套卡片叠三层。左边层层描边，右边只用极小的明度差——切换深色看差距更明显。</p></div>
    </div>
    <div class="split">
      <div class="pane bad">
        <div class="pane-h"><span class="tag no">✕ 每层都描边</span><span class="count">1px 边框 ×3</span></div>
        <div class="stage plain">
          <div class="lay lay-border">
            <div class="lay l1">面板
              <div class="lay l2">分组
                <div class="lay l3">卡片内容</div>
              </div>
            </div>
          </div>
        </div>
        <p class="note">框中框、线压线，越往里越脏，边界反而更难读。</p>
      </div>
      <div class="pane good">
        <div class="pane-h"><span class="tag ok">✓ 只靠明度差</span><span class="count">#fcfcfb → #f5f5f3</span></div>
        <div class="stage plain">
          <div class="lay lay-tone">
            <div class="lay l1">面板
              <div class="lay l2">分组
                <div class="lay l3">卡片内容</div>
              </div>
            </div>
          </div>
        </div>
        <p class="note">不描边，靠 1%~3% 的亮度阶梯，层次自然浮起来。</p>
      </div>
    </div>
  </section>

  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 02</span>
      <div><h2>流式打字：逐字弹出，还是像墨一样晕开</h2>
      <p>点重播，两只字同时开跑。右边每个字从 blur(6px) 到清晰 90ms，相邻字错开 30ms。</p></div>
    </div>
    <div class="split">
      <div class="pane bad">
        <div class="pane-h"><span class="tag no">✕ 硬弹出</span><span class="count">0ms / 0ms</span></div>
        <div class="stage" style="min-height:120px;align-items:flex-start">
          <div class="typing" id="typeA"></div>
        </div>
        <p class="note">像打印机吐字，每个字「啪」地出现，节奏很硬。</p>
      </div>
      <div class="pane good">
        <div class="pane-h"><span class="tag ok">✓ 墨晕式</span><span class="count">90ms / 错开 30ms</span></div>
        <div class="stage" style="min-height:120px;align-items:flex-start">
          <div class="typing" id="typeB"></div>
        </div>
        <p class="note">字与字之间有模糊到清晰的过渡，阅读时更像人在写。</p>
      </div>
    </div>
    <div class="row" style="margin-top:12px"><button class="btn sm primary" id="replayType">重播两端</button></div>
  </section>

  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 03</span>
      <div><h2>数字抖动：等宽数字到底救的是什么</h2>
      <p>下面两组订单金额每秒刷新。左边比例数字，每换一次，整列都在左右蹭。</p></div>
    </div>
    <div class="split">
      <div class="pane bad">
        <div class="pane-h"><span class="tag no">✕ 比例数字</span><span class="count">font-variant: normal</span></div>
        <div class="stage">
          <div class="numtable" id="numA">
            <div class="ntrow"><span>订单 A</span><b class="num">1,280.00</b></div>
            <div class="ntrow"><span>订单 B</span><b class="num">9.90</b></div>
            <div class="ntrow"><span>订单 C</span><b class="num">111,111.11</b></div>
            <div class="ntrow"><span>合计</span><b class="num">112,401.01</b></div>
          </div>
        </div>
        <p class="note">「1」比「8」窄，长度一变整列右边缘就跳，读数很累。</p>
      </div>
      <div class="pane good">
        <div class="pane-h"><span class="tag ok">✓ tabular-nums</span><span class="count">等宽锁死</span></div>
        <div class="stage">
          <div class="numtable tab" id="numB">
            <div class="ntrow"><span>订单 A</span><b class="num">1,280.00</b></div>
            <div class="ntrow"><span>订单 B</span><b class="num">9.90</b></div>
            <div class="ntrow"><span>订单 C</span><b class="num">111,111.11</b></div>
            <div class="ntrow"><span>合计</span><b class="num">112,401.01</b></div>
          </div>
        </div>
        <p class="note">每个数字占同样宽度，刷新时小数点不动，眼睛不用重新对位。</p>
      </div>
    </div>
  </section>

  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 04</span>
      <div><h2>动效有性格：过阻尼 vs 欠阻尼</h2>
      <p>同样的位移，左边瞬间吸附、零回弹；右边带一点 Q 弹。点按钮看差别。</p></div>
    </div>
    <div class="split">
      <div class="pane">
        <div class="pane-h"><span class="tag v">过阻尼 · 1200 / 80</span><span class="count">拖拽吸附感</span></div>
        <div class="stage">
          <div class="rail"><span class="pilldot" id="sp1"></span></div>
          <button class="btn sm" data-spring="1">发送一下</button>
        </div>
        <p class="note">没有回弹，像被磁场吸住——适合拖拽、吸附、面板停靠。</p>
      </div>
      <div class="pane">
        <div class="pane-h"><span class="tag t">欠阻尼 · 380 / 18</span><span class="count">点赞回弹</span></div>
        <div class="stage">
          <div class="rail"><span class="pilldot bounce" id="sp2"></span></div>
          <button class="btn sm" data-spring="2">点赞一下</button>
        </div>
        <p class="note">轻微过冲再回到位，有生命感——适合点赞、勾选、成功反馈。</p>
      </div>
    </div>
  </section>
""",
    extra_css="""
.lay{border-radius:16px;padding:14px;font-size:12px;color:var(--ink-2);transition:background .3s var(--ease)}
.lay-border{background:#fffaf7;box-shadow:inset 0 0 0 1px #e3ddd6}
.lay-border .l1{background:#fffaf7;box-shadow:inset 0 0 0 1px #e3ddd6;margin-top:8px}
.lay-border .l2{background:#fffaf7;box-shadow:inset 0 0 0 1px #e3ddd6;margin-top:8px}
.lay-border .l3{background:#fffaf7;box-shadow:inset 0 0 0 1px #e3ddd6;margin-top:8px;padding:11px 12px;border-radius:9px}
[data-theme="dark"] .lay-border{background:#191917;box-shadow:inset 0 0 0 1px #2c2c29}
[data-theme="dark"] .lay-border .l1,[data-theme="dark"] .lay-border .l2,[data-theme="dark"] .lay-border .l3{background:#191917;box-shadow:inset 0 0 0 1px #2c2c29}
.lay-tone{background:#fcfcfb}
.lay-tone .l1{background:#f5f5f3;margin-top:8px}
.lay-tone .l2{background:#efefec;margin-top:8px}
.lay-tone .l3{background:#e9e9e5;margin-top:8px;padding:11px 12px;border-radius:9px}
[data-theme="dark"] .lay-tone{background:#0f0f0e}
[data-theme="dark"] .lay-tone .l1{background:#151515}
[data-theme="dark"] .lay-tone .l2{background:#1a1a19}
[data-theme="dark"] .lay-tone .l3{background:#20201e}
.typing{font-size:13px;line-height:1.85;color:var(--ink);min-height:76px}
.typing .ink{display:inline-block;animation:inkIn .09s var(--ease) both}
@keyframes inkIn{from{opacity:0;filter:blur(6px);transform:translateY(2px)}to{opacity:1;filter:blur(0);transform:none}}
.numtable{width:100%;display:grid;gap:9px;font-size:12.5px}
.ntrow{display:flex;align-items:center;justify-content:space-between;gap:10px;
  background:var(--card);border-radius:9px;padding:8px 11px;box-shadow:inset 0 0 0 1px var(--line)}
.ntrow span{color:var(--ink-3)}
.ntrow b{font-weight:600;font-variant-numeric:normal}
.numtable.tab .ntrow b{font-variant-numeric:tabular-nums}
.rail{height:44px;border-radius:12px;background:var(--card);box-shadow:inset 0 0 0 1px var(--line);
  display:flex;align-items:center;padding:0 6px;overflow:hidden}
.pilldot{width:32px;height:32px;border-radius:10px;background:var(--teal);display:block;
  transform:translateX(0);transition:transform .55s cubic-bezier(.16,.9,.25,1)}
.pilldot.bounce{background:var(--violet);transition:transform .62s cubic-bezier(.34,1.7,.5,1)}
""",
    js="""
(function(){
  /* 流式打字 */
  var TEXT='不画边框，靠 1% 的亮度差分出层次，字与字之间用 30ms 的错开把句子晕开。';
  function run(){
    var A=document.getElementById('typeA'), B=document.getElementById('typeB');
    A.innerHTML=''; B.innerHTML='';
    var i=0;
    clearInterval(run._t);
    run._t=setInterval(function(){
      if(i>=TEXT.length){ clearInterval(run._t); return; }
      var ch=TEXT[i];
      var s1=document.createElement('span'); s1.textContent=ch; A.appendChild(s1);
      var s2=document.createElement('span'); s2.className='ink'; s2.textContent=ch;
      s2.style.animationDelay=(i*30)+'ms'; B.appendChild(s2);
      i++;
    },52);
  }
  document.getElementById('replayType').addEventListener('click',run); run();

  /* 等宽数字抖动 */
  var numsA=document.querySelectorAll('#numA .num'), numsB=document.querySelectorAll('#numB .num');
  function rnd(){ var v=Math.random()*100000/Math.pow(10,Math.floor(Math.random()*3));
    return v.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2}); }
  setInterval(function(){
    numsA.forEach(function(n){ n.textContent=rnd(); });
    numsB.forEach(function(n){ n.textContent=rnd(); });
  },900);

  /* 弹簧动效 */
  document.querySelectorAll('[data-spring]').forEach(function(b){
    b.addEventListener('click',function(){
      var el=document.getElementById('sp'+b.dataset.spring);
      var far=el.style.transform==='translateX(178px)';
      el.style.transform=far?'translateX(0)':'translateX(178px)';
    });
  });
})();
""",
    notes=[
        "<b>不画边框</b>：靠 1%~3% 的亮度先后分层，且不要用纯黑 #000；浅色 #f5f5f3 / #fcfcfb，深色 #0b0b0a / #151515 / #1a1a19 / #20201e。",
        "<b>暗色补偿</b>：深色底上把字重降一档（400 → 380 左右），白字才不会显胖。",
        "<b>流式打字</b>：每字 blur(6px)→清晰 90ms，cubic-bezier(.215,.61,.355,1)，相邻字错开 30ms。",
        "<b>数字要锁宽</b>：tabular-nums，避免刷新时整列左右跳。",
        "<b>折叠用 Grid</b>：0fr→1fr 过渡，别用 JS 算高度。",
        "<b>动效分性格</b>：拖拽过阻尼 1200/80 零回弹，点赞欠阻尼 380/18 有回弹。",
        "<b>细节补丁</b>：行内图标 vertical-align:-0.125em 对齐；正文加 text-wrap:pretty 防孤字；复制成功的勾 2.5 秒自动淡出。",
    ],
)

P04 = dict(
    no="04", short="AI 界面 5 细节", title="大厂 AI 界面的 5 个隐藏细节｜下篇",
    bvid="BV1jUnd66Em2", dur="02:50", date="2026-10-26",
    kicker="Bilibili · KD一对A · AI 界面细节 · 第七期",
    lede="这些细节平时没人说，但缺了就会让人骂「这软件好难用」：中文没上屏就误发送、看历史被拽回底部、圆角看着别扭、文件夹名被截成半截、分屏拖过头。逐个点开对比一下。",
    tag1="输入法 / 滚动", tag2="圆角 / 截断 / 分屏",
    quote="「AI 产品的打磨不在模型，在这些『你根本没注意，但一用就别扭』的地方。」",
    demos="""
  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 01</span>
      <div><h2>中文还在选字，Enter 就发出去了？</h2>
      <p>点「开始拼音输入」，然后在两个输入框里各按一次 Enter。</p></div>
    </div>
    <div class="split">
      <div class="pane bad">
        <div class="pane-h"><span class="tag no">✕ 候选态直接发送</span><span class="count" id="imeStateA">未输入</span></div>
        <div class="stage">
          <input class="field" id="imeA" placeholder="在这里按 Enter 试试">
          <div class="cand" id="candA" hidden>候选：<span>你好</span><span>拟好</span><span>你</span></div>
        </div>
        <p class="note" id="imeNoteA">把 Enter 一律当发送，选字时误触直接把半句话丢出去。</p>
      </div>
      <div class="pane good">
        <div class="pane-h"><span class="tag ok">✓ 先上屏，不发送</span><span class="count" id="imeStateB">未输入</span></div>
        <div class="stage">
          <input class="field" id="imeB" placeholder="在这里按 Enter 试试">
          <div class="cand" id="candB" hidden>候选：<span>你好</span><span>拟好</span><span>你</span></div>
        </div>
        <p class="note" id="imeNoteB">候选态下 Enter 只负责「选字上屏」，绝不当成发送。</p>
      </div>
    </div>
    <div class="row" style="margin-top:12px">
      <button class="btn sm" id="imeStart">开始拼音输入</button>
      <button class="btn sm ghost" id="imeEnd">结束输入</button>
      <span class="count">真实中文输入法同样会触发 composition 状态</span>
    </div>
  </section>

  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 02</span>
      <div><h2>看历史时，别把用户拽回底部</h2>
      <p>点「持续输出」，然后把右边的列表往上滚——左边会一直把你拉回去。</p></div>
    </div>
    <div class="split">
      <div class="pane bad">
        <div class="pane-h"><span class="tag no">✕ 永远跟着最新</span><span class="count">scrollTop 被强制</span></div>
        <div class="stage" style="padding:0;overflow:hidden">
          <div class="chat" id="chatA"></div>
        </div>
        <p class="note">用户想翻两句之前的回答，每次新 token 落地就把他拽回来。</p>
      </div>
      <div class="pane good">
        <div class="pane-h"><span class="tag ok">✓ 上滚即停跟</span><span class="count" id="followB">跟随中</span></div>
        <div class="stage" style="padding:0;overflow:hidden">
          <div class="chat" id="chatB"></div>
          <button class="jump" id="jumpB" hidden>↓ 回到最新</button>
        </div>
        <p class="note">一旦检测到用户在向上滚，就停止跟随，并给一个「回到最新」的按钮。</p>
      </div>
    </div>
    <div class="row" style="margin-top:12px">
      <button class="btn sm primary" id="streamBtn">持续输出</button>
      <button class="btn sm ghost" id="streamStop">暂停</button>
    </div>
  </section>

  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 03</span>
      <div><h2>同心圆角：外圈 = 内圈 + 间距</h2>
      <p>拖滑块改内层内边距，看右边那个「外内同值」的角什么时候开始出戏。</p></div>
    </div>
    <div class="split">
      <div class="pane good">
        <div class="pane-h"><span class="tag ok">✓ 同心</span><span class="count" id="radA">外 20 / 内 12</span></div>
        <div class="stage">
          <div class="radbox" id="radOuterA"><div class="radinner" id="radInnerA"></div></div>
        </div>
        <p class="note">外圈半径跟着间距走，两个弧线看起来是同一个圆心。</p>
      </div>
      <div class="pane bad">
        <div class="pane-h"><span class="tag no">✕ 外内同值</span><span class="count" id="radB">外 20 / 内 20</span></div>
        <div class="stage">
          <div class="radbox" id="radOuterB"><div class="radinner" id="radInnerB"></div></div>
        </div>
        <p class="note">角看起来「胖了一块」，说不上哪里错，就是别扭。</p>
      </div>
    </div>
    <div class="row" style="margin-top:12px;gap:14px">
      <span class="count">间距</span>
      <input type="range" id="radRange" min="2" max="16" value="8" style="max-width:260px">
    </div>
  </section>

  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 04</span>
      <div><h2>长文件名截断，也要留住扩展名</h2>
      <p>同样宽度下，左边把 .docx 一起省略了，右边保住后缀。</p></div>
    </div>
    <div class="split">
      <div class="pane bad">
        <div class="pane-h"><span class="tag no">✕ 直接 ellipsis</span><span class="count">text-overflow</span></div>
        <div class="stage">
          <div class="filerow"><span class="fico">▤</span><span class="fname cut">2026年第三季度市场分析与增长策略复盘报告_v3_终稿_真的终稿.docx</span></div>
        </div>
        <p class="note">用户看不出这是 Word 还是 PDF，也就不知道该用什么打开。</p>
      </div>
      <div class="pane good">
        <div class="pane-h"><span class="tag ok">✓ 保留扩展名</span><span class="count">中间省略</span></div>
        <div class="stage">
          <div class="filerow"><span class="fico">▤</span><span class="fname keep"><span class="stem">2026年第三季度市场分析与增长策略复盘报告_v3_终稿_真的终稿</span><span class="ext">.docx</span></span></div>
        </div>
        <p class="note">名字再长，后缀永远在；还能顺手用后缀决定图标。</p>
      </div>
    </div>
  </section>

  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 05</span>
      <div><h2>分屏拖过 80%，自动折叠</h2>
      <p>拖中间的竖线。超过 80% 就折叠，按 Esc 或双击竖线复原。</p></div>
    </div>
    <div class="pane">
      <div class="pane-h"><span class="tag v">Split view</span><span class="count" id="splitState">左 50% / 右 50%</span></div>
      <div class="stage" style="padding:0;overflow:hidden">
        <div class="splitview" id="splitview">
          <div class="sp-left" id="spLeft"><span>对话区</span></div>
          <div class="sp-div" id="spDiv"></div>
          <div class="sp-right" id="spRight"><span>预览区</span></div>
        </div>
      </div>
      <p class="note" id="splitNote">拖到 80% 以上会自动折叠成单栏，避免留下一条看不清的窄缝。</p>
    </div>
  </section>
""",
    extra_css="""
.cand{font-size:12px;color:var(--ink-2);background:var(--card);border-radius:9px;padding:7px 10px;
  box-shadow:inset 0 0 0 1px var(--line-2);display:flex;gap:8px;align-items:center}
.cand span{background:var(--violet-2);color:var(--violet);border-radius:6px;padding:3px 8px}
.cand span:first-of-type{outline:1.5px solid var(--violet)}
.chat{height:190px;overflow:auto;padding:12px;display:flex;flex-direction:column;gap:9px;position:relative}
.msg{background:var(--card);border-radius:11px;padding:9px 11px;font-size:12.5px;color:var(--ink-2);
  box-shadow:inset 0 0 0 1px var(--line);animation:popIn .28s var(--ease)}
.msg.me{background:var(--teal-2);color:var(--ink);align-self:flex-end;box-shadow:none}
.jump{position:absolute;left:50%;bottom:10px;transform:translateX(-50%);font-size:11.5px;
  padding:6px 12px;border-radius:99px;background:var(--ink);color:var(--bg);box-shadow:var(--sh2);z-index:3}
[data-theme="dark"] .jump{background:var(--card-3);color:var(--ink)}
.radbox{width:112px;height:112px;background:var(--violet-2);display:grid;place-items:center;
  box-shadow:inset 0 0 0 1px var(--violet-3);transition:border-radius .18s var(--ease);margin:0 auto}
.radinner{background:var(--card);box-shadow:inset 0 0 0 1px var(--line-2);transition:all .18s var(--ease)}
.filerow{display:flex;align-items:center;gap:10px;background:var(--card);border-radius:11px;padding:11px 13px;
  box-shadow:inset 0 0 0 1px var(--line);min-width:0}
.fico{color:var(--ink-3);flex:0 0 auto}
.fname{font-size:13px;color:var(--ink);min-width:0;display:block}
.fname.cut{overflow:hidden;white-space:nowrap;text-overflow:ellipsis}
.fname.keep{display:flex;min-width:0}
.fname.keep .stem{overflow:hidden;white-space:nowrap;text-overflow:ellipsis;min-width:0}
.fname.keep .ext{flex:0 0 auto;color:var(--ink-2)}
.splitview{display:flex;height:190px;background:var(--card);position:relative;user-select:none}
.sp-left,.sp-right{display:grid;place-items:center;font-size:12.5px;color:var(--ink-3);min-width:0;overflow:hidden}
.sp-left{background:var(--card-2);width:50%}
.sp-right{flex:1}
.sp-div{width:5px;background:var(--line-2);cursor:col-resize;position:relative;flex:0 0 auto;transition:background .2s}
.sp-div::after{content:"";position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);
  width:1px;height:22px;background:var(--card);opacity:.9}
.sp-div:hover{background:var(--teal)}
.splitview.collapsed .sp-right{width:0;flex:0}
""",
    js="""
(function(){
  /* 01 输入法 */
  var state={A:false,B:false};
  function setCand(el,on){ el.hidden=!on; }
  var a=document.getElementById('imeA'), b=document.getElementById('imeB');
  var candA=document.getElementById('candA'), candB=document.getElementById('candB');
  var sA=document.getElementById('imeStateA'), sB=document.getElementById('imeStateB');
  var nA=document.getElementById('imeNoteA'), nB=document.getElementById('imeNoteB');
  var composing={A:false,B:false};
  function bind(inp,key,cand,st,nt,label){
    inp.addEventListener('compositionstart',function(){ composing[key]=true; setCand(cand,true); st.textContent='选字中'; });
    inp.addEventListener('compositionend',function(){ composing[key]=false; setCand(cand,false); st.textContent='已上屏'; });
    inp.addEventListener('keydown',function(e){
      if(e.key!=='Enter') return;
      e.preventDefault();
      if(composing[key]){
        if(key==='A'){ st.textContent='错误：已发送半句话'; nt.textContent='候选态按 Enter 被当成发送，输入框被清空，内容丢了。';
          toast('半句话被发出去了'); inp.value=''; composing.A=false; setCand(cand,false); }
        else { st.textContent='只上屏，未发送'; nt.textContent='Enter 只负责选字上屏，光标留在输入框，继续写。'; toast('上屏成功，没有发送'); }
      } else {
        st.textContent='已发送';
        nt.textContent = label==='A' ? '正常态发送：这里两边行为一致。' : '正常态发送：内容已提交。';
        toast('已发送：'+(inp.value||'（空）'));
        inp.value='';
      }
    });
  }
  bind(a,'A',candA,sA,nA,'A'); bind(b,'B',candB,sB,nB,'B');
  document.getElementById('imeStart').addEventListener('click',function(){
    a.value='ni hao'; b.value='ni hao';
    composing.A=true; composing.B=true;
    setCand(candA,true); setCand(candB,true);
    sA.textContent='选字中'; sB.textContent='选字中';
    toast('现在按 Enter 试试');
  });
  document.getElementById('imeEnd').addEventListener('click',function(){
    composing.A=false; composing.B=false; candA.hidden=true; candB.hidden=true;
    sA.textContent='已结束'; sB.textContent='已结束';
  });

  /* 02 滚动跟随 */
  var chatA=document.getElementById('chatA'), chatB=document.getElementById('chatB');
  var jump=document.getElementById('jumpB'), followLabel=document.getElementById('followB');
  var lines=['收到，我来梳理一下。','先看第一点：输入法状态。','第二点：滚动不能抢用户。','第三点：圆角要同心。','第四点：截断保留后缀。','第五点：分屏阈值 80%。','补充：Esc 应该能复原。','还在生成中…'];
  var idx=0, timer=null, follow=true;
  chatB.addEventListener('scroll',function(){
    var near = chatB.scrollHeight - chatB.scrollTop - chatB.clientHeight < 24;
    follow = near;
    jump.hidden = near;
    followLabel.textContent = near ? '跟随中' : '已停止跟随';
  });
  function push(){
    var t=lines[idx%lines.length];
    [chatA,chatB].forEach(function(c){
      var d=document.createElement('div'); d.className='msg'; d.textContent=t; c.appendChild(d);
    });
    idx++;
    chatA.scrollTop=chatA.scrollHeight;          /* 错误示范：无条件拽到底 */
    if(follow) chatB.scrollTop=chatB.scrollHeight;
  }
  document.getElementById('streamBtn').addEventListener('click',function(){
    if(timer) return; push(); timer=setInterval(push,700);
  });
  document.getElementById('streamStop').addEventListener('click',function(){ clearInterval(timer); timer=null; });
  jump.addEventListener('click',function(){ chatB.scrollTop=chatB.scrollHeight; follow=true; jump.hidden=true; followLabel.textContent='跟随中'; });

  /* 03 同心圆角 */
  var range=document.getElementById('radRange');
  function rad(){
    var gap=parseInt(range.value,10);
    var outer=20, inner=outer-gap;
    var oA=document.getElementById('radOuterA'), iA=document.getElementById('radInnerA');
    var oB=document.getElementById('radOuterB'), iB=document.getElementById('radInnerB');
    oA.style.borderRadius=outer+'px'; oA.style.padding=gap+'px';
    iA.style.borderRadius=Math.max(2,inner)+'px'; iA.style.width='100%'; iA.style.height='100%';
    oB.style.borderRadius=outer+'px'; oB.style.padding=gap+'px';
    iB.style.borderRadius=outer+'px'; iB.style.width='100%'; iB.style.height='100%';
    document.getElementById('radA').textContent='外 '+outer+' / 内 '+Math.max(2,inner);
    document.getElementById('radB').textContent='外 '+outer+' / 内 '+outer;
  }
  range.addEventListener('input',rad); rad();

  /* 05 分屏 */
  var sv=document.getElementById('splitview'), left=document.getElementById('spLeft'), div=document.getElementById('spDiv');
  var stateEl=document.getElementById('splitState'), noteEl=document.getElementById('splitNote');
  var dragging=false;
  function setPct(p){
    p=Math.max(12,Math.min(88,p));
    if(p>80){ sv.classList.add('collapsed'); stateEl.textContent='已折叠（>80%）';
      noteEl.textContent='超过 80% 自动折叠成单栏，避免留下一条看不清的窄缝。按 Esc 复原。'; return; }
    sv.classList.remove('collapsed');
    left.style.width=p+'%'; stateEl.textContent='左 '+Math.round(p)+'% / 右 '+Math.round(100-p)+'%';
  }
  function move(e){
    if(!dragging) return;
    var r=sv.getBoundingClientRect();
    var x=(e.touches?e.touches[0].clientX:e.clientX);
    setPct((x-r.left)/r.width*100);
  }
  div.addEventListener('mousedown',function(e){ dragging=true; e.preventDefault(); });
  div.addEventListener('touchstart',function(e){ dragging=true; },{passive:true});
  window.addEventListener('mousemove',move); window.addEventListener('touchmove',move,{passive:true});
  window.addEventListener('mouseup',function(){ dragging=false; }); window.addEventListener('touchend',function(){ dragging=false; });
  div.addEventListener('dblclick',function(){ sv.classList.remove('collapsed'); left.style.width='50%'; stateEl.textContent='左 50% / 右 50%'; });
  document.addEventListener('keydown',function(e){
    if(e.key==='Escape' && sv.classList.contains('collapsed')){
      sv.classList.remove('collapsed'); left.style.width='50%'; stateEl.textContent='左 50% / 右 50%'; toast('Esc 复原了分屏');
    }
  });
})();
""",
    notes=[
        "<b>输入法状态</b>：composition 期间 Enter 只能上屏，不能发送；否则用户会把半句话发出去。",
        "<b>滚动跟随</b>：往上滚就停止自动跟随，并给「回到最新」；不要用 scrollTop 硬拽。",
        "<b>描边只包一层</b>：不要在容器上再套一层边，按钮靠背景色区分即可。",
        "<b>圆角同心</b>：外圈半径 = 内圈半径 + 间距，否则角落会显得「胖」。",
        "<b>分屏阈值</b>：拖过 80% 自动折叠，Esc 复原、双击竖线回到 50/50。",
        "<b>彩蛋</b>：长文件名截断时，扩展名必须保留——它决定用户「用什么打开」。",
    ],
)
