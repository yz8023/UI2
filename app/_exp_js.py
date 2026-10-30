# -*- coding: utf-8 -*-
"""体验馆 + 项目结构 + 全局搜索的前端逻辑（注入到 App 里）。"""

EXP_JS = r"""
/* ══════════════ 体验馆（XPopup / motion-web）· 项目结构 · 全局搜索 ══════════════ */
(function(){
  var TYPES = window.__XPTYPES, ANIMS = window.__XPANIMS, SETTINGS = window.__XPSET,
      GEST = window.__XPGEST, RECIPES = window.__MRECIPES, SPECS = window.__MSPECS,
      TOKENS = window.__MTOKENS, PROJ = window.__MPROJ;

  var EX = { hall:'xp', xp:'list', mw:'case', proj:'webapp', feats:{popup:1, nav:1, form:1, motion:1},
             specOpen:-1, lab:'duration', labIdx:0 };

  function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }

  function seg(items, cur, attr){
    return '<div class="xp-seg">' + items.map(function(x){
      return '<b class="' + (x[0] === cur ? 'on' : '') + '" data-' + attr + '="' + x[0] + '">' + x[1] + '</b>';
    }).join('') + '</div>';
  }

  /* ─────────── XPopup：弹窗 ─────────── */
  function xpList(){
    var groups = {}, order = [];
    TYPES.forEach(function(t){
      if(!groups[t[0]]){ groups[t[0]] = []; order.push(t[0]); }
      groups[t[0]].push(t);
    });
    return order.map(function(g){
      return '<div class="xp-group">' + esc(g) + ' · ' + groups[g].length + '</div><div class="xp-list">' +
        groups[g].map(function(t){
          return '<div class="xp-item" data-xp="' + t[1] + '">' +
            '<div class="ico">◱</div><div class="txt"><h4>' + esc(t[2]) + ' <i>' + esc(t[3]) + '</i></h4>' +
            '<p>' + esc(t[4]) + '</p><div class="chips">' +
            t[5].map(function(c){ return '<s>' + esc(c) + '</s>'; }).join('') +
            '</div></div><div class="go">›</div></div>';
        }).join('') + '</div>';
    }).join('');
  }

  /* ─────────── XPopup：动画 ─────────── */
  function xpAnim(){
    return '<div class="note" style="margin:10px 2px 12px">PopupAnimation 的全部 20 个枚举值。点任意一个看效果；' +
      'XPopup 会按弹窗类型自动兜底一个最合适的，你不必手动指定。</div>' +
      '<div class="an-grid">' + ANIMS.map(function(a, i){
        return '<div class="an-t" data-anim="' + i + '"><b>' + (i + 1) + '</b>' +
          '<div class="an-stage"><div class="an-card"></div></div>' +
          '<span>' + esc(a[1]) + '</span><em>' + esc(a[0]) + '</em></div>';
      }).join('') + '</div>' +
      '<div class="actrow" style="margin-top:14px"><button class="btn primary" id="anAll">全部播一遍</button>' +
      '<span class="tip">时长 360ms（animationDuration）</span></div>';
  }

  /* ─────────── XPopup：设置 ─────────── */
  var LIVE = { dismissOnTouchOutside:'dismissOutside', dismissOnBackPressed:'dismissBack',
               hasShadowBg:'shadow', hasBlurBg:'blur', isDarkTheme:'dark',
               enableDrag:'drag', isThreeDrag:'three' };
  function xpSet(){
    var groups = {}, order = [];
    SETTINGS.forEach(function(s){
      if(!groups[s[0]]){ groups[s[0]] = []; order.push(s[0]); }
      groups[s[0]].push(s);
    });
    return '<div class="note" style="margin:10px 2px 12px">XPopup.Builder 的 45 个方法，按用途分了组。' +
      '带开关的会真的作用到上面的弹窗；灰掉的是需要 Android 环境才有意义的。</div>' +
      order.map(function(g){
        return '<div class="xp-group">' + g + '</div><div class="setlist">' +
          groups[g].map(function(s){
            var live = !!LIVE[s[1]];
            var on = live && window.__XP.get()[LIVE[s[1]]];
            return '<div class="setrow2"><div class="lab"><b>' + esc(s[2]) + '</b>' +
              '<code>' + esc(s[1]) + '</code><p>' + esc(s[4]) + '</p></div>' +
              '<div class="ctl">' + (live
                ? '<div class="mini-sw ' + (on ? 'on' : '') + '" data-set="' + s[1] + '"></div>'
                : '<span class="mini-val">' + esc(String(s[3])) + '</span>') + '</div></div>';
          }).join('') + '</div>';
      }).join('');
  }

  /* ─────────── XPopup：手势 ─────────── */
  function xpGest(){
    return '<div class="note" style="margin:10px 2px 12px">这些是「手感」的部分，光看代码看不出来，只能玩。</div>' +
      GEST.map(function(g){
        return '<div class="xp-item" data-gest="' + g[0] + '" style="margin-bottom:8px">' +
          '<div class="ico">✋</div><div class="txt"><h4>' + esc(g[1]) + '</h4><p>' + esc(g[2]) + '</p></div>' +
          '<div class="go">›</div></div>';
      }).join('') +
      '<div class="mini-demo" id="gestStage"><div class="tag">手势实验台</div>' +
      '<div class="hint">滚轮 / 拖动试试</div></div>';
  }

  /* ─────────── motion-web：案例 ─────────── */
  function mwCase(){
    var cases = (window.__ITEMS || []).filter(function(it){ return it.coll === 'motion'; });
    return '<div class="note" style="margin:10px 2px 12px">motion-web 的 7 个完整 case，每个都是可跑的长页面（Canvas / DOM 物理）。' +
      '点卡片进详情，或直接打开完整演示页。</div>' +
      cases.map(function(it, i){
        var slug = (it.src || '').replace('motion-web · ', '');
        return '<div class="xp-item" data-case="' + it.id + '" style="margin-bottom:8px">' +
          '<div class="ico">◈</div><div class="txt"><h4>' + esc(it.name) +
          ' <i>cases/' + esc(slug) + '</i></h4>' +
          '<p>' + esc(it.title) + '。' + esc(it.mech.slice(0, 46)) + '…</p>' +
          '<div class="chips"><s>全屏演示</s><s>' + esc(it.diff) + ' 难度</s><s>可在 7 个之间切换</s></div></div>' +
          '<div class="go">›</div></div>';
      }).join('');
  }



  /* ─────────── 案例剧场：全屏尺寸的单个 case ─────────── */
  function caseList(){
    return (window.__ITEMS || []).filter(function(it){ return it.coll === 'motion'; });
  }

  function caseHTML(id){
    var list = caseList();
    var i = 0;
    for(var k=0;k<list.length;k++) if(list[k].id === id) i = k;
    if(i < 0) i = 0;
    var it = list[i];
    var prev = list[(i - 1 + list.length) % list.length], next = list[(i + 1) % list.length];
    var slug = (it.src || '').replace('motion-web · ', '');
    var rail = list.map(function(c, j){
      return '<div class="th-tab' + (c.id === it.id ? ' on' : '') + '" data-case="' + c.id + '">' +
        '<b>' + (j + 1) + '</b><span>' + esc(c.name) + '</span></div>';
    }).join('');
    return '<div class="backrow" data-hall="mw">‹ 体验馆</div>' +
      '<h1 class="th-title">' + esc(it.name) + '</h1>' +
      '<div class="th-sub">' + esc(it.title) + '</div>' +
      '<div class="th-meta"><s>cases/' + esc(slug) + '</s><s>' + esc(it.dur) + '</s><s>' + esc(it.diff) + '</s><s>canvas 2D</s></div>' +
      '<div class="th-stage" id="thStage"><div class="mini th-mini" data-mini="' + it.id + '" data-h="380">' +
        '<div class="th-hint">在画面上拖动试试</div></div></div>' +
      '<div class="th-info">' +
        '<div class="th-k"><em>机制</em><p>' + esc(it.mech) + '</p></div>' +
        '<div class="th-k"><em>关键参数</em><p>' + esc(it.params) + '</p></div>' +
        '<div class="th-k"><em>判据</em><p>' + esc(it.verify) + '</p></div>' +
      '</div>' +
      '<div class="actrow" style="margin-top:12px">' +
        '<button class="btn primary" id="thCopy">复制提示词</button>' +
        '<a class="btn ghost" href="' + esc(it.path) + '" target="_blank" rel="noopener">完整演示页 ↗</a>' +
        '<button class="btn ghost" data-open="' + it.id + '">素材详情</button>' +
      '</div>' +
      '<div class="sec">7 个案例 · 直接切</div>' +
      '<div class="th-tabs">' + rail + '</div>' +
      '<div class="th-pn">' +
        '<div class="th-p" data-case="' + prev.id + '">‹ ' + esc(prev.name) + '</div>' +
        '<div class="th-p" data-case="' + next.id + '">' + esc(next.name) + ' ›</div>' +
      '</div>';
  };

  /* ─────────── motion-web：配方 ─────────── */
  function mwRecipe(){
    return '<div class="note" style="margin:10px 2px 12px">pattern-recipes.md 的 20 条配方，每条都在跑。' +
      '标题与「用来做什么」取自上游原文。</div>' +
      RECIPES.map(function(r, i){
        return '<div style="margin-bottom:14px"><div style="display:flex;gap:8px;align-items:baseline;margin-bottom:6px">' +
          '<span style="font-size:10px;color:rgba(157,204,255,.9);font-family:ui-monospace,Menlo,monospace">' +
          (r.no < 10 ? '0' + r.no : r.no) + '</span>' +
          '<b style="font-size:12.5px">' + esc(r.name) + '</b></div>' +
          '<div style="font-size:10px;color:rgba(233,239,247,.45);line-height:1.65;margin-bottom:6px">' +
          esc(r.what) + '</div>' +
          '<div class="mini-demo" style="height:200px;margin-top:0"><div class="mr" data-rec="' + i +
          '" style="position:absolute;inset:0;display:grid;place-items:center;padding:12px"></div>' +
          '<button class="cpbtn" data-cp-rec="' + i + '">复制提示词</button></div>' +
          '<div class="recuse">用来做什么：' + esc(r.use) + '</div></div>';
      }).join('');
  }

  /* ─────────── motion-web：令牌实验室 ─────────── */
  function mwToken(){
    var tabs = [['duration','时长 7 档'],['easing','曲线 9 条'],['spring','弹簧 6 组'],['stagger','错峰 5 种']];
    return seg(tabs, EX.lab, 'lab') +
      '<div class="mini-demo" id="labStage" style="height:190px;margin-top:10px">' +
      '<div class="tag" id="labTag">点下面的行换参数</div><div class="hint">点一下重播</div></div>' +
      '<div id="labRows" style="margin-top:10px">' + labRows() + '</div>';
  }

  function labRows(){
    if(EX.lab === 'duration'){
      return TOKENS.duration.map(function(d, i){
        return '<div class="xp-item" data-dur="' + i + '" style="margin-bottom:6px;padding:9px 11px">' +
          '<div class="txt"><h4>' + esc(d[0]) + ' <i>' + esc(d[1]) + '</i></h4><p>' + esc(d[2]) + '</p></div>' +
          '<div class="go">▶</div></div>';
      }).join('');
    }
    if(EX.lab === 'easing'){
      return TOKENS.easing.map(function(d, i){
        return '<div class="xp-item" data-ease="' + i + '" style="margin-bottom:6px;padding:9px 11px">' +
          '<div class="txt"><h4>' + esc(d[0]) + ' <i>' + esc(d[1]) + '</i></h4><p>' + esc(d[2]) + '</p></div>' +
          '<div class="go">▶</div></div>';
      }).join('');
    }
    if(EX.lab === 'spring'){
      return TOKENS.spring.map(function(d, i){
        return '<div class="xp-item" data-spring="' + i + '" style="margin-bottom:6px;padding:9px 11px">' +
          '<div class="txt"><h4>' + esc(d[0]) + ' <i>k ' + d[1] + ' · c ' + d[2] + '</i></h4><p>' + esc(d[4]) + '</p></div>' +
          '<div class="go">▶</div></div>';
      }).join('');
    }
    return TOKENS.stagger.map(function(d, i){
      return '<div class="xp-item" data-stag="' + i + '" style="margin-bottom:6px;padding:9px 11px">' +
        '<div class="txt"><h4>' + esc(d[0]) + ' <i>' + d[1] + 'ms</i></h4><p>' + esc(d[2]) + '</p></div>' +
        '<div class="go">▶</div></div>';
    }).join('');
  }

  /* ─────────── motion-web：规范索引 ─────────── */
  function mwSpec(){
    return '<div class="note" style="margin:10px 2px 12px">references/ 下的 25 篇规范原文索引：标题、' +
      '首段摘录与真实章节列表（章节名按上游原样保留）。点开看结构，照着写就不会跑偏。</div>' +
      SPECS.map(function(s, i){
        var open = EX.specOpen === i;
        return '<div class="spec" data-spec="' + i + '" style="margin-bottom:8px;border-radius:14px;' +
          'border:1px solid rgba(255,255,255,.1);background:rgba(255,255,255,.035);padding:12px 13px;cursor:pointer">' +
          '<div style="display:flex;gap:8px;align-items:baseline"><b style="font-size:12.5px">' + esc(s.title) + '</b>' +
          '<span style="margin-left:auto;font-size:9.5px;color:rgba(233,239,247,.32)">' +
          s.secs.length + ' 节</span></div>' +
          '<div style="font-size:10.5px;color:rgba(233,239,247,.72);line-height:1.7;margin-top:5px">' +
            esc((window.__SPECZH || {})[s.file] || s.lede) + '</div>' +
          '<div style="font-size:9px;color:rgba(233,239,247,.3);line-height:1.6;margin-top:3px">原文：' +
            esc(String(s.lede).slice(0, 78)) + '…</div>' +
          (open ? '<div style="margin-top:9px;padding-top:9px;border-top:1px solid rgba(255,255,255,.08);' +
            'font-size:10.5px;line-height:1.9;color:rgba(157,204,255,.85)">' +
            s.secs.map(function(h){ return '· ' + esc(h); }).join('<br>') + '</div>' : '') +
          '<div style="margin-top:7px;font-size:9px;color:rgba(233,239,247,.28);font-family:ui-monospace,Menlo,monospace">' +
          esc(s.file) + '</div></div>';
      }).join('');
  }

  /* ─────────── 体验馆总装 ─────────── */
  window.__EXP = {};
  window.__EXP.expHTML = function(){
    var head = '<h1 class="title" style="font-size:22px">体验馆</h1>' +
      '<div class="lede2">两个项目的全部内容，做成能直接玩的样子：' +
      '<b>XPopup</b> 的 20 个弹窗 / 20 个动画 / 45 个设置 / 5 个手势，' +
      '<b>motion-web</b> 的 7 个 case / 20 条配方 / 4 组令牌 / 25 篇规范。</div>' +
      seg([['xp','XPopup · 弹层'],['mw','motion-web · 动效']], EX.hall, 'hall');
    var body = '';
    if(EX.hall === 'xp'){
      body = seg([['list','弹窗 20'],['anim','动画 20'],['set','设置 45'],['gest','手势 5']], EX.xp, 'xptab') +
        (EX.xp === 'list' ? xpList() : EX.xp === 'anim' ? xpAnim() : EX.xp === 'set' ? xpSet() : xpGest());
    } else {
      body = seg([['case','案例 7'],['rec','配方 20'],['tok','令牌'],['spec','规范 25']], EX.mw, 'mwtab') +
        (EX.mw === 'case' ? mwCase() : EX.mw === 'rec' ? mwRecipe() : EX.mw === 'tok' ? mwToken() : mwSpec());
    }
    return head + body;
  };

  /* ─────────── 项目结构 ─────────── */
  function treeHTML(){
    var p = PROJ.platforms.filter(function(x){ return x.id === EX.proj; })[0] || PROJ.platforms[1];
    return '<div class="tree">' + p.tree.map(function(t){
      var depth = (t[0].match(/\//g) || []).length;
      var name = t[0].split('/').pop();
      var dir = t[0].slice(-1) === '/';
      return '<div class="tr" style="padding-left:' + (depth * 12) + 'px">' +
        '<span class="ic">' + (dir ? '▸' : '·') + '</span>' +
        '<span class="nm' + (dir ? ' dir' : '') + '">' + esc(name) + '</span>' +
        (t[2] && t[2] !== '—' ? '<span class="mt">' + t[2] + '</span>' : '') +
        '<span class="nt">' + esc(t[1]) + '</span></div>';
    }).join('') + '</div>';
  }

  function featHTML(){
    return PROJ.features.map(function(f){
      var on = !!EX.feats[f.id];
      return '<div class="feat' + (on ? ' on' : '') + '" data-feat="' + f.id + '">' +
        '<b>' + f.icon + '</b><div><h5>' + esc(f.name) + '</h5><p>' + esc(f.desc) + '</p>' +
        '<div class="chips2">' + f.mats.map(function(m){ return '<s>' + m + '</s>'; }).join('') +
        (f.xp.length ? '<s class="xp">XPopup ' + f.xp.length + '</s>' : '') +
        (f.rec.length ? '<s class="rc">配方 ' + f.rec.length + '</s>' : '') +
        '</div></div><i>' + (on ? '✓' : '') + '</i></div>';
    }).join('');
  }

  function mapHTML(){
    var rows = [];
    PROJ.features.forEach(function(f){
      if(!EX.feats[f.id]) return;
      rows.push('<div class="maprow"><div class="k">' + esc(f.name) + '</div><div class="v">' +
        f.mats.map(function(m){ return '<a data-jump="' + m + '">' + m + '</a>'; }).join('') +
        f.xp.map(function(x){ return '<a class="xpj" data-xpj="' + x + '">' + x + '</a>'; }).join('') +
        f.rec.map(function(r){ return '<a class="rcj" data-jump-rec="' + r + '">R' + r + '</a>'; }).join('') +
        '</div></div>');
    });
    return rows.length ? rows.join('') : '<div class="note">上面勾选至少一个功能。</div>';
  }

  function promptText(){
    var p = PROJ.platforms.filter(function(x){ return x.id === EX.proj; })[0] || PROJ.platforms[1];
    var feats = PROJ.features.filter(function(f){ return EX.feats[f.id]; });
    var mats = [];
    feats.forEach(function(f){ f.mats.forEach(function(m){ if(mats.indexOf(m) < 0) mats.push(m); }); });
    var xps = [];
    feats.forEach(function(f){ f.xp.forEach(function(x){ if(xps.indexOf(x) < 0) xps.push(x); }); });
    return PROJ.prompt
      .replace('{platform}', p.name + '（' + p.sub + '）')
      .replace('{desc}', p.desc)
      .replace('{tree}', p.tree.map(function(t){ return '  ' + t[0] + (t[1] !== '—' ? '   // ' + t[1] : ''); }).join('\n'))
      .replace('{feats}', feats.length ? feats.map(function(f){ return '· ' + f.name + '：' + f.desc; }).join('\n') : '（未选择）')
      .replace('{matlist}', mats.length ? '  ' + mats.join(' / ') : '  （无）')
      .replace('{xplist}', xps.length ? xps.join(' / ') : '（本次不需要）');
  }

  function projBodyHTML(){
    return '<div class="sec">要做的功能</div>' + '<div class="featwrap">' + featHTML() + '</div>' +
      '<div class="sec">素材映射</div>' + mapHTML() +
      '<div class="actrow" style="margin-top:14px"><button class="btn primary" id="copyProj">复制项目结构 + 提示词</button>' +
      '<button class="btn ghost" id="copyTree">只复制目录树</button></div>' +
      '<pre class="pcode" id="projOut" style="margin-top:12px">' + esc(promptText()) + '</pre>';
  }

  window.__EXP.caseHTML = caseHTML;

  window.__EXP.projHTML = function(){
    var p = PROJ.platforms.filter(function(x){ return x.id === EX.proj; })[0] || PROJ.platforms[1];
    return '<h1 class="title" style="font-size:22px">搭项目</h1>' +
      '<div class="lede2">选平台、勾功能，直接给你<b>目录结构</b>、<b>每个文件对应哪条素材</b>，以及一段能贴给 AI 的开工提示词。</div>' +
      seg(PROJ.platforms.map(function(x){ return [x.id, x.name]; }), EX.proj, 'proj') +
      '<div class="note" style="margin:12px 2px">' + esc(p.sub) + ' · ' + esc(p.desc) + '</div>' +
      '<div class="sec">目录结构</div>' + treeHTML() +
      '<div id="projBody">' + projBodyHTML() + '</div>';
  };

  /* 只重画「功能 / 映射 / 提示词」这一段，页面位置不动 */
  function refreshProjBody(root){
    var box = root.querySelector('#projBody');
    if(!box) return;
    box.innerHTML = projBodyHTML();
    window.__EXP.wire(root);
  }

  /* ─────────── 全局搜索 ─────────── */
  function buildIndex(){
    var idx = [];
    (window.__ITEMS || []).forEach(function(it){
      idx.push({t:'素材', id:it.id, name:it.name, sub:it.title, cat:it.coll,
                kw:(it.name + ' ' + it.title + ' ' + it.mech + ' ' + it.params + ' ' + it.dur)});
    });
    TYPES.forEach(function(t){ idx.push({t:'弹窗', id:'xp:' + t[1], name:t[2], sub:t[3], cat:'XPopup',
                kw:(t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5].join(' '))}); });
    ANIMS.forEach(function(a){ idx.push({t:'动画', id:'an:' + a[0], name:a[1], sub:a[0], cat:'XPopup',
                kw:(a[0] + ' ' + a[1] + ' ' + a[2])}); });
    RECIPES.forEach(function(r){ idx.push({t:'配方', id:'rec:' + r.no, name:r.name, sub:r.what, cat:'motion-web',
                kw:(r.name + ' ' + r.what + ' ' + r.use)}); });
    SPECS.forEach(function(s){ idx.push({t:'规范', id:'spec:' + s.file, name:s.title, sub:s.file, cat:'motion-web',
                kw:(s.title + ' ' + s.secs.join(' ') + ' ' + s.lede)}); });
    PROJ.features.forEach(function(f){ idx.push({t:'功能', id:'feat:' + f.id, name:f.name, sub:f.desc, cat:'项目结构',
                kw:(f.name + ' ' + f.desc)}); });
    var SYN = {
      '弹窗':'popup dialog modal 弹层 浮层 提示框 对话框',
      '动画':'motion anim 动效 过渡 transition 缓动',
      '表单':'form 输入 校验 选择',
      '导航':'nav 菜单 标签栏 抽屉 顶栏',
      '图表':'chart 统计 数据 可视化',
      '加载':'loading 进度 骨架 等待'
    };
    Object.keys(SYN).forEach(function(k){
      idx.forEach(function(x){ if(x.name.indexOf(k) >= 0) x.kw += ' ' + SYN[k]; });
    });
    return idx;
  }
  var INDEX = null;
  var SYN = {
    '弹窗':'弹层 浮层 对话框 提示框 popup dialog modal',
    '抽屉':'侧边栏 抽屉导航 drawer panel',
    '图表':'折线 柱状 环形 饼图 面积 表格 数据 可视化 chart',
    '数据':'折线 柱状 环形 表格 统计 图表',
    '校验':'验证 报错 错误 表单 form validate',
    '表单':'输入 校验 选择 步进 分段 表单 form',
    '引导':'新手 首次 教程 分步 onboarding',
    '错峰':'逐个 依次 stagger 序列 延迟',
    '弹簧':'弹性 spring 回弹 阻尼',
    '加载':'等待 进度 骨架 loading skeleton',
    '导航':'菜单 标签栏 顶栏 面包屑 侧边栏',
    '按钮':'button 主要 次要 幽灵',
    '设置':'开关 分组 settings toggle',
    '令牌':'token 时长 曲线 easing duration',
    '规范':'文档 规则 判据 验收',
    '结构':'目录 文件 项目 proj 骨架',
    '手势':'拖拽 滑动 drag gesture',
    '主题':'深色 浅色 暗色 theme'
  };
  function expand(t){
    var out = [t];
    Object.keys(SYN).forEach(function(k){
      var list = (k + ' ' + SYN[k]).toLowerCase().split(/\s+/);
      if(k === t || SYN[k].toLowerCase().indexOf(t) >= 0 || list.indexOf(t) >= 0){
        out = out.concat([k.toLowerCase()].concat(SYN[k].toLowerCase().split(/\s+/)));
      }
    });
    var uniq = [];
    out.forEach(function(x){ if(x && uniq.indexOf(x) < 0) uniq.push(x); });
    return uniq;
  }

  window.__EXP.searchHTML = function(q){
    if(!INDEX) INDEX = buildIndex();
    var raw = q.trim().toLowerCase();
    if(!raw) return '';
    var tokens = raw.split(/\s+/).filter(Boolean);
    var ex = [];
    tokens.forEach(function(t){ ex = ex.concat(expand(t)); });
    var scored = [];
    INDEX.forEach(function(x){
      var name = (x.name || '').toLowerCase(), sub = String(x.sub || '').toLowerCase(),
          kw = (x.kw || '').toLowerCase(), sc = 0, hitAll = true;
      tokens.forEach(function(t){
        var best = 0, parts = expand(t);
        parts.forEach(function(p, pi){
          var w = pi === 0 ? 1 : .55;
          if(name.indexOf(p) >= 0) best = Math.max(best, 12 * w);
          else if(sub.indexOf(p) >= 0) best = Math.max(best, 7 * w);
          else if(kw.indexOf(p) >= 0) best = Math.max(best, 2.5 * w);
        });
        if(best === 0) hitAll = false;
        sc += best;
      });
      if(sc > 0) scored.push({x:x, sc:sc, all:hitAll});
    });
    scored.sort(function(a, b){ return (b.all - a.all) || (b.sc - a.sc); });
    var hits = scored.slice(0, 48).map(function(o){ return o.x; });
    if(!hits.length){
      return '<div class="empty">没有匹配「' + esc(q) + '」的条目。<br>' +
        '<span style="font-size:11px">试试：弹窗 / 抽屉 / 图表 / 弹簧 / 校验 / 引导 / 错峰</span></div>';
    }
    var groups = {};
    hits.forEach(function(h){ (groups[h.t] = groups[h.t] || []).push(h); });
    var order = ['素材','弹窗','动画','配方','规范','功能'];
    return '<div class="srhead">「' + esc(q) + '」找到 ' + hits.length + ' 条 · 按相关度排</div>' +
      order.filter(function(o){ return groups[o]; }).map(function(o){
        return '<div class="xp-group">' + o + ' · ' + groups[o].length + '</div>' +
          groups[o].map(function(h){
            return '<div class="srow" data-sr="' + esc(h.id) + '"><b>' + esc(h.name) + '</b>' +
              '<span>' + esc(String(h.sub).slice(0, 54)) + '</span>' +
              '<i>' + esc(h.t) + '</i></div>';
          }).join('');
      }).join('');
  };

  /* ─────────── 事件接线 ─────────── */
  window.__EXP.wire = function(root){
    /* 顶层 hall / 各 tab */
    root.querySelectorAll('[data-hall]').forEach(function(b){
      b.addEventListener('click', function(){ EX.hall = b.dataset.hall; rerender(); });
    });
    root.querySelectorAll('[data-xptab]').forEach(function(b){
      b.addEventListener('click', function(){ EX.xp = b.dataset.xptab; rerender(); });
    });
    root.querySelectorAll('[data-mwtab]').forEach(function(b){
      b.addEventListener('click', function(){ EX.mw = b.dataset.mwtab; rerender(); });
    });
    root.querySelectorAll('[data-lab]').forEach(function(b){
      b.addEventListener('click', function(){ EX.lab = b.dataset.lab; rerender(); });
    });
    root.querySelectorAll('[data-xp]').forEach(function(b){
      b.addEventListener('click', function(){
        if(navigator.vibrate) try{ navigator.vibrate(8); }catch(e){}
        window.__XP.open(b.dataset.xp);
      });
    });
    /* 动画网格 */
    root.querySelectorAll('[data-anim]').forEach(function(t){
      t.addEventListener('click', function(){ playAnim(t, +t.dataset.anim); });
    });
    var all = root.querySelector('#anAll');
    if(all) all.addEventListener('click', function(){ playAll(root); });
    /* 设置开关 */
    root.querySelectorAll('[data-set]').forEach(function(sw){
      sw.addEventListener('click', function(){
        var k = LIVE[sw.dataset.set];
        if(!k) return;
        var on = !window.__XP.get()[k];
        window.__XP.set(k, on);
        sw.classList.toggle('on', on);
        var names = { shadow:'半透明背景', blur:'背景模糊', dark:'深色主题', dismissOutside:'点外部关闭',
                      dismissBack:'返回键关闭', drag:'拖拽关闭', three:'三阶拖拽' };
        window.__XP.toast(names[k] + (on ? ' 已开启' : ' 已关闭'));
      });
    });
    /* 手势 */
    root.querySelectorAll('[data-gest]').forEach(function(g){
      g.addEventListener('click', function(){
        var id = g.dataset.gest;
        if(id === 'drag' || id === 'three') window.__XP.open('bottomList');
        else if(id === 'nested') window.__XP.open('zhihu');
        else if(id === 'outside') window.__XP.open('attach');
        else if(id === 'blur'){ window.__XP.set('blur', true); window.__XP.open('confirm'); }
        stageGesture(root, id);
      });
    });
    /* 配方 */
    root.querySelectorAll('[data-rec]').forEach(function(st){
      mountRecipe(st);
    });
    root.querySelectorAll('[data-cp-rec]').forEach(function(b){
      b.addEventListener('click', function(e){
        e.stopPropagation();
        copyText(recPrompt(+b.dataset.cpRec), b);
      });
    });
    /* 令牌实验室 */
    var stage = root.querySelector('#labStage');
    if(stage) runLab(stage);
    root.querySelectorAll('[data-dur],[data-ease],[data-spring],[data-stag]').forEach(function(row){
      row.addEventListener('click', function(){
        var st2 = root.querySelector('#labStage');
        if(!st2) return;
        if(row.dataset.dur !== undefined) runLab(st2, 'duration', +row.dataset.dur);
        if(row.dataset.ease !== undefined) runLab(st2, 'easing', +row.dataset.ease);
        if(row.dataset.spring !== undefined) runLab(st2, 'spring', +row.dataset.spring);
        if(row.dataset.stag !== undefined) runLab(st2, 'stagger', +row.dataset.stag);
      });
    });
    /* 规范折叠 */
    root.querySelectorAll('[data-spec]').forEach(function(c){
      c.addEventListener('click', function(){ EX.specOpen = (+c.dataset.spec === EX.specOpen) ? -1 : +c.dataset.spec; rerender(); });
    });
    /* 项目结构 */
    root.querySelectorAll('[data-proj]').forEach(function(b){
      b.addEventListener('click', function(){ EX.proj = b.dataset.proj; rerender(); });
    });
    root.querySelectorAll('[data-feat]').forEach(function(f){
      f.addEventListener('click', function(){
        var id = f.dataset.feat;
        EX.feats[id] = !EX.feats[id];
        var box = root.querySelector('#projBody');
        if(box){
          var y = window.scrollY;
          box.innerHTML = projBodyHTML();
          window.__EXP.wire(root);
          window.scrollTo(0, y);      /* 勾选不跳回顶部 */
        } else rerender();
      });
    });
    var cp = root.querySelector('#copyProj');
    if(cp) cp.addEventListener('click', function(){ copyText(promptText(), cp); });
    var ct = root.querySelector('#copyTree');
    if(ct) ct.addEventListener('click', function(){
      var p = PROJ.platforms.filter(function(x){ return x.id === EX.proj; })[0];
      copyText(p.tree.map(function(t){ return t[0] + (t[1] !== '—' ? '   // ' + t[1] : ''); }).join('\n'), ct);
    });
    root.querySelectorAll('[data-jump]').forEach(function(a){
      a.addEventListener('click', function(){ if(window.__OPEN) window.__OPEN(a.dataset.jump); });
    });
    root.querySelectorAll('[data-xpj]').forEach(function(a){
      a.addEventListener('click', function(){
        S_go('exp'); EX.hall = 'xp'; EX.xp = 'list'; rerender();
        setTimeout(function(){ window.__XP.open(a.dataset.xpj); }, 260);
      });
    });
    root.querySelectorAll('[data-jump-rec]').forEach(function(a){
      a.addEventListener('click', function(){ S_go('exp'); EX.hall = 'mw'; EX.mw = 'rec'; rerender(); });
    });
    /* 搜索结果 */
    root.querySelectorAll('[data-case]').forEach(function(r){
      r.addEventListener('click', function(){ if(window.__CASE) window.__CASE(r.dataset.case); });
    });
    root.querySelectorAll('[data-hall]').forEach(function(r){
      if(r.classList.contains('backrow')) r.addEventListener('click', function(){
        EX.hall = r.dataset.hall; if(window.__GOTO) window.__GOTO('exp');
      });
    });
    var tc = root.querySelector('#thCopy');
    if(tc) tc.addEventListener('click', function(){
      var id = (root.querySelector('.th-mini') || {}).dataset;
      var it = (window.__ITEMS || []).filter(function(x){ return id && x.id === id.mini; })[0];
      if(it) copyText(it.prompt, tc);
    });
    root.querySelectorAll('[data-open]').forEach(function(r){
      r.addEventListener('click', function(){ if(window.__OPEN) window.__OPEN(r.dataset.open); });
    });
    root.querySelectorAll('[data-sr]').forEach(function(r){
      r.addEventListener('click', function(){ var v = r.dataset.sr; if(window.__SRGO) window.__SRGO(v); });
    });
  };

  function S_go(v){ if(window.__GOTO) window.__GOTO(v); }
  function rerender(){ if(window.__GOTO) window.__GOTO(window.__VIEW ? window.__VIEW() : 'exp', true); }

  function playAnim(tile, i){
    var card = tile.querySelector('.an-card');
    var a = ANIMS[i];
    card.classList.remove('anim');
    card.style.transition = 'none';
    card.style.transform = a[3] === 'none' ? '' : a[3];
    card.style.opacity = a[4];
    requestAnimationFrame(function(){
      card.style.transition = 'transform .4s cubic-bezier(.2,.9,.3,1.12), opacity .34s ease';
      card.style.transform = '';
      card.style.opacity = 1;
    });
  }
  function playAll(root){
    var tiles = root.querySelectorAll('[data-anim]');
    tiles.forEach(function(t, i){ setTimeout(function(){ playAnim(t, i); }, i * 170); });
  }

  function stageGesture(root, id){
    var st = root.querySelector('#gestStage');
    if(!st) return;
    if(id === 'nested'){
      st.innerHTML = '<div class="tag">嵌套滚动</div><div style="position:absolute;inset:26px 12px 12px;overflow:auto;' +
        'border-radius:10px;border:1px solid rgba(255,255,255,.1)">' +
        Array.from({length:14}).map(function(_, i){
          return '<div style="height:34px;border-bottom:1px solid rgba(255,255,255,.06);display:flex;align-items:center;' +
            'padding:0 10px;font-size:10.5px;color:rgba(233,239,247,.5)">评论 ' + (i+1) + '</div>';
        }).join('') + '</div><div class="hint">列表先滚到底，再拖才开始关弹窗</div>';
    } else if(id === 'blur'){
      st.innerHTML = '<div class="tag">背景模糊</div><div class="hint">刚才的确认弹窗背后已经模糊了（hasBlurBg）</div>';
    } else {
      st.innerHTML = '<div class="tag">' + id + '</div><div class="hint">上方已经弹出可拖拽的弹窗，拖着试</div>';
    }
  }

  function recPrompt(i){
    var r = RECIPES[i];
    return '【参考】feitangyuan/motion-web · references/pattern-recipes.md 配方 ' +
      (r.no < 10 ? '0' + r.no : r.no) + '「' + r.name + '」（CC BY-NC 4.0，自己重写行为，不要照抄源码）\n' +
      '【这条配方是什么】' + r.what + '\n' +
      '【用来做什么】' + r.use + '\n' +
      '【变更要求】\n' +
      '· 参数从令牌里取：duration / easing / spring / stagger 各选一档，和全站保持一致\n' +
      '· 目标平台：移动端优先，触摸与鼠标都要能用；prefers-reduced-motion 时降级为淡入\n' +
      '· 首帧不能跳：初始态在 JS 之前就用 CSS 写死\n' +
      '【产出约束】\n' +
      '· 单个自包含 HTML，CSS/JS 内联，不用 CDN、不用外部字体或图片\n' +
      '· 揭示式入场用 transform / opacity，只碰合成层\n' +
      '· 60fps：每帧只读一次布局，事件里不做样式写\n' +
      '· 附一段「判据」注释：怎么算达标，怎么复现问题';
  }

  /* 配方挂载 */
  function mountRecipe(st){
    var i = +st.dataset.rec, r = RECIPES[i];
    if(!window.__REC || !window.__REC[i]) return;
    st.innerHTML = window.__REC[i].html;
    var s = document.createElement('style');
    if(!document.getElementById('rec-style-' + i)){
      s.id = 'rec-style-' + i;
      s.textContent = window.__REC[i].css.replace(/\.mr\b/g, '[data-rec="' + i + '"].mr');
      document.head.appendChild(s);
    }
    st.classList.add('mr');
    try {
      var fn = window.__REC[i].js;
      if(typeof fn === 'string') fn = (new Function('return (' + fn + ')'))();
      if(typeof fn === 'function') fn(st);
    } catch(e){ console.warn('recipe', i, e); }
  }

  /* 令牌实验室 */
  function runLab(stage, kind, idx){
    kind = kind || EX.lab;
    var first = !stage.querySelector('.labbox');
    stage.innerHTML = '<div class="tag" id="labTag"></div><div class="hint">点一下重播</div>' +
      '<div style="position:absolute;inset:0;display:grid;place-items:center">' +
      '<div class="labbox" style="position:relative;width:200px;height:70px"></div></div>';
    var tag = stage.querySelector('#labTag'), box = stage.querySelector('.labbox');
    function replay(){ if(kind === 'duration') labDur(box, tag, idx || 0);
      else if(kind === 'easing') labEase(box, tag, idx || 0);
      else if(kind === 'spring') labSpring(box, tag, idx || 0);
      else labStagger(box, tag, idx || 0); }
    stage.addEventListener('click', replay);
    replay();
  }

  function labDur(box, tag, i){
    var d = TOKENS.duration[i];
    tag.textContent = d[0] + ' · ' + d[1] + ' · ' + d[2];
    box.innerHTML = '<div class="lb" style="position:absolute;left:0;top:22px;width:22px;height:22px;border-radius:6px;' +
      'background:linear-gradient(150deg,#cfe3ff,#9dccff);transition:transform ' + (d[3] || 800) +
      'ms cubic-bezier(.16,1,.3,1)"></div>';
    var el = box.firstChild;
    requestAnimationFrame(function(){ el.style.transform = 'translateX(178px)'; });
    setTimeout(function(){ el.style.transition = 'none'; el.style.transform = 'none'; }, (d[3] || 800) + 500);
  }

  function labEase(box, tag, i){
    var e = TOKENS.easing[i];
    tag.textContent = e[0] + ' · ' + e[1];
    box.innerHTML = '<canvas width="200" height="70" style="position:absolute;inset:0"></canvas>';
    var c = box.firstChild, g = c.getContext('2d');
    function curve(fn){
      g.clearRect(0, 0, 200, 70);
      g.strokeStyle = 'rgba(255,255,255,.12)'; g.beginPath(); g.moveTo(0, 60); g.lineTo(200, 60); g.stroke();
      g.beginPath(); g.strokeStyle = '#9dccff'; g.lineWidth = 2;
      for(var t = 0; t <= 1; t += .02){
        var y = fn(t);
        var x = t * 178 + 8, yy = 60 - y * 50;
        t === 0 ? g.moveTo(x, yy) : g.lineTo(x, yy);
      }
      g.stroke();
    }
    var bez = [0,0,1,1];
    if(e[1].indexOf('cubic') === 0) bez = e[1].replace(/[a-z()]/g,'').split(',').map(Number);
    var ball = document.createElement('div');
    ball.style.cssText = 'position:absolute;left:0;top:50px;width:16px;height:16px;border-radius:50%;' +
      'background:#cfe3ff;box-shadow:0 4px 12px rgba(120,180,240,.5)';
    box.appendChild(ball);
    function loop(){
      var t0 = performance.now();
      function step(now){
        var p = Math.min(1, (now - t0) / 1000);
        ball.style.transform = 'translateX(' + (p * 184) + 'px) translateY(' + (-(p) * 0) + 'px)';
        if(p < 1) requestAnimationFrame(step); else setTimeout(loop, 420);
      }
      requestAnimationFrame(step);
    }
    curve(function(t){
      var x1 = bez[0], y1 = bez[1], x2 = bez[2], y2 = bez[3];
      var u = 1 - t;
      return 3*u*u*t*y1 + 3*u*t*t*y2 + t*t*t;
    });
    loop();
  }

  function labSpring(box, tag, i){
    var s = TOKENS.spring[i];
    tag.textContent = s[0] + ' · k ' + s[1] + ' c ' + s[2] + ' m ' + s[3];
    box.innerHTML = '<div style="position:absolute;left:0;top:22px;width:22px;height:22px;border-radius:50%;' +
      'background:linear-gradient(150deg,#5fdba8,#2f9e75)"></div>';
    var el = box.firstChild, x = 0, v = 0, target = 178, last = 0, k = s[1], c = s[2], m = s[3];
    function step(t){
      var dt = Math.min(1/30, Math.max(1/240, (t - (last || t)) / 1000)); last = t;
      var a = (-k * (x - target) - c * v) / m;
      v += a * dt; x += v * dt;
      if(Math.abs(x - target) < .4 && Math.abs(v) < 2){ x = target; v = 0; }
      el.style.transform = 'translateX(' + x.toFixed(2) + 'px) translateY(' + (Math.sin(x / 22) * 3).toFixed(2) + 'px)';
      if(!(x === target && v === 0)) requestAnimationFrame(step);
      else setTimeout(function(){ labSpring(box, tag, i); }, 700);
    }
    requestAnimationFrame(step);
  }

  function labStagger(box, tag, i){
    var d = TOKENS.stagger[i];
    tag.textContent = d[0] + ' · 每项 ' + d[1] + 'ms';
    var cols = 5, rows = 3, html = '';
    for(var r = 0; r < rows; r++) for(var c = 0; c < cols; c++){
      var n = r * cols + c;
      html += '<i style="position:absolute;left:' + (c * 30) + 'px;top:' + (r * 20) + 'px;width:18px;height:12px;' +
        'border-radius:3px;background:rgba(157,204,255,' + (0.35 + n * .04) + ');' +
        'transition:transform .5s cubic-bezier(.16,1,.3,1) ' + (n * d[1]) + 'ms,opacity .4s ' + (n * d[1]) + 'ms;' +
        'transform:translateY(14px);opacity:0"></i>';
    }
    box.innerHTML = html;
    var its = box.querySelectorAll('i');
    requestAnimationFrame(function(){
      its.forEach(function(el){ el.style.transform = 'none'; el.style.opacity = 1; });
    });
    setTimeout(function(){ its.forEach(function(el){ el.style.transition = 'none'; el.style.transform = 'translateY(14px)'; el.style.opacity = 0; });
      setTimeout(function(){ labStagger(box, tag, i); }, 260); }, 1400 + rows * cols * d[1]);
  }

  function copyText(t, btn){
    var done = function(ok){
      if(btn){ var old = btn.textContent; btn.textContent = ok ? '已复制 ✓' : '复制失败'; setTimeout(function(){ btn.textContent = old; }, 1400); }
      if(window.__XP) window.__XP.toast(ok ? '已复制到剪贴板' : '复制失败，请长按选择');
    };
    if(window.AndroidBridge && window.AndroidBridge.copy){ try{ window.AndroidBridge.copy(t); return done(true); }catch(e){} }
    if(navigator.clipboard && navigator.clipboard.writeText){
      navigator.clipboard.writeText(t).then(function(){ done(true); }, function(){
        fallback(); });
    } else fallback();
    function fallback(){
      try{
        var ta = document.createElement('textarea'); ta.value = t; ta.style.position = 'fixed';
        ta.style.top = '-1000px'; document.body.appendChild(ta); ta.select();
        var ok = document.execCommand('copy'); ta.remove(); done(ok);
      }catch(e){ done(false); }
    }
  }

  window.__EXP.promptText = promptText;
  window.__EXP.setHall = function(h){ EX.hall = h || 'xp'; };
  window.__EXP.setXpTab = function(t){ EX.xp = t; };
  window.__EXP.setMwTab = function(t){ EX.mw = t; };
})();
"""
