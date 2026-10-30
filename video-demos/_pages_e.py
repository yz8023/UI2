# -*- coding: utf-8 -*-
"""页面 07、08：全球化布局 / 两个游戏视频"""

P07 = dict(
    no="07", short="全球化布局", title="界面走向全球化，按钮为什么总被外文撑爆",
    bvid="BV1gex76PECV", dur="04:22", date="2026-10-28",
    kicker="Bilibili · KD一对A · 国际化 / 布局",
    lede="改个语言，按钮就炸了：中文一行放得下，德语换三行，整张卡片被顶出屏幕。这一页把 3 个隐藏坑做成可以切换语言的实景，顺便看看泰语变音符和阿拉伯语镜像怎么处理。",
    tag1="多语言 / 溢出", tag2="RTL / 行高",
    quote="「10 个字母以内的短词，译成欧洲语言后长度会涨到 <b>2~3 倍</b>——固定宽度按钮必炸。」",
    demos="""
  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 01</span>
      <div><h2>固定宽度 vs 百分比分栏</h2>
      <p>切语言看卡片底部的操作栏。左边写死宽度，右边按「左固定 + 右弹性」分栏。</p></div>
    </div>
    <div class="row" style="margin-bottom:14px">
      <div class="seg" id="langSeg">
        <button data-lang="zh" aria-selected="true">中文</button>
        <button data-lang="en">English</button>
        <button data-lang="de">Deutsch</button>
        <button data-lang="th">ไทย</button>
        <button data-lang="ar">العربية</button>
      </div>
    </div>
    <div class="split">
      <div class="pane bad">
        <div class="pane-h"><span class="tag no">✕ 按钮写死 96px</span><span class="count" id="ovStateA">中文：刚好</span></div>
        <div class="stage" style="align-items:stretch">
          <div class="mockcard" id="cardA">
            <div class="mc-body"><b>订阅方案</b><span>Pro · 每月 ¥29</span></div>
            <div class="mc-bar fixed">
              <button class="aux" data-k="aux">取消</button>
              <button class="main" data-k="main">保存更改</button>
            </div>
          </div>
        </div>
        <p class="note" id="noteA">中文刚好一行；切成德语，按钮换行把卡片顶高了。</p>
      </div>
      <div class="pane good">
        <div class="pane-h"><span class="tag ok">✓ 左固定 + 右弹性</span><span class="count" id="ovStateB">中文：刚好</span></div>
        <div class="stage" style="align-items:stretch">
          <div class="mockcard" id="cardB">
            <div class="mc-body"><b>订阅方案</b><span>Pro · 每月 ¥29</span></div>
            <div class="mc-bar flex">
              <button class="aux" data-k="aux">取消</button>
              <button class="main" data-k="main">保存更改</button>
            </div>
          </div>
        </div>
        <p class="note" id="noteB">按钮区弹性占满剩余空间，超长就压缩 + 省略，还放不下就退化成图标。</p>
      </div>
    </div>
  </section>

  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 02</span>
      <div><h2>泰语 / 越南语的变音符，会被固定行高裁掉</h2>
      <p>同一句泰语，左边行高写死 1.1，上下的符号被切掉了。</p></div>
    </div>
    <div class="split">
      <div class="pane bad">
        <div class="pane-h"><span class="tag no">✕ line-height: 1.1</span><span class="count">overflow: hidden</span></div>
        <div class="stage">
          <div class="thai clip">เปลี่ยนภาษาไทย<br>การตั้งค่าระบบ</div>
        </div>
        <p class="note">上下标被裁，字看起来像「缺了一块」，用户会以为是字体坏了。</p>
      </div>
      <div class="pane good">
        <div class="pane-h"><span class="tag ok">✓ line-height: 1.6</span><span class="count">留足行距</span></div>
        <div class="stage">
          <div class="thai">เปลี่ยนภาษาไทย<br>การตั้งค่าระบบ</div>
        </div>
        <p class="note">多语言场景下别把行高写死，给变音符留出上方空间。</p>
      </div>
    </div>
  </section>

  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 03</span>
      <div><h2>阿拉伯语：整页镜像，但数字和进度还是从左到右</h2>
      <p>切换 RTL，看布局整体翻转、进度条和金额保持原方向。</p></div>
    </div>
    <div class="pane">
      <div class="pane-h">
        <span class="tag v">dir 属性</span>
        <label class="switch" id="rtlSwitch" role="switch" aria-checked="false"><span class="track"><span class="knob"></span></span>RTL 镜像</label>
      </div>
      <div class="stage">
        <div class="rtlcard" id="rtlCard" dir="ltr">
          <div class="rtlrow">
            <span class="rtlavatar">A</span>
            <div class="rtltxt"><b>تمويل المشروع</b><span>مشروع تجريبي · 2026</span></div>
            <span class="rtlamt">¥1,280.00</span>
          </div>
          <div class="rtlbar"><i></i></div>
          <div class="rtlrow small">
            <span class="rtltxt">تم إنجاز 62% من الميزانية</span>
            <span class="rtlamt">62%</span>
          </div>
        </div>
      </div>
      <p class="note">整页镜像后，头像在右、文字右对齐；但金额、百分比、进度条仍然是 LTR——数字的阅读顺序不能跟着翻。</p>
    </div>
  </section>
""",
    extra_css="""
.mockcard{background:var(--card);border-radius:13px;padding:13px;box-shadow:inset 0 0 0 1px var(--line);
  display:flex;flex-direction:column;gap:12px;width:100%;max-width:330px;margin:0 auto;overflow:hidden}
.mc-body{display:flex;justify-content:space-between;gap:8px;font-size:12.5px;color:var(--ink-3)}
.mc-body b{font-size:13px;color:var(--ink)}
.mc-bar{display:flex;align-items:center;gap:8px}
.mc-bar button{border-radius:9px;font-size:12.5px;padding:8px 10px}
.mc-bar .aux{background:var(--card-2);color:var(--ink-2)}
.mc-bar .main{background:var(--teal);color:#fff}
[data-theme="dark"] .mc-bar .main{color:#06211d}
.mc-bar.fixed button{width:96px;white-space:normal;line-height:1.3}
.mc-bar.fixed .main{flex:0 0 96px}
.mc-bar.flex .aux{flex:0 0 auto}
.mc-bar.flex .main{flex:1 1 auto;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.mc-bar.flex.icons .main{padding:8px;display:grid;place-items:center}
.mockcard.overflowing{box-shadow:inset 0 0 0 1px var(--red-3)}
.thai{font-size:14px;line-height:1.6;color:var(--ink);letter-spacing:0}
.thai.clip{line-height:1.1;height:31px;overflow:hidden}
.rtlcard{width:100%;max-width:360px;margin:0 auto;background:var(--card);border-radius:13px;padding:13px;
  box-shadow:inset 0 0 0 1px var(--line);display:flex;flex-direction:column;gap:12px;transition:direction .2s}
.rtlrow{display:flex;align-items:center;gap:10px}
.rtlrow.small{font-size:12px;color:var(--ink-3)}
.rtlavatar{width:28px;height:28px;border-radius:9px;background:var(--violet-2);color:var(--violet);
  display:grid;place-items:center;font-size:12px;font-weight:600;flex:0 0 auto}
.rtltxt{flex:1;min-width:0;display:flex;flex-direction:column}
.rtltxt b{font-size:13px}
.rtltxt span{font-size:11.5px;color:var(--ink-3)}
.rtlamt{font-size:13px;font-weight:600;direction:ltr;unicode-bidi:isolate;white-space:nowrap}
.rtlbar{height:6px;border-radius:99px;background:var(--card-2);overflow:hidden;direction:ltr}
.rtlbar i{display:block;height:100%;width:62%;background:var(--teal);border-radius:99px}
""",
    js="""
(function(){
  var dict={
    zh:{aux:'取消',main:'保存更改',state:'中文：刚好'},
    en:{aux:'Cancel',main:'Save changes',state:'英文：刚好'},
    de:{aux:'Abbrechen',main:'Änderungen speichern',state:'德语：文本涨了 2 倍'},
    th:{aux:'ยกเลิก',main:'บันทึกการเปลี่ยนแปลง',state:'泰语：明显变长'},
    ar:{aux:'إلغاء',main:'حفظ التغييرات',state:'阿拉伯语：字数接近'}
  };
  var cur='zh';
  function paint(){
    var d=dict[cur];
    document.querySelectorAll('.mc-bar .aux').forEach(function(b){ b.textContent=d.aux; });
    document.querySelectorAll('.mc-bar .main').forEach(function(b){ b.textContent=d.main; });
    document.getElementById('ovStateA').textContent=d.state;
    document.getElementById('ovStateB').textContent=d.state;
    /* 检测左侧是否溢出 */
    var cardA=document.getElementById('cardA');
    var barA=cardA.querySelector('.mc-bar');
    var over = barA.scrollWidth > cardA.clientWidth + 2 || (cardA.querySelector('.main').offsetHeight>44);
    cardA.classList.toggle('overflowing',over);
    document.getElementById('noteA').textContent = over
      ? '已经溢出了：按钮换行把卡片顶高，右侧内容被挤出可视区。'
      : '中文刚好一行；切成德语试试。';
    /* 右侧：放不下就退化成图标 */
    var barB=document.getElementById('cardB').querySelector('.mc-bar');
    var mainB=barB.querySelector('.main');
    var squeezed = mainB.scrollWidth > mainB.clientWidth + 2;
    if(squeezed && cur!=='zh' && cur!=='en'){
      mainB.innerHTML='<svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="m5 13 4 4L19 7" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
      barB.classList.add('icons');
      document.getElementById('noteB').textContent='弹性区放不下长词，降级成通用图标（保存）——语义不变，但不再溢出。';
    } else {
      barB.classList.remove('icons');
    }
  }
  document.querySelectorAll('#langSeg button').forEach(function(b){
    b.addEventListener('click',function(){
      document.querySelectorAll('#langSeg button').forEach(function(x){ x.setAttribute('aria-selected',String(x===b)); });
      cur=b.dataset.lang; paint();
    });
  });
  paint();

  var rtl=document.getElementById('rtlSwitch'), card=document.getElementById('rtlCard');
  rtl.addEventListener('click',function(){
    var on = rtl.getAttribute('aria-checked')!=='true';
    rtl.setAttribute('aria-checked', String(on));
    card.setAttribute('dir', on?'rtl':'ltr');
    toast(on? '已镜像：进度与数字仍是 LTR':'已回到 LTR');
  });
})();
""",
    notes=[
        "<b>短词膨胀</b>：10 个字母以内的短词，译成欧洲语言会涨 2~3 倍，固定宽度必炸。",
        "<b>百分比分栏</b>：底部操作栏左侧辅助区按层级定宽，右侧按钮弹性填满剩余空间。",
        "<b>降级策略</b>：极长词先压缩、再省略，仍放不下就换通用图标。",
        "<b>别写死行高</b>：泰语、越南语的变音符会被裁掉，给上方留空间。",
        "<b>RTL 整页镜像</b>，但进度条、数字、金额仍然 LTR。",
        "<b>测试方法</b>：切到最长的语言做一遍，别只测中英文。",
    ],
)

