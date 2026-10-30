# -*- coding: utf-8 -*-
"""motion-web 的规范索引与配方清单（从上游 references/ 的真实章节提取，未改写内容）"""

SPECS = [
{
"file": "affordance.md",
"title": "Affordance — 能点 ≠ 看得出能点",
"secs": [
"§0 The false pass",
"§1 The three questions",
"§2 The invitation must outlive the dwell (窗口 ⊇",
"§3 A tidiness rule must never close the last e",
"§4 描出来的，不是淡进来的",
"§5 Multiple invitations stagger; they don't sp",
"§6 The mark hugs the painted pixels, not the b",
"§7 Click and drag on the same element: 按下记坑，抬手",
"§8 Copy narrates; it never explains the intera",
"§9 Numeric oracles — 量出来，不是看出来",
"§10 The invisible handoff — 交接那一帧必须一样大",
"§11 When brightness runs out, spend on motion "
],
"lede": "Everything else in this skill makes motion happen. This file is about whether a human ever finds it.",
"lines": 396
},
{
"file": "baseline-ui.md",
"title": "Baseline UI — the floor, not the design",
"secs": [
"§1 The page works with motion switched off",
"§2 Nothing essential lives behind hover",
"§3 Keyboard and focus survive the choreography",
"§4 Hit targets and input hygiene",
"§5 Layout stability",
"§6 Responsive floor",
"§7 Performance floor",
"§8 Failure patterns"
],
"lede": "Everything here is checkable. If an item can only be argued about, it belongs in `page-design.md`.",
"lines": 101
},
{
"file": "build-mode.md",
"title": "Build Mode",
"secs": [
"Build Order",
"CSS Layering Rules",
"Tech Stack Decision Ladder (climb only when th",
"Implementation Rules",
"Performance Rules",
"Framework-Specific Rules",
"Verification Checklist",
"Numeric Oracles Over Screenshots",
"Failure Patterns to Avoid"
],
"lede": "Use `build` only when one of these is true: 1. A `MOTION_SPEC.md` or equivalent approved motion contract exists 2. The",
"lines": 332
},
{
"file": "choreography-arc.md",
"title": "Choreography Arc",
"secs": [
"What Is a Choreography Arc?",
"Arc Types",
"Transition Rhythm Rules",
"Opening Beat Checklist",
"Common Arc Failures"
],
"lede": "Use this reference when designing the full motion narrative of a page — not individual component animations, but how t",
"lines": 107
},
{
"file": "components.md",
"title": "Components — 组件级的craft，页面真正由什么构成",
"secs": [
"§1 There are two component dialects, and they ",
"§2 Every interactive component owes a state ma",
"§3 Header / nav",
"§4 Hero",
"§5 Buttons",
"§6 Eyebrow, tag, badge",
"§7 Cards",
"§8 Media and figures",
"§9 Forms and fields",
"§10 Accordion / FAQ",
"§11 Dialog, drawer, popover",
"§12 Index / filter / tabs"
],
"lede": "`page-design.md` decides the page's shape. This file is the vocabulary that fills it: nav, hero, button, card, field, ",
"lines": 406
},
{
"file": "composition-guide.md",
"title": "Dynamic Composition & Orchestration Guide",
"secs": [
"The Agentic Ideation Flow (动态创意合成流)",
"1. Deconstructing the Semantic Vibe",
"2. Dynamic Visual Synthesis (色彩与排版编排)",
"3. Designing Bespoke Narrative Grids (版面结构)",
"4. Choreographing Tactile Motion (动效与交互编排)",
"5. Inventing the Signature Mechanic (每页一个签名交互，",
"6. Asset Prompt Patterns (需要用户生成图片素材时)",
"Output Contract (The Creative Report)"
],
"lede": "This guide defines how to use the motion and visual banks as **raw materials and design logic**, rather than rigid tem",
"lines": 150
},
{
"file": "design-slop.md",
"title": "Design Slop — 动效页专属的 AI 味闸门",
"secs": [
"A. Still-frame gates (motion off)",
"B. Motion gates (motion on)",
"C. What to do with a hit"
],
"lede": "Generic anti-slop advice (\"use a real type scale\", \"don't invent metrics\") applies here too, but it is not what makes ",
"lines": 112
},
{
"file": "handfeel.md",
"title": "Handfeel — Why Motion Feels Dead and How to Fix It",
"secs": [
"Diagnosis Table",
"§1 Underdamped Spring (replaces lerp)",
"§2 Velocity Coupling (lean into movement)",
"§3 Wheel Momentum Guard",
"§4 Secondary Motion / Jelly Wobble",
"§5 Fake Lighting on Flat Images (2.5D)",
"§6 Idle Breathing",
"§7 Following — the half that must *not* oversh",
"§8 Screen shake",
"Composition Rule"
],
"lede": "The user saying \"手感差 / 太生硬 / 四平八稳 / 不跟手 / 没那种感觉\" almost always maps to one of the mechanical gaps below. Diagnose agai",
"lines": 248
},
{
"file": "image-asset-pipeline.md",
"title": "Image Asset Pipeline — 图片资产怎么造出来",
"secs": [
"§1 Keying: distance from *this image's own* ba",
"§2 Crop to the alpha bbox — the empty margin *",
"§3 Line art is a different asset: alpha = ink,",
"§4 Measure the placement metadata in the same ",
"§5 Sprite atlases: same batch, same sun",
"§6 Resolution budget is **per element**, and t",
"§7 A texture's density is a function of the di",
"§8 Provenance",
"§9 Cheap wins at the asset layer — 一张白图喂十五层",
"§10 Checklist"
],
"lede": "`image-plane-3d.md` starts at \"each asset ships with measured `w/h/cx/baseline`\". **This file is the step before that*",
"lines": 289
},
{
"file": "image-plane-3d.md",
"title": "Image Planes in a Real Camera — 用图片资产做出真纵深",
"secs": [
"§1 Why it works at all",
"§2 The asset contract — 素材必须带四个数",
"§3 The long lens is the look — `fov 26`, not 5",
"§4 Occlusion beats every shader — 剪影必须咬住",
"§5 Transparent planes: sort by hand",
"§6 Contact shadow is not optional — and a shad",
"§7 「有拼接感」 is a colour-temperature bug — 量，别看",
"§8 One environment pass over everything",
"§9 Vertex motion: uv.y² or it isn't bending",
"§10 Measure the projection; don't derive it",
"§11 Checklist",
"§12 Two proven topologies — 相机走 vs 世界走"
],
"lede": "The route almost nobody takes: **flat PNG cutouts placed as upright planes at real world coordinates, inside a real `P",
"lines": 427
},
{
"file": "light-3d.md",
"title": "Light 3D",
"secs": [
"1. Work Division (工种分工)",
"2. Cross-Skill Handoff Contract (资产交付契约)",
"3. Implementation Rules",
"4. Environment Lighting Tints Everything It To",
"5. DOM Over a Moving Scene (两套坐标系，撞上只是迟早)",
"6. Spec Fields"
],
"lede": "Use light 3D when a webpage needs spatial interaction, product staging, shader atmosphere, or camera choreography.",
"lines": 112
},
{
"file": "motion-spec.md",
"title": "Motion Spec",
"secs": [
"Reference Entry Fields",
"`MOTION_SPEC.md` Template",
"1. Goal",
"2. Choreography",
"3. Motion Tokens",
"4. Interaction Map",
"5. Scroll Timeline",
"6. 3D / Canvas / Media",
"7. Baseline UI",
"8. Accessibility And Performance",
"9. Stack",
"10. References"
],
"lede": "Use this file whenever a task needs motion extraction, motion design, or implementation handoff.",
"lines": 131
},
{
"file": "motion-tokens.md",
"title": "Motion Tokens",
"secs": [
"Duration Scale",
"Easing Dictionary",
"Stagger Patterns",
"Transform Property Budget",
"Reduced Motion Fallback Ladder",
"`will-change` Rules"
],
"lede": "Complete reference for duration, easing, spring config, and stagger values. Use these as your first lookup before inve",
"lines": 158
},
{
"file": "page-blueprints.md",
"title": "Page Blueprints — 这个页面到底该有哪些板块，每块写什么",
"secs": [
"§1 The section vocabulary",
"§2 Blueprints",
"§3 Ordering: what actually decides the sequenc",
"§4 Copy is the design's other half",
"§5 Information architecture: one page or sever",
"§6 How this maps onto the motion macrostructur",
"§7 Checklist"
],
"lede": "`page-design.md` §1 picks the **macrostructure** (single scene / acts / editorial / index / instrument). This file is ",
"lines": 253
},
{
"file": "page-design.md",
"title": "Page Design — 动效页的设计，不是通用 UI 设计",
"secs": [
"§1 Macrostructure comes from the mechanic's de",
"§2 Measured — what current award winners actua",
"§3 Design the space the motion needs",
"§4 Typography — scale contrast *is* the design",
"§5 Colour — commit, then let the artwork bring",
"§6 Spacing rhythm and section pacing",
"§7 Mobile is a different design, not a smaller",
"§8 Checklist"
],
"lede": "The still frame is half the deliverable. This file is how the page looks and reads **before anything moves**; `design-",
"lines": 211
},
{
"file": "pattern-recipes.md",
"title": "Pattern Recipes",
"secs": [
"1. Text Split Reveal (Line by Line)",
"2. Magnetic Hover",
"3. Clip-Path Curtain Reveal",
"4. Scroll-Velocity Skew",
"5. Horizontal Scroll Rail",
"6. Parallax Depth Stack",
"7. Cursor Trail / Custom Cursor",
"8. Route / Page Transition (Framer Motion)",
"9. Scroll-Pinned Sequence (GSAP)",
"10. Number/Counter Reveal",
"11. SVG Goo Metaball Reveal (悬停/拖拽揭示第二形态)",
"12. Lenis + GSAP ScrollTrigger Canonical Wirin"
],
"lede": "Ready-to-use motion pattern implementations for creative web. Each recipe includes: - What it does and when to use it ",
"lines": 1023
},
{
"file": "production-polish.md",
"title": "Production Polish — 从「能跑」到「像成品」",
"secs": [
"§1 The head, in full",
"§2 The OG image",
"§3 404, error, and the routes nobody designed",
"§4 The states that only exist off the happy pa",
"§5 Dark mode — only if you mean it",
"§6 The small things that read as \"finished\"",
"§7 Structure that machines read",
"§8 Analytics, consent, third parties",
"§9 Pre-ship: run these, don't estimate them",
"§10 Checklist"
],
"lede": "The page builds, the mechanic works, the design gate passed. It still reads as a demo, because the twenty things that ",
"lines": 256
},
{
"file": "project-setup.md",
"title": "Project Setup — 0→1 把一个网页真的立起来",
"secs": [
"§1 Page stack ladder (climb only when the lowe",
"§2 The token layer — three levels, one substra",
"§3 Type and space scales — fluid, and anchored",
"§4 Fonts — the one thing that shifts the layou",
"§5 Cascade layers — one order, no specificity ",
"§6 File layout",
"§7 Images — the other half of the first paint",
"§8 Budget and deploy",
"§9 Checklist"
],
"lede": "`page-design.md` decides what the page looks like. This file decides what it *is*: which stack, which token layer, whi",
"lines": 357
},
{
"file": "render-layer.md",
"title": "Render Layer — 用什么画，比画什么先决定",
"secs": [
"1. Choosing the layer",
"2. Fonts are part of the layer",
"3. Ink render — measured from `ink-crowd.verce",
"4. Two opposite motion contracts, both correct"
],
"lede": "Every other doc here assumes the page is DOM + CSS. That assumption is the ceiling this skill kept hitting: seven case",
"lines": 227
},
{
"file": "scene-audio.md",
"title": "Scene Audio — 场景声音",
"secs": [
"§1 Three buses, because there are three compla",
"§2 Balance is the relationship between the lin",
"§3 Duck the bed under the hand — fast down, sl",
"§4 Add discrete events, not another continuous",
"§5 A continuous quantity fed to a hand sound w",
"§6 The filter eats 10–20 dB. Look at the chain",
"§7 Measuring: per-sample subtraction, on a det",
"§8 Checklist"
],
"lede": "Sound for a scroll-driven scene: a music bed, an ambient world, and the noises the visitor's own hand makes. All three",
"lines": 209
},
{
"file": "scene-streaming.md",
"title": "Scene Streaming — 大场景怎么装得下",
"secs": [
"§1 Activate by screen window, not by index",
"§2 Scan cooperatively — yield inside the loop,",
"§3 DOM mutations are not frame work — batch an",
"§4 Dispose everything, and cache by URL",
"§5 Slice a large plate instead of uploading it",
"§6 Stream audio the same way",
"§7 Checklist"
],
"lede": "A scroll scene with hundreds of plates cannot hold them all. The machinery below is what makes a long image-plane piec",
"lines": 151
},
{
"file": "shaders-spec.md",
"title": "WebGL Shaders Specification & Recipes",
"secs": [
"1. Do Shaders Need Installation? (关于安装与依赖)",
"2. WebGL Integration Patterns (集成技术栈对比)",
"3. React Integration via `@paper-design/shader",
"4. Standard Shader Uniforms (控制变量)",
"5. The Core GLSL Recipes Catalog (核心算法库)",
"6. Integration Traps (三个静默失败 + 两个真实配方)",
"7. Performance & Degradation Rules (性能与降级红线)"
],
"lede": "Fragment shaders (GLSL) are the ultimate design material for high-end organic animations (liquid, fluid, distortion, g",
"lines": 553
},
{
"file": "tactile-texture.md",
"title": "Web Tactile Texture Specification & Technical Stack",
"secs": [
"1. SVG Filter Engine (粘滞流体与置换噪点)",
"2. CSS Houdini Paint API (多线程程序噪声)",
"3. OffscreenCanvas & Threaded Render (多线程异步渲染)",
"4. Canvas Pattern Buffering (高性能静态噪点)",
"5. High-Resolution Display Rules (高分屏与防抖)"
],
"lede": "To create high-end premium web experiences, motion must be paired with **tactile textures (触觉质感)**.",
"lines": 197
},
{
"file": "timeline-orchestration.md",
"title": "Timeline Orchestration — 多轨滚动时间轴",
"secs": [
"§1 Read the schedule horizontally, not per lay",
"§2 Easing lives in exactly one layer",
"§3 Easing evens out the parameter, not what th",
"§4 One window, one event — a fade eats everyth",
"§5 A keyframe with zero velocity guarantees a ",
"§6 The apparatus must not outlive its content",
"§7 An instruction cannot precede its referent",
"§8 Every act owes one money frame (定妆帧)",
"§9 Stagger copy blocks; don't fade a screenful",
"§10 Threshold dissolves: the histogram of the ",
"§11 「灵动 vs 飘」 is a stillness ratio, not an eas",
"§12 Checklist"
],
"lede": "`choreography-arc.md` picks the arc. This file is about what goes wrong once a page has **many tracks sharing one scro",
"lines": 281
},
{
"file": "verification-harness.md",
"title": "Verification Harness — 判据台架",
"secs": [
"§0 The one thing that makes a harness harmful",
"§1 The probe surface is a design contract",
"§2 `__seek` lies about anything with a lifetim",
"§3 The general oracle: render the same frame t",
"§4 When the frame is always moving, a before/a",
"§5 State exits: how you measure an interaction",
"§6 Don't race the clock in headless",
"§7 Sampling rate: ≤ 1/5 of the event, and neve",
"§8 Peak is not weight; and never measure a lin",
"§9 The ruler has a resolution floor",
"§10 Harness hygiene",
"§11 Two neighbouring rulers live in `3d-scene-"
],
"lede": "`affordance.md` §9 lists *which* numbers to print. This file is the machinery that makes those numbers trustworthy, an",
"lines": 429
}
]

