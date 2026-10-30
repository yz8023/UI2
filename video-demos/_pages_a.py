# -*- coding: utf-8 -*-
"""页面 01、02：浮层基础 / 6 种高级浮层"""

P01 = dict(
    no="01", short="弹窗选型", title="别把所有弹出来的东西都叫「弹窗」",
    bvid="BV1hgnb6DEpQ", dur="01:57", date="2026-10-23",
    kicker="Bilibili · KD一对A · 浮层与反馈 · 上篇",
    lede="新手最容易犯的错，是把 Toast、Drawer、Modal、Page 统统叫「弹窗」。结果做出来的东西要么打断用户，要么装不下信息。这一页把「同一件事该用哪个壳」变成可以点着讲的东西。",
    tag1="浮层 / 弹窗", tag2="选型 / 三条铁律",
    quote="「先把容器叫对，再谈交互。弹窗 vs 抽屉 vs 页面，其实是在回答一个问题：<b>这件事需要打断用户到什么程度。</b>」",
    demos="""
  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 01</span>
      <div><h2>同一件事，三种承载</h2>
      <p>切换场景，看看「模态弹窗 / 侧边抽屉 / 独立页面」分别把用户逼到了什么程度。</p></div>
    </div>
    <div class="pane">
      <div class="pane-h">
        <div class="seg" id="ovSeg">
          <button data-scene="a" aria-selected="true">确认删除一条评论</button>
          <button data-scene="b">编辑商品详情</button>
          <button data-scene="c">要被分享的商品页</button>
        </div>
        <span class="count" id="ovVerdict">推荐：弹窗</span>
      </div>
      <div class="stage tall">
        <div class="mockapp" id="ovApp">
          <div class="mocklist">
            <div class="mockrow"><span class="av"></span><span class="ln w60"></span></div>
            <div class="mockrow"><span class="av"></span><span class="ln w80"></span></div>
            <div class="mockrow"><span class="av"></span><span class="ln w45"></span></div>
          </div>
          <div class="ovlayer" id="ovLayer"></div>
        </div>
      </div>
      <div class="row" style="margin-top:12px">
        <button class="btn sm" id="ovOpen">打开当前承载</button>
        <button class="btn sm ghost" id="ovReset">关闭</button>
        <span class="note" style="margin:0" id="ovNote">确认类操作只需要一次干扰，用模态弹窗。</span>
      </div>
    </div>
  </section>

  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 02</span>
      <div><h2>反馈四件套：什么时候打断，什么时候别打扰</h2>
      <p>四个按钮，四种反馈。点一下，看它出现的位置、能不能撤销、会不会自己消失。</p></div>
    </div>
    <div class="fbgrid">
      <div class="pane">
        <div class="pane-h"><span class="tag">Toast 轻提示</span><span class="count">不打断</span></div>
        <div class="stage">
          <button class="btn sm" data-fb="toast">保存草稿</button>
          <div class="mini" id="fbToast" hidden>草稿已保存</div>
        </div>
        <p class="note">2 秒自动消失，<b>不能撤销</b>；只用于「已经成功、你不需要做任何事」。</p>
      </div>
      <div class="pane">
        <div class="pane-h"><span class="tag v">Snackbar + 撤销</span><span class="count">可撤销</span></div>
        <div class="stage">
          <button class="btn sm" data-fb="snack">删除这条评论</button>
          <div class="mini bar" id="fbSnack" hidden><span>已删除 1 条评论</span><button data-fb="undo">撤销</button></div>
        </div>
        <p class="note">删除类操作用<b>可撤销</b>替代确认弹窗，少一次「是否删除」的对话。</p>
      </div>
      <div class="pane">
        <div class="pane-h"><span class="tag w">Inline 内联</span><span class="count">常驻</span></div>
        <div class="stage">
          <input class="field" id="fbInput" placeholder="手机号，试试留空直接提交">
          <button class="btn sm" data-fb="inline">提交</button>
          <div class="mini err" id="fbErr" hidden>请填写手机号，否则无法接收验证码</div>
        </div>
        <p class="note">错误必须<b>一直挂在出问题的地方</b>，不能像 Toast 一样几秒后消失。</p>
      </div>
      <div class="pane">
        <div class="pane-h"><span class="tag no">AlertDialog</span><span class="count">强打断</span></div>
        <div class="stage">
          <button class="btn sm danger" data-fb="alert">删除整个项目</button>
          <span class="mini" style="background:transparent;box-shadow:none;color:var(--ink-3)" id="fbAlertHint">点遮罩和 Esc 都关不掉</span>
        </div>
        <p class="note">不可逆、代价高的操作才配用<b>点不掉</b>的对话框，逼用户明确选择。</p>
      </div>
    </div>
  </section>

  <section class="demo">
    <div class="demo-head"><span class="dnum">铁律</span>
      <div><h2>三条避坑清单</h2><p>可以直接抄进评审 checklist。</p></div>
    </div>
    <div class="rules3">
      <div class="rulecard"><span class="tag ok">01</span><p><b>能用页面就别用弹窗。</b>内容需要滚动、需要被分享、需要浏览器后退键兜底的，做成页面。</p></div>
      <div class="rulecard"><span class="tag ok">02</span><p><b>能撤销就别确认。</b>删除先执行、给 5 秒撤销，比先弹「确定删除吗」更顺。</p></div>
      <div class="rulecard"><span class="tag ok">03</span><p><b>错误留在现场。</b>表单校验用内联红字，别用飘走就忘的 Toast。</p></div>
    </div>
  </section>
""",
    extra_css="""
.mockapp{position:relative;background:var(--card);border-radius:12px;padding:14px;min-height:206px;overflow:hidden;
  box-shadow:inset 0 0 0 1px var(--line)}
.mocklist{display:grid;gap:12px;transition:filter .3s var(--ease),opacity .3s var(--ease)}
.mockrow{display:flex;align-items:center;gap:10px}
.mockrow .av{width:26px;height:26px;border-radius:50%;background:var(--card-3);flex:0 0 auto}
.mockrow .ln{height:9px;border-radius:99px;background:var(--card-3);display:block}
.w45{width:45%}.w60{width:60%}.w80{width:80%}
.mockapp.dim .mocklist{filter:blur(2px);opacity:.45}
.ovlayer{position:absolute;inset:0;display:none;align-items:center;justify-content:center;padding:14px}
.ovlayer.on{display:flex}
.ovlayer::before{content:"";position:absolute;inset:0;background:rgba(20,20,18,.28);opacity:0;transition:opacity .3s var(--ease)}
.ovlayer.on::before{opacity:1}
[data-theme="dark"] .ovlayer::before{background:rgba(0,0,0,.5)}
.ovbody{position:relative;background:var(--card);border-radius:14px;box-shadow:var(--sh2);padding:16px;z-index:2;
  animation:popIn .3s var(--ease)}
@keyframes popIn{from{opacity:0;transform:translateY(8px) scale(.97)}to{opacity:1;transform:none}}
.ovbody h4{font-size:14px}
.ovbody p{font-size:12.5px;color:var(--ink-3);margin-top:5px}
.ovbody .row{margin-top:13px;justify-content:flex-end}
.modalbox{width:min(340px,100%)}
.drawerbox{position:absolute;right:0;top:0;bottom:0;width:min(74%,300px);border-radius:0;
  animation:slideIn .34s var(--ease);display:flex;flex-direction:column}
@keyframes slideIn{from{transform:translateX(100%)}to{transform:none}}
.drawerbox .lines{display:grid;gap:8px;margin-top:14px}
.drawerbox .lines i{height:9px;border-radius:99px;background:var(--card-3);display:block}
.pagebox{position:absolute;inset:0;border-radius:0;animation:pageIn .3s var(--ease);display:flex;flex-direction:column;gap:10px}
@keyframes pageIn{from{opacity:0;transform:scale(1.02)}to{opacity:1;transform:none}}
.pagebox .bar{display:flex;align-items:center;gap:8px;font-size:12px;color:var(--ink-3)}
.pagebox .block{height:44px;border-radius:10px;background:var(--card-2)}
.pagebox .block.tall2{height:76px}
.fbgrid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.fbgrid .stage{min-height:132px;gap:10px;align-items:flex-start}
.mini{font-size:12px;padding:8px 11px;border-radius:9px;background:var(--ink);color:var(--bg);
  animation:popIn .25s var(--ease)}
.mini.bar{display:flex;align-items:center;gap:10px;width:100%;justify-content:space-between}
.mini.bar button{color:var(--teal);font-weight:600;font-size:12px}
[data-theme="dark"] .mini{background:var(--card-3);color:var(--ink)}
.mini.err{background:var(--red-2);color:var(--red);box-shadow:inset 0 0 0 1px var(--red-3)}
.rules3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.rulecard{background:var(--card);border-radius:var(--r2);padding:16px;box-shadow:var(--sh);font-size:13px;color:var(--ink-2);line-height:1.7}
.rulecard p{margin-top:9px}
.rulecard b{color:var(--ink);font-weight:600}
@media (max-width:880px){.fbgrid,.rules3{grid-template-columns:1fr}}
""",
    js="""
(function(){
  var scenes={
    a:{type:'modal',verdict:'推荐：弹出式对话框（Modal）',note:'确认类操作只需要一次干扰，用模态弹窗。',
       html:'<div class="ovbody modalbox"><h4>删除这条评论？</h4><p>删除后不可恢复，也不会通知作者。</p><div class="row"><button class="btn sm">取消</button><button class="btn sm danger">删除</button></div></div>'},
    b:{type:'drawer',verdict:'推荐：侧边抽屉（Drawer）',note:'内容多但要保留列表上下文，用抽屉，用户随时能回头对照。',
       html:'<div class="ovbody drawerbox"><h4>编辑商品详情</h4><p>12 个字段 · 需要对照列表修改</p><div class="lines"><i style="width:90%"></i><i style="width:70%"></i><i style="width:82%"></i><i style="width:55%"></i></div><div class="row" style="margin-top:auto"><button class="btn sm">取消</button><button class="btn sm primary">保存</button></div></div>'},
    c:{type:'page',verdict:'推荐：独立页面（Page）',note:'需要分享、收藏、刷新后还在的，必须是页面——弹窗没有 URL。',
       html:'<div class="ovbody pagebox"><div class="bar"><span>←</span><span>商品详情</span></div><div class="block tall2"></div><div class="block"></div><div class="block" style="width:60%"></div></div>'}
  };
  var cur='a', app=document.getElementById('ovApp'), layer=document.getElementById('ovLayer');
  var verdict=document.getElementById('ovVerdict'), note=document.getElementById('ovNote');
  function open(){
    var s=scenes[cur];
    layer.innerHTML=s.html; layer.classList.add('on'); app.classList.add('dim');
    verdict.textContent=s.verdict; note.textContent=s.note;
  }
  function close(){ layer.classList.remove('on'); app.classList.remove('dim'); layer.innerHTML=''; }
  document.getElementById('ovOpen').addEventListener('click',open);
  document.getElementById('ovReset').addEventListener('click',close);
  layer.addEventListener('click',function(e){
    if(e.target.closest('.ovbody')) return;
    if(cur==='a'){ toast('模态弹窗：点遮罩通常可以关闭'); close(); }
    else if(cur==='b'){ close(); }
    else { toast('页面不会被遮罩关掉，只能返回'); }
  });
  document.querySelectorAll('#ovSeg button').forEach(function(b){
    b.addEventListener('click',function(){
      document.querySelectorAll('#ovSeg button').forEach(function(x){x.setAttribute('aria-selected',String(x===b));});
      cur=b.dataset.scene; close(); open();
    });
  });

  /* 反馈四件套 */
  var tEl=document.getElementById('fbToast'), sEl=document.getElementById('fbSnack');
  var eEl=document.getElementById('fbErr'), iEl=document.getElementById('fbInput');
  document.querySelectorAll('[data-fb]').forEach(function(b){
    b.addEventListener('click',function(){
      var k=b.dataset.fb;
      if(k==='toast'){ tEl.hidden=false; clearTimeout(tEl._t); tEl._t=setTimeout(function(){tEl.hidden=true;},2000); }
      if(k==='snack'){ sEl.hidden=false; sEl.querySelector('span').textContent='已删除 1 条评论'; clearTimeout(sEl._t);
        sEl._t=setTimeout(function(){sEl.hidden=true;},5000); }
      if(k==='undo'){ sEl.querySelector('span').textContent='已恢复这条评论'; clearTimeout(sEl._t);
        sEl._t=setTimeout(function(){sEl.hidden=true;},1500); toast('撤销成功'); }
      if(k==='inline'){
        if(!iEl.value.trim()){ eEl.hidden=false; iEl.style.boxShadow='inset 0 0 0 1.5px var(--red)'; toast('校验失败：错误停在现场'); }
        else { eEl.hidden=true; iEl.style.boxShadow=''; toast('提交成功'); }
      }
      if(k==='alert'){ toast('AlertDialog：遮罩和 Esc 都关不掉，只能选一个'); }
    });
  });
})();
""",
    notes=[
        "<b>先分容器再谈样式</b>：Toast / Snackbar / Inline / AlertDialog / Modal / Drawer / Page，打断程度依次升高。",
        "<b>弹窗只解决一句话的事</b>：确认、警示、极短表单；超过 3 个字段就该考虑抽屉或页面。",
        "<b>抽屉保留上下文</b>：适合「一边看列表一边改」；关掉后用户还站在原地。",
        "<b>页面才是可以被引用的东西</b>：有 URL、能分享、能后退、能刷新不丢。",
        "<b>删除优先做撤销</b>：Snackbar + Undo 替代二次确认，流程更短也更安全。",
        "<b>错误必须留在现场</b>：Inline Alert 常驻，不能自动消失。",
    ],
)