P08 = dict(
    no="08", short="虎先锋 · 无伤实录", title="无伤虎先锋：1060 古董卡，40 帧还能这么丝滑？",
    bvid="BV1k8s4eeEuG", dur="03:06", date="2024-08-27",
    kicker="Bilibili · KD一对A · 非 UI 内容 · 游戏实录",
    lede="账号里最早期还有两期《黑神话：悟空》的无伤实况，和 UI 科普完全无关，属于个人记录。这一条是虎先锋：纯棍式、禁法术、全程闪避。没有组件规则可提炼，所以这页做两件事——把视频信息收好，再用「帧率观感」示意说明标题里那句「40 帧还能这么丝滑」为什么值得惊讶。",
    tag1="游戏实录", tag2="帧率 / 观感",
    quote="「不管界面还是游戏，<b>流畅感都是被『帧与帧之间的空隙』决定的</b>——只不过一边是动画曲线，一边是显卡。」",
    demos="""
  <section class="demo">
    <div class="demo-head"><span class="dnum">信息</span>
      <div><h2>这条视频</h2><p>标题、时间、内容摘要来自视频页公开信息。</p></div>
    </div>
    <div class="pane">
      <div class="pane-h"><span class="tag w">2024-08-27 · 03:06</span><span class="count">412 播放 · 0 弹幕</span></div>
      <div class="stage" style="align-items:flex-start;gap:10px">
        <b style="font-size:14px">全程闪避、禁法术、纯棍式、无伤虎先锋，1060 古董 40 帧还能这么丝滑？</b>
        <p style="font-size:13px;color:var(--ink-2);line-height:1.75">GTX 1060 / 1080p 录屏，作者自述画质偏糙；第一次玩 ARPG，前后打了约 8 小时才做到无伤，自评「不完美但还行」。</p>
        <div class="row" style="margin-top:4px">
          <span class="pill" style="background:var(--amber-2);color:var(--amber)">纯棍式</span>
          <span class="pill" style="background:var(--amber-2);color:var(--amber)">禁法术</span>
          <span class="pill" style="background:var(--amber-2);color:var(--amber)">全程闪避</span>
        </div>
      </div>
      <div class="row" style="margin-top:12px"><a class="btn sm ghost" href="https://www.bilibili.com/video/BV1k8s4eeEuG" target="_blank" rel="noopener" style="text-decoration:none">在 B 站打开 ↗</a><a class="btn sm ghost" href="09-寅虎-·-无伤实录.html" style="text-decoration:none">看另一条：寅虎 →</a></div>
    </div>
  </section>

  <section class="demo">
    <div class="demo-head"><span class="dnum">演示</span>
      <div><h2>帧率观感示意：同样是 1 秒，30 帧和 60 帧差在哪</h2>
      <p>这是本页自制示意，不是视频原画——但能说明标题那句「40 帧还能这么丝滑」为什么值得惊讶。</p></div>
    </div>
    <div class="split">
      <div class="pane bad">
        <div class="pane-h"><span class="tag no">✕ 30fps · 步进</span><span class="count">steps(30)</span></div>
        <div class="stage">
          <div class="fpsrail"><span class="fpsball choppy"></span></div>
        </div>
        <p class="note">动作一格一格跳，快速镜头转换时会糊成一片。</p>
      </div>
      <div class="pane good">
        <div class="pane-h"><span class="tag ok">✓ 60fps · 连续</span><span class="count">linear</span></div>
        <div class="stage">
          <div class="fpsrail"><span class="fpsball smooth"></span></div>
        </div>
        <p class="note">每一帧都接得上，眼睛看到的是「移动」而不是「闪」。</p>
      </div>
    </div>
    <div class="row" style="margin-top:12px">
      <button class="btn sm primary" id="fpsReplay">重播</button>
      <span class="count">动作游戏里，40fps 稳定往往比 60fps 波动更「舒服」</span>
    </div>
  </section>
""",
    extra_css="""
.fpsrail{position:relative;height:64px;border-radius:12px;background:var(--card);overflow:hidden;
  box-shadow:inset 0 0 0 1px var(--line)}
.fpsrail::before{content:"";position:absolute;left:0;right:0;bottom:9px;height:1px;background:var(--line-2)}
.fpsball{position:absolute;bottom:9px;left:6px;width:26px;height:26px;border-radius:8px;background:var(--teal);display:block}
.fpsball.choppy{animation:move30 1.6s steps(30) infinite alternate;background:var(--red)}
.fpsball.smooth{animation:move60 1.6s cubic-bezier(.45,0,.55,1) infinite alternate}
@keyframes move30{from{left:6px}to{left:calc(100% - 32px)}}
@keyframes move60{from{left:6px}to{left:calc(100% - 32px)}}
.paused .fpsball{animation-play-state:paused}
""",
    js="""
(function(){
  document.getElementById('fpsReplay').addEventListener('click',function(){
    document.querySelectorAll('.fpsrail').forEach(function(r){
      r.classList.add('paused');
      setTimeout(function(){ r.classList.remove('paused'); },60);
    });
    toast('重新播放');
  });
})();
""",
    notes=[
        "<b>非 UI 内容</b>：2024 年的《黑神话：悟空》虎先锋无伤实况，和账号的 UI 科普主线无关。",
        "<b>配置</b>：GTX 1060 + 1080p，画质偏糙，作者自己也在简介里道歉。",
        "<b>流派</b>：纯棍式、禁法术、全程靠闪避规避伤害，容错率极低。",
        "<b>代价</b>：第一次玩 ARPG，打了约 8 小时才完成；结尾差一点没打出四段棍。",
        "<b>为什么强调 40 帧</b>：动作游戏里「稳定」比「高但抖」更影响手感。",
        "<b>可迁移的一点</b>：界面动效同理——均匀的 60fps 曲线，比忽快忽慢的位移更高级。",
    ],
)

