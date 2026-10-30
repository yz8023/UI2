# -*- coding: utf-8 -*-
"""素材库 App：交互逻辑（路由 / 搜索 / 详情 / 对比 / 设置 / 提示词）"""

APP_JS = r"""
(function(){
  var ITEMS = __DATA__;
  var byId = {};
  ITEMS.forEach(function(it){ byId[it.id] = it; });
  var M = window.__MINI || {};
  var CATS = [
    ['组件','基础组件','按钮 / 输入 / 开关 / 滑块 / 勾选 / 头像','F01–F06'],
    ['表单','表单输入','校验 / 步进 / 分段 / 搜索 / 上传 / 选择器','F07–F12'],
    ['导航','导航','标签栏 / 顶栏 / 抽屉 / 面包屑 / 标签页 / 侧边栏','F13–F18'],
    ['布局','布局','Bento / 分组列表 / 瀑布流 / 栅格 / 粘性堆叠 / 安全区','F19–F24'],
    ['反馈','反馈','Toast / 对话框 / 底部面板 / 骨架 / 空态 / 进度 / 加载按钮','F25–F31'],
    ['数据','数据展示','折线 / 柱状 / 环形 / 数据卡 / 表格 / 时间线','F32–F37'],
    ['动效','动效','弹簧拖拽 / 错峰 / 手势卡 / 转场 / 视差','F38–F42'],
    ['模板','应用模板','引导页 / 登录页 / 设置页 / 个人主页','F43–F46']
  ];
  var COLL_NAME = { lib:'完整素材库', video:'视频拆解', motion:'动效复刻', glass:'液态玻璃' };
  var COLL_TAG  = { lib:'f', video:'v', motion:'m', glass:'g' };

  /* 设置持久化（浏览器 localStorage / WebView 的 DomStorage 都能用） */
  var LS = {
    get:function(k, d){ try{ var v = localStorage.getItem('uikit.'+k); return v===null?d:JSON.parse(v); }catch(e){ return d; } },
    set:function(k, v){ try{ localStorage.setItem('uikit.'+k, JSON.stringify(v)); }catch(e){} }
  };
  var S = {
    view:'home', filter:'all', cat:'', q:'', more:'cmp', caseId:'m01',
    cmp: LS.get('cmp', ['m01','l01']),
    reqs:{},
    custom:{}
  };

  /* 恢复上次的主题 / 玻璃开关 / 减少动效 */
  (function restore(){
    var pal = LS.get('palette','aurora');
    if(pal) document.body.dataset.palette = pal;
    if(LS.get('glassOn', true) === false) document.body.classList.add('normal');
    if(LS.get('reduce', false)) document.body.classList.add('reduce');
  })();

  /* ---------------- mini 生命周期 ---------------- */
  var reg = new Map();
  var io = ('IntersectionObserver' in window) ? new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(e.isIntersecting){ mount(e.target, e.target.dataset.mini); }
      else { kill(e.target); }
    });
  }, {rootMargin:'160px 0px'}) : null;

  function mount(el, id){
    if(!el || reg.has(el) || !M[id]) return;
    var stop = null;
    try { stop = M[id](el); } catch(err) { console.warn('mini fail', id, err); }
    reg.set(el, typeof stop === 'function' ? stop : function(){});
  }
  function kill(el){
    var f = reg.get(el);
    if(f){ try { f(); } catch(e){} reg.delete(el); if(io) io.unobserve(el); }
  }
  function observe(root){
    var els = root.querySelectorAll('[data-mini]');
    for(var i=0;i<els.length;i++){
      if(io) io.observe(els[i]);
      else mount(els[i], els[i].dataset.mini);
    }
  }
  function killAll(){
    reg.forEach(function(f, el){ try { f(); } catch(e){} if(io) io.unobserve(el); });
    reg.clear();
  }

  /* ---------------- 通用 ---------------- */
  function esc(s){ return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
  var toastT;
  function toast(msg){
    var t = document.getElementById('toast');
    t.textContent = msg; t.classList.add('on');
    clearTimeout(toastT); toastT = setTimeout(function(){ t.classList.remove('on'); }, 2000);
  }
  function copyText(text, btn, doneLabel){
    /* 原生 WebView 壳里优先走 Android 剪贴板桥 */
    if(window.AndroidBridge && window.AndroidBridge.copy){
      try { window.AndroidBridge.copy(text); if(btn){
        var ob = btn.textContent;
        btn.classList.add('done'); btn.textContent = doneLabel || '已复制 ✓';
        setTimeout(function(){ btn.classList.remove('done'); btn.textContent = ob; }, 1700);
      } else { toast('已复制到剪贴板'); } return; } catch(e){}
    }
    function done(){
      if(!btn) return toast('已复制到剪贴板');
      var old = btn.textContent;
      btn.classList.add('done'); btn.textContent = doneLabel || '已复制 ✓';
      setTimeout(function(){ btn.classList.remove('done'); btn.textContent = old; }, 1700);
    }
    function fb(){
      var ta = document.createElement('textarea');
      ta.value = text; ta.style.cssText = 'position:fixed;opacity:0;top:0;left:0';
      document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy'); done(); } catch(e){ toast('请手动选择文本复制'); }
      document.body.removeChild(ta);
    }
    if(navigator.clipboard && navigator.clipboard.writeText){
      navigator.clipboard.writeText(text).then(done).catch(fb);
    } else { fb(); }
  }
  function promptFor(it){
    var picked = S.reqs[it.id] || [];
    var out = it.prompt.trim();
    if(picked.length) out += '\n\n【变更要求】\n' + picked.map(function(r){ return '- ' + r; }).join('\n');
    var c = (S.custom[it.id] || '').trim();
    if(c) out += '\n\n【自定义要求】\n' + c;
    return out;
  }

  /* ---------------- 卡片 ---------------- */
  function cardHTML(it, extraClass){
    return '<article class="card ' + (extraClass||'') + '" data-open="' + it.id + '">' +
      '<div class="mini' + (it.coll === 'lib' ? ' lib' : '') + '" data-mini="' + it.id + '" style="margin-top:0;background:#0a0f14"></div>' +
      '<div class="card-b">' +
        '<div class="card-t"><span class="num">' + it.id.toUpperCase() + '</span>' + esc(it.name) + '</div>' +
        '<div class="card-s">' + esc(it.use || it.title) + '</div>' +
        '<div class="tags"><span class="tag ' + COLL_TAG[it.coll] + '">' + COLL_NAME[it.coll] + '</span>' +
          '<span class="tag">' + esc(it.dur) + '</span><span class="tag">' + it.diff + '</span></div>' +
      '</div></article>';
  }

  /* ---------------- 首页 ---------------- */
  function homeHTML(){
    var pick = ['m01','l01','m06','v05'];
    var cnt = function(c){ return ITEMS.filter(function(x){ return x.coll === c; }).length; };
    var libN = cnt('lib');
    var head = '' +
      '<div class="hx-head">' +
        '<div class="hx-hi">素材 · 弹层 · 动效 · 结构</div>' +
        '<h1 class="hx-title">把界面拆成<em>能抄</em>的零件。</h1>' +
        '<p class="hx-sub">' + libN + ' 条完整素材、22 个交互拆解；XPopup 的 20 种弹窗与 45 个设置、' +
          'motion-web 的 20 条配方全部能点能拖。选一条，复制提示词，开工。</p>' +
      '</div>' +
      '<div class="hx-search" id="hxGoSearch">' +
        '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="6.5"/><path d="m16 16 4.5 4.5"/></svg>' +
        '<span>搜功能：弹窗 / 校验 / 图表 / 弹簧</span><i>' + ITEMS.length + ' 条 + 体验</i>' +
      '</div>';

    var grid = '' +
      '<div class="hx-grid">' +
        '<div class="hx-card wide" data-go="lib">' +
          '<div class="k"><svg viewBox="0 0 24 24"><rect x="4" y="4" width="6.6" height="6.6" rx="2"/>' +
          '<rect x="13.4" y="4" width="6.6" height="6.6" rx="2"/><rect x="4" y="13.4" width="6.6" height="6.6" rx="2"/>' +
          '<rect x="13.4" y="13.4" width="6.6" height="6.6" rx="2"/></svg><b>素材库</b></div>' +
          '<h3>按分类找，或直接搜功能</h3>' +
          '<p>组件 / 表单 / 导航 / 布局 / 反馈 / 数据 / 动效 / 模板，8 个分类各一页</p>' +
          '<div class="chips"><s>8 个分类</s><s>搜索直达</s><s>每张卡都能跑</s></div>' +
          '<div class="n">' + libN + '</div>' +
        '</div>' +
        '<div class="hx-card" data-go="exp" data-hall="xp">' +
          '<div class="k"><svg viewBox="0 0 24 24"><rect x="4" y="6" width="16" height="12" rx="3"/><path d="M4 13h16"/></svg><b>弹层</b></div>' +
          '<h3>XPopup 全家</h3><p>20 弹窗 · 20 动画 · 45 设置</p>' +
          '<div class="chips"><s>真弹</s><s>可拖</s></div><div class="n">20</div>' +
        '</div>' +
        '<div class="hx-card" data-go="exp" data-hall="mw">' +
          '<div class="k"><svg viewBox="0 0 24 24"><path d="M3 14c2.5 0 3-7 5.5-7S11 17 13.5 17 16 6 18.5 6 21 12 21 12"/></svg><b>动效</b></div>' +
          '<h3>motion-web</h3><p>20 配方 · 4 组令牌 · 25 规范</p>' +
          '<div class="chips"><s>实时跑</s><s>复制提示词</s></div><div class="n">20</div>' +
        '</div>' +
        '<div class="hx-card wide" data-go="proj">' +
          '<div class="k"><svg viewBox="0 0 24 24"><path d="M12 3.5v5"/><rect x="8.5" y="8.5" width="7" height="5" rx="1.6"/>' +
          '<path d="M12 13.5v3M6.5 20v-3.5h11V20"/></svg><b>搭项目</b></div>' +
          '<h3>勾功能 → 出目录树 + 开工提示词</h3>' +
          '<p>3 个平台（纯静态 / Vite+TS / Android+XPopup）× 11 个功能，每个文件标好对应哪条素材</p>' +
          '<div class="chips"><s>目录结构</s><s>素材映射</s><s>一键复制</s></div>' +
        '</div>' +
      '</div>';

    var rail = '' +
      '<div class="sec">先看这几个</div>' +
      '<div class="hx-rail">' + pick.map(function(id){ return cardHTML(byId[id]); }).join('') + '</div>';

    var src = '' +
      '<div class="sec">按来源进入</div>' +
      '<div class="hx-row" data-coll="lib"><div class="bx"><svg viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h10"/></svg></div>' +
        '<div><h4>完整素材库 · ' + libN + ' 条</h4><p>每条一套四件套文档 + HTML 独立页</p></div><em>' + libN + ' ›</em></div>' +
      '<div class="hx-row" data-coll="video"><div class="bx"><svg viewBox="0 0 24 24"><rect x="3.5" y="6" width="17" height="12" rx="3"/><path d="M10 9.5l5 2.5-5 2.5z"/></svg></div>' +
        '<div><h4>视频拆解 · 9</h4><p>对着真实产品的界面拆交互</p></div><em>9 ›</em></div>' +
      '<div class="hx-row" data-coll="motion"><div class="bx"><svg viewBox="0 0 24 24"><path d="M3 14c2.5 0 3-7 5.5-7S11 17 13.5 17 16 6 18.5 6 21 12 21 12"/></svg></div>' +
        '<div><h4>动效复刻 · 7</h4><p>绳幕 / 乌鸦 / 绳钟 / 叠压 / 滚轮 / 翻页 / 手绘</p></div><em>7 ›</em></div>' +
      '<div class="hx-row" data-coll="glass"><div class="bx"><svg viewBox="0 0 24 24"><path d="M12 3.5 20 12l-8 8.5L4 12z"/><path d="M8.5 12h7"/></svg></div>' +
        '<div><h4>液态玻璃 · 6</h4><p>折射 / 色散 / 菲涅尔 / 4-pass</p></div><em>6 ›</em></div>';

    var how = '' +
      '<div class="sec">怎么用</div>' +
      '<div class="hx-row" data-go="lib"><div class="bx"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/></svg></div>' +
        '<div><h4>1 · 找一条素材</h4><p>分类页浏览，或搜索框直接搜功能词</p></div></div>' +
      '<div class="hx-row" data-go="exp" data-hall="xp"><div class="bx"><svg viewBox="0 0 24 24"><path d="M12 4v6M12 14v6M4 12h6M14 12h6"/></svg></div>' +
        '<div><h4>2 · 在体验馆里试手感</h4><p>弹窗能拖、动画能放、配方能点重播</p></div></div>' +
      '<div class="hx-row" data-go="proj"><div class="bx"><svg viewBox="0 0 24 24"><path d="M12 3.5v5"/><rect x="8.5" y="8.5" width="7" height="5" rx="1.6"/><path d="M12 13.5v3"/></svg></div>' +
        '<div><h4>3 · 拿提示词开工</h4><p>结构页拼好目录树与要求，一键复制</p></div></div>';

    return head + grid + rail + src + how;
  }

  function collCard(k, n, d){
    return '<div class="coll glass" data-coll="' + k + '">' +
      '<div class="k">' + n + '</div><div class="n">' + COLL_NAME[k] + '</div><div class="d">' + d + '</div></div>';
  }

  /* ---------------- 素材库 ---------------- */
  function filtered(){
    var q = S.q.trim().toLowerCase();
    return ITEMS.filter(function(it){
      if(S.filter !== 'all' && it.coll !== S.filter) return false;
      if(S.cat && it.dur !== S.cat) return false;
      if(!q) return true;
      var hay = (it.name + ' ' + it.title + ' ' + it.mech + ' ' + it.params + ' ' + it.dur + ' ' + COLL_NAME[it.coll]).toLowerCase();
      return hay.indexOf(q) >= 0;
    });
  }
  var REL = {
    '组件':[['xp:attach','依附弹窗'],['xp:bubble','气泡弹窗'],['rec:5','配方 05 按压反馈']],
    '表单':[['xp:input','输入弹窗'],['xp:centerList','中间列表'],['rec:12','配方 12 校验抖动']],
    '导航':[['xp:drawerL','左侧抽屉'],['xp:drawerR','右侧抽屉'],['rec:9','配方 09 转场']],
    '布局':[['xp:partTop','局部阴影'],['xp:bindLayout','复用布局'],['rec:3','配方 03 粘性堆叠']],
    '反馈':[['xp:confirm','确认弹窗'],['xp:loading','加载弹窗'],['xp:bottomList','底部列表']],
    '数据':[['xp:fullScreen','全屏弹窗'],['rec:14','配方 14 数字滚动'],['an:ScaleAlphaFromCenter','20 种动画']],
    '动效':[['rec:1','配方 01 逐行入场'],['rec:7','配方 07 弹簧跟随'],['tok:spring','弹簧令牌']],
    '模板':[['xp:fullScreen','全屏弹窗'],['xp:drawerL','抽屉导航'],['rec:16','配方 16 分步引导']]
  };

  function catDetail(){
    var c = CATS.filter(function(x){ return x[0] === S.cat; })[0];
    if(!c) return '';
    var list = ITEMS.filter(function(x){ return x.coll === 'lib' && x.dur === c[0]; });
    var rel = (REL[c[0]] || []).map(function(r){
      return '<div class="rlink" data-sr="' + r[0] + '"><b>' + esc(r[1]) + '</b><span>直接体验 ›</span></div>';
    }).join('');
    var sub = list.filter(function(x){ return x.demos && x.demos.length; })
      .map(function(x){ return '<s>' + esc(x.name) + '</s>'; }).slice(0, 6).join('');
    return '<div class="backrow" data-cat="">‹ 全部分类</div>' +
      '<h1 class="title" style="font-size:23px">' + c[1] + '</h1>' +
      '<div class="lede2">' + c[2] + '。这一类共 <b>' + list.length + '</b> 条素材，<b>' + c[3] +
      '</b> 区间，每条都带可跑演示与可复制提示词。</div>' +
      '<div class="catmeta">' + sub + '</div>' +
      '<div class="sec">这一类里的 ' + list.length + ' 条</div>' +
      '<div class="grid">' + list.map(function(it){ return cardHTML(it); }).join('') + '</div>' +
      '<div class="sec">直接去体验</div>' + '<div class="rlinks">' + rel + '</div>';
  }

  function libHTML(){
    if(S.q.trim()){
      return '<h1 class="title" style="font-size:22px">素材库</h1>' + searchBar(0) +
        '<div id="srBox">' + (window.__EXP ? window.__EXP.searchHTML(S.q) : '') + '</div>';
    }
    if(S.cat) return catDetail();
    var list = filtered();
    var total = ITEMS.filter(function(x){ return x.coll === 'lib'; }).length;
    var cats = CATS.map(function(c){
      var n = ITEMS.filter(function(x){ return x.coll === 'lib' && x.dur === c[0]; }).length;
      return '<div class="catcard' + (S.cat === c[0] ? ' on' : '') + '" data-cat="' + c[0] + '">' +
        '<div class="code">' + c[3] + '</div>' +
        '<h4>' + c[1] + ' <em>' + n + '</em></h4>' +
        '<p>' + c[2] + '</p><span class="n">' + c[0] + '</span></div>';
    }).join('');
    var chips = [['all','全部 68'],['lib','完整素材库 46'],['video','视频拆解 9'],['motion','动效复刻 7'],['glass','液态玻璃 6']]
      .map(function(c){
        return '<div class="fchip' + (S.filter === c[0] ? ' on' : '') + '" data-f="' + c[0] + '">' + c[1] + '</div>';
      }).join('');
    return '' +
    '<h1 class="title" style="font-size:22px">素材库</h1>' +
    '<div class="lede2">按<b>分类</b>找东西最快：8 个分类覆盖一个 App 从组件到页面的全部界面；也可以直接搜功能词（弹窗 / 校验 / 图表 / 弹簧）。</div>' +
    searchBar(list.length) +
    '<div class="catgrid">' + cats + '</div>' +
    '<div class="sec">全部集合</div>' +
    '<div class="filters">' + chips + '</div>' +
    (list.length ? '<div class="grid">' + list.map(function(it){ return cardHTML(it); }).join('') + '</div>'
                 : '<div class="empty">这个分类下暂时没有条目。</div>');
  }

  function searchBar(n){
    return '<div class="searchrow"><div class="search">' +
      '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><circle cx="11" cy="11" r="6.5" ' +
      'stroke="rgba(233,239,247,.5)" stroke-width="1.8"/><path d="m16 16 4 4" stroke="rgba(233,239,247,.5)" ' +
      'stroke-width="1.8" stroke-linecap="round"/></svg>' +
      '<input id="q" placeholder="搜功能词：弹窗 / 校验 / 图表 / 弹簧" value="' + esc(S.q) + '">' +
      (S.q ? '<span class="cnt" id="qClear">清空</span>' : (n ? '<span class="cnt">' + n + ' 条</span>' : '')) +
    '</div></div>';
  }

  /* ---------------- 详情面板 ---------------- */
  var sheetEl = document.getElementById('sheet');
  var sheetItem = null;
  function openSheet(id){
    var it = byId[id]; if(!it) return;
    sheetItem = it;
    var picked = S.reqs[it.id] || (S.reqs[it.id] = []);
    var demos = (it.demos && it.demos.length)
      ? '<div class="kv" style="margin-top:2px"><div class="row"><span class="k">包含对比</span><span class="v">' +
        it.demos.map(function(d){ return '· ' + esc(d); }).join('<br>') + '</span></div></div>'
      : '';
    sheetEl.innerHTML = '<div class="sheet-box">' +
      '<div class="sheet-h">' +
        '<div><h2>' + esc(it.name) + ' · ' + esc(it.title) + '</h2>' +
        '<div class="sub">' + esc(it.src) + ' · ' + esc(it.dur) + ' · ' + it.diff + '</div></div>' +
        '<div class="grow"></div><div class="x" data-close="1">✕</div>' +
      '</div>' +
      '<div class="mini' + (it.coll === 'lib' ? ' lib' : '') + '" data-mini="' + it.id + '" style="margin-top:0;background:#0a0f14"></div>' +
      '<div class="kv">' +
        '<div class="row"><span class="k">机制</span><span class="v">' + esc(it.mech) + '</span></div>' +
        '<div class="row"><span class="k">关键参数</span><span class="v">' + esc(it.params) + '</span></div>' +
        '<div class="row"><span class="k">判据</span><span class="v">' + esc(it.verify) + '</span></div>' +
      '</div>' + demos +
      '<div class="sec" style="margin:16px 0 2px">变更要求（可勾选）</div>' +
      '<div class="reqs" id="reqs">' + (it.reqs || []).map(function(r){
        return '<div class="req' + (picked.indexOf(r) >= 0 ? ' on' : '') + '" data-r="' + esc(r) + '">' + esc(r) + '</div>';
      }).join('') + '</div>' +
      '<textarea class="custom" id="custom" placeholder="再补一句你的要求，例如：换成中秋主题 / 做成导航栏 / 加一个导出按钮…">' +
        esc(S.custom[it.id] || '') + '</textarea>' +
      '<pre class="pcode" id="pOut"></pre>' +
      '<div class="actrow">' +
        '<button class="btn primary" id="copyBtn">一键复制提示词</button>' +
        '<button class="btn" id="shareBtn">分享</button>' +
        '<a class="btn ghost" href="' + it.path + '" target="_blank" rel="noopener">打开完整演示页 ↗</a>' +
        '<span class="tip">' + it.prompt.length + ' 字 · 参考项目 + 变更要求 + 产出约束</span>' +
      '</div></div>';
    sheetEl.classList.add('on');
    sheetEl.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    /* 让系统返回键 / 浏览器后退先关掉详情：打开时压一条 history */
    try{
      if(history.state && history.state.sheet) history.replaceState({sheet:id}, '', '#'+id);
      else history.pushState({sheet:id}, '', '#'+id);
    }catch(e){}
    var mini = sheetEl.querySelector('[data-mini]');
    mount(mini, it.id);
    refreshPrompt();
    sheetEl.querySelector('[data-close]').addEventListener('click', closeSheet);
    sheetEl.querySelectorAll('#reqs .req').forEach(function(el){
      el.addEventListener('click', function(){
        el.classList.toggle('on');
        var r = el.dataset.r, arr = S.reqs[it.id], i = arr.indexOf(r);
        if(i >= 0) arr.splice(i,1); else arr.push(r);
        refreshPrompt();
      });
    });
    sheetEl.querySelector('#custom').addEventListener('input', function(){
      S.custom[it.id] = this.value; refreshPrompt();
    });
    sheetEl.querySelector('#copyBtn').addEventListener('click', function(){
      copyText(document.getElementById('pOut').textContent, this);
    });
    sheetEl.querySelector('#shareBtn').addEventListener('click', function(){
      var text = document.getElementById('pOut').textContent;
      if(window.AndroidBridge && window.AndroidBridge.share){
        window.AndroidBridge.share(text);
      } else {
        copyText(text, this);
      }
    });
  }
  function refreshPrompt(){
    var out = document.getElementById('pOut');
    if(out && sheetItem) out.textContent = promptFor(sheetItem);
  }
  function closeSheet(fromPop){
    var was = sheetEl.classList.contains('on');
    sheetEl.classList.remove('on');
    sheetEl.setAttribute('aria-hidden','true');
    document.body.style.overflow = '';
    var mini = sheetEl.querySelector('[data-mini]');
    if(mini) kill(mini);
    if(was && !fromPop && history.state && history.state.sheet){
      try{ history.back(); return; }catch(e){}
    }
  }
  sheetEl.addEventListener('click', function(e){ if(e.target === sheetEl) closeSheet(); });
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape') closeSheet(); });
  window.addEventListener('popstate', function(){
    if(sheetEl.classList.contains('on')) closeSheet(true);
  });

  /* ---------------- 对比 ---------------- */
  function cmpHTML(){
    function slotHTML(side){
      var it = byId[S.cmp[side]];
      return '<div class="slot">' +
        '<div class="slot-h"><span class="badge">' + (side ? 'B' : 'A') + '</span>' +
          '<select data-side="' + side + '">' + ITEMS.map(function(x){
            return '<option value="' + x.id + '"' + (x.id === it.id ? ' selected' : '') + '>' +
              x.id.toUpperCase() + ' · ' + esc(x.name) + '</option>';
          }).join('') + '</select></div>' +
        '<div class="mini" data-mini="' + it.id + '"></div>' +
        '<div class="note" style="margin-top:8px"><b>' + esc(it.name) + '</b> · ' + esc(it.dur) +
          '<br>' + esc(it.mech.slice(0, 78)) + (it.mech.length > 78 ? '…' : '') + '</div>' +
      '</div>';
    }
    var a = byId[S.cmp[0]], b = byId[S.cmp[1]];
    function row(k, fa, fb){
      return '<div class="drow"><div class="k">' + k + '</div><div class="v1">' + fa + '</div>' +
             '<div class="v2">' + fb + '</div></div>';
    }
    return '' +
    '<h1 class="title" style="font-size:22px">并排对比</h1>' +
    '<p class="lede">两个素材同时跑，比的是机制与参数，不是截图。换任意一边的素材，下面的差异表会跟着变。</p>' +
    '<div class="cmp" style="margin-top:14px">' +
      '<div class="slots">' + slotHTML(0) + slotHTML(1) + '</div>' +
      '<div class="actrow" style="margin-top:10px"><button class="btn sm" id="sync">同步重开两个演示</button>' +
        '<span class="tip">用来对比「同一时刻的起点」</span></div>' +
      '<div class="diffs">' +
        '<div class="drow head"><div class="k">维度</div><div class="v1">A · ' + esc(a.name) + '</div>' +
          '<div class="v2">B · ' + esc(b.name) + '</div></div>' +
        row('来源', esc(COLL_NAME[a.coll]) + ' · ' + esc(a.dur), esc(COLL_NAME[b.coll]) + ' · ' + esc(b.dur)) +
        row('机制', esc(a.mech), esc(b.mech)) +
        row('关键参数', esc(a.params), esc(b.params)) +
        row('判据', esc(a.verify), esc(b.verify)) +
      '</div>' +
    '</div>';
  }

  /* ---------------- 设置 ---------------- */
  function setHTML(){
    return '' +
    '<h1 class="title" style="font-size:22px">设置</h1>' +
    '<section class="glass" style="padding:6px 16px;margin-top:12px">' +
      '<div class="setrow"><div class="lab">主题配色<small>7 套，跟着背景一起变</small></div>' +
        '<div class="pal">' +
        ['aurora','mint','sunset','mono','coral','sakura','galaxy'].map(function(p){
          return '<div class="dot dot-' + p + (document.body.dataset.palette === p ? ' on' : '') +
                 '" data-p="' + p + '"></div>';
        }).join('') + '</div></div>' +
      '<div class="setrow"><div class="lab">液态玻璃<small>关掉后回到实心卡片，无折射无模糊</small></div>' +
        '<div class="sw' + (document.body.classList.contains('normal') ? '' : ' on') + '" id="swGlass"></div></div>' +
      '<div class="setrow"><div class="lab">减少动效<small>关闭背景漂移与入场动画（演示本身不动）</small></div>' +
        '<div class="sw' + (document.body.classList.contains('reduce') ? ' on' : '') + '" id="swReduce"></div></div>' +
      '<div class="setrow"><div class="lab">新手引导<small>第一次打开时的三步说明</small></div>' +
        '<button class="btn sm" id="reWelcome">重新查看</button></div>' +
    '</section>' +
    '<div class="sec">数据</div>' +
    '<section class="glass" style="padding:16px 18px">' +
      '<div class="note">素材清单可以导出成 JSON（68 条：id / 名称 / 来源 / 机制 / 关键参数 / 判据 / 提示词），' +
      '方便接到你自己的素材库或文档里。</div>' +
      '<div class="actrow"><button class="btn" id="expJson">复制素材清单 JSON</button>' +
      '<button class="btn ghost" id="expPrompt">复制全部提示词</button></div>' +
    '</section>' +
    '<div class="sec">两套形态</div>' +
    '<section class="glass" style="padding:16px 18px">' +
      '<div class="note"><b>应用形态</b>（你正在看的这一页）：46 条素材 + 22 个交互拆解的库，可搜索 / 筛选 / 对比 / 复制提示词。<br>' +
      '<b>HTML 形态</b>：每个素材还有一张独立演示页，带完整的滑杆、多画布对照与长提示词面板。</div>' +
      '<div class="linkrow">' +
        '<a href="../index.html">工作区总入口 · 两套形态对照表</a>' +
        '<a href="../motion-demos/index.html" target="_blank">motion-demos · 7 页</a>' +
        '<a href="../glass-demos/index.html" target="_blank">glass-demos · 6 页</a>' +
        '<a href="../video-demos/index.html" target="_blank">video-demos · 9 页</a>' +
      '</div>' +
    '</section>' +
    '<div class="sec">关于</div>' +
    '<section class="glass" style="padding:16px 18px">' +
      '<div class="note">素材来源：<b>feitangyuan/motion-web</b>（CC BY-NC 4.0，禁止商用）、' +
      '<b>iyinchao/liquid-glass-studio</b>（MIT）、以及 9 个 UI 拆解视频（B 站，仅做要点还原）。<br>' +
      '本页所有演示都是<b>按机制重新实现</b>的代码，不是原项目截图或素材；玻璃背景全部程序化生成。<br>' +
      '形制参考：<b>yz8023/ui</b> 素材库的「深色极光 + 液态玻璃 + 底部胶囊标签栏」。</div>' +
    '</section>';
  }

  function moreHTML(){
    var segv = [['cmp','并排对比'],['set','设置']].map(function(x){
      return '<div class="fchip' + (S.more === x[0] ? ' on' : '') + '" data-more="' + x[0] + '">' + x[1] + '</div>';
    }).join('');
    return '<h1 class="title" style="font-size:22px">更多</h1>' +
      '<div class="filters" style="margin-top:4px">' + segv + '</div>' +
      (S.more === 'cmp' ? cmpHTML() : setHTML());
  }

  /* ---------------- 渲染与路由 ---------------- */
  var LAST = {view: '', y: 0};
  function render(keepScroll){
    /* 同一页重绘就留在原地，换页才回顶部 */
    var same = (LAST.view === S.view);
    if(same) LAST.y = window.scrollY;
    var y = keepScroll ? LAST.y : (same ? LAST.y : 0);
    killAll();
    var main = document.getElementById('main');
    if(S.view === 'home') main.innerHTML = homeHTML();
    else if(S.view === 'lib') main.innerHTML = libHTML();
    else if(S.view === 'exp') main.innerHTML = window.__EXP.expHTML();
    else if(S.view === 'proj') main.innerHTML = window.__EXP.projHTML();
    else if(S.view === 'case') main.innerHTML = window.__EXP.caseHTML(S.caseId);
    else if(S.view === 'more') main.innerHTML = moreHTML();
    else main.innerHTML = setHTML();
    wire(main);
    if(S.view === 'exp' || S.view === 'proj' || S.view === 'lib' || S.view === 'case') window.__EXP.wire(main);
    observe(main);
    if(S.view === 'lib'){
      var qc = main.querySelector('#qClear');
      if(qc) qc.addEventListener('click', function(){ S.q = ''; render(); });
      var q = main.querySelector('#q');
      if(q){
        var timer = 0;
        q.addEventListener('input', function(){
          var v = this.value;
          clearTimeout(timer);
          timer = setTimeout(function(){ S.q = v; render(); }, 180);
        });
      }
    }
    window.scrollTo(0, y);
    LAST.view = S.view;
  }

  function wire(root){
    root.querySelectorAll('[data-open]').forEach(function(el){
      el.addEventListener('click', function(){ openSheet(el.dataset.open); });
    });
    var hs = root.querySelector('#hxGoSearch');
    if(hs) hs.addEventListener('click', function(){
      S.view = 'lib'; S.q = ''; S.cat = ''; syncTabs(); render();
      setTimeout(function(){ var q = document.getElementById('q'); if(q) q.focus(); }, 80);
    });
    root.querySelectorAll('[data-coll]').forEach(function(el){
      el.addEventListener('click', function(){ S.filter = el.dataset.coll; S.view = 'lib'; syncTabs(); render(); });
    });
    root.querySelectorAll('.fchip').forEach(function(el){
      el.addEventListener('click', function(){
        if(el.dataset.more){ S.more = el.dataset.more; render(); return; }
        if(el.dataset.f){ S.filter = el.dataset.f; render(); }
      });
    });
    root.querySelectorAll('[data-cat]').forEach(function(el){
      el.addEventListener('click', function(){
        S.cat = el.dataset.cat || '';
        if(S.cat) S.filter = 'lib';
        S.q = '';
        render();
        window.scrollTo(0, 0);
        LAST.y = 0;
      });
    });
    root.querySelectorAll('[data-go]').forEach(function(el){
      el.addEventListener('click', function(){
        if(el.dataset.hall && window.__EXHALL) window.__EXHALL(el.dataset.hall);
        S.view = el.dataset.go; syncTabs(); render();
      });
    });
    root.querySelectorAll('select[data-side]').forEach(function(sel){
      sel.addEventListener('change', function(){
        S.cmp[+sel.dataset.side] = sel.value;
        LS.set('cmp', S.cmp);
        render();
      });
    });
    var sync = root.querySelector('#sync');
    if(sync) sync.addEventListener('click', function(){ render(); toast('两个演示已同时重开'); });

    var sg = root.querySelector('#swGlass');
    if(sg) sg.addEventListener('click', function(){
      var on = !document.body.classList.contains('normal');
      document.body.classList.toggle('normal', on);
      sg.classList.toggle('on', !on);
      LS.set('glassOn', !on);
      toast(on ? '已切到实心卡片（无玻璃）' : '已开启液态玻璃');
    });
    var sr = root.querySelector('#swReduce');
    if(sr) sr.addEventListener('click', function(){
      var on = !document.body.classList.contains('reduce');
      document.body.classList.toggle('reduce', on);
      sr.classList.toggle('on', on);
      LS.set('reduce', on);
    });
    var wb = root.querySelector('#reWelcome');
    if(wb) wb.addEventListener('click', function(){ showWelcome(true); });
    var ej = root.querySelector('#expJson');
    if(ej) ej.addEventListener('click', function(){
      var data = ITEMS.map(function(it){
        return { id:it.id.toUpperCase(), name:it.name, title:it.title, coll:COLL_NAME[it.coll],
                 page:it.path, type:it.dur, mech:it.mech, params:it.params, verify:it.verify,
                 prompt:promptFor(it) };
      });
      copyText(JSON.stringify(data, null, 2), this, '已复制 ✓');
    });
    var ep = root.querySelector('#expPrompt');
    if(ep) ep.addEventListener('click', function(){
      var all = ITEMS.map(function(it){ return '===== ' + it.id.toUpperCase() + ' · ' + it.name + ' =====\n' + promptFor(it); }).join('\n\n');
      copyText(all, this, '已复制 ✓');
    });
    root.querySelectorAll('.pal .dot').forEach(function(d){
      d.addEventListener('click', function(){
        document.body.dataset.palette = d.dataset.p;
        LS.set('palette', d.dataset.p);
        document.querySelectorAll('.dot').forEach(function(x){
          x.classList.toggle('on', x.dataset.p === d.dataset.p);
        });
      });
    });
  }

  /* ---------------- 标签栏 ---------------- */
  function syncTabs(){
    document.querySelectorAll('.tab').forEach(function(t){
      t.classList.toggle('active', t.dataset.v === S.view);
    });
    var tabs = document.querySelectorAll('#tabs .tab');
    var i = ['home','lib','exp','proj','more'].indexOf(S.view === 'case' ? 'exp' : S.view);
    var el = tabs[i], pill = document.getElementById('pill');
    var bar = document.getElementById('tabs');
    if(el && pill && bar){
      var a = el.getBoundingClientRect(), b = bar.getBoundingClientRect();
      pill.style.width = a.width + 'px';
      pill.style.transform = 'translateX(' + (a.left - b.left - 6) + 'px)';
    }
  }
  document.querySelectorAll('#tabs .tab').forEach(function(t){
    t.addEventListener('click', function(){ S.view = t.dataset.v; syncTabs(); render(); });
  });
  window.addEventListener('resize', syncTabs);

  var gb = document.getElementById('glassBtn');
  if(gb) gb.addEventListener('click', function(){
    document.body.classList.toggle('normal');
    toast(document.body.classList.contains('normal') ? '已切到实心卡片（无玻璃）' : '已开启液态玻璃');
  });

  /* 在原生壳里把 target="_blank" 收回来，避免开新窗口失败 */
  if(window.AndroidBridge){
    document.addEventListener('click', function(e){
      var a = e.target && e.target.closest ? e.target.closest('a[target="_blank"]') : null;
      if(a){ a.removeAttribute('target'); }
    }, true);
  }

  requestAnimationFrame(function(){ syncTabs(); });
  render();

  /* ---------------- 新手引导 ---------------- */
  function showWelcome(force){
    var el = document.getElementById('welcome');
    if(!el) return;
    el.classList.add('on');
    el.setAttribute('aria-hidden','false');
  }
  function hideWelcome(remember){
    var el = document.getElementById('welcome');
    if(!el) return;
    el.classList.remove('on');
    el.setAttribute('aria-hidden','true');
    if(remember) LS.set('welcome', 1);
  }
  (function initWelcome(){
    var el = document.getElementById('welcome');
    if(!el) return;
    var go = el.querySelector('[data-w-go]');
    var close = el.querySelector('[data-w-close]');
    var goDemo = el.querySelector('[data-w-demo]');
    if(go) go.addEventListener('click', function(){ hideWelcome(true); S.view='lib'; syncTabs(); render(); });
    if(close) close.addEventListener('click', function(){ hideWelcome(true); });
    if(goDemo) goDemo.addEventListener('click', function(){
      hideWelcome(true);
      if(window.__EXHALL) window.__EXHALL('xp');
      S.view='exp'; syncTabs(); render();
    });
    if(!LS.get('welcome', 0)) setTimeout(function(){ showWelcome(false); }, 420);
  })();

  /* 给体验馆 / 项目结构 / 搜索用的全局钩子 */
  window.__ITEMS = ITEMS;
  window.__OPEN = openSheet;
  window.__VIEW = function(){ return S.view; };
  window.__CASE = function(id){
    S.caseId = id; S.view = 'case'; syncTabs(); render(); window.scrollTo(0, 0);
  };
  window.__GOTO = function(v, keep){ S.view = v; syncTabs(); render(); };
  window.__EXHALL = function(h){ if(window.__EXP && h){ window.__EXP.setHall(h); if(h === 'xp') window.__EXP.setXpTab('list'); } };
  window.__EXPHALL = function(h){ if(window.__EXP) window.__EXP.setHall(h); };
  window.__EXPXPTAB = function(t){ if(window.__EXP) window.__EXP.setXpTab(t); };
  window.__EXPMWTAB = function(t){ if(window.__EXP) window.__EXP.setMwTab(t); };
  window.__SRGO = function(id){
    if(id.indexOf('xp:') === 0){ window.__XP.open(id.slice(3)); return; }
    if(id.indexOf('an:') === 0){ if(window.__EXPHALL) window.__EXPHALL('xp'); S.view = 'exp'; syncTabs(); render();
      setTimeout(function(){ if(window.__EXPXPTAB) window.__EXPXPTAB('anim'); }, 120); return; }
    if(id.indexOf('rec:') === 0){ if(window.__EXPHALL) window.__EXPHALL('mw'); S.view = 'exp'; syncTabs(); render();
      setTimeout(function(){ if(window.__EXPMWTAB) window.__EXPMWTAB('rec'); }, 120); return; }
    if(id.indexOf('spec:') === 0){ if(window.__EXPHALL) window.__EXPHALL('mw'); S.view = 'exp'; syncTabs(); render();
      setTimeout(function(){ if(window.__EXPMWTAB) window.__EXPMWTAB('spec'); }, 120); return; }
    if(id.indexOf('feat:') === 0){ S.view = 'proj'; syncTabs(); render(); return; }
    openSheet(id);
  };

  /* 支持 #m05 / #l01 这样的深链：直接从别处打开某个素材 */
  function openFromHash(){
    var id = (location.hash || '').replace('#','').toLowerCase();
    if(id && byId[id] && !sheetEl.classList.contains('on')){
      if(S.view !== 'lib'){ S.view = 'lib'; syncTabs(); render(); }
      setTimeout(function(){ openSheet(id); }, 120);
    }
  }
  window.addEventListener('hashchange', openFromHash);
  openFromHash();
})();
"""
