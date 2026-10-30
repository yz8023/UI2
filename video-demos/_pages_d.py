# -*- coding: utf-8 -*-
"""页面 05、06：下拉 vs 选择器 / 你总是点不中按钮"""

P05 = dict(
    no="05", short="下拉 vs 选择器", title="别乱叫「下拉框」",
    bvid="BV1qmnd6gEkk", dur="03:06", date="2026-10-26",
    kicker="Bilibili · KD一对A · 组件辨析 · 播放最高的一期",
    lede="两个视觉几乎一样的东西，大厂组件库非要拆成两个。这一页把它们放进真实界面里各点一次，再配三条选型铁律——看完你可以直接跟产品和 AI 说清楚要哪个。",
    tag1="Dropdown / Select", tag2="组件选型",
    quote="「<b>Select 是拿来选的</b>，而 <b>Dropdown 是一堆命令的集合</b>。」—— Arco Design",
    demos="""
  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 01</span>
      <div><h2>并排点一次：一个执行命令，一个回填数值</h2>
      <p>左边点「分享」会立刻发生一件事；右边选完城市只是把值写进框里，还要等提交。</p></div>
    </div>
    <div class="split">
      <div class="pane" style="box-shadow:inset 0 0 0 1px var(--violet-3),var(--sh)">
        <div class="pane-h"><span class="tag v">Dropdown 下拉菜单</span><span class="count">导航 / 操作</span></div>
        <div class="stage">
          <div class="toolbar">
            <button class="btn sm">返回列表</button>
            <div class="pop" id="ddP">
              <button class="trig" id="ddT">分享
                <svg width="12" height="12" viewBox="0 0 16 16" fill="none"><path d="m3.5 6 4.5 4.5L12.5 6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
              </button>
              <div class="menu" id="ddM">
                <button data-cmd="复制链接">复制链接<kbd>⌘C</kbd></button>
                <button data-cmd="生成图片">生成分享图</button>
                <button data-cmd="分享到微信">分享到微信</button>
                <i class="sep"></i>
                <button class="danger" data-cmd="删除订单">删除订单</button>
              </div>
            </div>
          </div>
          <div class="logbox" id="ddLog">还没有执行任何命令</div>
        </div>
        <p class="note">没有「当前值」这个概念，点完就关闭，不需要回显。</p>
      </div>

      <div class="pane" style="box-shadow:inset 0 0 0 1px var(--teal-3),var(--sh)">
        <div class="pane-h"><span class="tag t" style="background:var(--teal-2);color:var(--teal)">Select 选择器</span><span class="count">数据录入</span></div>
        <div class="stage">
          <label class="flabel">所属城市 <b style="color:var(--red)">*</b></label>
          <div class="pop" id="selP" style="display:block">
            <button class="strig" id="selT">
              <span id="selVal" class="ph">请选择城市</span>
              <svg width="12" height="12" viewBox="0 0 16 16" fill="none"><path d="m3.5 6 4.5 4.5L12.5 6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
            </button>
            <div class="menu wide" id="selM">
              <div class="mnote">单选 · 可清除</div>
              <button data-val="上海">上海</button>
              <button data-val="北京">北京</button>
              <button data-val="深圳">深圳</button>
              <button data-val="东京">东京</button>
            </div>
          </div>
          <div class="row"><button class="btn sm primary" id="selSubmit">提交</button><span class="count" id="selEcho">未选择</span></div>
        </div>
        <p class="note">选中的值回填进输入框，校验通过才随表单一起提交。</p>
      </div>
    </div>
  </section>

  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 02</span>
      <div><h2>三条铁律：2 个用开关，5 个以内平铺，超过 10 个限高加搜索</h2>
      <p>三组对照都能点，右上角记着你为它付出的点击。</p></div>
    </div>
    <div class="trio">
      <div class="pane bad">
        <div class="pane-h"><span class="tag no">✕ 2 个选项还做菜单</span><span class="count" id="r1c">点击 0 次</span></div>
        <div class="stage">
          <div class="pop" id="twoP">
            <button class="strig" id="twoT" style="width:150px"><span id="twoV" class="ph">开关</span>
              <svg width="12" height="12" viewBox="0 0 16 16" fill="none"><path d="m3.5 6 4.5 4.5L12.5 6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></button>
            <div class="menu" id="twoM" style="min-width:150px"><button data-v="开启">开启</button><button data-v="关闭">关闭</button></div>
          </div>
        </div>
        <p class="note">展开 + 选择 = 2 次点击，还不如直接给一个开关。</p>
      </div>
      <div class="pane good">
        <div class="pane-h"><span class="tag ok">✓ 开关 / 单选</span><span class="count" id="r1d">点击 0 次</span></div>
        <div class="stage">
          <div class="switch" id="twoSwitch" role="switch" aria-checked="false" tabindex="0"><span class="track"><span class="knob"></span></span>自动同步</div>
        </div>
        <p class="note">一次点击完成，状态一眼可见。</p>
      </div>
    </div>

    <div class="trio" style="margin-top:14px">
      <div class="pane bad">
        <div class="pane-h"><span class="tag no">✕ 4 个选项藏起来</span><span class="count">要点开才知道有什么</span></div>
        <div class="stage">
          <div class="pop" id="fourP">
            <button class="strig" id="fourT" style="width:170px"><span id="fourV" class="ph">选择周期</span>
              <svg width="12" height="12" viewBox="0 0 16 16" fill="none"><path d="m3.5 6 4.5 4.5L12.5 6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></button>
            <div class="menu" id="fourM" style="min-width:170px"><button data-v="日">日</button><button data-v="周">周</button><button data-v="月">月</button><button data-v="年">年</button></div>
          </div>
        </div>
        <p class="note">4 个选项完全放得下，却让用户先「探索」一次。</p>
      </div>
      <div class="pane good">
        <div class="pane-h"><span class="tag ok">✓ 分段控件平铺</span><span class="count">全部可见</span></div>
        <div class="stage">
          <div class="seg" id="fourSeg">
            <button aria-selected="true">日</button><button>周</button><button>月</button><button>年</button>
          </div>
        </div>
        <p class="note">切换只要 1 次点击，无需展开。</p>
      </div>
    </div>

    <div class="pane" style="margin-top:14px">
      <div class="pane-h"><span class="tag ok">✓ 超过 10 个：限高 264px + 搜索</span><span class="count" id="listMeta">36 项</span></div>
      <div class="stage" style="align-items:stretch">
        <input class="field" id="citySearch" placeholder="搜索城市，例如「杭」" style="max-width:320px">
        <div class="longlist" id="cityList"></div>
      </div>
      <p class="note">列表永远在容器里滚，不会把页面顶长；输入即过滤，不用在几十行里找。</p>
    </div>
  </section>
""",
    extra_css="""
.toolbar{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.pop{position:relative;display:inline-block}
.trig{display:inline-flex;align-items:center;gap:6px;padding:8px 11px;border-radius:10px;font-size:13px;color:var(--ink)}
.trig:hover{background:var(--card-3)}
.strig{display:flex;align-items:center;justify-content:space-between;gap:8px;width:100%;padding:10px 12px;
  border-radius:11px;background:var(--card);box-shadow:inset 0 0 0 1px var(--line-2);font-size:13px;text-align:left}
.strig .ph{color:var(--ink-3)}
.menu{position:absolute;left:0;top:calc(100% + 7px);min-width:190px;z-index:40;padding:6px;
  background:var(--card);border-radius:13px;box-shadow:var(--sh2);
  opacity:0;transform:translateY(-6px) scale(.98);pointer-events:none;transform-origin:top left;
  transition:opacity .16s var(--ease),transform .2s var(--ease)}
.menu.wide{width:100%;min-width:0}
.pop.on .menu{opacity:1;transform:none;pointer-events:auto}
.menu button{display:flex;align-items:center;gap:9px;width:100%;padding:9px 10px;border-radius:9px;
  font-size:13px;color:var(--ink);text-align:left}
.menu button:hover{background:var(--card-2)}
.menu button.danger{color:var(--red)}
.menu kbd{margin-left:auto;font-size:11px;color:var(--ink-3);background:var(--card-2);border-radius:5px;padding:2px 6px}
.menu .sep{display:block;height:1px;background:var(--line);margin:5px 6px}
.mnote{padding:7px 10px 5px;font-size:11.5px;color:var(--ink-3)}
.logbox{font-size:12px;color:var(--ink-3);background:var(--card);border-radius:10px;padding:9px 11px;
  box-shadow:inset 0 0 0 1px var(--line);min-height:36px}
.logbox b{color:var(--ink);font-weight:600}
.flabel{font-size:12.5px;color:var(--ink-2);margin-bottom:6px;display:block}
.trio{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.longlist{max-height:264px;overflow:auto;border-radius:11px;background:var(--card);padding:6px;
  box-shadow:inset 0 0 0 1px var(--line);scrollbar-width:thin}
.longlist button{display:flex;align-items:center;justify-content:space-between;width:100%;padding:8px 10px;
  border-radius:8px;font-size:13px;color:var(--ink);text-align:left}
.longlist button:hover{background:var(--card-2)}
.longlist button[aria-selected="true"]{color:var(--teal);font-weight:600}
@media (max-width:880px){.trio{grid-template-columns:1fr}}
""",
    js="""
(function(){
  function pop(pid){
    var p=document.getElementById(pid);
    return {
      open:function(){ p.classList.add('on'); },
      close:function(){ p.classList.remove('on'); },
      toggle:function(){ p.classList.toggle('on'); },
      isOpen:function(){ return p.classList.contains('on'); }
    };
  }
  var dd=pop('ddP'), sel=pop('selP'), two=pop('twoP'), four=pop('fourP');

  document.getElementById('ddT').addEventListener('click',function(e){ e.stopPropagation(); dd.toggle(); });
  document.querySelectorAll('#ddM button').forEach(function(b){
    b.addEventListener('click',function(e){
      e.stopPropagation();
      document.getElementById('ddLog').innerHTML='已执行 · <b>'+b.dataset.cmd+'</b>';
      dd.close(); toast('已执行：'+b.dataset.cmd);
    });
  });

  var selVal=document.getElementById('selVal'), echo=document.getElementById('selEcho');
  document.getElementById('selT').addEventListener('click',function(e){ e.stopPropagation(); sel.toggle(); });
  document.querySelectorAll('#selM button').forEach(function(b){
    b.addEventListener('click',function(e){
      e.stopPropagation();
      selVal.textContent=b.dataset.val; selVal.classList.remove('ph');
      document.querySelectorAll('#selM button').forEach(function(x){ x.setAttribute('aria-selected',String(x===b)); });
      echo.textContent='当前值：'+b.dataset.val+'（未提交）';
      sel.close();
    });
  });
  document.getElementById('selSubmit').addEventListener('click',function(){
    echo.textContent='已提交：'+selVal.textContent;
    toast('表单已提交');
  });

  /* 铁律 1 */
  var c1=0;
  document.getElementById('twoT').addEventListener('click',function(e){
    e.stopPropagation(); two.toggle();
    c1++; document.getElementById('r1c').textContent='点击 '+c1+' 次';
  });
  document.querySelectorAll('#twoM button').forEach(function(b){
    b.addEventListener('click',function(e){
      e.stopPropagation();
      document.getElementById('twoV').textContent=b.dataset.v;
      document.getElementById('twoV').classList.remove('ph');
      c1++; document.getElementById('r1c').textContent='点击 '+c1+' 次';
      two.close();
    });
  });
  var sw=document.getElementById('twoSwitch'), c1b=0;
  function flip(){ sw.setAttribute('aria-checked', sw.getAttribute('aria-checked')==='true'?'false':'true');
    c1b++; document.getElementById('r1d').textContent='点击 '+c1b+' 次'; }
  sw.addEventListener('click',flip); sw.addEventListener('keydown',function(e){ if(e.key===' '||e.key==='Enter'){e.preventDefault();flip();} });

  /* 铁律 2 */
  document.getElementById('fourT').addEventListener('click',function(e){ e.stopPropagation(); four.toggle(); });
  document.querySelectorAll('#fourM button').forEach(function(b){
    b.addEventListener('click',function(e){
      e.stopPropagation(); document.getElementById('fourV').textContent=b.dataset.v;
      document.getElementById('fourV').classList.remove('ph'); four.close();
    });
  });
  document.querySelectorAll('#fourSeg button').forEach(function(b){
    b.addEventListener('click',function(){
      document.querySelectorAll('#fourSeg button').forEach(function(x){ x.setAttribute('aria-selected',String(x===b)); });
    });
  });

  document.addEventListener('click',function(){ dd.close(); sel.close(); two.close(); four.close(); });

  /* 铁律 3 */
  var cities=['北京','上海','广州','深圳','杭州','成都','重庆','武汉','西安','南京','苏州','天津','长沙','郑州','青岛','宁波','东莞','无锡','佛山','合肥','昆明','沈阳','大连','厦门','福州','哈尔滨','济南','温州','石家庄','南宁','常州','泉州','南昌','贵阳','太原','珠海'];
  var list=document.getElementById('cityList'), input=document.getElementById('citySearch'), meta=document.getElementById('listMeta');
  function render(kw){
    var data=cities.filter(function(c){ return kw? c.indexOf(kw)!==-1 : true; });
    list.innerHTML='';
    if(!data.length){ list.innerHTML='<div style="padding:20px;text-align:center;font-size:12.5px;color:var(--ink-3)">没有匹配的城市</div>'; }
    data.forEach(function(c){
      var b=document.createElement('button'); b.textContent=c;
      b.addEventListener('click',function(){
        list.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-selected','false'); });
        b.setAttribute('aria-selected','true'); toast('已选：'+c);
      });
      list.appendChild(b);
    });
    meta.textContent=data.length+' 项';
  }
  input.addEventListener('input',function(){ render(input.value.trim()); });
  render('');
})();
""",
    notes=[
        "<b>判定一句话</b>：Select 是拿来选的，Dropdown 是一堆命令的集合。",
        "<b>Dropdown</b> 属于导航 / 操作，触发器无边框，点了就执行，不需要回显。",
        "<b>Select</b> 属于数据录入，必须有带边框的输入框、占位符、回显、清除和校验。",
        "<b>铁律一</b>：只有 2 个选项，用开关或单选，别做下拉。",
        "<b>铁律二</b>：少于 5 个选项，直接平铺在主界面。",
        "<b>铁律三</b>：超过 10 个选项，限高（如 264px）并给搜索；出生日期这种熟悉数据直接输入。",
    ],
)