P02 = dict(
    no="02", short="6 种高级浮层", title="别只知道 Modal：6 种高级浮层",
    bvid="BV1Qunb6HEEW", dur="02:46", date="2026-10-24",
    kicker="Bilibili · KD一对A · 浮层与反馈 · 下篇",
    lede="上篇讲清楚「弹窗 / 抽屉 / 页面」，这一篇解决评论区最常问的四个灵魂拷问：半屏评论算什么、删除为什么不再确认、什么对话框必须关不掉、红色错误为什么不能自动消失。",
    tag1="Bottom Sheet", tag2="撤销 / 不可关闭",
    quote="「大厂越来越不喜欢弹『确认删除』，是因为<b>撤销比阻止更高效</b>；而真正不可逆的操作，才配得上一个关不掉的对话框。」",
    demos="""
  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 01</span>
      <div><h2>Bottom Sheet 的三档屏高：30% / 60% / 80%</h2>
      <p>抖音半屏评论、地图路线卡片都属于它。拖动或点档位，看它如何分三档停靠。</p></div>
    </div>
    <div class="split">
      <div class="pane">
        <div class="pane-h"><span class="tag v">Bottom Sheet</span><span class="count" id="bsNow">60%</span></div>
        <div class="stage tall" style="padding:0;overflow:hidden">
          <div class="phone">
            <div class="phone-map"><span>地图 / 视频画面</span></div>
            <div class="bsheet" id="bsheet">
              <div class="grab" id="bgrab"></div>
              <div class="bshead"><b>评论 1,204</b><span>按热度</span></div>
              <div class="bsbody"><i></i><i style="width:82%"></i><i style="width:64%"></i><i style="width:76%"></i></div>
            </div>
          </div>
        </div>
        <div class="row" style="margin-top:12px">
          <div class="seg" id="bsSeg">
            <button data-h="30">30%</button><button data-h="60" aria-selected="true">60%</button><button data-h="80">80%</button>
          </div>
          <span class="note" style="margin:0">拖动手柄也可以换档</span>
        </div>
      </div>
      <div class="pane">
        <div class="pane-h"><span class="tag">它和 Drawer 有什么不同</span></div>
        <div class="stage" style="min-height:230px;justify-content:flex-start;gap:14px">
          <div class="cmprow"><span class="tag v">Bottom Sheet</span><p>从底部升起，覆盖下半屏，<b>手指天然够得到</b>；关闭时下沉，画面不被切断。</p></div>
          <div class="cmprow"><span class="tag">Drawer</span><p>从侧边滑出，通常整屏高，适合<b>导航和筛选</b>；在手机上单手够不到右上角的关闭。</p></div>
          <div class="cmprow"><span class="tag w">三档的意义</span><p>30% 只露标题（继续看内容）、60% 半屏（边看边聊）、80% 专注（沉浸输入）。</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 02</span>
      <div><h2>删除：先确认，还是先执行再给撤销？</h2>
      <p>两边各删一次，数一数你点了几下、有没有被打断。</p></div>
    </div>
    <div class="split">
      <div class="pane bad">
        <div class="pane-h"><span class="tag no">✕ 二次确认</span><span class="count" id="cDelCount">点击 0 次</span></div>
        <div class="stage">
          <div class="delrow" id="delRowA"><span class="dot"></span><div><b>「周末露营清单」</b><small>3 个协作者</small></div><button class="btn sm danger" id="delBtnA">删除</button></div>
          <div class="cfm" id="cfmA" hidden><p>确定删除？此操作不可恢复。</p><div class="row"><button class="btn sm" data-c="cancel">取消</button><button class="btn sm danger" data-c="ok">确定</button></div></div>
        </div>
        <p class="note" id="noteA">用户被拦下来，多一次对话；点「取消」什么都没发生。</p>
      </div>
      <div class="pane good">
        <div class="pane-h"><span class="tag ok">✓ 直接执行 + 撤销</span><span class="count" id="cDelCountB">点击 0 次</span></div>
        <div class="stage">
          <div class="delrow" id="delRowB"><span class="dot"></span><div><b>「周末露营清单」</b><small>3 个协作者</small></div><button class="btn sm danger" id="delBtnB">删除</button></div>
          <div class="snack" id="snackB" hidden><span>已删除「周末露营清单」</span><button id="undoB">撤销</button><i class="prog"></i></div>
        </div>
        <p class="note" id="noteB">一次点击完成；后悔了在 5 秒内撤销，不用被打断。</p>
      </div>
    </div>
  </section>

  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 03</span>
      <div><h2>什么对话框必须关不掉？</h2>
      <p>两个对话框都试试：点遮罩、按 Esc。左：普通弹窗。右：不可逆扣费。</p></div>
    </div>
    <div class="split">
      <div class="pane">
        <div class="pane-h"><span class="tag">普通弹窗 · 可以关</span><span class="count">Dialog</span></div>
        <div class="stage">
          <button class="btn sm" id="d1open">打开</button>
          <div class="dlg" id="d1" hidden><div class="dlgmask"></div><div class="dlgbox"><h4>重命名文件</h4><input class="field" value="未命名文档"><div class="row"><button class="btn sm" data-close="1">取消</button><button class="btn sm primary">保存</button></div></div></div>
        </div>
        <p class="note">低风险编辑：点遮罩、按 Esc 都应该能退出，别拿它当牢房。</p>
      </div>
      <div class="pane bad">
        <div class="pane-h"><span class="tag no">AlertDialog · 关不掉</span><span class="count">不可逆</span></div>
        <div class="stage">
          <button class="btn sm danger" id="d2open">立即支付 ¥1,280</button>
          <div class="dlg" id="d2" hidden><div class="dlgmask"></div><div class="dlgbox"><h4>确认支付 ¥1,280？</h4><p>付款后不支持退款，也无法撤销。</p><div class="row"><button class="btn sm" data-close="2">我再想想</button><button class="btn sm danger" data-close="2">确认支付</button></div></div></div>
        </div>
        <p class="note">点遮罩 / Esc 都只提示不给走，必须明确选一个按钮。</p>
      </div>
    </div>
  </section>

  <section class="demo">
    <div class="demo-head"><span class="dnum">演示 04</span>
      <div><h2>红色的错误提示，为什么不能自动消失</h2>
      <p>两个表单都提交空手机号。左边错误留在原地，右边 3 秒后自己走了。</p></div>
    </div>
    <div class="split">
      <div class="pane good">
        <div class="pane-h"><span class="tag ok">Inline Alert · 常驻</span><span class="count">推荐</span></div>
        <div class="stage">
          <input class="field" id="e1" placeholder="手机号">
          <button class="btn sm primary" id="e1btn">提交</button>
          <div class="ierr" id="e1msg" hidden>请输入 11 位手机号</div>
        </div>
        <p class="note">用户修完字段错误才消失，视线不用来回找。</p>
      </div>
      <div class="pane bad">
        <div class="pane-h"><span class="tag no">Toast · 3 秒消失</span><span class="count" id="e2state">未提交</span></div>
        <div class="stage">
          <input class="field" id="e2" placeholder="手机号">
          <button class="btn sm danger" id="e2btn">提交</button>
          <div class="toastbox" id="e2msg" hidden>请输入 11 位手机号</div>
        </div>
        <p class="note">3 秒后消息没了，用户回来只看到一堆空字段，不知道错在哪。</p>
      </div>
    </div>
  </section>
""",
    extra_css="""
.phone{position:relative;width:100%;height:230px;border-radius:14px;overflow:hidden;background:var(--card);box-shadow:inset 0 0 0 1px var(--line)}
.phone-map{position:absolute;inset:0;display:grid;place-items:center;font-size:12px;color:var(--ink-3);
  background:repeating-linear-gradient(45deg,var(--card-2),var(--card-2) 11px,var(--card-3) 11px,var(--card-3) 22px)}
.bsheet{position:absolute;left:0;right:0;bottom:0;height:60%;background:var(--card);border-radius:16px 16px 0 0;
  box-shadow:0 -10px 30px rgba(0,0,0,.13);padding:10px 14px;transition:height .42s var(--ease);display:flex;flex-direction:column}
.grab{width:36px;height:4px;border-radius:99px;background:var(--line-2);margin:2px auto 10px;cursor:grab}
.bshead{display:flex;align-items:center;justify-content:space-between;font-size:12.5px;color:var(--ink-3)}
.bshead b{color:var(--ink);font-size:13px}
.bsbody{display:grid;gap:9px;margin-top:12px}
.bsbody i{height:9px;border-radius:99px;background:var(--card-2);display:block}
.cmprow{display:grid;gap:6px}
.cmprow p{font-size:12.5px;color:var(--ink-2);line-height:1.65}
.cmprow b{color:var(--ink)}
.delrow{display:flex;align-items:center;gap:11px;background:var(--card);border-radius:11px;padding:11px 13px;box-shadow:inset 0 0 0 1px var(--line);transition:opacity .3s var(--ease),transform .3s var(--ease)}
.delrow.gone{opacity:.32;text-decoration:line-through}
.delrow .dot{width:9px;height:9px;border-radius:50%;background:var(--violet);flex:0 0 auto}
.delrow div{flex:1;min-width:0}
.delrow b{font-size:13px;display:block}
.delrow small{font-size:11.5px;color:var(--ink-3)}
.cfm{background:var(--card);border-radius:11px;padding:12px;box-shadow:var(--sh2);animation:popIn .25s var(--ease)}
.cfm p{font-size:12.5px;color:var(--ink-2)}
.cfm .row{margin-top:10px;justify-content:flex-end}
.snack{position:relative;overflow:hidden;display:flex;align-items:center;gap:10px;justify-content:space-between;
  background:var(--ink);color:var(--bg);border-radius:11px;padding:10px 13px;font-size:12.5px;animation:popIn .25s var(--ease)}
[data-theme="dark"] .snack{background:var(--card-3);color:var(--ink)}
.snack button{color:var(--teal);font-weight:600}
.snack .prog{position:absolute;left:0;bottom:0;height:2px;background:var(--teal);width:100%;transform-origin:left;animation:drain 5s linear forwards}
@keyframes drain{to{transform:scaleX(0)}}
.dlg{position:absolute;inset:0;z-index:5;display:grid;place-items:center;padding:12px}
.dlgmask{position:absolute;inset:0;background:rgba(20,20,18,.3)}
[data-theme="dark"] .dlgmask{background:rgba(0,0,0,.55)}
.dlgbox{position:relative;width:min(300px,100%);background:var(--card);border-radius:13px;padding:14px;box-shadow:var(--sh2);animation:popIn .26s var(--ease)}
.dlgbox h4{font-size:13.5px}
.dlgbox p{font-size:12px;color:var(--ink-3);margin-top:4px}
.dlgbox .field{margin-top:10px}
.dlgbox .row{margin-top:11px;justify-content:flex-end}
.dlg.shake .dlgbox{animation:shake .4s var(--ease)}
@keyframes shake{10%,90%{transform:translateX(-2px)}30%,70%{transform:translateX(4px)}50%{transform:translateX(-5px)}}
.ierr{font-size:12px;color:var(--red);background:var(--red-2);border-radius:8px;padding:8px 10px;
  box-shadow:inset 0 0 0 1px var(--red-3);animation:popIn .2s var(--ease)}
.toastbox{font-size:12px;padding:8px 11px;border-radius:9px;background:var(--ink);color:var(--bg);animation:popIn .2s var(--ease)}
[data-theme="dark"] .toastbox{background:var(--card-3);color:var(--ink)}
@media (max-width:880px){.fbgrid{grid-template-columns:1fr}}
""",
    js="""
(function(){
  /* Bottom sheet */
  var sheet=document.getElementById('bsheet'), now=document.getElementById('bsNow');
  function setH(h){ sheet.style.height=h+'%'; now.textContent=h+'%';
    document.querySelectorAll('#bsSeg button').forEach(function(b){ b.setAttribute('aria-selected', String(b.dataset.h===String(h))); }); }
  document.querySelectorAll('#bsSeg button').forEach(function(b){ b.addEventListener('click',function(){ setH(b.dataset.h); }); });
  var dragging=false, startY=0, startH=0;
  var grab=document.getElementById('bgrab');
  function down(e){ dragging=true; startY=(e.touches?e.touches[0].clientY:e.clientY);
    startH=parseFloat(sheet.style.height)||60; e.preventDefault(); }
  function move(e){
    if(!dragging) return;
    var y=(e.touches?e.touches[0].clientY:e.clientY);
    var h=startH+(startY-y)/2.3;
    sheet.style.height=Math.max(18,Math.min(88,h))+'%';
  }
  function up(){
    if(!dragging) return; dragging=false;
    var h=parseFloat(sheet.style.height);
    var snap = h<45?30:(h<70?60:80);
    setH(snap);
  }
  grab.addEventListener('mousedown',down); window.addEventListener('mousemove',move); window.addEventListener('mouseup',up);
  grab.addEventListener('touchstart',down,{passive:false}); window.addEventListener('touchmove',move,{passive:false}); window.addEventListener('touchend',up);

  /* 删除：确认 vs 撤销 */
  var ca=0, cb=0;
  var countA=document.getElementById('cDelCount'), countB=document.getElementById('cDelCountB');
  var cfm=document.getElementById('cfmA'), rowA=document.getElementById('delRowA');
  document.getElementById('delBtnA').addEventListener('click',function(){ ca++; countA.textContent='点击 '+ca+' 次'; cfm.hidden=false; });
  cfm.addEventListener('click',function(e){
    var b=e.target.closest('[data-c]'); if(!b) return;
    ca++; countA.textContent='点击 '+ca+' 次';
    if(b.dataset.c==='ok'){ rowA.classList.add('gone'); document.getElementById('noteA').textContent='确认后删掉了，但用户为此点了 '+(ca)+' 次并被打断一次。'; }
    cfm.hidden=true;
  });
  var snack=document.getElementById('snackB'), rowB=document.getElementById('delRowB');
  document.getElementById('delBtnB').addEventListener('click',function(){
    cb++; countB.textContent='点击 '+cb+' 次';
    rowB.classList.add('gone'); snack.hidden=false;
    snack.querySelector('span').textContent='已删除「周末露营清单」';
    clearTimeout(snack._t);
    snack._t=setTimeout(function(){ snack.hidden=true; rowB.classList.remove('gone');
      document.getElementById('noteB').textContent='撤销窗口过期，删除正式生效——全程只有 '+(cb)+' 次打断。'; },5000);
  });
  document.getElementById('undoB').addEventListener('click',function(){
    cb++; countB.textContent='点击 '+cb+' 次'; snack.hidden=true; rowB.classList.remove('gone');
    document.getElementById('noteB').textContent='撤销成功，条目回来了；用户只在需要时才付出额外一次点击。';
  });

  /* AlertDialog */
  function bindDlg(id, closable){
    var el=document.getElementById(id);
    el.addEventListener('click',function(e){
      if(e.target.closest('[data-close]')){ el.hidden=true; toast('已作出选择'); return; }
      if(e.target.classList.contains('dlgmask') || e.target.classList.contains('dlg')){
        if(closable){ el.hidden=true; toast('点遮罩关闭了'); }
        else { el.classList.add('shake'); toast('这个对话框不接受点遮罩：请明确选择'); setTimeout(function(){el.classList.remove('shake');},450); }
      }
    });
  }
  document.getElementById('d1open').addEventListener('click',function(){ document.getElementById('d1').hidden=false; });
  document.getElementById('d2open').addEventListener('click',function(){ document.getElementById('d2').hidden=false; });
  bindDlg('d1',true); bindDlg('d2',false);
  document.addEventListener('keydown',function(e){
    if(e.key!=='Escape') return;
    var d1=document.getElementById('d1'), d2=document.getElementById('d2');
    if(!d1.hidden){ d1.hidden=true; toast('Esc 关闭了普通弹窗'); }
    if(!d2.hidden){ d2.classList.add('shake'); toast('Esc 关不掉：这是不可逆操作'); setTimeout(function(){d2.classList.remove('shake');},450); }
  });

  /* Inline vs Toast */
  var e1=document.getElementById('e1'), e1msg=document.getElementById('e1msg');
  document.getElementById('e1btn').addEventListener('click',function(){
    if(e1.value.replace(/\\s/g,'').length!==11){ e1msg.hidden=false; } else { e1msg.hidden=true; toast('提交成功'); }
  });
  var e2=document.getElementById('e2'), e2msg=document.getElementById('e2msg'), e2state=document.getElementById('e2state');
  document.getElementById('e2btn').addEventListener('click',function(){
    if(e2.value.replace(/\\s/g,'').length!==11){
      e2msg.hidden=false; e2state.textContent='已报错 3 秒后消失';
      clearTimeout(e2msg._t);
      e2msg._t=setTimeout(function(){ e2msg.hidden=true; e2state.textContent='提示已消失 · 错误仍存在'; toast('现在用户不知道哪里错了'); },3000);
    } else { e2msg.hidden=true; toast('提交成功'); }
  });
})();
""",
    notes=[
        "<b>Bottom Sheet 的三档屏高</b>：30% 露出标题、60% 边看边聊、80% 沉浸输入；拖拽要吸附到档位，不要停在一半。",
        "<b>它不等于 Drawer</b>：底部上升是指指可及，侧边滑出更适合导航与筛选。",
        "<b>删除先执行</b>：Snackbar + 撤销，比先弹「确定删除吗」少一次对话。",
        "<b>不可逆操作用 AlertDialog</b>：点遮罩、按 Esc 都不关闭，必须明确选择。",
        "<b>Inline Alert 不能自动消失</b>：它锚在出错的字段旁边，是「诊断书」，不是「通知」。",
        "<b>上篇 + 下篇</b>合起来覆盖主流组件库里 18 种浮层与反馈形态。",
    ],
)
