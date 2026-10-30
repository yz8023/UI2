# -*- coding: utf-8 -*-
"""素材库 App：6 个玻璃素材的迷你演示（直接复用真实 WebGL2 渲染器）"""

MINIS_GLASS_JS = r"""
(function(){
  var M = window.__MINI;

  function glassMini(root, opts, noteText, onTick){
    root.innerHTML = '';
    var holder = document.createElement('div');
    holder.style.cssText = 'position:relative;height:176px;background:#0a0c14';
    var cv = document.createElement('canvas');
    cv.style.cssText = 'width:100%;height:176px;display:block;touch-action:none';
    holder.appendChild(cv);
    root.appendChild(holder);
    if(noteText){
      var chip = document.createElement('div');
      chip.className = 'mini-chip'; chip.textContent = noteText;
      holder.appendChild(chip);
    }
    var inst = Glass.make(cv, opts);
    var iv = null, t = 0;
    if(onTick){
      iv = setInterval(function(){ t += 1; onTick(inst, t); }, 1100);
    }
    return {
      inst: inst, cv: cv,
      stop: function(){
        if(iv) clearInterval(iv);
        if(inst && inst.dispose) inst.dispose();
        holder.remove();
      }
    };
  }

  /* l01 · 折射与色散：点画布在「最终 / 边缘因子 / 法线 / SDF / 菲涅尔」之间切 */
  M['l01'] = function(root){
    var g = glassMini(root, {debug:0, follow:'spring'}, '点画布切步骤');
    var steps = [3, 2, 1, 0], i = 0;
    g.cv.addEventListener('click', function(){
      i = (i + 1) % steps.length;
      g.inst.P.debug = steps[i];
    });
    return g.stop;
  };

  /* l02 · 菲涅尔与眩光：光源自动旋转 */
  M['l02'] = function(root){
    var g = glassMini(root, {follow:'spring', glareAngle:-45}, '光源在转',
      function(inst, t){ if(inst) inst.P.glareAngle = -45 + t * 24; });
    return g.stop;
  };

  /* l03 · 超椭圆：n 在 2↔7 之间来回走 */
  M['l03'] = function(root){
    var g = glassMini(root,
      {roundness:5, radius:70, shapeW:230, shapeH:150, showBlob:1, merge:0.06},
      'n 2 ↔ 7',
      function(inst, t){ if(inst) inst.P.roundness = 2 + (t % 12 <= 6 ? (t % 12) : (12 - t % 12)) * (5/6); });
    return g.stop;
  };

  /* l04 · 模糊与阴影：模糊半径呼吸 6→34 */
  M['l04'] = function(root){
    var g = glassMini(root, {shapeW:230, shapeH:150, radius:70}, '模糊 6 ↔ 34px',
      function(inst, t){ if(inst) inst.P.blurR = 6 + (t % 10) * 3.2; });
    return g.stop;
  };

  /* l05 · 弹簧跟随：指针进入画布，玻璃会追过去并过冲 */
  M['l05'] = function(root){
    var g = glassMini(root,
      {stiff:150, damp:13, sizeSpring:0.5, shapeW:200, shapeH:130, radius:56, idle:true},
      '指针追玻璃');
    return g.stop;
  };

  /* l06 · 渲染步骤：每 1.1s 走下一个切面 */
  M['l06'] = function(root){
    var order = [10, 11, 12, 1, 2, 3, 6, 0], k = 0;
    var g = glassMini(root, {debug:0, shapeW:240, shapeH:150, radius:70}, 'STEP 自动播放',
      function(inst){
        if(!inst) return;
        k = (k + 1) % order.length;
        inst.P.debug = order[k];
      });
    return g.stop;
  };
})();
"""