RECIPES = [
{
"no": 1,
"name": "Text Split Reveal (Line by Line)",
"what": "Each line of a heading is wrapped in a clip-path mask and slides up into view.",
"use": "Editorial section headers, hero text, chapter titles. (Arc: `editorial`, `cold-open`)"
},
{
"no": 2,
"name": "Magnetic Hover",
"what": "An element (button, icon, avatar) bends toward the cursor when the mouse enters its radius.",
"use": "CTAs, social icons, nav links, creative portfolio buttons."
},
{
"no": 3,
"name": "Clip-Path Curtain Reveal",
"what": "An image or block reveals itself by animating a clip-path from closed to open, like a curtain being pulled.",
"use": "Project thumbnails, editorial images, section transitions."
},
{
"no": 4,
"name": "Scroll-Velocity Skew",
"what": "Elements skew on the Y (or X) axis proportional to how fast the user is scrolling. The faster the scroll, the more lean. Snaps back elastically on slow/stop.",
"use": "Large serif headings, editorial sections, hero type."
},
{
"no": 5,
"name": "Horizontal Scroll Rail",
"what": "A section scrolls horizontally while the page scroll is vertical. The section \"pins\" in place while the horizontal rail scrubs through.",
"use": "Portfolio project galleries, timeline sequences, case study slides."
},
{
"no": 6,
"name": "Parallax Depth Stack",
"what": "Multiple layers move at different speeds during scroll, creating spatial depth.",
"use": "Hero sections, product atmosphere, editorial feature images."
},
{
"no": 7,
"name": "Cursor Trail / Custom Cursor",
"what": "A custom circle follows the mouse with spring lag. Optionally morphs on hover states.",
"use": "Creative portfolios, award sites, interactive product pages."
},
{
"no": 8,
"name": "Route / Page Transition (Framer Motion)",
"what": "Page content fades or slides out on navigation and the next page fades/slides in.",
"use": "Next.js portfolios, multi-page creative sites."
},
{
"no": 9,
"name": "Scroll-Pinned Sequence (GSAP)",
"what": "A section pins to the viewport and plays an animation as the user scrolls through a scroll distance, like a video scrubbed by scroll.",
"use": "Product feature reveals, storytelling sequences, step-by-step process sections."
},
{
"no": 10,
"name": "Number/Counter Reveal",
"what": "A number animates from 0 (or previous value) to its final value when scrolled into view.",
"use": "Stats, metrics, data reveals."
},
{
"no": 11,
"name": "SVG Goo Metaball Reveal (悬停/拖拽揭示第二形态)",
"what": "A cluster of SVG circles follows the pointer, blurred and re-thresholded via `feGaussianBlur` + `feColorMatrix` so they melt into one blobby shape (\"goo\" effect). That blob is then used as a `<mask>` over a second image/layer — wherever the pointer drags, the hidden layer shows through. Zero WebGL.",
"use": "\"Reveal the alternate form\" interactions — drag to unmask a hidden illustration, hover to reveal a photo negative, paint-away overlays. (✅ 实测 2026-07: drag-across-face → viking helmet reveal)"
},
{
"no": 12,
"name": "Lenis + GSAP ScrollTrigger Canonical Wiring",
"what": "The standard three-piece hookup for inertial smooth-scroll (Lenis) driving GSAP's ScrollTrigger. Missing any one piece causes scroll-jank or ScrollTrigger reading stale positions.",
"use": "Any GSAP ScrollTrigger build that also wants smooth/inertial scrolling rather than native scroll."
},
{
"no": 13,
"name": "Scroll-Adaptive Header Theme (背景感知反色 Header)",
"what": "A fixed header/nav that flips between light and dark styling based on what section is currently behind it — reading each candidate section's actual computed background color rather than hardcoding \"section 3 is dark\".",
"use": "Fixed headers over pages that alternate light/dark full-bleed sections."
},
{
"no": 14,
"name": "Drawn Annotation Ring (朱砂圈 — 圈住一个东西，邀请点它)",
"what": "A hand-drawn-looking ellipse that *draws itself* around a target, sized to the target's real",
"use": "Inviting a click on something that lives in the artwork rather than in the UI — a figure in a"
},
{
"no": 15,
"name": "Verlet Text Curtain (文字帘 — 悬挂、被滚动激励、可拨开)",
"what": "A block of copy hung as physical strings — each column is an independent vertical Verlet chain.",
"use": "editorial hero copy, poem/lyric sections, a menu that should feel touchable, anything where"
},
{
"no": 16,
"name": "Native Scroll Reveal & CSS-Only Stagger (no library, no observer)",
"what": "The two things almost every page uses GSAP for — reveal-on-enter and staggered lists — now have",
"use": ""
},
{
"no": 17,
"name": "Corner-Pin Warp (四角形变 — 把矩形元素贴进任意四边形)",
"what": "Map any DOM element onto an arbitrary convex quadrilateral with one `matrix3d`. A projective",
"use": "cards that bend as they hang or drag, a hero image keystoned into a surface, a page-fold or"
},
{
"no": 18,
"name": "Verlet Card Chain (卡片链 — 一串图片挂在光标下，跟着摆动并弯折)",
"what": "N image cards strung on a Verlet chain that hangs from the pointer. Each card is corner-pinned",
"use": "a work index where hovering a row trails its images, a drag-to-browse gallery, a cursor that"
},
{
"no": 19,
"name": "Slack String Between Anchor and Datum (软绳硬端点 —— 中段乱写，端点不许说谎)",
"what": "",
"use": ""
},
{
"no": 20,
"name": "Cumulative Emergence (堆积式涌现 —— 数量本身就是构图，而且一动不动)",
"what": "",
"use": ""
}
]


