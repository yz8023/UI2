# -*- coding: utf-8 -*-
"""XPopup 体验馆：20 个弹窗 + 20 个动画 + 45 个 Builder 设置 + 5 个手势行为。

数据来自 junixapp/XPopup（Apache-2.0）的真实 API 面：impl/core/enums 三个包里的
弹窗类型、PopupAnimation 的 20 个枚举值、XPopup.Builder 的 45 个方法。
演示是按这些行为在 Web 上重写的，不含上游任何源码或图片。
"""

# ─────────────────────────── 弹窗清单 ───────────────────────────
TYPES = [
    # group, id, name, api, desc, chips
    ('内置弹窗', 'confirm', '确认弹窗', 'asConfirm()',
     '标题 + 正文 + 取消/确认，可隐藏取消键、可加「不再提示」勾选。默认从中心缩放淡入。',
     ['Center', 'ScaleAlphaFromCenter', '点背景关闭']),
    ('内置弹窗', 'input', '输入弹窗', 'asInputConfirm()',
     '带输入框的确认框：自动聚焦、字数计数、确认后回传文本，可换行多行。',
     ['Center', 'autoOpenSoftInput', '键盘上移']),
    ('内置弹窗', 'loading', '加载弹窗', 'asLoading()',
     '两种样式：环形 ProgressBar 与 Spinner；可延时关闭、可只换标题不重建弹窗。',
     ['Center', '不响应返回键', '样式热切换']),

    ('列表与选择', 'centerList', '中间列表', 'asCenterList()',
     '中间弹出的列表：超过最大高度就内部滚动，支持图标、选中态、回调位置。',
     ['Center', '内部滚动', 'OnSelectListener']),
    ('列表与选择', 'centerCheck', '中间列表 · 选中', 'asCenterList(checked)',
     '传入 checkedPosition 后长这样：选中项高亮 + 左侧对勾，点一项即回传。',
     ['Center', 'checkedPosition', '回传 index']),
    ('列表与选择', 'bottomList', '底部列表', 'asBottomList()',
     '从底部弹出、可手势拖拽关闭；内容超长时内部滚动，且和外层手势不打架（嵌套滚动）。',
     ['Bottom', '拖拽关闭', '嵌套滚动']),
    ('列表与选择', 'bottomCheck', '底部列表 · 选中', 'asBottomList(checked)',
     '底部列表 + 选中态，默认给一组「重置 / 确定」这样的操作区。',
     ['Bottom', '选中态', '三阶拖拽']),

    ('抽屉与阴影', 'drawerL', '左侧抽屉', 'asDrawer(Left)',
     '像 DrawerLayout，但可以从任何页面弹；支持边缘拖拽、宽度可配。',
     ['Drawer', '边缘拖拽', 'PopupPosition.Left']),
    ('抽屉与阴影', 'drawerR', '右侧抽屉', 'asDrawer(Right)',
     '右侧抽屉 + 状态栏阴影；列表型抽屉自带选中态与分组标题。',
     ['Drawer', '状态栏阴影', 'PopupPosition.Right']),
    ('抽屉与阴影', 'partTop', '局部阴影 · 上', 'asPartShadow(Top)',
     '只压住目标 View 下方的一块，其余区域保持可见可点 —— 筛选栏下拉就是这个。',
     ['PartShadow', 'atView', '不挡其余界面']),
    ('抽屉与阴影', 'partBottom', '局部阴影 · 下', 'asPartShadow(Bottom)',
     '从目标 View 向上展开，锚点跟着被点的那个标签走。',
     ['PartShadow', '智能翻转', '不挡其余界面']),

    ('媒体与全屏', 'imageViewer', '大图浏览', 'asImageViewer()',
     '双指缩放、双击放大、下拉淡出关闭、左右切换、页码；超长图按需加载不会 OOM。',
     ['ImageViewer', '捏合缩放', '下拉关闭']),
    ('媒体与全屏', 'fullScreen', '全屏弹窗', 'asFullScreen()',
     '看起来就是一个 Activity：自带标题栏与返回，适合登录、分步选择这类页面级内容。',
     ['FullScreen', '可配任意动画', '返回键关闭']),

    ('依附与定位', 'attach', '依附弹窗', 'asAttachList()',
     '贴着某个 View 弹出来，自动判断上下、空间不够时翻转；微信朋友圈点赞就是这一类。',
     ['Attach', '自动翻转', 'atView']),
    ('依附与定位', 'bubble', '气泡弹窗', 'asBubbleAttach()',
     '带小三角的气泡，横竖两个方向都能用；三角会自动对齐锚点。',
     ['Bubble', '四方向', 'offset 微调']),
    ('依附与定位', 'position', '自由定位', 'asPosition()',
     '想放哪就放哪：左侧消息条、屏幕中部、顶部通知都是这一套 + 不同动画。',
     ['Position', 'offsetX/Y', 'TranslateFromTop']),

    ('自定义', 'zhihu', '知乎式评论', 'asCustom()',
     '自绘底部弹层：标题栏 + 列表 + 输入条，打开时列表跟着上移，关闭时回收。',
     ['Bottom', '嵌套滚动', 'isViewMode']),
    ('自定义', 'drawerList', '列表抽屉', 'asCustom(Drawer)',
     '抽屉里放列表：分组标题 + 选中态 + 图标，宽度约 78%，右侧留一条可点的背景。',
     ['Drawer', '分组列表', '拖拽关闭']),
    ('自定义', 'multi', '多层弹窗', 'asCustom() x2',
     '弹窗里再弹一个：父弹窗压暗但不销毁，关闭子弹窗后父弹窗状态还在。',
     ['多实例', '层级栈', 'isDestroyOnDismiss']),
    ('自定义', 'bindLayout', '复用已有布局', 'bindLayout(id)',
     '布局完全用你自己的，只借用 XPopup 的动画、手势、阴影和键盘处理。',
     ['bindLayout', 'id 约定', '零侵入']),
]

