# UI 素材库 · Android 壳

单 Activity + WebView，把 `/home/user` 下的离线页面打进 APK 的 `assets/www/`。

## 目录
- `AndroidManifest.xml` — package `com.arena.uikit`，minSdk 24 / targetSdk 34，只有 LAUNCHER，无任何权限
- `java/com/arena/uikit/MainActivity.java` — WebView 壳：全屏深色、返回键回退、站内链接留在同窗口、
  注入 `AndroidBridge`（copy / toast / open）、`target=_blank` 自动收回、外链交给系统浏览器
- `res/` — 自适应图标（矢量前景 + 5 档 PNG 兜底）、深色主题
- `add_assets.py` — 用 Python 写 zip（关键：给中文文件名置 UTF-8 标志位，aapt2 -A 会写成乱码）
- `build.sh` — 手工构建：aapt2 → javac → d8 → zip(python) → zipalign → apksigner
- `debug.keystore` — 自签名用（storepass/keypass 均为 android）

## 重新打包
```bash
export JAVA_HOME=/var/tmp/jdk17/jdk-17.0.21+9     # 必须 JDK 17（JDK 11 的 PKCS12 缺 HmacPBESHA256，apksigner 签名会失败）
export ANDROID_SDK_ROOT=/tmp/asdk                 # android-14/ = build-tools 34；platforms/android-34/android.jar
bash android-src/build.sh                         # 产物：apk/uikit-library-3.0.apk
```

### SDK 从零装（沙箱里 /opt 不可写，全部放在 /tmp）
```bash
mkdir -p /tmp/asdk && cd /tmp/asdk
curl -sSLO https://dl.google.com/android/repository/build-tools_r34-linux.zip && unzip -qo build-tools_r34-linux.zip
# 解压出来是 android-14/，就是 build-tools 34（aapt2 / d8 / zipalign / apksigner 都在里面）
mkdir -p platforms && cd platforms
curl -sSLO https://dl.google.com/android/repository/platform-34-ext12_r01.zip && unzip -qo platform-34-ext12_r01.zip
mv android-34-ext12 android-34
curl -sSL -o /var/tmp/j17.tgz "https://api.adoptium.net/v3/binary/latest/17/ga/linux/x64/jdk/hotspot/normal/eclipse"
mkdir -p /var/tmp/jdk17 && tar xzf /var/tmp/j17.tgz -C /var/tmp/jdk17   # /tmp 只有 ~1 GB，JDK 放 /var/tmp
```
注：`build.sh` 里 `SDK` 默认回落到 `/tmp/asdk`、`BT=$SDK/android-14`、`JAVA_HOME` 回落到 `/var/tmp/jdk17/...`，
换机器时用环境变量覆盖即可。

改页面后：先重建 HTML（`app/_build.py`、`_portal.py`、三套目录的 `_make*.py`），再跑 `build.sh`。

## 2.0 新增（完整素材库）
- 新增 `library/` 47 个 HTML：总览页 + 46 条素材（每条一页，含演示 / 实现方案 / 参考来源 / 环境要求 / 提示词）
- App 里新增第 4 个集合「完整素材库 46」：卡片是**实时演示**（按 300×210 画布等比缩放），详情里仍可勾变更要求 + 一键复制
- 素材 CSS 按 `[data-item="Fxx"]` 作用域隔离（46 条样式合并到一页也不会互串），keyframes 也加了条目后缀
- 打包脚本改为把 `library/**` 的 HTML 原样写进 `assets/www/library/`，保留 `Fxx-slug` 目录
- 首页/欢迎页文案、筛选 chips、门户页全部更新到 68 个素材

## 1.1 新增
- 系统分享（`AndroidBridge.share` → ACTION_SEND chooser），详情里提示词可直接发出去
- 手势/系统返回键先关详情（`pushState` + `popstate`）
- 设置持久化：配色 / 玻璃开关 / 减少动效 / 对比选择（localStorage，WebView DomStorage）
- 首次启动三步新手引导，设置里可重看
- 修掉移动端 `@media` 把设置页配色点一起隐藏的问题

