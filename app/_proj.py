# -*- coding: utf-8 -*-
"""项目结构设计器：选平台 + 选功能 → 目录树 + 素材映射 + 可复制的开工提示词。"""

PLATFORMS = [
    dict(id='static', name='纯静态页', sub='一个 index.html 就能跑',
         desc='适合素材页、落地页、单页演示。没有构建、没有依赖，双击即开，也能直接塞进 WebView。',
         tree=[
             ('index.html', '入口：总览 + 详情面板 + 一键复制提示词', 'F01'),
             ('assets/tokens.css', '设计令牌：色板 / 圆角 / 间距 / 动效曲线', 'F01'),
             ('assets/demo.css', '演示舞台：.dz 画布 + 卡片 + 玻璃层', 'F19'),
             ('demos/button.html', '单条素材的独立演示页（演示 + 文档 + 提示词）', 'F01'),
             ('demos/dialog.html', '同上，一条一个文件，方便整段复制', 'F26'),
             ('docs/实现方案.md', '效果 / 机制 / 步骤 / 判据 / 红线 / 失败指纹', '—'),
             ('docs/参考来源.md', '借鉴了谁、许可证、边界', '—'),
             ('docs/环境要求.md', '浏览器基线、文件清单、接入说明', '—'),
             ('CREDITS.md', '全库致谢与许可证', '—'),
         ]),
    dict(id='webapp', name='Web App', sub='Vite + TypeScript',
         desc='真正要做产品时用这套：令牌层 → 组件层 → 页面层，动效走统一 motion.ts，弹层走 lib/popup。',
         tree=[
             ('index.html', 'Vite 入口', '—'),
             ('src/main.ts', '挂载根组件 + 注册路由', '—'),
             ('src/design/tokens.css', '颜色 / 圆角 / 阴影 / 间距刻度', 'F01'),
             ('src/design/motion.ts', 'duration 7 档 + easing 9 条 + spring 6 组', 'F38'),
             ('src/design/theme.ts', '深/浅色、7 套主题、持久化', 'F45'),
             ('src/components/ui/Button.tsx', '三档层级 + 加载态 + 图标位', 'F01'),
             ('src/components/ui/Field.tsx', '浮动标签 + 清除键 + 错误三重表达', 'F02'),
             ('src/components/ui/Switch.tsx', '按下拉长 + 回弹', 'F03'),
             ('src/components/feedback/Toast.tsx', '堆叠 / 上限 3 条 / 独立计时', 'F25'),
             ('src/components/feedback/Dialog.tsx', '焦点圈定 + Esc + 危险态禁点遮罩', 'F26'),
             ('src/components/feedback/Sheet.tsx', '拖拽关闭 + 遮罩联动', 'F27'),
             ('src/components/nav/TabBar.tsx', '胶囊指示器 + 安全区', 'F13'),
             ('src/components/nav/TopBar.tsx', '大标题折叠，一个进度驱动三件事', 'F14'),
             ('src/components/layout/Grid.tsx', 'Bento / 瀑布流 / 响应式栅格', 'F19'),
             ('src/components/data/LineChart.tsx', 'Catmull-Rom + 描边生长 + 吸附', 'F32'),
             ('src/lib/popup/popup.ts', '弹层内核：挂载 / 层级栈 / 遮罩 / 关闭策略', 'F26'),
             ('src/lib/popup/animators.ts', '20 种进出场动画（对应 PopupAnimation）', 'F38'),
             ('src/lib/popup/drag.ts', '拖拽关闭 / 三阶拖拽 / 嵌套滚动', 'F40'),
             ('src/lib/spring.ts', '按 dt 积分的弹簧，注入初始速度', 'F38'),
             ('src/pages/Onboarding/', '引导页：三屏 + 进度胶囊', 'F43'),
             ('src/pages/Login/', '登录页：校验 + 抖动 + 锁定宽度', 'F44'),
             ('src/pages/Settings/', '设置页：分组 + 整行可点开关', 'F45'),
             ('src/pages/Profile/', '个人主页：头图视差 + 统计滚动', 'F46'),
             ('public/manifest.webmanifest', '可安装 PWA（可选）', '—'),
             ('docs/项目说明.md', '目录约定 + 命名规范 + 验收清单', '—'),
         ]),
    dict(id='android', name='Android App', sub='原生 + WebView + XPopup',
         desc='要出 APK 时用这套：XPopup 直接依赖（弹层全家桶），素材库 HTML 打进 assets 离线看，',
         tree=[
             ('app/build.gradle', "implementation 'com.github.li-xiaojun:XPopup:2.x'", '—'),
             ('app/src/main/AndroidManifest.xml', 'minSdk 21+，零权限（除悬浮窗场景）', '—'),
             ('app/src/main/java/…/MainActivity.java', '入口 + 底部导航', 'F13'),
             ('app/src/main/java/…/ui/popup/AppPopup.java', 'XPopup.Builder 的统一封装（主题 / 圆角 / 模糊）', 'F26'),
             ('app/src/main/java/…/ui/popup/ConfirmPopup.java', 'asConfirm 封装：危险操作默认禁点遮罩', 'F26'),
             ('app/src/main/java/…/ui/popup/BottomSheet.java', 'asBottomList + 三阶拖拽 + 嵌套滚动', 'F27'),
             ('app/src/main/java/…/ui/popup/ImageViewer.java', 'asImageViewer 封装 + 长图不 OOM', 'F32'),
             ('app/src/main/java/…/ui/component/Button.kt', 'Compose 版按钮（与 HTML 版同参数）', 'F01'),
             ('app/src/main/java/…/ui/page/OnboardingActivity.kt', '引导页', 'F43'),
             ('app/src/main/java/…/ui/page/SettingsActivity.kt', '设置页', 'F45'),
             ('app/src/main/res/layout/', 'bindLayout 复用的布局（含约定 id）', '—'),
             ('app/src/main/res/values/themes.xml', '深色主题 + 状态栏 / 导航栏', '—'),
             ('assets/www/library/', '离线素材库（46 条 HTML）', '—'),
             ('assets/www/app/index.html', 'WebView 里的素材库 App', '—'),
             ('docs/构建.md', 'aapt2 → javac → d8 → zipalign → apksigner', '—'),
         ]),
]