# ─────────────────────────── 20 个动画 ───────────────────────────
# (枚举名, 中文, 分组, 初始 transform, 初始 opacity)
ANIMS = [
    ('ScaleAlphaFromCenter', '中心缩放淡入', '缩放', 'scale(.86)', .0),
    ('ScaleAlphaFromLeftTop', '左上角缩放', '缩放', 'translate(-30%,-30%) scale(.86)', .0),
    ('ScaleAlphaFromRightTop', '右上角缩放', '缩放', 'translate(30%,-30%) scale(.86)', .0),
    ('ScaleAlphaFromLeftBottom', '左下角缩放', '缩放', 'translate(-30%,30%) scale(.86)', .0),
    ('ScaleAlphaFromRightBottom', '右下角缩放', '缩放', 'translate(30%,30%) scale(.86)', .0),
    ('TranslateAlphaFromLeft', '左移入淡入', '平移+淡入', 'translateX(-26%)', .0),
    ('TranslateAlphaFromRight', '右移入淡入', '平移+淡入', 'translateX(26%)', .0),
    ('TranslateAlphaFromTop', '上移入淡入', '平移+淡入', 'translateY(-26%)', .0),
    ('TranslateAlphaFromBottom', '下移入淡入', '平移+淡入', 'translateY(26%)', .0),
    ('TranslateFromLeft', '左移入', '纯平移', 'translateX(-100%)', 1),
    ('TranslateFromRight', '右移入', '纯平移', 'translateX(100%)', 1),
    ('TranslateFromTop', '上移入', '纯平移', 'translateY(-100%)', 1),
    ('TranslateFromBottom', '下移入', '纯平移', 'translateY(100%)', 1),
    ('ScrollAlphaFromLeft', '左滚入', '滚入', 'translateX(-40%) scale(.94)', .0),
    ('ScrollAlphaFromLeftTop', '左上滚入', '滚入', 'translate(-40%,-40%) scale(.9)', .0),
    ('ScrollAlphaFromTop', '上滚入', '滚入', 'translateY(-40%) scale(.94)', .0),
    ('ScrollAlphaFromRightTop', '右上滚入', '滚入', 'translate(40%,-40%) scale(.9)', .0),
    ('ScrollAlphaFromRight', '右滚入', '滚入', 'translateX(40%) scale(.94)', .0),
    ('ScrollAlphaFromBottom', '下滚入', '滚入', 'translateY(40%) scale(.94)', .0),
    ('NoAnimation', '无动画', '无', 'none', 1),
]

# ─────────────────────────── 45 个 Builder 设置 ───────────────────────────
# (组, 方法名, 中文, 默认值, 说明, 是否有实时效果)
SETTINGS = [
    ('显隐与时序', 'dismissOnBackPressed', '返回键关闭', True, '按系统返回键是否关闭弹窗', True),
    ('显隐与时序', 'dismissOnTouchOutside', '点外部关闭', True, '点半透明背景是否关闭', True),
    ('显隐与时序', 'autoDismiss', '自动关闭', False, '展示后立即关闭（做嵌套弹窗时用）', False),
    ('显隐与时序', 'isDestroyOnDismiss', '关闭即销毁', False, '一次性弹窗开这个，省内存防泄漏', False),
    ('显隐与时序', 'animationDuration', '动画时长', '360ms', '全局动画时长，默认 360ms', True),
    ('显隐与时序', 'keepScreenOn', '保持常亮', False, '弹窗展示期间屏幕不熄灭', False),
    ('显隐与时序', 'popupAnimation', '指定动画', '按类型兜底', '20 种动画任选，见「动画」页', True),
    ('显隐与时序', 'customAnimator', '自定义动画器', '无', '继承 PopupAnimator 实现三段式', False),
    ('背景', 'hasShadowBg', '半透明背景', True, '关掉后背景完全透出', True),
    ('背景', 'shadowBgColor', '背景色', '#50000000', '半透明遮罩的颜色', True),
    ('背景', 'hasBlurBg', '背景模糊', False, '把背后的界面做高斯模糊', True),
    ('背景', 'isClickThrough', '点击穿透', False, '背景区域的点击透到下层', False),
    ('背景', 'isTouchThrough', '触摸穿透', False, '常用于只做提示的气泡', False),
    ('背景', 'borderRadius', '圆角', '14dp', '统一改弹窗四个角的圆角', True),
    ('尺寸', 'popupWidth', '固定宽度', '自适应', '指定宽，不再按内容撑开', False),
    ('尺寸', 'popupHeight', '固定高度', '自适应', '指定高，常用于底部弹层', False),
    ('尺寸', 'maxWidth', '最大宽度', '594dp', '超过就撑满可用宽度', True),
    ('尺寸', 'maxHeight', '最大高度', '屏幕 0.8', '列表类弹窗的滚动阈值', True),
    ('尺寸', 'isCenterHorizontal', '水平居中', False, 'Position 弹窗按屏幕中线对齐', True),
    ('尺寸', 'positionByWindowCenter', '以窗口中线定位', False, '横屏小窗时按窗口而不是屏幕定位', False),
    ('输入法', 'autoOpenSoftInput', '自动弹键盘', False, '展示时直接拉起输入法', True),
    ('输入法', 'moveUpToKeyboard', '键盘上移', True, '弹窗跟随键盘上移，不被挡住', True),
    ('输入法', 'isCoverSoftInput', '覆盖键盘', False, '弹窗压在键盘之上而不是让位', False),
    ('输入法', 'autoFocusEditText', '自动聚焦输入框', True, '弹窗里的 EditText 自动获得焦点', True),
    ('定位', 'atView', '依附到 View', '无', 'Attach / PartShadow 的锚点', True),
    ('定位', 'atPoint', '依附到坐标', '无', '长按位置弹菜单时用', False),
    ('定位', 'watchView', '跟随 View 移动', '无', '锚点移动时弹窗跟着走', False),
    ('定位', 'popupPosition', '指定方向', '自动', 'Left / Top / Right / Bottom，手动覆盖自动翻转', True),
    ('定位', 'offsetX', 'X 偏移', '0', '在自动定位基础上再偏移', True),
    ('定位', 'offsetY', 'Y 偏移', '0', '同上，竖直方向', True),
    ('定位', 'isViewMode', 'View 模式', False, '用 View 而不是 Dialog 承载，可放 Fragment/ViewPager', True),
    ('状态栏', 'hasStatusBar', '占用状态栏', True, '内容是否延伸到状态栏下面', True),
    ('状态栏', 'hasStatusBarShadow', '状态栏阴影', False, '顶部加一层渐变阴影，抽屉常用', True),
    ('状态栏', 'isLightStatusBar', '浅色状态栏图标', '跟随', '深色弹窗要设成 true', False),
    ('状态栏', 'statusBarBgColor', '状态栏底色', '透明', '给状态栏上色', False),
    ('导航栏', 'hasNavigationBar', '占用导航栏', True, '底部手势条区域的处理', False),
    ('导航栏', 'isLightNavigationBar', '浅色导航栏图标', '跟随', '同上', False),
    ('导航栏', 'navigationBarColor', '导航栏底色', '透明', '给导航栏上色', False),
    ('手势', 'enableDrag', '开启拖拽', True, '底部/抽屉弹窗可以拖着关', True),
    ('手势', 'isThreeDrag', '三阶拖拽', False, '拖到中间停一下再松手才关闭', True),
    ('手势', 'notDismissWhenTouchInView', '区域内不关闭', '无', '手指落在这个 View 上时不算点外部', False),
    ('主题', 'isDarkTheme', '深色主题', True, '内置弹窗的深/浅色两套皮肤', True),
    ('主题', 'customHostLifecycle', '绑定生命周期', '无', '页面销毁自动 dismiss，防泄漏', False),
    ('回调', 'setPopupCallback', '生命周期回调', '无', 'onShow / onDismiss / onCreated / onDrag', False),
    ('后台', 'enableShowWhenAppBackground', '后台可弹', False, '需要悬浮窗权限，通知类场景', False),
]