SPEC_ZH = {
 'affordance.md': '能点的东西要长得像能点：光标、位移、描边、按压反馈，四件套缺一个用户就找不到。',
 'baseline-ui.md': '最低标准清单：对齐、层级、间距、对比度、焦点态——这些只是地板，不是设计。',
 'build-mode.md': '什么时候可以开始写：先有 motion contract / 验收口径，再动手敲代码。',
 'choreography-arc.md': '整页的编排弧线：入场 → 停留 → 高潮 → 收尾，一页只讲一次高潮。',
 'components.md': '组件级手活：按钮、卡片、输入框、标签各自的状态机与手感。',
 'composition-guide.md': '多元素怎么编排：谁先动、谁跟随、谁保持静止，才有主次。',
 'design-slop.md': 'AI 味闸门：套路渐变、无意义漂浮、粒子上瘾、每块都动——逐条删。',
 'handfeel.md': '手感为什么死：把时序、缓动、质量感拆开，逐项对照修。',
 'image-asset-pipeline.md': '图片资产怎么造：生成、抠图、压缩、图集、懒加载的完整链路。',
 'image-plane-3d.md': '用图片层做真纵深：相机运动、视差层、遮挡关系怎么排。',
 'light-3d.md': '轻量 3D：不引引擎，也能有光、有反射、有空间感。',
 'motion-spec.md': '动效契约模板：触发、时长、曲线、降级、验收，写成一张能对的表。',
 'motion-tokens.md': '令牌表：7 档时长、9 条曲线、6 组弹簧、5 种错峰——所有动效从这里取数。',
 'page-blueprints.md': '页面该有哪些板块，每块写什么，顺序为什么是这样。',
 'page-design.md': '动效页的设计逻辑：和通用 UI 设计不是一回事，先定叙事再定版式。',
 'pattern-recipes.md': '20 条可复用配方，每条都给了 vanilla / Framer / GSAP 三种写法。',
 'production-polish.md': '从「能跑」到「像成品」：最后一公里清单（降级、性能、边缘态）。',
 'project-setup.md': '0→1 把网页立起来：目录、构建、部署、环境变量。',
 'render-layer.md': '用什么画先于画什么：DOM / Canvas / WebGL 的取舍与混用边界。',
 'scene-audio.md': '场景声音：什么时候出声、音量曲线、静音开关与无障碍。',
 'scene-streaming.md': '大场景怎么装得下：分块加载、预取、降级与首帧预算。',
 'shaders-spec.md': '着色器配方：噪声、液态玻璃、色散、扫光的可抄写法。',
 'tactile-texture.md': '触感质感：颗粒、噪点、材质叠层，让平面看起来有厚度。',
 'timeline-orchestration.md': '多轨滚动时间轴：一屏一轨，用滚动位置驱动进度而不是定时器。',
 'verification-harness.md': '判据台架：怎么证明动效达标，而不是「看着还行」。',
}