## 3.1 变更（Dock 外壳 / 案例剧场 / 勾选不跳顶）
- 外壳换成 v3：底部悬浮 **Dock**（图标格 + 滑动指示器）+ 顶栏浮动玻璃条；近黑中性底 + 低饱和光团，去掉大面积蓝色极光
- 首页重做：大标语 + 一条搜索直通 + 2×2 磁贴（素材库宽卡 / 弹层 / 动效 / 搭项目宽卡）+ 横滑「先看这几个」+ 按来源进入 + 怎么用
- 7 个 case 改成**全屏剧场**：380（720 以上 440）高的画布、机制/参数/判据三卡、复制提示词、完整演示页、7 个案例直接切 + 上下篇
- 修 m07 手绘 3D 空白：首帧时间戳早于 t0 导致抖动表为空 → 预置 12 个抖动点并按长度兜底；`loop()` 现在单帧异常不会杀死整段动画
- m01–m07 在小舞台里重做尺寸与自动演示：m02 弦铺满 + 自动拨弦、m04 高度自适应 + 自动滚一屏、m05 自动巡游 + 词随轨道升起、m06 姿态放大 + 自动翻、m07 骨架放大
- 结构页勾选只重画「功能 / 映射 / 提示词」这一段，滚动位置不动
- 门户页移除 APK 安装包区块

## 3.0 新增（体验馆 / 搭项目 / 分类搜索）
- 底部导航改成 5 个：首页 / 素材 / 体验 / 结构 / 更多（对比与设置收进「更多」）
- 体验馆 —— XPopup：20 种弹窗（7 大家族全在，真弹真拖；attach/bubble/position 用锚点示例行）、
  20 种 `PopupAnimation`（小舞台逐个播 + 全部播一遍）、45 个 Builder 设置按 8 组列出（7 个开关直达运行时）、5 组手势实验台
- 体验馆 —— motion-web：7 个 case（进详情页）、20 条配方（每条一个实时挂载的 `.mr` 舞台 + 复制提示词）、
  4 组令牌实验室（duration 7 / easing 9 / spring 6 / stagger 5，点一下重播）、25 篇规范索引（折叠章节 + 中文导读）
- 搭项目：3 个平台（纯静态 / Vite+TS / Android+XPopup）× 11 个功能开关 → 目录树 + 文件↔素材映射 + 开工提示词
  （提示词随选择实时变化，可一键复制整段或只复制目录树）
- 素材库：8 个分类卡进分类详情页（该类全部素材 + 直接去体验的直达入口）、全局搜索按相关度排序并支持同义词
  （弹窗↔popup↔dialog、图表↔折线/柱状/环形、错峰↔stagger…），搜索结果点弹窗类直接弹、点素材类直接开详情
- 修掉一个老 bug：`.feat` 在首页四卡与项目结构功能卡之间撞名，首页四卡改名 `.pick4`

## 2.0 验证
- 74 个 assets / 87 个 zip 条目，中文文件名 UTF-8 标志位齐全，`zipalign -c 4` 通过，v2+v3 签名
- 解包后用 Chromium 走 `file://` 冒烟：App 68 张卡 0 报错；46 条素材页各 6 个文档面板全部渲染；检索 图表/深色/弹簧/导航 均命中
- 详情页「打开完整演示页」相对路径 `../library/F25-toast/index.html` 校验存在

## 已验证
- `apksigner verify`：v2 + v3 签名通过；`zipalign -c 4` 通过
- 27 个 HTML 全在 assets 里，中文文件名正确
- 模拟 AndroidBridge 后：App 复制、演示页复制、卡片跳转、目录互跳、玻璃 WebGL 渲染均正常，零外部请求、零 JS 错误
- 1.1 专项：首启引导出现/关闭 ✓、详情 pushState `#m03` 且系统返回关闭 ✓、分享走桥 656 字 ✓、
  配色 mint + 实心卡片重载后仍保留 ✓、引导不再自动弹 ✓、设置里重开引导 ✓