P09 = dict(
    no="09", short="寅虎 · 无伤实录", title="寅虎：你礼貌吗？——无伤挑战里的节奏",
    bvid="BV12pH9eVE94", dur="02:10", date="2024-09-06",
    kicker="Bilibili · KD一对A · 非 UI 内容 · 游戏实录",
    lede="兵器的「无伤」不是靠手速，而是靠对帧的耐心：起手看得见、判定只有几帧、收招才是惩罚窗口。这页把寅虎的一次出招拆成时间轴，你可以拖着玩一次——看看早闪、完美闪、和站着不动的区别。",
    tag1="游戏实录", tag2="招式节奏 / 闪避窗口",
    quote="「<b>寅虎</b>：你礼貌吗？」——标题是个玩家梗；Boss 的出招节奏，恰恰是最讲道理的那部分。",
    demos="""
  <section class="demo">
    <div class="demo-head"><span class="dnum">信息</span>
      <div><h2>这条视频</h2><p>标题、时间、内容摘要来自视频页公开信息。</p></div>
    </div>
    <div class="pane">
      <div class="pane-h"><span class="tag w">2024-09-06 · 02:10</span><span class="count">464 播放 · 0 弹幕</span></div>
      <div class="stage" style="align-items:flex-start;gap:10px">
        <b style="font-size:14px">寅虎：你礼貌吗？</b>
        <p style="font-size:13px;color:var(--ink-2);line-height:1.75">同样是 GTX 1060 老显卡 + 禁字法术流的无伤挑战，作者自述磨了两天才过；结尾差一点没打出四段棍，自嘲「虽然没有四段棍收尾，还是挺满意」。</p>
        <div class="row" style="margin-top:4px">
          <span class="pill" style="background:var(--amber-2);color:var(--amber)">禁字法术流</span>
          <span class="pill" style="background:var(--amber-2);color:var(--amber)">无伤</span>
          <span class="pill" style="background:var(--amber-2);color:var(--amber)">ARPG 新手</span>
        </div>
      </div>
      <div class="row" style="margin-top:12px"><a class="btn sm ghost" href="https://www.bilibili.com/video/BV12pH9eVE94" target="_blank" rel="noopener" style="text-decoration:none">在 B 站打开 ↗</a><a class="btn sm ghost" href="08-虎先锋-·-无伤实录.html" style="text-decoration:none">看另一条：虎先锋 →</a></div>
    </div>
  </section>

  <section class="demo">
    <div class="demo-head"><span class="dnum">演示</span>
      <div><h2>把一次出招拆成时间轴（自制示意）</h2>
      <p>拖游标到某一帧，再点「闪避」。判定期只有很窄一截，早了晚了都要吃伤害。</p></div>
    </div>
    <div class="split">
      <div class="pane">
        <div class="pane-h"><span class="tag v">寅虎 · 蓄力三连</span><span class="count" id="frameState">第 0 帧</span></div>
        <div class="stage" style="align-items:stretch;gap:14px">
          <div class="timeline" id="timeline">
            <div class="tlzone wind"><span>起手</span></div>
            <div class="tlzone hit"><span>判定</span></div>
            <div class="tlzone rec"><span>收招</span></div>
            <div class="playhead" id="playhead"></div>
          </div>
          <input type="range" id="frameRange" min="0" max="100" value="24" step="1">
          <div class="row">
            <button class="btn sm primary" id="dodgeBtn">闪避</button>
            <span class="count" id="dodgeResult">等待操作</span>
          </div>
        </div>
        <p class="note" id="dodgeNote">判定帧前 2~3 帧按下闪避，无敌帧刚好盖住伤害——这就是所谓「完美闪避」。</p>
      </div>
      <div class="pane">
        <div class="pane-h"><span class="tag">五连测试</span><span class="count" id="hpState">血量 5 / 5</span></div>
        <div class="stage" style="justify-content:flex-start;gap:12px">
          <div class="hpips" id="hpips"><i></i><i></i><i></i><i></i><i></i></div>
          <div class="logstack" id="dodgeLog">连续 5 次闪避，看看能不能零伤害收尾。</div>
        </div>
        <p class="note">无伤的关键不是「一直按」，而是<strong>每次都在正确的窗口里按一次</strong>。</p>
      </div>
    </div>
  </section>
""",
    extra_css="""
.timeline{position:relative;height:56px;border-radius:11px;overflow:hidden;display:flex;
  box-shadow:inset 0 0 0 1px var(--line);background:var(--card)}
.tlzone{display:flex;align-items:flex-end;justify-content:center;padding-bottom:6px;font-size:10.5px;color:var(--ink-3);position:relative}
.tlzone.wind{flex:0 0 40%;background:var(--card-2)}
.tlzone.hit{flex:0 0 18%;background:var(--red-2);color:var(--red)}
.tlzone.rec{flex:1;background:var(--teal-2);color:var(--teal)}
.tlzone+.tlzone{border-left:1px solid var(--line)}
.playhead{position:absolute;top:0;bottom:0;width:2px;background:var(--ink);left:24%;transition:left .08s linear}
.playhead::after{content:"";position:absolute;top:-1px;left:-4px;width:10px;height:10px;border-radius:50%;background:var(--ink)}
.hpips{display:flex;gap:7px}
.hpips i{width:26px;height:8px;border-radius:99px;background:var(--red);display:block;transition:background .25s var(--ease),transform .25s var(--spring)}
.hpips i.lost{background:var(--card-3);transform:scaleX(.72)}
.logstack{font-size:12.5px;color:var(--ink-2);line-height:1.7;background:var(--card);border-radius:10px;
  padding:10px 12px;box-shadow:inset 0 0 0 1px var(--line);width:100%;min-height:66px}
.logstack b{color:var(--ink)}
.logstack .ok{color:var(--teal);font-weight:600}
.logstack .bad{color:var(--red);font-weight:600}
""",
    js="""
(function(){
  var range=document.getElementById('frameRange'), head=document.getElementById('playhead');
  var state=document.getElementById('frameState');
  var result=document.getElementById('dodgeResult'), note=document.getElementById('dodgeNote');
  function paint(){
    var v=parseInt(range.value,10);
    head.style.left=v+'%';
    var phase = v<40?'起手':(v<58?'判定':'收招');
    state.textContent='第 '+v+' 帧 · '+phase;
    return v;
  }
  range.addEventListener('input',paint); paint();

  var hp=5, tries=0;
  var pips=document.querySelectorAll('#hpips i');
  var log=document.getElementById('dodgeLog'), hpState=document.getElementById('hpState');
  function hit(){
    hp=Math.max(0,hp-1);
    pips.forEach(function(p,i){ p.classList.toggle('lost', i>=hp); });
    hpState.textContent='血量 '+hp+' / 5';
  }
  document.getElementById('dodgeBtn').addEventListener('click',function(){
    var v=parseInt(range.value,10);
    tries++;
    var msg='', ok=false;
    if(v>=52 && v<60){ msg='<span class="ok">完美闪避</span>：无敌帧盖住判定帧，反手一棍'; ok=true;
      result.textContent='完美闪避'; note.textContent='判定帧前一瞬按下，无敌帧刚好覆盖伤害——收益也最高。'; }
    else if(v<22){ msg='<span class="bad">闪早了</span>：无敌帧用光，正好撞上判定'; hit();
      result.textContent='闪早了'; note.textContent='闪避有很短的冷却，太早按下等于空放，判定来时只能硬吃。'; }
    else if(v<52){ msg='<span class="bad">早了半拍</span>：无敌帧结束时判定还没到'; hit();
      result.textContent='早了半拍'; note.textContent='距离完美窗口还差一点，再等几帧就行。'; }
    else if(v<70){ msg='<span class="ok">闪开了</span>：判定已过，安全但没收益'; ok=true;
      result.textContent='安全闪开'; note.textContent='判定帧已经过去，这一下不亏，但也错过了完美闪避的增益。'; }
    else { msg='<span class="ok">收招期闪避</span>：安全，只是浪费了体力'; ok=true;
      result.textContent='收招闪避'; note.textContent='收招期其实是输出窗口，闪避反而把机会让了出去。'; }
    log.innerHTML='第 '+tries+' 次 · 第 '+v+' 帧 —— '+msg + (hp===0?'<br><b>血量归零，无伤挑战失败。</b> 从头再来。':'');
    if(hp===0){ setTimeout(reset,900); }
    toast(ok? '闪开了':'吃到伤害');
  });
  function reset(){ hp=5; tries=0; pips.forEach(function(p){p.classList.remove('lost');});
    hpState.textContent='血量 5 / 5'; log.textContent='连续 5 次闪避，看看能不能零伤害收尾。'; }
})();
""",
    notes=[
        "<b>非 UI 内容</b>：2024 年的《黑神话：悟空》寅虎无伤实况，属于个人游戏记录。",
        "<b>配置与流派</b>：GTX 1060 + 禁字法术流，作者自述磨了两天才过。",
        "<b>「你礼貌吗」是梗</b>：吐槽 Boss 出招毫不留情，尤其是贴身的三连。",
        "<b>无伤的真相</b>：不是手速，是记住「起手—判定—收招」的节奏，在该按的那一帧按一次。",
        "<b>和 UI 的相通点</b>：动画的「缓入缓出」、按钮的「按下—抬起」，同样是在时间轴上安排窗口。",
    ],
)
