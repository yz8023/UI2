# -*- coding: utf-8 -*-
"""素材库 App：迷你演示（视频拆解类 9 个 + 动效类 7 个）"""

MINI_CSS = """
/* ---------- mini 容器通用 ---------- */
.mini{height:176px;margin-top:9px;background:rgba(255,255,255,.045);border:1px solid rgba(255,255,255,.10);
  border-radius:13px;overflow:hidden;position:relative}
.mini canvas{display:block;width:100%;touch-action:none}
.mini-note{position:absolute;left:9px;bottom:7px;font-size:10.5px;color:rgba(255,255,255,.42);
  background:rgba(0,0,0,.28);padding:2px 7px;border-radius:99px;pointer-events:none}
.mini-chip{position:absolute;right:8px;top:8px;font-size:10px;color:#cfe4ff;
  background:rgba(22,74,112,.72);border:1px solid rgba(157,204,255,.35);padding:2px 8px;border-radius:99px;pointer-events:none}

/* ---------- m04 粘性堆叠 ---------- */
.m4scroll{height:176px;overflow-y:auto;border-radius:12px;scrollbar-width:none}
.m4scroll::-webkit-scrollbar{display:none}
.m4wrap{padding:6px 6px 0}
.m4screen{position:sticky;top:0;height:132px;border-radius:13px;display:flex;flex-direction:column;
  justify-content:flex-end;padding:12px 14px;margin-bottom:8px;overflow:hidden;
  box-shadow:0 -12px 24px rgba(0,0,0,.35)}
.m4screen b{font-size:15px;letter-spacing:.02em;color:#fff}
.m4screen span{font-size:11px;color:rgba(255,255,255,.66);margin-top:3px}
.m4bar{position:absolute;left:0;top:0;height:3px;background:#9dccff;box-shadow:0 0 10px #9dccff}

/* ---------- v01 浮层 ---------- */
.vwrap{position:relative;height:176px;overflow:hidden}
.vstage-in{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;gap:7px}
.vbtnp{font-size:11.5px;padding:7px 12px;border-radius:9px;color:#dceaff;
  background:rgba(157,204,255,.14);border:1px solid rgba(157,204,255,.32);cursor:pointer}
.toast-m{position:absolute;left:50%;bottom:12px;transform:translateX(-50%);font-size:11px;
  padding:7px 12px;border-radius:9px;background:rgba(20,26,32,.94);border:1px solid rgba(255,255,255,.18);
  color:#eaf3ff;opacity:0;transition:opacity .2s}
.toast-m.on{opacity:1}
.drawer-m{position:absolute;top:0;right:0;bottom:0;width:44%;background:rgba(24,32,40,.97);
  border-left:1px solid rgba(255,255,255,.16);transform:translateX(100%);
  transition:transform .34s cubic-bezier(.2,.9,.3,1.1);padding:12px;font-size:11.5px;color:#d6e6f7}
.drawer-m.on{transform:none}
.modal-m{position:absolute;inset:0;background:rgba(6,10,14,.62);display:flex;align-items:center;
  justify-content:center;opacity:0;pointer-events:none;transition:opacity .22s}
.modal-m.on{opacity:1;pointer-events:auto}
.modal-card{width:72%;background:#1b242c;border:1px solid rgba(255,255,255,.14);border-radius:13px;
  padding:14px;font-size:11.5px;color:#e8f1fa;transform:scale(.92);transition:transform .26s cubic-bezier(.2,.9,.3,1.2)}
.modal-m.on .modal-card{transform:none}

/* ---------- v02 六种浮层 ---------- */
.v2grid{position:relative;height:176px;padding:10px}
.v2btn{position:absolute;font-size:11px;padding:6px 11px;border-radius:8px;background:rgba(157,204,255,.16);
  border:1px solid rgba(157,204,255,.3);color:#dceaff;cursor:pointer}
.v2pop{position:absolute;background:#1c252d;border:1px solid rgba(255,255,255,.16);border-radius:10px;
  font-size:10.5px;color:#dbe8f6;padding:8px 10px;box-shadow:0 12px 28px rgba(0,0,0,.5);
  transform-origin:30% 0;opacity:0;transform:scale(.9);transition:.22s cubic-bezier(.2,.9,.3,1.2)}
.v2pop.on{opacity:1;transform:none}

/* ---------- v03 质感 5 招 ---------- */
.v3card{margin:5px 9px 0;border-radius:13px;padding:11px;transition:.35s;background:#1a222a;
  border:1px solid rgba(255,255,255,.12)}
.v3card.hi{background:linear-gradient(160deg,#233140,#161d24);border-color:rgba(157,204,255,.4);
  box-shadow:0 14px 34px rgba(0,0,0,.55),inset 0 1px 0 rgba(255,255,255,.22)}
.v3card h4{font-size:12.5px;color:#eaf3ff}
.v3card p{font-size:10.5px;color:rgba(231,240,250,.62);margin-top:4px;line-height:1.5}
.v3row{display:flex;gap:4px;flex-wrap:wrap;padding:8px 9px 0}
.v3tg{font-size:9.5px;padding:3px 7px;border-radius:99px;border:1px solid rgba(255,255,255,.16);
  color:rgba(232,237,244,.55);cursor:pointer;user-select:none}
.v3tg.on{background:rgba(157,204,255,.18);color:#bcdcff;border-color:rgba(157,204,255,.5)}

/* ---------- v04 AI 流式 ---------- */
.v4box{margin:12px;border-radius:13px;background:#161d24;border:1px solid rgba(255,255,255,.1);padding:12px}
.v4txt{font-size:11.5px;line-height:1.75;color:#e6eff8;min-height:52px}
.v4caret{display:inline-block;width:6px;height:12px;background:#9dccff;vertical-align:-1px;animation:blink 1s steps(1) infinite}
@keyframes blink{50%{opacity:0}}
.v4row{display:flex;gap:6px;margin-top:10px;align-items:center}
.v4pill{font-size:10px;padding:3px 8px;border-radius:99px;background:rgba(157,204,255,.14);
  color:#a9cdf0;border:1px solid rgba(157,204,255,.28)}

/* ---------- v05 下拉 vs 选择器 ---------- */
.v5wrap{display:flex;gap:10px;padding:11px;height:176px}
.v5col{flex:1;position:relative}
.v5btn{width:100%;font-size:11px;padding:7px 9px;border-radius:9px;background:rgba(255,255,255,.07);
  border:1px solid rgba(255,255,255,.18);color:#e2ecf7;cursor:pointer;display:flex;justify-content:space-between}
.v5menu{position:absolute;left:0;right:0;top:34px;background:#1c252d;border:1px solid rgba(255,255,255,.16);
  border-radius:10px;padding:4px;opacity:0;transform:translateY(-6px);pointer-events:none;transition:.18s;z-index:3}
.v5menu.on{opacity:1;transform:none;pointer-events:auto}
.v5mi{font-size:10.5px;padding:6px 8px;border-radius:7px;color:#dbe8f6;cursor:pointer;display:flex;gap:6px;align-items:center}
.v5mi:hover{background:rgba(157,204,255,.14)}
.v5mi.sel{background:rgba(157,204,255,.2);color:#fff}
.v5log{font-size:9.5px;color:rgba(232,237,244,.5);margin-top:34px;line-height:1.55;min-height:56px}

/* ---------- v06 热区 ---------- */
.v6wrap{position:relative;height:176px}
.v6note{position:absolute;right:9px;top:8px;font-size:10px;color:rgba(232,237,244,.55)}
.v6tg{position:absolute;left:9px;top:8px;font-size:10px;padding:3px 8px;border-radius:99px;
  background:rgba(157,204,255,.16);border:1px solid rgba(157,204,255,.4);color:#c9e3ff;cursor:pointer}

/* ---------- v07 全球化 ---------- */
.v7wrap{padding:11px;height:176px}
.v7langs{display:flex;gap:5px;margin-bottom:9px}
.v7lg{font-size:10px;padding:3px 8px;border-radius:99px;border:1px solid rgba(255,255,255,.16);
  color:rgba(232,237,244,.6);cursor:pointer}
.v7lg.on{background:rgba(157,204,255,.2);color:#fff;border-color:rgba(157,204,255,.55)}
.v7row{display:flex;gap:8px;align-items:center;margin-bottom:7px}
.v7lab{font-size:9.5px;color:rgba(232,237,244,.45);width:40px;flex:0 0 auto}
.v7btn{font-size:10.5px;padding:6px 10px;border-radius:8px;background:rgba(157,204,255,.18);
  border:1px solid rgba(157,204,255,.35);color:#e7f1fb;white-space:nowrap}
.v7btn.auto{max-width:100%;overflow:hidden;text-overflow:ellipsis}
.v7btn.trunc{max-width:96px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.v7btn.bad{max-width:52px;overflow:visible;white-space:nowrap;background:rgba(255,143,163,.2);
  border-color:rgba(255,143,163,.5)}

/* ---------- v08 / v09 游戏帧 ---------- */
.v8hud{position:absolute;left:9px;top:8px;font-size:10px;color:rgba(232,237,244,.6);
  font-family:ui-monospace,monospace;line-height:1.5}
.v8hit{color:#6ff0c0}
"""