# 功能 → 需要的素材 / XPopup 组件 / 动效配方
FEATURES = [
    dict(id='onboard', name='首次引导', icon='①', desc='新用户三步说明，可重看',
         mats=['F43'], xp=[], rec=[1, 10]),
    dict(id='auth', name='登录 / 注册', icon='②', desc='校验、错误抖动、提交锁宽',
         mats=['F44', 'F07', 'F02'], xp=[], rec=[11]),
    dict(id='nav', name='导航骨架', icon='③', desc='底栏 + 顶部大标题 + 抽屉',
         mats=['F13', 'F14', 'F15', 'F18'], xp=['drawerL', 'drawerR'], rec=[13]),
    dict(id='popup', name='弹层与确认', icon='④', desc='确认、输入、列表、局部阴影',
         mats=['F26', 'F27', 'F25'], xp=['confirm', 'input', 'centerList', 'partTop'], rec=[8]),
    dict(id='form', name='表单与输入', icon='⑤', desc='输入框、校验、步进、分段、选择器',
         mats=['F02', 'F07', 'F08', 'F09', 'F12'], xp=['input'], rec=[]),
    dict(id='list', name='列表与网格', icon='⑥', desc='分组列表、Bento、瀑布流',
         mats=['F20', 'F19', 'F21', 'F22'], xp=['bottomList', 'centerCheck'], rec=[5]),
    dict(id='feedback', name='加载与反馈', icon='⑦', desc='骨架屏、进度、空态、加载按钮',
         mats=['F28', 'F29', 'F30', 'F31'], xp=['loading'], rec=[10]),
    dict(id='chart', name='数据展示', icon='⑧', desc='折线、柱状、环形、表格、时间线',
         mats=['F32', 'F33', 'F34', 'F36', 'F37'], xp=[], rec=[20]),
    dict(id='media', name='图片与媒体', icon='⑨', desc='上传、大图浏览、超长图',
         mats=['F11'], xp=['imageViewer', 'fullScreen'], rec=[3, 17]),
    dict(id='motion', name='动效与手势', icon='⑩', desc='弹簧拖拽、错峰、手势卡片、转场、视差',
         mats=['F38', 'F39', 'F40', 'F41', 'F42'], xp=[], rec=[1, 2, 6, 9, 15]),
    dict(id='settings', name='设置与关于', icon='⑪', desc='分组设置、危险操作二次确认、致谢页',
         mats=['F45', 'F46'], xp=['confirm'], rec=[]),
]

PROMPT = """【项目结构】{platform}
{desc}

【目录】
{tree}

【本次要做的界面】
{feats}

【素材从哪来】
· 组件与页面：素材库对应条目（每条都有实现方案 / 参考来源 / 环境要求 / 提示词）
{matlist}
· 弹层：XPopup（Apache-2.0）—— {xplist}
· 动效节奏：motion-web 的 duration / easing / spring / stagger 令牌

【产出约束】
1. 令牌先行：颜色、圆角、间距、动效曲线只在 tokens / motion 一处定义。
2. 组件按目录分：ui（原子）、feedback（反馈）、nav（导航）、layout（布局）、data（数据）。
3. 弹层统一走一个 popup 内核，不要每个弹窗各写一套遮罩和关闭逻辑。
4. 动效只用令牌里的时长与曲线，不出现随手写的 0.3s。
5. 全部离线可跑：不引 CDN、字体、图片；图形用 SVG / CSS 程序化生成。
6. 每个界面写清：状态矩阵（默认 / hover / active / 禁用 / 加载 / 错误 / 空）。
7. 验收：窄屏 360、宽屏 1440 都不溢出；prefers-reduced-motion 有降级。
"""
