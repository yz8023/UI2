# UI2 · UI 素材库

把一个 App 从组件到页面需要的 UI 素材，做成**能点、能调、能复制提示词**的东西。两种形态：单文件离线 HTML，和可安装的 Android APK。

- **68 条素材**：46 条完整素材（组件 6 · 表单 6 · 导航 6 · 布局 6 · 反馈 7 · 数据 6 · 动效 5 · 模板 4）+ 22 个交互拆解
- **XPopup 全量**：20 种弹窗（7 大族）· 20 种 `PopupAnimation` · 45 个 Builder 设置 · 5 组手势
- **motion-web 全量**：7 个 case（全屏剧场）· 20 条配方（每条都在跑）· 4 组令牌实验室 · 25 篇规范索引
- **结构生成器**：3 个平台 × 11 个功能开关 → 目录树 + 文件↔素材映射 + 开工提示词
- 全部**单文件、内联 CSS/JS、零 CDN、零外部图片字体**，断网可跑

> 参考并重写自：[junixapp/XPopup](https://github.com/junixapp/XPopup)（Apache-2.0）、[feitangyuan/motion-web](https://github.com/feitangyuan/motion-web)（CC BY-NC 4.0）、[yz8023/ui](https://github.com/yz8023/ui)（MIT）、[iyinchao/liquid-glass-studio](https://github.com/iyinchao/liquid-glass-studio)（MIT）。
> 只重写行为与机制说明，不含上游源码或素材。

---

## 在线看 / 两个入口

- 门户页：<https://yz8023.github.io/UI2/>
- 素材库 App：<https://yz8023.github.io/UI2/app/index.html>
- 安装包：[Releases · v3.1](https://github.com/yz8023/UI2/releases/latest)（APK + 两个单文件 HTML 也一起附上）

| 文件 | 是什么 |
| --- | --- |
| [`index.html`](index.html) | 门户页：两套形态对照 + 各套目录 |
| [`app/index.html`](app/index.html) | **素材库 App**（单文件，505 KB）：悬浮 Dock 导航，5 个入口 |

App 的 5 个入口：

1. **首页** — 大标语 + 搜索直通 + 功能磁贴 + 横滑精选 + 按来源进入
2. **素材** — 8 个分类页（每类一条明细）+ 全局功能搜索（同义词、按相关度排）
3. **体验** — XPopup 弹层馆 + motion-web 动效馆（详见下）
4. **结构** — 平台 × 功能 → 目录树 / 素材映射 / 提示词（勾选不跳顶）
5. **更多** — 并排对比（68 条任选，两个演示同步起跑）+ 设置（7 套主题 / 玻璃 / 减少动效 / 导出 JSON）

### 体验馆有什么

**XPopup · 弹层**
- 弹窗 20：确认 / 输入 / 加载 / 中间列表 / 中间勾选 / 底部列表 / 底部勾选 / 左右抽屉 / 局部阴影上下 / 图片浏览 / 全屏 / 依附 / 气泡 / 定位 / 知乎式嵌套滚动 / 抽屉列表 / 多层 / 复用布局 —— 全部真弹、可拖、可关
- 动画 20：全部 `PopupAnimation` 枚举，点一张小舞台就播一次，也能「全部播一遍」
- 设置 45：按 8 组列出，其中 7 个开关（点外部关闭 / 返回键 / 背景阴影 / 模糊 / 深色 / 拖拽 / 三阶拖拽）直连运行时，改完立刻作用到下一次弹窗
- 手势 5：拖拽关闭 / 三阶拖拽 / 嵌套滚动 / 点外部与点穿 / 背景模糊

**motion-web · 动效**
- 案例 7：每个都进**全屏剧场**（380 高画布 + 机制 / 参数 / 判据 + 复制提示词 + 完整演示页 + 7 个之间直接切）
- 配方 20：每条一个实时挂载的舞台，配「用来做什么」和一条可复制的生成提示词
- 令牌：时长 7 档 / 曲线 9 条 / 弹簧 6 组 / 错峰 5 种，点一下重播
- 规范 25：标题 + 中文导读 + 原文摘录 + 可折叠章节

## 安装包

[`apk/uikit-library-3.1.apk`](apk/uikit-library-3.1.apk) · 1.0 MB

- `com.arena.uikit` · versionCode 5 / versionName 3.1 · minSdk 24 · targetSdk 34
- **零权限**（没有 `INTERNET`），一个 Activity + WebView 壳，全部页面在 `assets/www/`
- 证书 SHA-256 `711ad44d4598fbe8ec8c1ddea35a0af02ea988ba6161353f9ec16976d055eba8`（自签名 debug keystore，非商店包）
- 手势返回键先关详情再退出；`AndroidBridge.copy/.toast/.share/.open` 桥接系统剪贴板、Toast 与分享

下载直链：[`uikit-library-3.1.apk`](https://github.com/yz8023/UI2/releases/download/v3.1/uikit-library-3.1.apk)

## 源码结构

```
.
├── index.html              门户页（生成物）
├── _portal.py              门户页生成器
├── app/                    素材库 App
│   ├── index.html          单文件 App（生成物）
│   ├── _build.py           构建：注入 payload / CSS / JS
│   ├── _shell.py           外壳（v3 Dock 样式 + HTML）
│   ├── _app_js.py          路由 / 视图 / 详情页 / 对比
│   ├── _library.py         46 条素材数据 + 作用域 CSS
│   ├── _app_data.py        素材聚合（lib + motion + glass + video）
│   ├── _minis.py           18 个迷你演示（canvas / DOM）
│   ├── _xp.py              XPopup 运行时 + 20 弹窗 + 20 动画 + 45 设置
│   ├── _mw.py              20 条配方演示 + 4 组令牌
│   ├── _spec.py            25 篇规范索引 + 中文导读
│   ├── _exp_js.py          体验馆 / 案例剧场 / 结构页 / 全局搜索
│   ├── _exp_css.py         对应样式
│   └── _proj.py            3 个平台 + 11 个功能 + 提示词模板
├── library/                完整素材库 HTML（46 条 + 总览）
├── motion-demos/           motion-web 7 页
├── glass-demos/            液态玻璃 6 页
├── video-demos/            视频拆解 9 页
├── android-src/            APK 壳（MainActivity + manifest + build.sh + add_assets.py）
└── .github/workflows/      CI：重建 HTML → 打包 APK
```

## 本地构建

```bash
# 1) 生成全部单文件 HTML
python3 app/_build.py && python3 _portal.py
(cd library && python3 gen_library.py) && (cd motion-demos && python3 _make.py)
(cd glass-demos && python3 _glass_make.py) && (cd video-demos && python3 _make_pages.py)

# 2) 打 APK（需要 JDK 17 + Android build-tools 34 + platform 34）
ANDROID_SDK_ROOT=/path/to/sdk bash android-src/build.sh
```

沙箱里从零装 SDK 的完整步骤见 [`android-src/README.md`](android-src/README.md)。
CI 也会在每次 push 时重建 HTML 并上传 APK artifact。

## 许可

本项目代码 MIT。文档里引用的第三方项目按各自许可：XPopup `Apache-2.0`，motion-web `CC BY-NC 4.0`，yz8023/ui 与 liquid-glass-studio `MIT`。