MINIS_JS = r"""
(function(){
  var M = {};
  window.__MINI = M;

  /* ---------- 基础工具 ---------- */
  function setup(root, h){
    root.innerHTML = '';
    var cv = document.createElement('canvas');
    cv.style.height = h + 'px';
    root.appendChild(cv);
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var st = {cv:cv, ctx:cv.getContext('2d'), w:0, h:0, dpr:dpr, H:h};
    st.fit = function(){
      var w = root.clientWidth || 300;
      st.w = Math.round(w); st.h = h;
      cv.width = Math.round(w*dpr); cv.height = Math.round(h*dpr);
      cv.style.height = h + 'px';
      st.ctx.setTransform(dpr,0,0,dpr,0,0);
      return st;
    };
    st.fit();
    return st;
  }
  function loop(fn){
    var alive = true, last = performance.now();
    function tick(t){
      if(!alive) return;
      var dt = Math.min((t-last)/1000, 1/24); last = t;
      /* 单帧异常不能把整段动画带走：先排下一帧，再画 */
      requestAnimationFrame(tick);
      try { fn(t, dt); } catch(e){ if(!tick._warned){ tick._warned = 1; console.warn('mini frame', e); } }
    }
    requestAnimationFrame(tick);
    return function(){ alive = false; };
  }
  function note(root, txt){
    var d = document.createElement('div'); d.className='mini-note'; d.textContent = txt;
    root.appendChild(d);
  }
  function rnd(a,b){ return a + Math.random()*(b-a); }

  /* =================================================================
     v01 · 弹窗选型：Toast / Drawer / Modal
     ================================================================= */
  M['v01'] = function(root){
    root.innerHTML =
      '<div class="vwrap"><div class="mini-chip">点三个按钮</div>' +
      '<div class="vstage-in">' +
        '<div class="vbtnp" data-k="toast">Toast</div>' +
        '<div class="vbtnp" data-k="drawer">Drawer</div>' +
        '<div class="vbtnp" data-k="modal">Modal</div>' +
      '</div>' +
      '<div class="toast-m">已保存到本地</div>' +
      '<div class="drawer-m">侧边抽屉<br><span style="color:rgba(214,230,247,.6);font-size:10px">不打断当前页面<br>适合设置 / 详情</span></div>' +
      '<div class="modal-m"><div class="modal-card">确认删除？<br><span style="color:rgba(232,241,250,.6);font-size:10px">必须打断，因为不可逆</span></div></div>' +
      '</div>';
    var t = root.querySelector('.toast-m'), d = root.querySelector('.drawer-m'), m = root.querySelector('.modal-m');
    var tm;
    function closeAll(){ t.classList.remove('on'); d.classList.remove('on'); m.classList.remove('on'); }
    root.querySelectorAll('.vbtnp').forEach(function(b){
      b.addEventListener('click', function(e){
        e.stopPropagation();
        var k = b.dataset.k;
        if(k === 'toast'){
          clearTimeout(tm); t.classList.add('on');
          tm = setTimeout(function(){ t.classList.remove('on'); }, 1500);
        } else if(k === 'drawer'){ closeAll(); d.classList.add('on'); }
        else { closeAll(); m.classList.add('on'); }
      });
    });
    root.addEventListener('click', function(e){
      if(e.target === m || e.target === d){ closeAll(); }
    });
  };

  /* =================================================================
     v02 · 6 种高级浮层
     ================================================================= */
  M['v02'] = function(root){
    var styles = [
      ['Popover', 'left:68px;top:44px', '跟着锚点，非模态'],
      ['Tooltip', 'left:68px;top:96px', '只解释，不承载操作'],
      ['Sheet', 'left:14px;top:104px;right:14px;border-radius:14px 14px 10px 10px', '从底部上来，可拖走'],
      ['Dialog', 'left:40px;top:52px;right:40px', '必须做决定才可用'],
      ['Menu', 'left:120px;top:44px', '一屏命令，选完即关'],
      ['Lightbox', 'left:22px;top:34px;right:22px;bottom:34px;display:grid;place-items:center', '看大图，背景压暗']
    ];
    var html = '<div class="v2grid"><div class="mini-chip">点按钮换一种</div>';
    html += '<div class="v2btn" style="left:12px;top:12px">打开浮层 ▾</div>';
    styles.forEach(function(s,i){
      html += '<div class="v2pop" data-i="'+i+'" style="'+s[1]+'"><b style="color:#bcdcff">'+s[0]+'</b><br>'+
              '<span style="color:rgba(219,232,246,.66);font-size:10px">'+s[2]+'</span></div>';
    });
    html += '</div>';
    root.innerHTML = html;
    var i = -1, pops = root.querySelectorAll('.v2pop');
    function show(n){
      pops.forEach(function(p,k){ p.classList.toggle('on', k === n); });
      i = n;
    }
    root.querySelector('.v2btn').addEventListener('click', function(){ show((i+1) % styles.length); });
    show(0);
  };

  /* =================================================================
     v03 · 大厂质感 5 招
     ================================================================= */
  M['v03'] = function(root){
    var tags = ['分层阴影', '内高光描边', '统一圆角', '留白节奏', '低对比渐变'];
    root.innerHTML =
      '<div class="v3row">' + tags.map(function(t,i){
        return '<div class="v3tg'+(i<2?' on':'')+'" data-i="'+i+'">'+t+'</div>';
      }).join('') + '</div>' +
      '<div class="v3card"><h4>本月预算</h4><p>¥ 12,480 / 20,000<br>还剩 7,520 元，比上月多花 12%</p></div>' +
      '<div class="v3row" style="padding-top:4px"><span style="font-size:9.5px;color:rgba(232,237,244,.4)">' +
      '逐个开合，看同一张卡片的「质感」从哪来</span></div>';
    var card = root.querySelector('.v3card');
    root.querySelectorAll('.v3tg').forEach(function(tg){
      tg.addEventListener('click', function(){
        tg.classList.toggle('on');
        var on = root.querySelectorAll('.v3tg.on').length;
        card.classList.toggle('hi', on >= 3);
        card.style.boxShadow = on >= 1 ? '0 14px 34px rgba(0,0,0,.55)' : 'none';
        card.style.borderColor = on >= 2 ? 'rgba(157,204,255,.4)' : 'rgba(255,255,255,.12)';
        card.style.borderRadius = on >= 3 ? '18px' : '14px';
        card.style.padding = on >= 4 ? '20px 18px' : '14px';
        card.style.background = on >= 5 ? 'linear-gradient(160deg,#233140,#161d24)' : '#1a222a';
      });
    });
  };

  /* =================================================================
     v04 · AI 界面 5 个细节（流式 + 可打断 + 复制 + 重新生成）
     ================================================================= */
  M['v04'] = function(root){
    root.innerHTML =
      '<div class="v4box"><div class="mini-chip" style="position:static;display:inline-block;margin-bottom:8px">流式输出</div>' +
      '<div class="v4txt"><span id="v4t"></span><i class="v4caret"></i></div>' +
      '<div class="v4row"><div class="v4pill">⌘ . 停止</div><div class="v4pill">复制</div>' +
      '<div class="v4pill">重新生成</div><span style="font-size:9.5px;color:rgba(232,237,244,.4)">token 38/s</span></div></div>';
    var full = '把「导出」拆成两步：先选格式，再选范围。三步之内给反馈，超过三秒给进度。';
    var el = root.querySelector('#v4t'), i = 0, alive = true;
    function tick(){
      if(!alive) return;
      i++;
      if(i > full.length){ i = 0; }
      el.textContent = full.slice(0, Math.min(i, full.length));
      setTimeout(tick, i > full.length ? 1400 : 55);
    }
    tick();
    return function(){ alive = false; };
  };

  /* =================================================================
     v05 · 下拉 vs 选择器
     ================================================================= */
  M['v05'] = function(root){
    root.innerHTML =
      '<div class="v5wrap">' +
        '<div class="v5col"><div class="v5btn" data-m="0"><span>分享 ▾</span></div>' +
          '<div class="v5menu" data-m="0"><div class="v5mi" data-a="复制链接">复制链接</div>' +
          '<div class="v5mi" data-a="发送给…">发送给…</div><div class="v5mi" data-a="导出 PDF">导出 PDF</div></div>' +
          '<div class="v5log" data-l="0">命令型：选完就执行</div></div>' +
        '<div class="v5col"><div class="v5btn" data-m="1"><span data-v>城市 ▾</span></div>' +
          '<div class="v5menu" data-m="1"><div class="v5mi" data-a="上海">上海</div>' +
          '<div class="v5mi" data-a="杭州">杭州</div><div class="v5mi" data-a="成都">成都</div></div>' +
          '<div class="v5log" data-l="1">选择型：只回填数值</div></div>' +
      '</div>';
    var menus = root.querySelectorAll('.v5menu');
    root.querySelectorAll('.v5btn').forEach(function(b){
      b.addEventListener('click', function(e){
        e.stopPropagation();
        var k = +b.dataset.m;
        menus.forEach(function(m){ m.classList.toggle('on', +m.dataset.m === k && !m.classList.contains('on')); });
      });
    });
    root.querySelectorAll('.v5mi').forEach(function(mi){
      mi.addEventListener('click', function(e){
        e.stopPropagation();
        var k = +mi.closest('.v5menu').dataset.m;
        var log = root.querySelector('.v5log[data-l="'+k+'"]');
        if(k === 0){
          log.innerHTML = '执行了：<b style="color:#8fe3c2">'+mi.dataset.a+'</b><br><span style="color:rgba(232,237,244,.4)">菜单关闭，按钮文字不变</span>';
        } else {
          root.querySelector('[data-v]').textContent = mi.dataset.a + ' ▾';
          root.querySelectorAll('.v5mi').forEach(function(x){ if(x.dataset.m !== '1') x.classList.remove('sel'); });
          mi.classList.add('sel');
          log.innerHTML = '回填了：<b style="color:#bcdcff">'+mi.dataset.a+'</b><br><span style="color:rgba(232,237,244,.4)">菜单关闭，没有执行任何动作</span>';
        }
        menus.forEach(function(m){ m.classList.remove('on'); });
      });
    });
  };

  /* =================================================================
     v06 · 热区与误触
     ================================================================= */
  M['v06'] = function(root){
    var S = setup(root, +root.dataset.h || 176);
    var big = false;
    var btn = document.createElement('div');
    btn.className = 'v6tg'; btn.textContent = '热区：32px（点我放大）';
    root.appendChild(btn);
    var nte = document.createElement('div'); nte.className = 'v6note'; root.appendChild(nte);
    var hits = 0, miss = 0, sparks = [];
    function targets(){
      var w = S.w, h = S.h;
      return [ {x:w*0.3, y:h*0.55, r:16}, {x:w*0.7, y:h*0.55, r:16} ];
    }
    S.cv.addEventListener('pointerdown', function(e){
      var r = S.cv.getBoundingClientRect();
      var x = e.clientX - r.left, y = e.clientY - r.top;
      var ok = false;
      targets().forEach(function(t){
        var d = Math.hypot(x-t.x, y-t.y);
        if(d < (big ? t.r + 12 : t.r)) ok = true;
      });
      sparks.push({x:x, y:y, ok:ok, t:performance.now()});
      if(ok) hits++; else miss++;
      nte.textContent = '命中 ' + hits + ' · 落空 ' + miss;
    });
    btn.addEventListener('click', function(){
      big = !big;
      btn.textContent = big ? '热区：56px（视觉不变）' : '热区：32px（点我放大）';
    });
    var stop = loop(function(now){
      var ctx = S.ctx, w = S.w, h = S.h;
      ctx.clearRect(0,0,w,h);
      targets().forEach(function(t){
        /* 视觉尺寸固定 32px；命中半径随开关变化 */
        ctx.beginPath(); ctx.arc(t.x, t.y, 16, 0, 7);
        ctx.fillStyle = 'rgba(157,204,255,.22)'; ctx.fill();
        ctx.strokeStyle = 'rgba(157,204,255,.55)'; ctx.lineWidth = 1; ctx.stroke();
        if(big){
          ctx.beginPath(); ctx.arc(t.x, t.y, 28, 0, 7);
          ctx.setLineDash([3,3]); ctx.strokeStyle='rgba(111,240,192,.55)'; ctx.stroke(); ctx.setLineDash([]);
        }
        ctx.fillStyle='rgba(232,237,244,.75)'; ctx.font='10px ui-sans-serif'; ctx.textAlign='center';
        ctx.fillText('按钮', t.x, t.y+3.5);
      });
      sparks = sparks.filter(function(s){ return now - s.t < 700; });
      sparks.forEach(function(s){
        var a = 1 - (now - s.t)/700;
        ctx.beginPath(); ctx.arc(s.x, s.y, 4 + (1-a)*10, 0, 7);
        ctx.fillStyle = s.ok ? 'rgba(111,240,192,'+a*0.8+')' : 'rgba(255,143,163,'+a*0.8+')';
        ctx.fill();
      });
      ctx.textAlign='left';
      ctx.fillStyle='rgba(232,237,244,.32)'; ctx.font='10px ui-sans-serif';
      ctx.fillText('点按钮附近，试试差 4px 会不会落空', 10, h-10);
    });
    return stop;
  };

  /* =================================================================
     v07 · 全球化布局
     ================================================================= */
  M['v07'] = function(root){
    var langs = { zh:'导出报表', en:'Export report', de:'Bericht exportieren', ru:'Экспорт отчёта' };
    root.innerHTML =
      '<div class="v7wrap"><div class="v7langs">' +
        '<div class="v7lg on" data-l="zh">中文</div><div class="v7lg" data-l="en">EN</div>' +
        '<div class="v7lg" data-l="de">DE</div><div class="v7lg" data-l="ru">RU</div></div>' +
        '<div class="v7row"><span class="v7lab">定宽</span><div class="v7btn bad">导出报表</div>' +
          '<span style="font-size:9px;color:#ff9db0">← 文字被截断 / 溢出</span></div>' +
        '<div class="v7row"><span class="v7lab">自适应</span><div class="v7btn trunc">导出报表</div>' +
          '<span style="font-size:9px;color:#8fe3c2">← 省略号 + 可读</span></div>' +
        '<div class="v7row"><span class="v7lab">可换行</span><div class="v7btn auto">导出报表</div></div>' +
      '</div>';
    var bad = root.querySelector('.v7btn.bad'), trunc = root.querySelector('.v7btn.trunc'), auto = root.querySelector('.v7btn.auto');
    root.querySelectorAll('.v7lg').forEach(function(l){
      l.addEventListener('click', function(){
        root.querySelectorAll('.v7lg').forEach(function(x){ x.classList.remove('on'); });
        l.classList.add('on');
        var t = langs[l.dataset.l];
        bad.textContent = t; trunc.textContent = t; auto.textContent = t;
      });
    });
  };

  /* =================================================================
     v08 · 无伤虎先锋：帧率与闪避窗口
     ================================================================= */
  M['v08'] = function(root){
    var S = setup(root, +root.dataset.h || 176);
    var frames = [], hit = 0, dodgeWin = 0, ok = 0, lastAtk = 0, attacking = false;
    var hud = document.createElement('div'); hud.className='v8hud'; root.appendChild(hud);
    root.addEventListener('keydown', function(e){ if(e.code === 'Space'){ e.preventDefault(); judge(); } });
    S.cv.addEventListener('pointerdown', function(){ judge(); });
    function judge(){
      var now = performance.now();
      var inWin = attacking && (now - lastAtk) > 320 && (now - lastAtk) < 700;
      if(inWin){ ok++; attacking = false; }
    }
    var stop = loop(function(now, dt){
      var ctx = S.ctx, w = S.w, h = S.h;
      /* 帧时间：模拟 1060 显卡，40fps 上下抖动 */
      frames.push(16 + Math.abs(Math.sin(now*0.004))*22 + Math.random()*6);
      if(frames.length > 54) frames.shift();
      if(!attacking && now - lastAtk > 1500){ attacking = true; lastAtk = now; }
      if(attacking && now - lastAtk > 700) attacking = false;

      ctx.clearRect(0,0,w,h);
      /* 帧时间柱状图 */
      ctx.fillStyle='rgba(232,237,244,.14)'; ctx.fillRect(0, h*0.62, w, 1);
      frames.forEach(function(f,i){
        var bh = Math.min(f/60, 1) * h*0.5;
        var x = 8 + i*(w-16)/54;
        ctx.fillStyle = f > 30 ? 'rgba(255,210,138,.85)' : 'rgba(157,204,255,.55)';
        ctx.fillRect(x, h*0.62 - bh, (w-16)/54 - 1.2, bh);
      });
      /* 闪避窗口 */
      var prog = attacking ? Math.min((now-lastAtk)/700, 1) : 1;
      ctx.fillStyle='rgba(232,237,244,.10)'; ctx.fillRect(8, h*0.72, w-16, 10);
      ctx.fillStyle = attacking ? 'rgba(255,143,163,.85)' : 'rgba(111,240,192,.35)';
      ctx.fillRect(8, h*0.72, (w-16)*prog, 10);
      /* 窗口高亮段 320–700ms */
      var x1 = 8 + (w-16)*0.457, x2 = 8 + (w-16)*1.0;
      ctx.strokeStyle='rgba(111,240,192,.9)'; ctx.lineWidth=1.5;
      ctx.strokeRect(x1, h*0.72-2, Math.max(4,(x2-x1)), 14);
      hud.innerHTML = '<div>FPS ≈ ' + Math.round(1000/(frames.reduce(function(a,b){return a+b;},0)/frames.length)) +
                      ' · 帧时间 ' + Math.round(frames[frames.length-1]) + 'ms</div>' +
                      '<div class="v8hit">闪避成功 ' + ok + ' 次</div>' +
                      '<div style="color:rgba(232,237,244,.4)">攻击瞬间点画面 = 闪避</div>';
    });
    return stop;
  };

  /* =================================================================
     v09 · 寅虎：节奏判定
     ================================================================= */
  M['v09'] = function(root){
    var S = setup(root, +root.dataset.h || 176);
    var beats = [], t0 = performance.now(), idx = 0;
    var msgs = [], score = {perfect:0, good:0, miss:0};
    for(var i=0;i<999;i++) beats.push(t0 + i*620);
    function tap(){
      var now = performance.now();
      var best = 1e9, bi = -1;
      beats.forEach(function(b, i){ var d = Math.abs(now - b); if(d < best){ best = d; bi = i; } });
      var txt, col;
      if(best < 70){ txt='PERFECT'; col='#6ff0c0'; score.perfect++; }
      else if(best < 140){ txt='GOOD'; col='#bcdcff'; score.good++; }
      else { txt='MISS'; col='#ff8fa3'; score.miss++; }
      msgs.push({txt:txt, col:col, t:now});
    }
    S.cv.addEventListener('pointerdown', tap);
    var stop = loop(function(now){
      var ctx = S.ctx, w = S.w, h = S.h;
      ctx.clearRect(0,0,w,h);
      var cy = h*0.52, cx = w/2;
      /* 三条判定线 */
      ctx.strokeStyle='rgba(232,237,244,.12)'; ctx.lineWidth=1;
      [0.18,0.30].forEach(function(k){ ctx.beginPath(); ctx.arc(cx, cy, w*k, 0, 7); ctx.stroke(); });
      ctx.strokeStyle='rgba(111,240,192,.55)';
      ctx.beginPath(); ctx.arc(cx, cy, w*0.24, 0, 7); ctx.stroke();
      ctx.fillStyle='rgba(157,204,255,.9)'; ctx.beginPath(); ctx.arc(cx, cy, 5, 0, 7); ctx.fill();
      /* 节拍点向圆心收拢：周期 620ms */
      var period = 620;
      for(var i=0;i<10;i++){
        var bt = t0 + (Math.floor((now-t0)/period)+i)*period;
        var k = 1 - (bt - now)/period;   /* 0 → 1 收回 */
        var rr = w*(0.48 - 0.24*k);
        var a = 0.25 + 0.6*Math.max(0, k);
        ctx.beginPath(); ctx.arc(cx, cy, rr, 0, 7);
        ctx.strokeStyle = 'rgba(232,237,244,' + a + ')'; ctx.lineWidth = 1.4; ctx.stroke();
      }
      msgs = msgs.filter(function(m){ return now-m.t < 620; });
      msgs.forEach(function(m, i){
        var a = 1-(now-m.t)/620;
        ctx.globalAlpha = a; ctx.fillStyle = m.col; ctx.font='bold 13px ui-monospace,monospace';
        ctx.textAlign='center'; ctx.fillText(m.txt, cx, cy - 34 - i*3);
        ctx.globalAlpha = 1;
      });
      ctx.textAlign='left'; ctx.font='10px ui-monospace,monospace';
      ctx.fillStyle='rgba(232,237,244,.45)';
      ctx.fillText('PERFECT '+score.perfect+'  GOOD '+score.good+'  MISS '+score.miss, 10, h-10);
      ctx.fillStyle='rgba(232,237,244,.28)';
      ctx.fillText('点画面打拍子', w-92, h-10);
    });
    return stop;
  };

  /* =================================================================
     m01 · 字符幕布（竖向 Verlet 绳，横推会分开）
     ================================================================= */
  M['m01'] = function(root){
    var S = setup(root, +root.dataset.h || 176);
    var ropes = [], N = 11, P = 9, px = -9999;
    function build(){
      S.fit();
      ropes = [];
      for(var i=0;i<N;i++){
        var x = (i+0.5)*S.w/N, arr = [];
        for(var j=0;j<P;j++) arr.push({x:x, rx:x, y:8 + j/(P-1)*(S.h-24), vx:0});
        ropes.push(arr);
      }
    }
    build();
    S.cv.addEventListener('pointermove', function(e){
      var r = S.cv.getBoundingClientRect(); px = e.clientX - r.left;
    });
    S.cv.addEventListener('pointerleave', function(){ px = -9999; });
    var R = 34;
    var stop = loop(function(){
      var ctx = S.ctx, w = S.w, h = S.h;
      ctx.clearRect(0,0,w,h);
      ropes.forEach(function(arr){
        for(var j=1;j<P;j++){
          var n = arr[j], fx = (n.rx - n.x)*0.055, f = 0;
          if(Math.abs(px - n.x) < R){ f = (n.x - px)/R * 5.2 * (1 - Math.abs(px-n.x)/R); }
          n.vx = (n.vx + fx + f) * 0.90;
          n.x += n.vx;
          n.x = n.x*0.72 + arr[j-1].x*0.28;
        }
        arr[0].x = arr[0].rx;
        ctx.beginPath();
        ctx.moveTo(arr[0].x, arr[0].y);
        for(var j=1;j<P;j++) ctx.lineTo(arr[j].x, arr[j].y);
        var v = Math.abs(arr[P-1].vx);
        ctx.strokeStyle = 'rgba(157,204,255,' + Math.min(0.25+v*0.5, 1) + ')';
        ctx.lineWidth = 1.3; ctx.stroke();
        ctx.fillStyle = 'rgba(232,237,244,' + Math.min(0.35+v*0.4, 0.9) + ')';
        ctx.beginPath(); ctx.arc(arr[P-1].x, arr[P-1].y, 1.4, 0, 7); ctx.fill();
      });
    });
    return stop;
  };

  /* =================================================================
     m02 · 拨弦落词，乌鸦改写尾巴
     ================================================================= */
  M['m02'] = function(root){
    var S = setup(root, +root.dataset.h || 176);
    var strings = [], words = [], crows = [];
    function build(){
      S.fit();
      strings = [];
      var top = Math.max(14, S.h*0.14), bot = S.h*0.86;
      for(var i=0;i<6;i++){
        var arr = [];
        for(var j=0;j<10;j++) arr.push({x:(i+0.6)*S.w/6.4, y:top + j/(9)*(bot-top), vx:0});
        strings.push(arr);
      }
      words = []; crows = [];
      for(var c=0;c<3;c++) crows.push({x:rnd(20,S.w-20), y:rnd(top, bot), tx:0, ty:0, word:'', a:1});
    }
    build();
    var WORD = ['ECHO','GLASS','MOTION','LOOP','TYPE'];
    function pluck(x){
      strings.forEach(function(s, i){
        var sx = s[0].x;
        if(Math.abs(sx - x) < 16){
          for(var j=1;j<s.length;j++) s[j].vx += rnd(-1.4, 1.4);
          if(words.length < 3){
            words.push({x:sx, y:S.h*0.8, vy:-30, t:WORD[Math.floor(Math.random()*WORD.length)], a:1});
            crows.forEach(function(c){ if(!c.target || c.a<=0){ c.tx = sx + rnd(-12,12); c.ty = 100; c.a = 1; } });
          }
        }
      });
    }
    S.cv.addEventListener('pointerdown', function(e){
      var r = S.cv.getBoundingClientRect();
      pluck(e.clientX - r.left);
    });
    var autoT = setInterval(function(){
      pluck(strings[Math.floor(Math.random()*strings.length)][0].x);
    }, 2400);
    setTimeout(function(){ pluck(strings[1][0].x); pluck(strings[4][0].x); }, 260);
    var stop = loop(function(now, dt){
      var ctx = S.ctx, w = S.w, h = S.h;
      ctx.clearRect(0,0,w,h);
      strings.forEach(function(s){
        for(var j=1;j<s.length;j++){
          s[j].vx = (s[j].vx + (s[0].x - s[j].x)*0.09) * 0.90;
          s[j].x += s[j].vx;
        }
        ctx.beginPath(); ctx.moveTo(s[0].x, s[0].y);
        for(var j=1;j<s.length;j++) ctx.lineTo(s[j].x, s[j].y);
        ctx.strokeStyle='rgba(157,204,255,.35)'; ctx.lineWidth=1; ctx.stroke();
      });
      words.forEach(function(wd){
        wd.y += wd.vy*dt; wd.vy *= 0.985;
        ctx.fillStyle = 'rgba(255,210,138,'+wd.a+')'; ctx.font='bold 11px ui-monospace,monospace';
        ctx.textAlign='center'; ctx.fillText(wd.t, wd.x, wd.y);
      });
      words = words.filter(function(wd){ return wd.a > 0.05; });
      crows.forEach(function(c){
        if(c.a <= 0.05) return;
        var tw = words[0];
        if(tw){ c.tx = tw.x; c.ty = tw.y; }
        c.x += (c.tx - c.x)*0.05; c.y += (c.ty - c.y)*0.05;
        if(tw && Math.hypot(c.x-tw.x, c.y-tw.y) < 14){
          c.word = tw.t; tw.a -= 0.09;
        }
        ctx.save(); ctx.translate(c.x, c.y);
        var dir = (c.tx >= c.x) ? 1 : -1; ctx.scale(dir, 1);
        ctx.beginPath();
        ctx.moveTo(7, 0); ctx.lineTo(-6, -6); ctx.lineTo(-3, 0); ctx.lineTo(-6, 6);
        ctx.closePath();
        ctx.fillStyle='rgba(238,242,247,'+c.a+')'; ctx.fill();
        ctx.restore();
        if(c.word){
          ctx.save(); ctx.translate(c.x-10, c.y+14); ctx.rotate(-0.12);
          ctx.fillStyle='rgba(157,204,255,'+c.a+')'; ctx.font='9px ui-monospace,monospace'; ctx.textAlign='center';
          ctx.fillText(c.word, 0, 0); ctx.restore();
        }
      });
      ctx.textAlign='left'; ctx.fillStyle='rgba(232,237,244,.32)'; ctx.font='10px ui-sans-serif';
      ctx.fillText('点竖向的弦拨一下', 10, h-9);
    });
    return stop;
  };

  /* =================================================================
     m03 · 绳钟：24 节跟随链
     ================================================================= */
  M['m03'] = function(root){
    var S = setup(root, +root.dataset.h || 176);
    var t0 = performance.now();
    function chain(ctx, cx, cy, ang, len, seg, width, col){
      var pts = [{x:cx, y:cy}];
      var tx = cx + Math.cos(ang)*len, ty = cy + Math.sin(ang)*len;
      for(var i=1;i<=seg;i++){
        var k = i/seg;
        var px = pts[i-1].x, py = pts[i-1].y;
        var dx = (cx + (tx-cx)*k) - px, dy = (cy + (ty-cy)*k) - py;
        var sag = Math.sin(Math.PI*k) * (len*0.06);
        var nx = px + dx*0.55, ny = py + dy*0.55 + sag*0.5;
        pts.push({x:nx, y:ny});
      }
      ctx.beginPath(); ctx.moveTo(pts[0].x, pts[0].y);
      for(var j=1;j<pts.length;j++) ctx.lineTo(pts[j].x, pts[j].y);
      ctx.strokeStyle = col; ctx.lineWidth = width; ctx.lineCap='round'; ctx.stroke();
    }
    var stop = loop(function(now){
      var ctx = S.ctx, w = S.w, h = S.h;
      ctx.clearRect(0,0,w,h);
      var cx = w/2, cy = h/2 + 4, R = Math.min(w,h)*0.36;
      ctx.beginPath(); ctx.arc(cx, cy, R, 0, 7);
      ctx.strokeStyle='rgba(232,237,244,.14)'; ctx.lineWidth=1; ctx.stroke();
      for(var i=0;i<12;i++){
        var a = i/12*Math.PI*2 - Math.PI/2;
        ctx.beginPath();
        ctx.arc(cx + Math.cos(a)*R, cy + Math.sin(a)*R, i%3===0?2:1, 0, 7);
        ctx.fillStyle='rgba(232,237,244,.4)'; ctx.fill();
      }
      var tt = (now - t0)/1000;
      var minute = (tt*0.35 % (Math.PI*2)) - Math.PI/2;
      var hour = (tt*0.03 % (Math.PI*2)) - Math.PI/2;
      chain(ctx, cx, cy, hour, R*0.55, 16, 3, 'rgba(157,204,255,.85)');
      chain(ctx, cx, cy, minute, R*0.82, 24, 2, 'rgba(255,210,138,.9)');
      ctx.beginPath(); ctx.arc(cx, cy, 3.5, 0, 7); ctx.fillStyle='#fff'; ctx.fill();
      ctx.fillStyle='rgba(232,237,244,.32)'; ctx.font='10px ui-sans-serif';
      ctx.fillText('两端位置正确，中间 24 节拒绝成直线', 10, h-9);
    });
    return stop;
  };

  /* =================================================================
     m04 · 粘性堆叠（真 DOM 滚动）
     ================================================================= */
  M['m04'] = function(root){
    var cols = ['#274a63','#3a3560','#1f5048'];
    var html = '<div class="m4scroll"><div class="m4wrap">';
    var copy = ['封面：先立起整页的胆', '正文：滚动反推进度', '图表：用进度擦出数据', '收尾：叠到顶再一起走'];
    for(var i=0;i<4;i++){
      html += '<div class="m4screen" style="background:linear-gradient(160deg,'+cols[i%3]+',#12181d 90%)">' +
              '<b>0'+(i+1)+' · '+copy[i]+'</b><span>sticky · top:0 · 用滚动位置驱动进度</span>' +
              '<div class="m4bar" style="width:'+((i+1)*22)+'%"></div></div>';
    }
    html += '</div></div>';
    root.innerHTML = '<div class="mini-chip">在框里滚动</div>' + html;
    var H = +root.dataset.h || 176;
    var sc = root.querySelector('.m4scroll');
    sc.style.height = '100%';
    root.querySelectorAll('.m4screen').forEach(function(el){
      el.style.height = Math.round(H * 0.62) + 'px';
    });
    var last = -1;
    function onScroll(){
      var p = Math.round(sc.scrollTop / 140);
      var bars = root.querySelectorAll('.m4bar');
      bars.forEach(function(b, i){ b.style.opacity = i <= p ? 1 : 0.25; });
      last = p;
    }
    sc.addEventListener('scroll', onScroll);
    onScroll();
    var auto = setInterval(function(){
      if(sc._touch) return;
      var max = sc.scrollHeight - sc.clientHeight;
      var next = sc.scrollTop + Math.round(H * 0.5);
      sc.scrollTo({top: next > max ? 0 : next, behavior:'smooth'});
    }, 2600);
    sc.addEventListener('pointerdown', function(){ sc._touch = 1; });
    sc.addEventListener('pointerup', function(){ sc._touch = 0; });
    return function(){ clearInterval(auto); };
  };

  /* =================================================================
     m05 · 滚轮被劫持（文档不动）
     ================================================================= */
  M['m05'] = function(root){
    var S = setup(root, +root.dataset.h || 176);
    var target = 0, cur = 0, spin = 0;
    /* 卡片里不劫持滚轮（否则页面滚不动），改成横向拖动来推轨道 */
    var dragging = false, lastX = 0;
    S.cv.addEventListener('pointerdown', function(e){ dragging = true; lastX = e.clientX; });
    window.addEventListener('pointerup', function(){ dragging = false; });
    S.cv.addEventListener('pointermove', function(e){
      if(!dragging) return;
      target += (e.clientX - lastX) * 1.4;
      target = Math.max(-240, Math.min(240, target));
      lastX = e.clientX;
    });
    /* 没有拖动时自己慢慢走，画面不静止 */
    var auto = 0;
    var stop = loop(function(now, dt){
      var ctx = S.ctx, w = S.w, h = S.h;
      auto += dt * 26;
      if(!dragging) target *= (1 - Math.min(1, dt*0.55));
      cur += (target + auto - cur) * (1 - Math.exp(-6.2*dt));
      spin += dt*0.6;
      ctx.clearRect(0,0,w,h);
      var layers = [ {k:0.35, y:h*0.40, w1:1.0, col:'rgba(157,204,255,.16)'},
                     {k:0.65, y:h*0.62, w1:1.5, col:'rgba(157,140,255,.16)'},
                     {k:1.0,  y:h*0.84, w1:2.1, col:'rgba(79,209,165,.15)'} ];
      layers.forEach(function(L){
        for(var i=-2;i<9;i++){
          var x = ((i*90 + cur*L.k) % (w+180)) - 90;
          ctx.fillStyle = L.col;
          ctx.fillRect(x, L.y - 18*L.w1, 62*L.w1, 18*L.w1);
        }
      });
      /* 分层的「词」：用轨道进度驱动低位升起 */
      var words = ['MOTION','RAIL','SCROLL','LAG','DEPTH','FLOW'];
      for(var q=0;q<6;q++){
        var k = (q % 3 === 0) ? 0.4 : (q % 3 === 1 ? 0.7 : 1);
        var x = ((q*137 + cur*k*0.6) % (w+80)) - 40;
        var rise = Math.abs(Math.sin((cur*k)/160 + q))*h*0.1;
        ctx.fillStyle = 'rgba(238,242,247,' + (0.1 + k*0.16) + ')';
        ctx.font = (9 + k*5).toFixed(0) + 'px ui-monospace,monospace';
        ctx.fillText(words[q], x, h*0.30 - rise);
      }
      /* 雷达 */
      var cx = w*0.82, cy = h*0.3, R = 22;
      ctx.beginPath(); ctx.arc(cx, cy, R, 0, 7);
      ctx.strokeStyle='rgba(232,237,244,.18)'; ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx,cy);
      ctx.arc(cx, cy, R, spin, spin+0.9); ctx.closePath();
      ctx.fillStyle='rgba(157,204,255,.22)'; ctx.fill();
      ctx.fillStyle='rgba(232,237,244,.32)'; ctx.font='10px ui-sans-serif';
      ctx.fillText('横向拖动：轨道动，文档 scrollY 恒 0', 10, 16);
      ctx.fillStyle='rgba(232,237,244,.2)';
      ctx.fillText('轨道位移 ' + Math.round(cur) + 'px', 10, h-9);
    });
    return stop;
  };

  /* =================================================================
     m06 · 翻页动画：12Hz 停格 + 4 姿态
     ================================================================= */
  M['m06'] = function(root){
    var S = setup(root, +root.dataset.h || 176);
    var ang = 0, vel = 0, dragging = false, lastX = 0, squash = 0;
    S.cv.addEventListener('pointerdown', function(e){ dragging = true; lastX = e.clientX; vel = 0; });
    window.addEventListener('pointerup', function(){ dragging = false; });
    S.cv.addEventListener('pointermove', function(e){
      if(!dragging) return;
      var dx = e.clientX - lastX; lastX = e.clientX;
      vel += dx * 0.02;
    });
    /* 没人动的时候自己翻：每 3.4s 甩一下 */
    var auto = setInterval(function(){ if(!dragging) vel += 0.55; }, 3400);
    var stop = loop(function(now, dt){
      var ctx = S.ctx, w = S.w, h = S.h;
      if(!dragging){ ang += vel; vel *= 0.96; }
      else { ang += vel; vel *= 0.6; }
      if(Math.abs(vel) > 0.42) squash = Math.min(1, Math.abs(vel) - 0.4);
      squash *= 0.93;
      /* 12Hz 停格量化成 4 个姿态 */
      var stepT = Math.floor(now/83.3);
      var pose = ((Math.floor(ang / (Math.PI/2)) % 4) + 4) % 4;
      ctx.clearRect(0,0,w,h);
      var cx = w/2, cy = h*0.54, s = Math.min(w,h)*0.42;
      ctx.save();
      ctx.translate(cx, cy);
      ctx.scale(1 - squash*0.16, 1 + squash*0.16);
      /* 桌面 */
      ctx.beginPath(); ctx.ellipse(0, s*1.06, s*0.9, s*0.1, 0, 0, 7);
      ctx.fillStyle='rgba(0,0,0,.35)'; ctx.fill();
      ctx.rotate(pose * Math.PI/2);
      ctx.fillStyle='rgba(157,204,255,.2)';
      ctx.strokeStyle='rgba(157,204,255,.85)'; ctx.lineWidth=1.6;
      ctx.beginPath(); ctx.roundRect(-s*0.42, -s*0.42, s*0.84, s*0.84, s*0.16);
      ctx.fill(); ctx.stroke();
      ctx.beginPath(); ctx.arc(0, 0, s*0.12, 0, 7); ctx.fillStyle='rgba(255,210,138,.85)'; ctx.fill();
      ctx.restore();
      ctx.fillStyle='rgba(232,237,244,.32)'; ctx.font='10px ui-sans-serif';
      ctx.fillText('横向拖动 / 快速甩 → 4 姿态硬切', 10, h-9);
      ctx.fillStyle='rgba(232,237,244,.16)';
      ctx.fillText('pose ' + (pose+1) + ' · 12Hz', w-78, h-9);
      /* 四个姿态的刻度 */
      for(var q=0;q<4;q++){
        ctx.beginPath();
        ctx.arc(w/2 + (q-1.5)*22, h-26, q === pose ? 3.4 : 2, 0, 7);
        ctx.fillStyle = q === pose ? 'rgba(157,204,255,.95)' : 'rgba(238,242,247,.22)';
        ctx.fill();
      }
    });
    return function(){ stop(); clearInterval(auto); };
  };

  /* =================================================================
     m07 · 手绘 3D：胶囊骨架 + 11Hz boil
     ================================================================= */
  M['m07'] = function(root){
    var S = setup(root, +root.dataset.h || 176);
    var t0 = performance.now(), stepT = -1, jit = [];
    for(var k=0;k<12;k++) jit.push({x:0, y:0});
    /* 胶囊骨架（屏幕空间，按画布尺寸缩放） */
    var bones = [
      {x:0, y:-46, x2:0, y2:-24, r:6},     /* 头 → 颈 */
      {x:0, y:-24, x2:0, y2:14, r:8},      /* 躯干 */
      {x:0, y:-6, x2:-26, y2:2, r:5},      /* 左臂 */
      {x:0, y:-6, x2:26, y2:2, r:5},       /* 右臂 */
      {x:-8, y:14, x2:-16, y2:46, r:5},    /* 左腿 */
      {x:8, y:14, x2:16, y2:46, r:5}       /* 右腿 */
    ];
    var stop = loop(function(now){
      var ctx = S.ctx, w = S.w, h = S.h;
      var st = Math.max(0, Math.floor((now - t0)/91));   /* ≈11Hz */
      if(st !== stepT || jit.length < 12){
        stepT = st; jit = [];
        for(var i=0;i<12;i++) jit.push({x:(Math.random()-0.5)*1.6, y:(Math.random()-0.5)*1.6});
      }
      ctx.clearRect(0,0,w,h);
      var sc = Math.min(w/320, h/180) * 1.15;
      var cx = w/2, cy = h*0.52, t = now*0.0006;
      /* 地面 */
      ctx.beginPath(); ctx.ellipse(cx, cy + 54*sc, 42*sc, 7*sc, 0, 0, 7);
      ctx.fillStyle = 'rgba(0,0,0,.42)'; ctx.fill();
      ctx.save();
      ctx.translate(cx, cy);
      ctx.scale(sc, sc);
      function pass(color, grow){
        bones.forEach(function(b, i){
          var sw = Math.sin(t + i*0.9) * 0.06;
          var x1 = b.x + jit[i].x, y1 = b.y + jit[i].y;
          var x2 = b.x2 + jit[i].x, y2 = b.y2 + jit[i].y;
          var mx = (x1+x2)/2, my = (y1+y2)/2, dx = x2-x1, dy = y2-y1;
          ctx.beginPath();
          ctx.lineCap = 'round';
          ctx.lineWidth = b.r*2 + grow;
          ctx.strokeStyle = color;
          /* 轻微摆动：绕中点旋转 */
          var ca = Math.cos(sw), sa = Math.sin(sw);
          function rot(px, py){
            px -= mx; py -= my;
            return [mx + px*ca - py*sa, my + px*sa + py*ca];
          }
          var p1 = rot(x1,y1), p2 = rot(x2,y2);
          ctx.moveTo(p1[0], p1[1]); ctx.lineTo(p2[0], p2[1]);
          ctx.stroke();
        });
      }
      pass('rgba(14,18,22,1)', 5);        /* 外描边 */
      pass('rgba(244,247,250,1)', 0);     /* 白色回填，吃掉内部接缝 */
      /* 眼睛：二值调色板 */
      ctx.fillStyle = '#0e1216';
      ctx.beginPath(); ctx.arc(-6.5, -40, 3, 0, 7); ctx.fill();
      ctx.beginPath(); ctx.arc( 6.5, -40, 3, 0, 7); ctx.fill();
      /* 手部小球 */
      ctx.fillStyle = 'rgba(244,247,250,1)';
      ctx.beginPath(); ctx.arc(-26 + jit[2].x, 2 + jit[2].y, 5.4, 0, 7); ctx.fill();
      ctx.beginPath(); ctx.arc( 26 + jit[3].x, 2 + jit[3].y, 5.4, 0, 7); ctx.fill();
      ctx.restore();
      /* 颗粒 */
      for(var g=0; g<26; g++){
        ctx.fillStyle = 'rgba(255,255,255,' + (Math.random()*0.045) + ')';
        ctx.fillRect(Math.random()*w, Math.random()*h, 1.4, 1.4);
      }
      ctx.fillStyle='rgba(232,237,244,.32)'; ctx.font='10px ui-sans-serif';
      ctx.fillText('描边只在深度断点 · 每秒 11 次抖动', 10, h-9);
      ctx.textAlign='right'; ctx.fillStyle='rgba(232,237,244,.16)';
      ctx.fillText('2 值调色板', w-10, h-9); ctx.textAlign='left';
    });
    return stop;
  };
})();
"""