P06 = dict(
    no="06", short="热区与误触", title="为什么你总是点不中那个按钮",
    bvid="BV139xT66Eyj", dur="02:26", date="2026-10-27",
    kicker="Bilibili · KD一对A · 触控体验 · 热区",
    lede="图标画得多精致，热区就跟着缩多小——这是最容易翻车的地方。这一页让你用鼠标亲手体验一次「点不中」，再看三招怎么救。",
    tag1="热区 / Fitts", tag2="误触 / 触感反馈",
    quote="「视觉 16，热区从 40 起、最小 28；两个热区之间必须留缝，可滑动区旁边留 20dp。」",
    demos="""
  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 01</span>
      <div><h2>命中测试：同样 16px 的图标，热区差一倍</h2>
      <p>两边各点 8 个点，看你能漏多少次。可以打开「显示热区」看清楚差别。</p></div>
    </div>
    <div class="split">
      <div class="pane bad">
        <div class="pane-h"><span class="tag no">✕ 热区 = 图标大小</span><span class="count" id="hitA">命中 0 / 0</span></div>
        <div class="stage" style="align-items:stretch">
          <div class="grid8 small" id="gridA"></div>
        </div>
        <p class="note" id="noteA">鼠标稍微抖一下就打空——手指只会更糟。</p>
      </div>
      <div class="pane good">
        <div class="pane-h"><span class="tag ok">✓ 热区 44px</span><span class="count" id="hitB">命中 0 / 0</span></div>
        <div class="stage" style="align-items:stretch">
          <div class="grid8 big" id="gridB"></div>
        </div>
        <p class="note" id="noteB">图标还是 16px，但可点区域扩大到 44px，几乎不会失手。</p>
      </div>
    </div>
    <div class="row" style="margin-top:12px">
      <label class="switch" id="showArea" role="switch" aria-checked="true"><span class="track"><span class="knob"></span></span>显示热区</label>
      <button class="btn sm ghost" id="resetHit">重来</button>
    </div>
  </section>

  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 02</span>
      <div><h2>两个热区挨在一起，等于开了一个隧道</h2>
      <p>两边都想点「编辑」，看误触发生在哪里。</p></div>
    </div>
    <div class="split">
      <div class="pane bad">
        <div class="pane-h"><span class="tag no">✕ 热区紧贴</span><span class="count" id="gapA">误触 0 次</span></div>
        <div class="stage">
          <div class="btnpair tight">
            <button data-b="编辑">编辑</button><button data-b="删除" class="del">删除</button>
          </div>
        </div>
        <p class="note">两片可点区域直接相接，手指落在缝上就会被判给错误的那一个。</p>
      </div>
      <div class="pane good">
        <div class="pane-h"><span class="tag ok">✓ 中间留 8px 缝</span><span class="count" id="gapB">误触 0 次</span></div>
        <div class="stage">
          <div class="btnpair loose">
            <button data-b="编辑">编辑</button><button data-b="删除" class="del">删除</button>
          </div>
        </div>
        <p class="note">缝里点到就什么都不会发生，比点错安全得多。</p>
      </div>
    </div>
  </section>

  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 03</span>
      <div><h2>滑动区会偷走点击</h2>
      <p>在卡片上按住横拖。左边的「收藏」会被滑动手势误触发，右边加了位移阈值。</p></div>
    </div>
    <div class="split">
      <div class="pane bad">
        <div class="pane-h"><span class="tag no">✕ 不判断位移</span><span class="count" id="swipeA">误收藏 0 次</span></div>
        <div class="stage" style="overflow:hidden">
          <div class="strip" id="stripA">
            <div class="scard"><b>旅行灵感</b><span>12 张图</span><button class="fav" data-fav="A">♡ 收藏</button></div>
            <div class="scard"><b>周末露营</b><span>8 张图</span><button class="fav" data-fav="A">♡ 收藏</button></div>
          </div>
        </div>
        <p class="note">手指从按钮上起势去滑，松手时 click 照样会来一下。</p>
      </div>
      <div class="pane good">
        <div class="pane-h"><span class="tag ok">✓ 位移 &gt; 8px 就取消</span><span class="count" id="swipeB">误收藏 0 次</span></div>
        <div class="stage" style="overflow:hidden">
          <div class="strip" id="stripB">
            <div class="scard"><b>旅行灵感</b><span>12 张图</span><button class="fav" data-fav="B">♡ 收藏</button></div>
            <div class="scard"><b>周末露营</b><span>8 张图</span><button class="fav" data-fav="B">♡ 收藏</button></div>
          </div>
        </div>
        <p class="note">只有「按下 → 松开」几乎没移动时才算一次点击，滑动就纯粹是滑动。</p>
      </div>
    </div>
  </section>

  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 04</span>
      <div><h2>看不见的反馈：让手指知道「点到了」</h2>
      <p>手指盖住按钮时，视觉反馈是看不见的，只能靠触感。</p></div>
    </div>
    <div class="pane">
      <div class="stage" style="align-items:center">
        <button class="hapticbtn" id="hapBtn">点我试试（支持时会有震动）</button>
        <p class="count" id="hapText">视觉脉冲 + navigator.vibrate(12)</p>
      </div>
      <p class="note">iOS 用 Taptic Engine，安卓用 vibrate；只给 10~15ms，别做成嗡嗡长震。</p>
    </div>
  </section>
""",
    extra_css="""
.grid8{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;width:100%}
.hit{position:relative;display:grid;place-items:center;border-radius:10px;min-height:54px;cursor:crosshair;
  transition:background .18s var(--ease)}
.hit .ico{width:16px;height:16px;border-radius:4px;background:var(--ink-3);display:block;position:relative;z-index:2}
.small .hit{background:transparent}
.big .hit{background:transparent}
.stage.showzone .small .hit::before{content:"";position:absolute;width:24px;height:24px;border-radius:7px;
  background:var(--red-2);box-shadow:inset 0 0 0 1px var(--red-3)}
.stage.showzone .big .hit::before{content:"";position:absolute;width:44px;height:44px;border-radius:11px;
  background:var(--teal-2);box-shadow:inset 0 0 0 1px var(--teal-3)}
.hit.miss{background:var(--red-2)}
.hit.hitmark{background:var(--teal-2)}
.btnpair{display:flex;border-radius:11px;overflow:hidden}
.btnpair button{flex:1;padding:12px;font-size:13px;background:var(--card);color:var(--ink)}
.btnpair button.del{color:var(--red)}
.btnpair.tight button+button{border-left:0}
.btnpair.loose{gap:8px}
.btnpair.loose button{border-radius:10px;box-shadow:inset 0 0 0 1px var(--line-2)}
.btnpair.tight button{box-shadow:inset 0 0 0 1px var(--line-2)}
.strip{display:flex;gap:10px;overflow-x:auto;padding-bottom:6px;scrollbar-width:thin}
.scard{flex:0 0 150px;background:var(--card);border-radius:12px;padding:12px;box-shadow:inset 0 0 0 1px var(--line);
  display:flex;flex-direction:column;gap:6px;font-size:12px;color:var(--ink-3)}
.scard b{font-size:13px;color:var(--ink)}
.fav{align-self:flex-start;font-size:12px;padding:5px 9px;border-radius:8px;background:var(--card-2);color:var(--ink-2)}
.fav.on{background:var(--red-2);color:var(--red)}
.hapticbtn{padding:14px 22px;border-radius:14px;background:var(--teal);color:#fff;font-size:13.5px;
  box-shadow:0 8px 22px var(--teal-2);transition:transform .12s var(--ease)}
[data-theme="dark"] .hapticbtn{color:#06211d}
.hapticbtn.pulse{animation:pulse .32s var(--spring)}
@keyframes pulse{0%{transform:scale(1)}45%{transform:scale(.94)}100%{transform:scale(1)}}
""",
    js="""
(function(){
  /* 01 命中测试 */
  function build(id, small){
    var g=document.getElementById(id);
    for(var i=0;i<8;i++){
      var d=document.createElement('div'); d.className='hit';
      d.innerHTML='<span class="ico"></span>';
      if(small){ d.style.cursor='crosshair'; }
      g.appendChild(d);
    }
  }
  build('gridA',true); build('gridB',false);
  var stat={A:{hit:0,total:0},B:{hit:0,total:0}};
  function render(){
    document.getElementById('hitA').textContent='命中 '+stat.A.hit+' / '+stat.A.total;
    document.getElementById('hitB').textContent='命中 '+stat.B.hit+' / '+stat.B.total;
    document.getElementById('noteA').textContent = stat.A.total? ('24px 热区：'+(stat.A.total-stat.A.hit)+' 次打空，手指只会更糟。') : '鼠标稍微抖一下就打空——手指只会更糟。';
    document.getElementById('noteB').textContent = stat.B.total? ('44px 热区：'+(stat.B.total-stat.B.hit)+' 次打空。') : '图标还是 16px，但可点区域扩大到 44px。';
  }
  function bindGrid(id,key){
    var g=document.getElementById(id);
    g.addEventListener('click',function(e){
      var hitEl=e.target.closest('.hit');
      stat[key].total++;
      if(hitEl){ stat[key].hit++; hitEl.classList.add('hitmark'); setTimeout(function(){hitEl.classList.remove('hitmark');},260); }
      else { var stage=g.closest('.stage'); stage.classList.add('flash');
        setTimeout(function(){stage.classList.remove('flash');},260); }
      render();
    });
    g.addEventListener('mousedown',function(e){ /* 记录一次「尝试」*/ });
  }
  bindGrid('gridA','A'); bindGrid('gridB','B');
  var show=document.getElementById('showArea');
  function syncZone(){
    document.querySelectorAll('.stage').forEach(function(s){});
    var on=show.getAttribute('aria-checked')==='true';
    document.getElementById('gridA').closest('.stage').classList.toggle('showzone',on);
    document.getElementById('gridB').closest('.stage').classList.toggle('showzone',on);
  }
  show.addEventListener('click',function(){ show.setAttribute('aria-checked', show.getAttribute('aria-checked')==='true'?'false':'true'); syncZone(); });
  syncZone();
  document.getElementById('resetHit').addEventListener('click',function(){
    stat={A:{hit:0,total:0},B:{hit:0,total:0}}; render();
  });
  render();

  /* 02 相邻热区 */
  var gapA=0, gapB=0;
  document.querySelectorAll('#gapA')&&null;
  document.querySelectorAll('.btnpair.tight button').forEach(function(b){
    b.addEventListener('click',function(){
      if(b.dataset.b==='删除'){ gapA++; document.getElementById('gapA').textContent='误触 '+gapA+' 次'; toast('点到了「删除」——差一点就出事了'); }
      else toast('编辑');
    });
  });
  document.querySelectorAll('.btnpair.loose button').forEach(function(b){
    b.addEventListener('click',function(){
      if(b.dataset.b==='删除'){ gapB++; document.getElementById('gapB').textContent='误触 '+gapB+' 次'; toast('点到了「删除」'); }
      else toast('编辑');
    });
  });

  /* 03 滑动偷点击 */
  function bindStrip(id,key){
    var strip=document.getElementById(id), moved=false, sx=0;
    strip.addEventListener('mousedown',function(e){ moved=false; sx=e.clientX; });
    strip.addEventListener('mousemove',function(e){ if(Math.abs(e.clientX-sx)>8) moved=true; });
    strip.addEventListener('click',function(e){
      var fav=e.target.closest('.fav'); if(!fav) return;
      if(key==='B' && moved){ e.stopPropagation(); return; }
      fav.classList.toggle('on');
      if(key==='A' && moved){
        document.getElementById('swipeA').textContent='误收藏 '+((parseInt(document.getElementById('swipeA').textContent.replace(/\\D/g,''))||0)+1)+' 次';
        toast('滑动结束时误触了收藏');
      }
    },true);
  }
  bindStrip('stripA','A'); bindStrip('stripB','B');

  /* 04 触感 */
  var hb=document.getElementById('hapBtn');
  hb.addEventListener('click',function(){
    hb.classList.remove('pulse'); void hb.offsetWidth; hb.classList.add('pulse');
    if(navigator.vibrate){ navigator.vibrate(12); document.getElementById('hapText').textContent='已触发震动 12ms（你的设备支持）'; }
    else { document.getElementById('hapText').textContent='你的浏览器不支持震动，仅看视觉脉冲'; }
    toast('点到啦');
  });
})();
""",
    notes=[
        "<b>视觉 16，热区 40 起</b>：图标可以画得很小，可点区域至少要 40px，底线 28px。",
        "<b>热区之间留缝</b>：两片可点区域紧贴，等于给误触开了一条隧道。",
        "<b>滑动区旁边留 20dp</b>：别让横滑手势偷走点击，用位移阈值判断是滑还是点。",
        "<b>手指会挡住画面</b>：看不见视觉反馈时，靠 10~15ms 的触感告诉用户「点到了」。",
        "<b>Fitts 定律</b>：目标越大、距离越近，命中越快；把高频操作放在拇指自然落点。",
    ],
)
