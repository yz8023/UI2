# -*- coding: utf-8 -*-
"""liquid-glass-studio 演示：共享 WebGL2 渲染器（4-pass：背景 → 纵向模糊 → 横向模糊 → 主合成）"""

GLASS_JS = r"""
(function(){
  var VS = `#version 300 es
  in vec2 a_pos;
  void main(){ gl_Position = vec4(a_pos, 0.0, 1.0); }`;

  /* ---------- pass 1：程序化背景 ---------- */
  var BG_FS = `#version 300 es
  precision highp float;
  out vec4 o;
  uniform vec2 u_res;
  uniform float u_time;
  uniform int u_bgMode;
  vec3 bg(vec2 uv){
    vec2 p = uv;
    vec3 c;
    if(u_bgMode==0){
      c = mix(vec3(0.055,0.075,0.145), vec3(0.115,0.155,0.265), clamp(p.y,0.0,1.0));
      c += vec3(0.62,0.28,0.98) * (1.0-smoothstep(0.0,0.62,length((p-vec2(0.24,0.30))*vec2(1.55,1.0)))) * 0.85;
      c += vec3(0.08,0.74,0.80) * (1.0-smoothstep(0.0,0.58,length((p-vec2(0.80,0.34))*vec2(1.55,1.0)))) * 0.78;
      c += vec3(1.00,0.52,0.22) * (1.0-smoothstep(0.0,0.56,length((p-vec2(0.56,0.88))*vec2(1.55,1.0)))) * 0.70;
      vec2 g = abs(fract(p*vec2(23.0,13.0))-0.5);
      float line = smoothstep(0.455,0.5,max(g.x,g.y));
      c = mix(c, vec3(0.93,0.96,1.0), line*0.20);
    } else {
      /* 横向色带：最容易看出折射与色散 */
      float band = sin((p.x*7.0 + p.y*2.5)*3.14159)*0.5+0.5;
      vec3 a = vec3(0.10,0.12,0.30), b = vec3(0.95,0.45,0.60), d = vec3(0.20,0.85,0.70);
      c = mix(a,b,band);
      c = mix(c,d, smoothstep(0.25,0.95,p.y));
      vec2 g = abs(fract(p*vec2(30.0,17.0))-0.5);
      c = mix(c, vec3(1.0), smoothstep(0.47,0.5,max(g.x,g.y))*0.16);
    }
    return c;
  }
  void main(){ vec2 uv = gl_FragCoord.xy/u_res; o = vec4(bg(uv),1.0); }`;

  /* ---------- pass 2/3：可分离高斯模糊 ---------- */
  var BLUR_FS = `#version 300 es
  precision highp float;
  out vec4 o;
  uniform sampler2D u_src;
  uniform vec2 u_res;
  uniform vec2 u_dir;
  uniform float u_radius;
  void main(){
    vec2 uv = gl_FragCoord.xy/u_res;
    float r = max(u_radius, 0.001);
    float sigma = max(r/3.0, 0.0001);
    vec3 acc = texture(u_src, uv).rgb;
    float wsum = 1.0;
    for(int i=1;i<=5;i++){
      float fi = float(i);
      float step_px = r/5.0;
      float w = exp(-0.5*pow(fi*step_px,2.0)/(sigma*sigma));
      vec2 off = u_dir * fi * step_px / u_res;
      acc += texture(u_src, uv+off).rgb * w;
      acc += texture(u_src, uv-off).rgb * w;
      wsum += w*2.0;
    }
    o = vec4(acc/wsum, 1.0);
  }`;

  /* ---------- pass 4：主合成 ---------- */
  var MAIN_FS = `#version 300 es
  precision highp float;
  out vec4 o;
  uniform sampler2D u_bg;
  uniform sampler2D u_blur;
  uniform sampler2D u_vblur;
  uniform vec2 u_res;
  uniform float u_dpr;
  uniform vec2 u_blob;
  uniform int u_showBlob;
  uniform float u_shapeW, u_shapeH, u_radius, u_roundness, u_merge;
  uniform float u_thick, u_refDist, u_refFactor, u_disp;
  uniform float u_fresRange, u_fresHard, u_fresFactor;
  uniform float u_glareRange, u_glareHard, u_glareFactor, u_glareConv, u_glareOpp, u_glareAngle;
  uniform float u_blurR;
  uniform int u_blurEdge;
  uniform vec4 u_tint;
  uniform float u_shExpand, u_shFactor;
  uniform vec2 u_shPos;
  uniform int u_debug;
  uniform float u_rim;
  uniform float u_time;

  float seCorner(vec2 p, float r, float n){
    p = abs(p);
    return pow(pow(p.x,n) + pow(p.y,n), 1.0/n) - r;
  }
  float sdRR(vec2 p, vec2 h, float r, float n){
    r = min(r, min(h.x,h.y));
    vec2 d = abs(p) - h + r;
    if(d.x > 0.0 && d.y > 0.0) return seCorner(d, r, n);
    return min(max(d.x,d.y),0.0) + length(max(d,0.0)) - r;
  }
  float smin(float a, float b, float k){
    if(k < 0.001) return min(a,b);
    float h = clamp(0.5 + 0.5*(b-a)/k, 0.0, 1.0);
    return mix(b,a,h) - k*h*(1.0-h);
  }
  float sd(vec2 p){
    vec2 h = vec2(u_shapeW, u_shapeH) * u_dpr * 0.5;
    float r = min(u_radius, min(u_shapeW,u_shapeH)*0.5) * u_dpr;
    float d1 = sdRR(p, h, r, u_roundness);
    if(u_showBlob == 0) return d1;
    float d2 = length(p - u_blob) - 86.0*u_dpr;
    return smin(d1, d2, u_merge*260.0*u_dpr);
  }
  vec2 nrm(vec2 p){
    float e = 1.2;
    vec2 g = vec2(sd(p+vec2(e,0.0)) - sd(p-vec2(e,0.0)),
                  sd(p+vec2(0.0,e)) - sd(p-vec2(0.0,e)));
    float l = length(g);
    return l < 1e-5 ? vec2(0.0,1.0) : g/l;
  }
  void main(){
    vec2 p = gl_FragCoord.xy - u_res*0.5;
    vec2 uv = gl_FragCoord.xy/u_res;
    float d = sd(p);
    float nd = -d;
    vec2 n = nrm(p);

    /* --- 边缘因子（Snell） --- */
    float thick = max(u_thick,1.0) * 1.1 * u_dpr;
    float xr = clamp(1.0 - nd/thick, 0.0, 1.0);
    float thI = asin(clamp(pow(xr,2.0),0.0,1.0));
    float thT = asin(clamp(sin(thI)/max(u_refFactor,1.0001), -1.0, 1.0));
    float edge = max(-tan(thT-thI), 0.0);
    if(nd >= thick) edge = 0.0;
    if(d >= 0.0) edge = 0.0;

    /* --- 色散：RGB 三个折射率（N_R .98 / N_G 1.0 / N_B 1.02） --- */
    float dg = u_disp/25.0;
    float eR = edge*(1.0 + 0.02*dg);
    float eG = edge;
    float eB = edge*(1.0 - 0.02*dg);
    vec2 k = n * u_refDist * 220.0 * u_dpr / u_res;
    vec2 oR = k*eR, oG = k*eG, oB = k*eB;

    vec3 sharp = texture(u_bg, uv).rgb;
    vec3 sharpR = vec3(texture(u_bg,uv+oR).r, texture(u_bg,uv+oG).g, texture(u_bg,uv+oB).b);
    vec3 blur = vec3(texture(u_blur,uv+oR).r, texture(u_blur,uv+oG).g, texture(u_blur,uv+oB).b);

    float bm = (u_blurEdge==1) ? smoothstep(0.0, thick*2.6, nd) : 1.0;
    vec3 refr = mix(sharpR, blur, bm);

    /* --- 菲涅尔 --- */
    float fres = pow(clamp(1.0 - nd/max(u_fresRange*u_dpr,1.0) + u_fresHard/100.0, 0.0, 1.0), 5.0);
    fres *= u_fresFactor/100.0;

    /* --- 高光眩光（方向性） --- */
    float ga = radians(u_glareAngle);
    vec2 gdir = vec2(cos(ga), sin(ga));
    float band = 1.0 - smoothstep(0.0, max(u_glareRange*u_dpr, 2.0), nd);
    float lit = clamp(dot(n, gdir), 0.0, 1.0);
    float crescent = pow(lit, mix(3.0, 0.6, u_glareHard/100.0));
    crescent = mix(crescent, smoothstep(0.15,1.0,crescent), u_glareConv/100.0);
    float glare = crescent * band * (u_glareFactor/100.0) * 0.70;
    float farCres = pow(clamp(dot(n,-gdir),0.0,1.0), 9.0) * band * (u_glareOpp/100.0) * 0.22;

    /* --- 阴影 --- */
    float sdSh = sd(p - u_shPos*u_dpr);
    float sh = (1.0 - smoothstep(0.0, max(u_shExpand*u_dpr,1.0), sdSh)) * (u_shFactor/100.0);

    vec3 outside = sharp * (1.0 - sh*0.72);
    vec3 inside = refr;
    inside = mix(inside, u_tint.rgb, u_tint.a);
    inside += vec3(1.0) * fres * 0.9;
    inside += vec3(1.0) * glare + vec3(0.82,0.90,1.0) * farCres;
    inside *= mix(0.90, 1.0, smoothstep(0.0, thick*0.85, nd));
    float rim = 1.0 - smoothstep(0.15, 1.7, abs(d));
    inside += vec3(0.94,0.97,1.0) * rim * 0.40 * u_rim;

    vec3 col = (d < 0.0) ? inside : outside;

    /* --- 渲染步骤查看 --- */
    if(u_debug == 1){
      float rings = 0.5 + 0.5*cos(nd*0.22);
      col = (d<0.0) ? vec3(0.42,0.72,1.0)*rings*0.95
                    : mix(vec3(0.98,0.80,0.45), vec3(0.30,0.22,0.18), 1.0-smoothstep(0.0,260.0,d));
      col = mix(col, vec3(1.0), 1.0-smoothstep(0.8,1.8,abs(d)));
    } else if(u_debug == 2){
      col = (d<0.0) ? 0.5+0.5*vec3(n.x, n.y, 1.0-abs(n.x*n.y)) : vec3(0.80);
    } else if(u_debug == 3){
      col = vec3(edge*2.2);
    } else if(u_debug == 4){
      col = vec3(fres);
    } else if(u_debug == 5){
      col = vec3(glare + farCres);
    } else if(u_debug == 6){
      col = vec3(fres*0.9 + glare + farCres);
    } else if(u_debug == 10){
      col = texture(u_bg, uv).rgb;
    } else if(u_debug == 11){
      col = texture(u_vblur, uv).rgb;
    } else if(u_debug == 12){
      col = texture(u_blur, uv).rgb;
    }
    o = vec4(col, 1.0);
  }`;

  function compile(gl, type, src){
    var s = gl.createShader(type);
    gl.shaderSource(s, src); gl.compileShader(s);
    if(!gl.getShaderParameter(s, gl.COMPILE_STATUS)){
      console.error(gl.getShaderInfoLog(s)); return null;
    }
    return s;
  }
  function program(gl, fs){
    var p = gl.createProgram();
    var v = compile(gl, gl.VERTEX_SHADER, VS), f = compile(gl, gl.FRAGMENT_SHADER, fs);
    if(!v || !f) return null;
    gl.attachShader(p, v); gl.attachShader(p, f); gl.linkProgram(p);
    if(!gl.getProgramParameter(p, gl.LINK_STATUS)){ console.error(gl.getProgramInfoLog(p)); return null; }
    return p;
  }

  var DEFAULTS = {
    thick:20, refDist:0.05, refFactor:1.4, disp:7,
    fresRange:30, fresHard:20, fresFactor:20,
    glareRange:30, glareHard:20, glareFactor:90, glareConv:50, glareOpp:80, glareAngle:-45,
    blurR:18, blurEdge:1,
    tint:[1,1,1,0],
    shExpand:25, shFactor:15, shPos:[0,-10],
    shapeW:380, shapeH:240, radius:110, roundness:5, merge:0.06, showBlob:0,
    debug:0, bgMode:0, rim:1,
    follow:'spring', stiff:170, damp:14, sizeSpring:0.4, idle:true
  };

  var instances = [];
  var raf = null, last = performance.now();

  function make(canvas, opts){
    var P = Object.assign({}, DEFAULTS, opts || {});
    P.tint = (P.tint || [1,1,1,0]).slice();
    P.shPos = (P.shPos || [0,-10]).slice();
    var gl = canvas.getContext('webgl2', {antialias:false, alpha:false, premultipliedAlpha:false});
    if(!gl){
      canvas.parentNode.classList.add('nowebgl');
      /* 返回一个空壳实例，页面上的滑杆/读数/动画循环都不会因为 null 抛错 */
      return {P:Object.assign({}, DEFAULTS, opts||{}), gl:null, canvas:canvas, cv:canvas, dpr:1,
              target:{x:0,y:0}, pos:{x:0,y:0}, vel:{x:0,y:0}, lag:0, moved:false, everMoved:false,
              overshoot:0, t:0, step:function(){}, resize:function(){}};
    }
    var pBg = program(gl, BG_FS), pBlur = program(gl, BLUR_FS), pMain = program(gl, MAIN_FS);
    if(!pBg || !pBlur || !pMain) return null;

    var quad = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, quad);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1, 3,-1, -1,3]), gl.STATIC_DRAW);

    function bindQuad(prog){
      var loc = gl.getAttribLocation(prog, 'a_pos');
      gl.bindBuffer(gl.ARRAY_BUFFER, quad);
      gl.enableVertexAttribArray(loc);
      gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
    }
    function makeRT(w,h){
      var tex = gl.createTexture();
      gl.bindTexture(gl.TEXTURE_2D, tex);
      gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, w, h, 0, gl.RGBA, gl.UNSIGNED_BYTE, null);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
      var fb = gl.createFramebuffer();
      gl.bindFramebuffer(gl.FRAMEBUFFER, fb);
      gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, tex, 0);
      gl.bindFramebuffer(gl.FRAMEBUFFER, null);
      return {tex:tex, fb:fb, w:w, h:h};
    }
    var rtBg = null, rtA = null, rtB = null, W = 0, H = 0;

    var inst = {
      P:P, gl:gl, canvas:canvas, cv:canvas,
      target:{x:0,y:0}, pos:{x:0,y:0}, vel:{x:0,y:0},
      lag:0, moved:false, everMoved:false, overshoot:0, t:0
    };

    function resize(){
      var dpr = Math.min(window.devicePixelRatio||1, 1.6);
      var r = canvas.getBoundingClientRect();
      var w = Math.max(64, Math.round(r.width*dpr)), h = Math.max(64, Math.round(r.height*dpr));
      if(w===W && h===H) return;
      W = w; H = h;
      canvas.width = w; canvas.height = h; inst.dpr = dpr;
      [rtBg, rtA, rtB].forEach(function(rt){
        if(rt){ gl.deleteTexture(rt.tex); gl.deleteFramebuffer(rt.fb); }
      });
      rtBg = makeRT(w,h); rtA = makeRT(w,h); rtB = makeRT(w,h);
    }
    inst.resize = resize; resize();

    var ucache = new WeakMap();
    function uloc(prog, name){
      var m = ucache.get(prog);
      if(!m){ m = {}; ucache.set(prog, m); }
      if(!(name in m)) m[name] = gl.getUniformLocation(prog, name);
      return m[name];
    }

    inst.step = function(dt, now){
      P = inst.P;
      resize();
      var dpr = inst.dpr || 1;
      /* 跟随 */
      if(!inst.moved && P.idle){
        if(inst.everMoved){
          inst.target.x = 0; inst.target.y = 0;
        } else {
          inst.target.x = Math.cos(now*0.00042)*Math.min(150, W/dpr*0.18)*dpr;
          inst.target.y = Math.sin(now*0.00061)*Math.min(90, H/dpr*0.16)*dpr;
        }
      }
      var tg = inst.target;
      if(P.follow === 'none'){
        inst.pos.x = tg.x; inst.pos.y = tg.y;
      } else if(P.follow === 'lerp'){
        var k = 1 - Math.exp(-6*dt);
        inst.pos.x += (tg.x-inst.pos.x)*k; inst.pos.y += (tg.y-inst.pos.y)*k;
      } else {
        var s = P.stiff, dmp = Math.exp(-P.damp*dt);
        inst.vel.x += (tg.x-inst.pos.x)*s*dt; inst.vel.y += (tg.y-inst.pos.y)*s*dt;
        inst.vel.x *= dmp; inst.vel.y *= dmp;
        inst.pos.x += inst.vel.x*dt; inst.pos.y += inst.vel.y*dt;
        var dx = tg.x-inst.pos.x, dy = tg.y-inst.pos.y;
        if(inst.vel.x*dx + inst.vel.y*dy < 0){
          inst.overshoot = Math.max(inst.overshoot, Math.hypot(dx,dy));
        } else if(inst.overshoot > 0){
          inst.overshoot *= Math.pow(0.985, dt*60);
        }
      }
      inst.lag = Math.hypot(tg.x-inst.pos.x, tg.y-inst.pos.y);

      /* pass 1 · 背景 */
      gl.bindFramebuffer(gl.FRAMEBUFFER, rtBg.fb);
      gl.viewport(0,0,W,H);
      gl.useProgram(pBg); bindQuad(pBg);
      gl.uniform2f(uloc(pBg,'u_res'), W, H);
      gl.uniform1f(uloc(pBg,'u_time'), now*0.001);
      gl.uniform1i(uloc(pBg,'u_bgMode'), P.bgMode|0);
      gl.drawArrays(gl.TRIANGLES, 0, 3);

      /* pass 2 · 纵向模糊 */
      gl.bindFramebuffer(gl.FRAMEBUFFER, rtA.fb);
      gl.useProgram(pBlur); bindQuad(pBlur);
      gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, rtBg.tex);
      gl.uniform1i(uloc(pBlur,'u_src'), 0);
      gl.uniform2f(uloc(pBlur,'u_res'), W, H);
      gl.uniform2f(uloc(pBlur,'u_dir'), 0, 1);
      gl.uniform1f(uloc(pBlur,'u_radius'), (P.blurR||0)*dpr);
      gl.drawArrays(gl.TRIANGLES, 0, 3);

      /* pass 3 · 横向模糊 */
      gl.bindFramebuffer(gl.FRAMEBUFFER, rtB.fb);
      gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, rtA.tex);
      gl.uniform2f(uloc(pBlur,'u_dir'), 1, 0);
      gl.drawArrays(gl.TRIANGLES, 0, 3);

      /* pass 4 · 主合成 */
      gl.bindFramebuffer(gl.FRAMEBUFFER, null);
      gl.viewport(0,0,W,H);
      gl.useProgram(pMain); bindQuad(pMain);
      gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, rtBg.tex);
      gl.uniform1i(uloc(pMain,'u_bg'), 0);
      gl.activeTexture(gl.TEXTURE1); gl.bindTexture(gl.TEXTURE_2D, rtB.tex);
      gl.uniform1i(uloc(pMain,'u_blur'), 1);
      gl.activeTexture(gl.TEXTURE2); gl.bindTexture(gl.TEXTURE_2D, rtA.tex);
      gl.uniform1i(uloc(pMain,'u_vblur'), 2);
      gl.uniform2f(uloc(pMain,'u_res'), W, H);
      gl.uniform1f(uloc(pMain,'u_dpr'), dpr);
      gl.uniform2f(uloc(pMain,'u_blob'), inst.pos.x, inst.pos.y);
      gl.uniform1i(uloc(pMain,'u_showBlob'), P.showBlob|0);
      var vm = Math.min(Math.hypot(inst.vel.x, inst.vel.y)/(dpr*260), 1);
      var ssc = 1 + vm * (P.sizeSpring||0) * 0.10;
      /* 形状按画布宽度自适应，窄屏（单列）不会把玻璃裁掉 */
      var fit = Math.min(1, (W/dpr) / (P.shapeW + 140));
      gl.uniform1f(uloc(pMain,'u_shapeW'), P.shapeW*ssc*fit);
      gl.uniform1f(uloc(pMain,'u_shapeH'), P.shapeH*ssc*fit);
      gl.uniform1f(uloc(pMain,'u_radius'), P.radius);
      gl.uniform1f(uloc(pMain,'u_roundness'), P.roundness);
      gl.uniform1f(uloc(pMain,'u_merge'), P.merge);
      gl.uniform1f(uloc(pMain,'u_thick'), P.thick);
      gl.uniform1f(uloc(pMain,'u_refDist'), P.refDist);
      gl.uniform1f(uloc(pMain,'u_refFactor'), P.refFactor);
      gl.uniform1f(uloc(pMain,'u_disp'), P.disp);
      gl.uniform1f(uloc(pMain,'u_fresRange'), P.fresRange);
      gl.uniform1f(uloc(pMain,'u_fresHard'), P.fresHard);
      gl.uniform1f(uloc(pMain,'u_fresFactor'), P.fresFactor);
      gl.uniform1f(uloc(pMain,'u_glareRange'), P.glareRange);
      gl.uniform1f(uloc(pMain,'u_glareHard'), P.glareHard);
      gl.uniform1f(uloc(pMain,'u_glareFactor'), P.glareFactor);
      gl.uniform1f(uloc(pMain,'u_glareConv'), P.glareConv);
      gl.uniform1f(uloc(pMain,'u_glareOpp'), P.glareOpp);
      gl.uniform1f(uloc(pMain,'u_glareAngle'), P.glareAngle);
      gl.uniform1f(uloc(pMain,'u_blurR'), P.blurR);
      gl.uniform1i(uloc(pMain,'u_blurEdge'), P.blurEdge|0);
      gl.uniform4f(uloc(pMain,'u_tint'), P.tint[0], P.tint[1], P.tint[2], P.tint[3]);
      gl.uniform1f(uloc(pMain,'u_shExpand'), P.shExpand);
      gl.uniform1f(uloc(pMain,'u_shFactor'), P.shFactor);
      gl.uniform2f(uloc(pMain,'u_shPos'), P.shPos[0], P.shPos[1]);
      gl.uniform1i(uloc(pMain,'u_debug'), P.debug|0);
      gl.uniform1f(uloc(pMain,'u_rim'), (P.rim===undefined?1:P.rim));
      gl.uniform1f(uloc(pMain,'u_time'), now*0.001);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
    };

    canvas.addEventListener('pointermove', function(e){
      var r = canvas.getBoundingClientRect();
      var dpr = inst.dpr || 1;
      inst.target.x = (e.clientX - r.left - r.width/2) * dpr;
      inst.target.y = -(e.clientY - r.top - r.height/2) * dpr;
      inst.moved = true; inst.everMoved = true;
    });
    canvas.addEventListener('pointerleave', function(){ inst.moved = false; });

    inst.dispose = function(){
      var i = instances.indexOf(inst);
      if(i >= 0) instances.splice(i, 1);
      [rtBg, rtA, rtB].forEach(function(rt){
        if(rt){ gl.deleteTexture(rt.tex); gl.deleteFramebuffer(rt.fb); }
      });
      rtBg = rtA = rtB = null;
      var lose = gl.getExtension('WEBGL_lose_context');
      if(lose) lose.loseContext();
    };
    instances.push(inst);
    if(!raf){ raf = requestAnimationFrame(tick); }
    return inst;
  }

  function tick(now){
    var dt = Math.min((now-last)/1000, 1/30); last = now;
    for(var i=0;i<instances.length;i++){
      try{ instances[i].step(dt, now); }catch(e){ console.error(e); }
    }
    raf = requestAnimationFrame(tick);
  }

  window.Glass = {
    make: make,
    DEFAULTS: DEFAULTS,
    /* 统一的滑杆绑定：slider id → params key */
    bind: function(inst, map, onChange){
      Object.keys(map).forEach(function(id){
        var el = document.getElementById(id);
        if(!el) return;
        var key = map[id];
        var ALIAS = {shadowExpand:'shExpand', shadowFactor:'shFactor'};
        key = ALIAS[key] || key;
        var out = document.getElementById(id+'-v');
        function sync(){
          var v = parseFloat(el.value);
          if(key === 'tintA'){ inst.P.tint[3] = v/100; }
          else if(key === 'tintC'){ inst.P.tint[0]=v[0]; inst.P.tint[1]=v[1]; inst.P.tint[2]=v[2]; }
          else { inst.P[key] = v; }
          if(out) out.textContent = (Math.round(v*100)/100);
          if(onChange) onChange(key, v);
        }
        el.addEventListener('input', sync); sync();
      });
    }
  };
})();
"""