# ─────────────────────────── 手势行为 ───────────────────────────
GESTURES = [
    ('drag', '拖拽关闭', '按住顶部把手往下拖，超过 30% 或速度够了就关闭，否则回弹。'),
    ('three', '三阶拖拽', '第一段跟手、第二段加速、第三段松手判定 —— 长列表里不会一滑就关。'),
    ('nested', '嵌套滚动', '列表先滚到底，再继续下拉才开始拖弹窗，两个手势不打架。'),
    ('outside', '点外部关闭 / 点穿', 'dismissOnTouchOutside 与 isTouchThrough 的区别。'),
    ('blur', '背景模糊', 'hasBlurBg 打开与关闭的观感差异（真做高斯模糊）。'),
]

XP_CSS = r"""
/* ══════════ XPopup 体验馆 ══════════ */
.xp-seg{display:flex;gap:4px;padding:4px;border-radius:14px;background:rgba(255,255,255,.05);
  border:1px solid rgba(255,255,255,.1);overflow:auto;scrollbar-width:none;margin:12px 0 4px}
.xp-seg::-webkit-scrollbar{display:none}
.xp-seg b{flex:1;text-align:center;padding:8px 10px;border-radius:10px;font-size:12px;font-weight:500;
  color:rgba(233,239,247,.62);white-space:nowrap;cursor:pointer;transition:.18s}
.xp-seg b.on{color:#06121c;font-weight:700;background:linear-gradient(180deg,#cfe3ff,#9dccff)}
.xp-group{font-size:10.5px;letter-spacing:.1em;color:rgba(233,239,247,.36);margin:18px 0 7px}
.xp-list{display:flex;flex-direction:column;gap:8px}
.xp-item{display:flex;gap:11px;padding:12px 13px;border-radius:16px;cursor:pointer;
  border:1px solid rgba(255,255,255,.09);background:rgba(255,255,255,.035);transition:.18s var(--ease)}
.xp-item:active{transform:scale(.985);background:rgba(255,255,255,.07)}
.xp-item .ico{width:34px;height:34px;flex:0 0 auto;border-radius:11px;display:grid;place-items:center;
  font-size:14px;background:linear-gradient(150deg,rgba(157,204,255,.22),rgba(95,219,168,.12));
  border:1px solid rgba(157,204,255,.26)}
.xp-item .txt{flex:1;min-width:0}
.xp-item h4{font-size:13px;font-weight:700;display:flex;align-items:center;gap:7px;flex-wrap:wrap}
.xp-item h4 i{font-style:normal;font-size:9.5px;font-weight:600;color:rgba(157,204,255,.95);
  padding:1px 6px;border-radius:5px;background:rgba(157,204,255,.12);font-family:ui-monospace,Menlo,monospace}
.xp-item p{font-size:10.5px;color:rgba(233,239,247,.5);line-height:1.65;margin-top:4px}
.xp-item .chips{display:flex;gap:4px;flex-wrap:wrap;margin-top:7px}
.xp-item .chips s{text-decoration:none;font-size:9px;padding:1.5px 6px;border-radius:99px;
  color:rgba(233,239,247,.62);border:1px solid rgba(255,255,255,.13)}
.xp-item .go{font-size:15px;color:rgba(233,239,247,.28);align-self:center}

/* ── 动画网格 ── */
.an-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(112px,1fr));gap:8px}
.an-t{position:relative;height:86px;border-radius:13px;overflow:hidden;cursor:pointer;
  border:1px solid rgba(255,255,255,.1);background:rgba(255,255,255,.04);
  display:grid;place-items:center;padding:6px}
.an-t span{position:absolute;left:7px;bottom:5px;font-size:8.5px;color:rgba(233,239,247,.4);z-index:2}
.an-t b{position:absolute;left:7px;top:5px;font-size:8.5px;color:rgba(157,204,255,.8);z-index:2;
  font-family:ui-monospace,Menlo,monospace}
.an-card{width:52px;height:34px;border-radius:9px;background:linear-gradient(150deg,#2a4b6b,#16222d);
  border:1px solid rgba(255,255,255,.22);box-shadow:0 6px 14px rgba(0,0,0,.45);
  display:grid;place-items:center;font-size:8px;color:rgba(255,255,255,.7)}
.an-card.anim{transition:transform .36s cubic-bezier(.2,.9,.3,1.15),opacity .36s}

/* ── 设置表 ── */
.setlist{display:flex;flex-direction:column;gap:1px;border-radius:14px;overflow:hidden;
  border:1px solid rgba(255,255,255,.1);background:rgba(255,255,255,.035)}
.setrow2{display:flex;align-items:flex-start;gap:10px;padding:10px 12px;background:rgba(13,20,29,.35)}
.setrow2:not(:last-child){border-bottom:1px solid rgba(255,255,255,.06)}
.setrow2 .lab{flex:1;min-width:0}
.setrow2 .lab b{font-size:11.5px;font-weight:600;display:block}
.setrow2 .lab code{font-family:ui-monospace,Menlo,monospace;font-size:9px;color:rgba(157,204,255,.8)}
.setrow2 .lab p{font-size:9.5px;color:rgba(233,239,247,.42);line-height:1.6;margin-top:2px}
.setrow2 .ctl{flex:0 0 auto;display:flex;align-items:center;gap:6px;padding-top:2px}
.mini-sw{width:34px;height:19px;border-radius:99px;background:rgba(255,255,255,.14);position:relative;
  transition:background .2s;cursor:pointer}
.mini-sw::after{content:"";position:absolute;left:2px;top:2px;width:15px;height:15px;border-radius:50%;
  background:#fff;transition:transform .22s cubic-bezier(.2,.9,.3,1.15)}
.mini-sw.on{background:#3d7fb8}
.mini-sw.on::after{transform:translateX(15px)}
.mini-val{font-size:10px;color:rgba(233,239,247,.6);font-family:ui-monospace,Menlo,monospace;
  min-width:46px;text-align:right}

/* ── 运行时弹窗层 ── */
.xp-wrap{position:fixed;inset:0;z-index:200;display:flex;pointer-events:none}
.xp-mask{position:absolute;inset:0;background:rgba(4,7,12,.62);opacity:0;transition:opacity .24s;pointer-events:auto}
.xp-wrap.t-anchor .xp-mask{-webkit-backdrop-filter:blur(3px);backdrop-filter:blur(3px);background:rgba(5,9,14,.66)}
.xp-wrap.blur .xp-mask{-webkit-backdrop-filter:blur(9px);backdrop-filter:blur(9px)}
.xp-wrap.noshadow .xp-mask{background:transparent}
.xp-wrap.on .xp-mask{opacity:1}
.xp-pop{position:relative;pointer-events:auto;will-change:transform,opacity}
.xp-wrap.center{align-items:center;justify-content:center}
.xp-wrap.bottom{align-items:flex-end;justify-content:center}
.xp-wrap.top{align-items:flex-start;justify-content:center}
.xp-box{background:#131c26;border:1px solid rgba(255,255,255,.14);border-radius:18px;
  box-shadow:0 26px 60px rgba(0,0,0,.6);color:#e9f0f8;overflow:hidden}
.xp-wrap.light .xp-box{background:#f6f8fb;border-color:rgba(0,0,0,.08);color:#0f1620}
.xp-h{padding:16px 18px 0;font-size:14.5px;font-weight:700;letter-spacing:-.01em}
.xp-c{padding:8px 18px 16px;font-size:12px;line-height:1.75;color:rgba(233,240,248,.6)}
.xp-wrap.light .xp-c{color:rgba(15,22,32,.62)}
.xp-b{display:flex;gap:8px;padding:0 14px 14px}
.xp-btn{flex:1;height:38px;border-radius:11px;font-size:12.5px;font-weight:600;cursor:pointer;
  background:rgba(255,255,255,.08);color:#e9f0f8;border:1px solid rgba(255,255,255,.12);
  font-family:inherit;transition:transform .15s}
.xp-btn:active{transform:scale(.97)}
.xp-btn.pri{background:linear-gradient(180deg,#cfe3ff,#9dccff);color:#06121c;border-color:transparent}
.xp-wrap.light .xp-btn{background:rgba(15,22,32,.06);color:#0f1620;border-color:rgba(0,0,0,.08)}
.xp-wrap.light .xp-btn.pri{background:#2f6fd0;color:#fff}
.xp-listbox{max-height:46vh;overflow:auto;padding:2px 8px 10px;scrollbar-width:thin}
.xp-row{display:flex;align-items:center;gap:10px;padding:11px 10px;border-radius:11px;font-size:12.5px;
  cursor:pointer;transition:background .15s}
.xp-row:active{background:rgba(255,255,255,.08)}
.xp-row.on{background:rgba(157,204,255,.14);color:#cfe3ff;font-weight:600}
.xp-row .tick{margin-left:auto;font-size:11px;color:#9dccff;opacity:0}
.xp-row.on .tick{opacity:1}
.xp-grip{width:34px;height:4px;border-radius:2px;background:rgba(255,255,255,.24);margin:8px auto 4px;
  cursor:grab}
.xp-input{width:calc(100% - 32px);margin:0 16px 12px;height:40px;border-radius:11px;padding:0 12px;
  background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.16);color:inherit;
  font:inherit;font-size:12.5px;outline:none}
.xp-input:focus{border-color:#7fb8f0}
.xp-loading{display:flex;flex-direction:column;align-items:center;gap:12px;padding:26px 34px}
.spin{width:34px;height:34px;border-radius:50%;border:3px solid rgba(255,255,255,.14);
  border-top-color:#9dccff;animation:xspin .8s linear infinite}
@keyframes xspin{to{transform:rotate(360deg)}}
.dash{width:44px;height:44px;border-radius:50%;border:3px dashed rgba(157,204,255,.7);animation:xspin 1.6s linear infinite}
.xp-full{position:absolute;inset:0;background:#0b1219;display:flex;flex-direction:column}
.xp-full .bar{height:52px;display:flex;align-items:center;gap:10px;padding:0 16px;
  border-bottom:1px solid rgba(255,255,255,.1);font-size:13.5px;font-weight:700}
.xp-full .bar .x{margin-left:auto;font-size:16px;color:rgba(233,240,248,.6);cursor:pointer}
.xp-full .body{flex:1;padding:18px;overflow:auto;font-size:12.5px;color:rgba(233,240,248,.66);line-height:1.9}
.xp-drawer{position:absolute;top:0;bottom:0;width:78%;max-width:320px;background:#111a23;
  border-right:1px solid rgba(255,255,255,.12);display:flex;flex-direction:column;
  box-shadow:0 0 60px rgba(0,0,0,.6)}
.xp-drawer.right{right:0;border-right:0;border-left:1px solid rgba(255,255,255,.12)}
.xp-drawer .hd{padding:18px 16px 12px;font-size:15px;font-weight:700}
.xp-attach{position:relative;background:#1b2531;border:1px solid rgba(255,255,255,.16);border-radius:11px;
  padding:6px;box-shadow:0 14px 30px rgba(0,0,0,.55);min-width:118px}
.xp-attach.bubble::after{content:"";position:absolute;width:10px;height:10px;background:#1b2531;
  border-right:1px solid rgba(255,255,255,.16);border-bottom:1px solid rgba(255,255,255,.16);
  transform:rotate(45deg)}
.xp-attach.bubble.down::after{bottom:-6px;left:50%;margin-left:-5px}
.xp-attach.bubble.up::after{top:-6px;left:50%;margin-left:-5px;transform:rotate(225deg)}
.xp-attach.bubble.right::after{right:-6px;top:50%;margin-top:-5px;transform:rotate(-45deg)}
.xp-attach .it{display:flex;align-items:center;gap:8px;padding:8px 10px;border-radius:8px;font-size:12px;
  cursor:pointer;white-space:nowrap}
.xp-attach .it:active{background:rgba(255,255,255,.09)}
.xp-part{position:absolute;left:12px;right:12px;max-width:420px;margin:0 auto;background:#111a23;
  border:1px solid rgba(255,255,255,.13);border-radius:16px;overflow:hidden;
  box-shadow:0 22px 48px rgba(0,0,0,.6)}
.xp-part.up{top:auto;bottom:18px}
.xp-part .cell{padding:13px 16px;font-size:12.5px;border-bottom:1px solid rgba(255,255,255,.06)}
.xp-part .cell:last-child{border-bottom:0}
/* 锚定类弹窗（Attach / Position）用的示例舞台 */
.xp-astage{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:flex-end;
  align-items:center;gap:9px;padding:0 16px 96px}
.xp-ademo{width:100%;max-width:400px;display:flex;align-items:center;gap:10px;padding:11px 12px;
  border-radius:15px;background:rgba(19,28,38,.94);border:1px solid rgba(255,255,255,.13);
  box-shadow:0 20px 44px rgba(0,0,0,.55);pointer-events:auto}
.xp-ademo .av{width:34px;height:34px;border-radius:10px;flex:0 0 auto;
  background:linear-gradient(150deg,#7fb8f0,#2b4f70)}
.xp-ademo .btn{margin-left:auto;height:30px;min-width:52px;padding:0 12px;border-radius:9px;
  display:grid;place-items:center;font-size:11px;font-weight:700;color:#cfe3ff;
  background:rgba(157,204,255,.14);border:1px solid rgba(157,204,255,.26)}
.xp-ademo .btn.on{box-shadow:0 0 0 3px rgba(157,204,255,.16)}
.xp-afloat{pointer-events:auto}
.xp-img{position:relative;width:100%;max-width:330px;aspect-ratio:3/4;border-radius:14px;overflow:hidden;
  background:linear-gradient(160deg,#20415f,#101a24);display:grid;place-items:center;touch-action:none}
.xp-img .art{width:74%;height:74%;border-radius:12px;
  background:radial-gradient(circle at 30% 26%,#7fb8f0,transparent 58%),
             radial-gradient(circle at 72% 72%,#5fdba8,transparent 56%),#16222d;
  transform-origin:center;transition:transform .2s}
.xp-img .pg{position:absolute;bottom:12px;left:50%;transform:translateX(-50%);font-size:10.5px;
  padding:3px 10px;border-radius:99px;background:rgba(0,0,0,.5);color:rgba(255,255,255,.8)}
.xp-toast{position:fixed;left:50%;bottom:96px;transform:translate(-50%,10px);z-index:260;
  padding:9px 16px;border-radius:99px;font-size:11.5px;background:rgba(22,32,43,.96);
  border:1px solid rgba(255,255,255,.16);color:#e9f0f8;opacity:0;pointer-events:none;transition:.24s var(--ease)}
.xp-toast.on{opacity:1;transform:translate(-50%,0)}
.mini-demo{position:relative;border-radius:14px;border:1px solid rgba(255,255,255,.1);overflow:hidden;
  height:190px;background:rgba(255,255,255,.03);margin-top:10px}
.mini-demo .tag{position:absolute;left:9px;top:8px;font-size:9px;color:rgba(233,239,247,.4);z-index:3}
.mini-demo .hint{position:absolute;right:9px;bottom:7px;font-size:9px;color:rgba(233,239,247,.36);z-index:3}
"""

XP_JS = r"""
/* ══════════ XPopup 体验馆运行时（按 XPopup 行为重写，不是上游源码）══════════ */
(function(){
  var S = { shadow:true, blur:false, dark:true, dismissOutside:true, dismissBack:true,
            anim:'ScaleAlphaFromCenter', dur:360, drag:true, three:false, radius:18,
            statusShadow:false, keyboard:true, maxH:.8, light:false };

  var wraps = [], S_SEQ = 0;

  function top(){ return wraps.length ? wraps[wraps.length - 1] : null; }
  function curEl(){ var t = top(); return t ? t.el : null; }

  function toast(msg){
    var t = document.querySelector('.xp-toast');
    if(!t){ t = document.createElement('div'); t.className = 'xp-toast'; document.body.appendChild(t); }
    t.textContent = msg; t.classList.add('on');
    clearTimeout(t._tm); t._tm = setTimeout(function(){ t.classList.remove('on'); }, 1700);
  }

  var ANIM_TABLE = window.__ANIM || [];
  function animIn(el, name){
    var map = {};
    for(var i=0;i<ANIM_TABLE.length;i++) map[ANIM_TABLE[i][0]] = ANIM_TABLE[i];
    var a = map[name || S.anim] || map.ScaleAlphaFromCenter;
    if(name === 'NoAnimation' || S.dur < 40){ el.style.transform = ''; el.style.opacity = 1; return; }
    el.style.transition = 'none';
    el.style.transform = a[3] === 'none' ? '' : a[3];
    el.style.opacity = a[4];
    requestAnimationFrame(function(){
      el.style.transition = 'transform ' + S.dur + 'ms cubic-bezier(.2,.9,.3,1.12), opacity ' +
        Math.round(S.dur*.8) + 'ms ease';
      el.style.transform = '';
      el.style.opacity = 1;
    });
  }

  /* 只关掉最上面那一层——嵌套弹窗时下面那层原样留着 */
  function close(){
    var t = wraps.pop();
    if(!t) return;
    var wrap = t.wrap, cfg = t.cfg, el = t.el, holder = t.holder;
    var out = 'transform ' + Math.round(S.dur*.7) + 'ms cubic-bezier(.4,0,.7,0), opacity ' +
              Math.round(S.dur*.6) + 'ms ease';
    try{
      holder.style.transition = out;
      holder.style.transform = (cfg.pos === 'bottom' || cfg.pos === 'top') ? 'translateY(14vh)' : 'scale(.94) translateY(6px)';
      holder.style.opacity = 0;
    }catch(e){}
    wrap.classList.remove('on');
    setTimeout(function(){
      try{ wrap.remove(); }catch(e){}
      if(cfg.onClose) cfg.onClose();
    }, Math.round(S.dur*.7) + 20);
  }

  function closeAll(){
    while(wraps.length) close();
  }

  function mount(cfg){
    var wrap = document.createElement('div');
    wrap.className = 'xp-wrap ' + (cfg.pos || 'center') + ' t-' + (cfg.type || 'center') +
                     (S.blur ? ' blur' : '') + (S.shadow ? '' : ' noshadow') + (S.dark ? '' : ' light');
    wrap.style.zIndex = 200 + wraps.length * 2;

    var el = document.createElement('div');
    el.className = 'xp-pop';
    el.innerHTML = cfg.html;
    if(cfg.type === 'full' || cfg.type === 'drawer' || cfg.type === 'part' || cfg.type === 'anchor'){
      el.style.position = 'absolute'; el.style.inset = '0'; el.style.pointerEvents = 'none';
    }
    if(cfg.type === 'bottom' || cfg.type === 'top'){
      el.style.width = '100%'; el.style.display = 'flex'; el.style.justifyContent = 'center';
      el.style.alignItems = cfg.pos === 'top' ? 'flex-start' : 'flex-end';
    }

    var holder = el.firstElementChild;
    if(holder && cfg.type !== 'full'){
      if(cfg.type === 'center'){
        holder.style.maxWidth = 'min(360px, calc(100vw - 48px))';
        holder.style.borderRadius = S.radius + 'px';
        if(holder.classList.contains('xp-img')) holder.style.width = 'min(300px, 70vw)';
      }
      if(cfg.type === 'bottom'){
        holder.style.width = '100%';
        holder.style.maxWidth = '560px';
        holder.style.borderRadius = S.radius + 'px ' + S.radius + 'px 0 0';
        holder.style.maxHeight = (S.maxH * 100) + 'vh';
        holder.style.display = 'flex';
        holder.style.flexDirection = 'column';
      }
      if(cfg.type === 'part' || cfg.type === 'drawer'){ holder.style.pointerEvents = 'auto'; }
      if(cfg.type === 'drawer'){ holder.style.height = '100%'; }
      if(cfg.type === 'anchor'){ holder.style.pointerEvents = 'auto'; }
    }

    var mask = document.createElement('div');
    mask.className = 'xp-mask';
    if(cfg.type === 'part' || cfg.type === 'anchor') mask.style.background = 'rgba(4,7,12,.42)';
    mask.addEventListener('click', function(){
      if(S.dismissOutside && cfg.closeOnOutside !== false) close();
    });
    wrap.appendChild(mask);
    wrap.appendChild(el);

    document.body.appendChild(wrap);
    wrap._seq = ++S_SEQ;
    var rec = {wrap:wrap, cfg:cfg, el:el, holder:holder || el, seq:wrap._seq};
    wraps.push(rec);

    requestAnimationFrame(function(){ wrap.classList.add('on'); });
    animIn(holder || el, cfg.anim);

    /* 拖拽关闭：底部弹窗 / 抽屉 */
    if(S.drag && (cfg.type === 'bottom' || cfg.type === 'drawer')){
      var grip = el.querySelector('.xp-grip') || holder;
      var sy = 0, dy = 0, drag = false, t0 = 0, axis = cfg.type === 'drawer' ? 'x' : 'y';
      var onDown = function(e){
        drag = true; sy = axis === 'x' ? e.clientX : e.clientY; t0 = performance.now(); dy = 0;
        holder.style.transition = 'none';
        try{ grip.setPointerCapture && grip.setPointerCapture(e.pointerId); }catch(err){}
      };
      var onMove = function(e){
        if(!drag) return;
        dy = Math.max(0, (axis === 'x' ? e.clientX : e.clientY) - sy);
        holder.style.transform = axis === 'x' ? 'translateX(' + dy + 'px)' : 'translateY(' + dy + 'px)';
      };
      var onUp = function(){
        if(!drag) return;
        drag = false;
        holder.style.transition = '';
        var h = axis === 'x' ? holder.offsetWidth : holder.offsetHeight;
        var v = dy / Math.max(1, performance.now() - t0);
        var limit = S.three ? h * .55 : h * .3;
        if(dy > limit || v > .62){ close(); if(dy > 0) holder.style.transform = ''; }
        else holder.style.transform = '';
        dy = 0;
      };
      grip.addEventListener('pointerdown', onDown);
      wrap.addEventListener('pointermove', onMove);
      wrap.addEventListener('pointerup', onUp);
      wrap.addEventListener('pointercancel', onUp);
    }

    el.querySelectorAll('[data-xp-close]').forEach(function(b){
      b.addEventListener('click', function(){ close(); });
    });
    el.querySelectorAll('.xp-row').forEach(function(r){
      r.addEventListener('click', function(){
        if(r.dataset.keep){ r.classList.toggle('on'); return; }
        el.querySelectorAll('.xp-row').forEach(function(x){ x.classList.remove('on'); });
        r.classList.add('on');
        var cb = cfg.onSelect;
        if(cb) cb(r.dataset.v || r.textContent.trim());
        if(cfg.type === 'center' && !r.dataset.multi) setTimeout(close, 140);
      });
    });
    var inp = el.querySelector('.xp-input');
    if(inp && S.keyboard !== false && el.dataset.focus !== '0'){
      setTimeout(function(){ try{ inp.focus({preventScroll:true}); }catch(e){} }, 300);
    }
    el.querySelectorAll('[data-xp-ok]').forEach(function(b){
      b.addEventListener('click', function(){
        var t = el.querySelector('.xp-input');
        toast('回传：' + (t && t.value ? t.value : '（空）'));
        close();
      });
    });
    return rec;
  }

  function open(cfg){
    var rec = mount(cfg);
    if(cfg.onMount) cfg.onMount(rec.el);
    return rec;
  }

  /* ── 各类弹窗的模板 ── */
  var L = ['条目 1','条目 2','条目 3','条目 4','条目 5','条目 6','条目 7','条目 8','条目 9','条目 10','条目 11','条目 12'];
  function rows(arr, checked){
    return arr.map(function(t, i){
      return '<div class="xp-row' + (i === checked ? ' on' : '') + '" data-v="' + t + '">' + t +
             '<span class="tick">✓</span></div>';
    }).join('');
  }

  var BUILD = {
    confirm: function(){
      return {type:'center', pos:'center', html:
        '<div class="xp-box"><div class="xp-h">删除这条素材？</div>' +
        '<div class="xp-c">删除后无法恢复；已导出的代码不受影响。这个弹窗默认从中心缩放淡入（ScaleAlphaFromCenter）。</div>' +
        '<div class="xp-b"><button class="xp-btn" data-xp-close>取消</button>' +
        '<button class="xp-btn pri" data-xp-ok>确定</button></div></div>'};
    },
    input: function(){
      return {type:'center', pos:'center', html:
        '<div class="xp-box"><div class="xp-h">给素材起个名字</div>' +
        '<div class="xp-c" style="padding-bottom:6px">最多 20 个字，点确定回传文本。</div>' +
        '<input class="xp-input" placeholder="例如：液态玻璃底栏" maxlength="20" value="">' +
        '<div class="xp-b"><button class="xp-btn" data-xp-close>取消</button>' +
        '<button class="xp-btn pri" data-xp-ok>确定</button></div></div>'};
    },
    loading: function(){
      return {type:'center', pos:'center', closeOnOutside:false, html:
        '<div class="xp-box"><div class="xp-loading"><div class="dash"></div>' +
        '<div style="font-size:12px;color:rgba(233,240,248,.66)">正在生成 46 条素材…</div></div>' +
        '<div class="xp-b"><button class="xp-btn" data-xp-close>收起到后台</button></div></div>',
        onClose: function(){ toast('loading 已关闭（delayDismiss 也会走到这里）'); }};
    },
    centerList: function(){
      return {type:'center', pos:'center', html:
        '<div class="xp-box" style="min-width:250px"><div class="xp-h">请选择一项</div>' +
        '<div class="xp-listbox">' + rows(L, -1) + '</div></div>'};
    },
    centerCheck: function(){
      return {type:'center', pos:'center', html:
        '<div class="xp-box" style="min-width:250px"><div class="xp-h">请选择一项</div>' +
        '<div class="xp-listbox">' + rows(L.slice(0,5), 2) + '</div></div>'};
    },
    bottomList: function(){
      return {type:'bottom', pos:'bottom', html:
        '<div class="xp-box"><div class="xp-grip"></div>' +
        '<div class="xp-h" style="padding-top:2px">请选择一项</div>' +
        '<div class="xp-listbox" style="max-height:38vh">' + rows(L, -1) + '</div>' +
        '<div class="xp-b"><button class="xp-btn" data-xp-close>取消</button></div></div>'};
    },
    bottomCheck: function(){
      return {type:'bottom', pos:'bottom', html:
        '<div class="xp-box"><div class="xp-grip"></div>' +
        '<div class="xp-h" style="padding-top:2px">排序方式</div>' +
        '<div class="xp-listbox" style="max-height:34vh"><div class="xp-row on" data-keep>最近更新<span class="tick">✓</span></div>' +
        '<div class="xp-row" data-keep>名称 A→Z<span class="tick">✓</span></div>' +
        '<div class="xp-row" data-keep>难度<span class="tick">✓</span></div>' +
        '<div class="xp-row" data-keep>手动排序<span class="tick">✓</span></div></div>' +
        '<div class="xp-b"><button class="xp-btn" data-xp-close>重置</button>' +
        '<button class="xp-btn pri" data-xp-ok>确定</button></div></div>'};
    },
    drawerL: function(){
      return {type:'drawer', pos:'bottom', html:
        '<div class="xp-drawer"><div class="hd">XPopup</div><div class="xp-listbox">' +
        rows(['快速开始','局部阴影','图片浏览','尝试动画','自定义弹窗','关于'], 0) + '</div></div>'};
    },
    drawerR: function(){
      return {type:'drawer', pos:'bottom', html:
        '<div class="xp-drawer right"><div class="hd">全部素材</div><div class="xp-listbox">' +
        rows(['基础组件 6','表单输入 6','导航 6','布局 6','反馈 7','数据展示 6','动效 5','应用模板 4'], 2) +
        '</div><div style="padding:12px 14px;border-top:1px solid rgba(255,255,255,.1)">' +
        '<button class="xp-btn" data-xp-close>关闭抽屉</button></div></div>'};
    },
    partTop: function(){
      return {type:'part', pos:'top', html:
        '<div style="position:absolute;inset:0;pointer-events:none">' +
        '<div class="xp-mask" style="background:rgba(4,7,12,.35);opacity:1;pointer-events:auto"></div>' +
        '<div class="xp-part" style="top:82px">' +
        '<div class="cell">综合排序</div><div class="cell">按价格</div><div class="cell">按销量</div>' +
        '</div></div>'};
    },
    partBottom: function(){
      return {type:'part', pos:'bottom', html:
        '<div style="position:absolute;inset:0;pointer-events:none">' +
        '<div class="xp-mask" style="background:rgba(4,7,12,.35);opacity:1;pointer-events:auto" data-xp-close></div>' +
        '<div class="xp-part up">' +
        '<div class="cell">只看有演示</div><div class="cell">只看可复制提示词</div><div class="cell">只看离线可用</div>' +
        '</div></div>'};
    },
    imageViewer: function(){
      return {type:'center', pos:'center', anim:'ScaleAlphaFromCenter', html:
        '<div class="xp-img"><div class="art"></div>' +
        '<div class="pg"><b data-pg>1 / 5</b> · 双击放大 · 左右滑动</div>' +
        '<div class="hit" style="position:absolute;inset:0"></div></div>',
        onMount: function(el){
          var art = el.querySelector('.art'), pgEl = el.querySelector('[data-pg]');
          var imgs = ['radial-gradient(circle at 30% 26%,#7fb8f0,transparent 58%),radial-gradient(circle at 72% 72%,#5fdba8,transparent 56%),#16222d',
                      'radial-gradient(circle at 68% 30%,#ffd39d,transparent 56%),radial-gradient(circle at 26% 74%,#ff8fa3,transparent 58%),#241a18',
                      'radial-gradient(circle at 40% 30%,#b9a6ff,transparent 58%),radial-gradient(circle at 74% 76%,#5ac8ff,transparent 56%),#1a1c2b',
                      'radial-gradient(circle at 34% 70%,#5fdba8,transparent 58%),radial-gradient(circle at 70% 24%,#8bd7ff,transparent 56%),#10231f',
                      'radial-gradient(circle at 50% 34%,#ffffff,transparent 46%),radial-gradient(circle at 50% 78%,#7fb8f0,transparent 60%),#141b26'];
          var i = 0, zoom = 1;
          function paint(){ art.style.background = imgs[i] + ', #16222d'; pgEl.textContent = (i+1) + ' / 5'; }
          paint();
          var last = 0;
          el.addEventListener('click', function(e){
            var now = performance.now();
            if(now - last < 320){
              zoom = zoom > 1 ? 1 : 2.2;
              art.style.transform = 'scale(' + zoom + ')';
              toast(zoom > 1 ? '双击放大 2.2×' : '已还原');
              last = 0; return;
            }
            last = now;
          });
          var sx = 0, sy = 0;
          el.addEventListener('pointerdown', function(e){ sx = e.clientX; sy = e.clientY; });
          el.addEventListener('pointerup', function(e){
            var dx = e.clientX - sx, dy = e.clientY - sy;
            if(Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy)){
              i = (i + (dx < 0 ? 1 : 4)) % 5; art.style.transform = ''; zoom = 1; paint();
            } else if(dy > 70 && Math.abs(dy) > Math.abs(dx)){
              close();
            }
          });
        }};
    },
    fullScreen: function(){
      return {type:'full', pos:'center', html:
        '<div class="xp-full"><div class="bar"><span data-xp-close style="cursor:pointer">✕</span>全屏弹窗' +
        '<span class="x" data-xp-close>关闭</span></div>' +
        '<div class="body"><b style="color:#e9f0f8">看起来就是一个 Activity</b><br>' +
        '标题栏 + 返回 + 可滚动内容；可以搭配 20 种动画里的任意一种进入，常见的是 TranslateFromBottom。<br><br>' +
        '适合：登录、分步选择、全屏表单、详情页这类「页面级」内容，避免为一个页面再写一个 Activity。<br><br>' +
        Array.from({length:6}).map(function(_, i){
          return '<div style="height:52px;margin:10px 0;border-radius:12px;border:1px solid rgba(255,255,255,.1);' +
                 'background:rgba(255,255,255,.04)"></div>';
        }).join('') +
        '</div></div>'};
    },
    attach: function(){
      return {type:'anchor', pos:'bottom', anim:'ScaleAlphaFromCenter', html:
        '<div class="xp-astage">' +
          '<div class="xp-afloat">' +
            '<div class="xp-attach bubble down" style="min-width:150px">' +
              '<div class="it">↗ 分享到…</div><div class="it">✎ 编辑</div>' +
              '<div class="it">⧉ 复制提示词</div><div class="it">☆ 收藏</div>' +
            '</div>' +
          '</div>' +
          '<div class="xp-ademo"><div class="av"></div>' +
            '<div><div style="font-size:12px;font-weight:700">液态玻璃底栏</div>' +
            '<div style="font-size:10px;color:rgba(233,240,248,.45);margin-top:2px">锚点：这一行右侧的按钮</div></div>' +
            '<div class="btn on">···</div>' +
          '</div>' +
        '</div>'};
    },
    bubble: function(){
      return {type:'anchor', pos:'bottom', anim:'ScaleAlphaFromCenter', html:
        '<div class="xp-astage">' +
          '<div class="xp-afloat" style="align-self:flex-end;margin-right:26px">' +
            '<div class="xp-attach bubble down" style="background:#1d3b2c;border-color:rgba(95,219,168,.36)">' +
              '<div class="it" style="color:#bff0d5">已复制提示词 ✓</div></div>' +
          '</div>' +
          '<div class="xp-ademo"><div class="av" style="background:linear-gradient(150deg,#5fdba8,#1d6b52)"></div>' +
            '<div><div style="font-size:12px;font-weight:700">复制成功的气泡</div>' +
            '<div style="font-size:10px;color:rgba(233,240,248,.45);margin-top:2px">箭头指向触发它的按钮</div></div>' +
            '<div class="btn on" style="background:rgba(95,219,168,.18);border-color:rgba(95,219,168,.34);color:#bff0d5">复制</div>' +
          '</div>' +
        '</div>'};
    },
    position: function(){
      return {type:'anchor', pos:'bottom', anim:'TranslateFromLeft', html:
        '<div class="xp-astage">' +
          '<div class="xp-afloat" style="align-self:flex-start;margin-left:26px">' +
            '<div class="xp-attach" style="padding:10px 14px;border-radius:12px">' +
              '<div style="font-size:12px;font-weight:700">新消息 · 林小满</div>' +
              '<div style="font-size:10.5px;color:rgba(233,240,248,.6);margin-top:3px">把引用方案搬进素材库了</div>' +
            '</div></div>' +
          '<div class="xp-ademo"><div class="av" style="background:linear-gradient(150deg,#cfe3ff,#3d6f9e)"></div>' +
            '<div><div style="font-size:12px;font-weight:700">atPoint(x, y)</div>' +
            '<div style="font-size:10px;color:rgba(233,240,248,.45);margin-top:2px">给一个坐标，弹在任意位置</div></div>' +
            '<div class="btn">定位</div>' +
          '</div>' +
        '</div>'};
    },
    zhihu: function(){
      return {type:'bottom', pos:'bottom', html:
        '<div class="xp-box" style="height:62vh"><div class="xp-grip"></div>' +
        '<div class="xp-h" style="padding-top:2px">32 条评论</div>' +
        '<div class="xp-listbox" style="flex:1;max-height:none">' +
        Array.from({length:9}).map(function(_, i){
          return '<div style="display:flex;gap:9px;padding:9px 8px">' +
            '<div style="width:26px;height:26px;border-radius:50%;flex:0 0 auto;background:linear-gradient(150deg,#3d6f9e,#1d3346)"></div>' +
            '<div><div style="font-size:11.5px;font-weight:600">用户 ' + (i+1) + '</div>' +
            '<div style="font-size:11px;color:rgba(233,240,248,.55);line-height:1.6;margin-top:2px">' +
            '这条评论用来演示「列表先滚到底，再继续下拉才开始拖弹窗」的嵌套滚动。</div></div></div>';
        }).join('') + '</div>' +
        '<div style="padding:8px 12px;border-top:1px solid rgba(255,255,255,.1);display:flex;gap:8px">' +
        '<input class="xp-input" style="margin:0;flex:1;height:34px" placeholder="写评论…">' +
        '<button class="xp-btn pri" style="flex:0 0 auto;width:64px;height:34px" data-xp-ok>发送</button></div></div>'};
    },
    drawerList: function(){
      return {type:'drawer', pos:'bottom', html:
        '<div class="xp-drawer"><div class="hd">素材库</div>' +
        '<div style="padding:0 8px;font-size:9.5px;color:rgba(233,240,247,.36);letter-spacing:.1em">分类</div>' +
        '<div class="xp-listbox">' + rows(['基础组件','表单输入','导航','布局','反馈','数据展示','动效','应用模板'], 3) +
        '</div></div>'};
    },
    multi: function(){
      return {type:'center', pos:'center', html:
        '<div class="xp-box"><div class="xp-h">第一层弹窗</div>' +
        '<div class="xp-c">点下面这个按钮会在它上面再弹一个，父弹窗不会被销毁。</div>' +
        '<div class="xp-b"><button class="xp-btn" data-xp-close>关闭</button>' +
        '<button class="xp-btn pri" id="xpSecond">再弹一层</button></div></div>',
        onMount: function(el){
          var b = el.querySelector('#xpSecond');
          if(b) b.addEventListener('click', function(){
            open({type:'center', pos:'center', html:
              '<div class="xp-box"><div class="xp-h">第二层弹窗</div>' +
              '<div class="xp-c">关掉我，第一层还在原处等你。</div>' +
              '<div class="xp-b"><button class="xp-btn pri" data-xp-close>好的</button></div></div>'});
          });
        }};
    },
    bindLayout: function(){
      return {type:'bottom', pos:'bottom', html:
        '<div class="xp-box"><div class="xp-grip"></div>' +
        '<div style="padding:14px 16px 4px;font-size:13px;font-weight:700">复用已有布局</div>' +
        '<div class="xp-c">这段内容可以是任意 HTML（相当于你项目里的 my_confirm_popup.xml）。' +
        '只要按约定给控件 id，XPopup 就能接管动画、手势、阴影、键盘。</div>' +
        '<div style="display:flex;gap:8px;padding:6px 16px 8px">' +
        '<div style="flex:1;height:44px;border-radius:10px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1)"></div>' +
        '<div style="flex:1;height:44px;border-radius:10px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1)"></div>' +
        '<div style="flex:1;height:44px;border-radius:10px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1)"></div></div>' +
        '<div class="xp-b"><button class="xp-btn" data-xp-close>取消</button>' +
        '<button class="xp-btn pri" data-xp-ok>确定</button></div></div>'};
    }
  };

  window.__XP = {
    open: function(id){
      var cfg = BUILD[id] ? BUILD[id]() : null;
      if(!cfg) return;
      open(cfg);
    },
    close: close,
    closeAll: closeAll,
    depth: function(){ return wraps.length; },
    set: function(k, v){ S[k] = v; },
    get: function(){ return S; },
    toast: toast
  };

  document.addEventListener('keydown', function(e){
    if(e.key === 'Escape' && wraps.length && S.dismissBack) close();
  });
})();
"""
