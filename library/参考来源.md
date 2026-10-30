# 致谢 · 参考文献

本素材库的**代码与视觉语言**建立在以下开源项目与公开文档之上。谢谢所有作者的无私分享。

## 一、方法论与视觉总来源

| 项目 | 链接 | 许可 | 借鉴了什么 |
| --- | --- | --- | --- |
| **yz8023/ui** | https://github.com/yz8023/ui | MIT | 素材库的「四件套」文档结构（实现方案 / 参考来源 / 环境要求）、
AGENTS 红线写法、验收清单与失败指纹的表达、深色极光 + 液态玻璃的界面语言 |

> 移植的是**方法与观感**，不是代码：上游是 Android Compose 工程，本库是 HTML/CSS/JS，
> 两者共享同一套文档骨架与视觉规则。

## 二、每个条目的直接参考

| 项目 | 链接 | 许可 | 借鉴了什么 |
| --- | --- | --- | --- |
| **Miuix · chibatching** | https://github.com/chibatching/Miuix | Apache-2.0 | MIUI 风格组件语义：开关、底栏、分组列表 |
| **shadcn/ui** | https://github.com/shadcn-ui/ui | MIT | 组件结构、变体命名（variant/size）与可访问性约定 |
| **Radix Primitives** | https://github.com/radix-ui/primitives | MIT | 对话框 / 弹层 / 焦点陷阱 / 键盘交互的无障碍模型 |
| **Motion (Framer Motion)** | https://github.com/motiondivision/motion | MIT | 弹簧参数 (stiffness, damping) 记法与预设 |
| **feitangyuan/motion-web** | https://github.com/feitangyuan/motion-web | CC BY-NC 4.0 | 动效 token、错峰入场、滚轮与视差机制 |
| **iyinchao/liquid-glass-studio** | https://github.com/iyinchao/liquid-glass-studio | MIT | 液态玻璃 4-pass 渲染与参数体系 |
| **yz8023/ui** | https://github.com/yz8023/ui | MIT | 素材库的「四件套」文档结构、深色极光 + 玻璃底栏视觉、AGENTS 红线写法 |
| **Material Design 3** | https://m3.material.io/ | 文档（CC BY 4.0） | 组件尺寸、状态层、Elevation 与色调映射 |
| **Apple Human Interface Guidelines** | https://developer.apple.com/design/human-interface-guidelines/ | 文档 | 触控热区 44pt、分组列表、分段控件与安全区 |
| **Ant Design** | https://github.com/ant-design/ant-design | MIT | 表单校验、表格、统计卡与数据展示规范 |
| **Vant** | https://github.com/youzan/vant | MIT | 移动端 Toast / 弹层 / 步进器 / 选择器的交互细节 |
| **Floating UI** | https://github.com/floating-ui/floating-ui | MIT | 锚定浮层的定位与碰撞翻转 |
| **Ionic Framework** | https://github.com/ionic-team/ionic-framework | MIT | 移动端手势（下拉关闭、滑动切页）的实现参考 |
| **Tailwind CSS** | https://github.com/tailwindlabs/tailwindcss | MIT | 间距 / 圆角 / 阴影的原子化尺度 |

## 三、许可证与使用边界

- 本库全部演示代码为**独立实现**（procedural），未复制任何上游项目的源码、截图、图标、字体。
- **feitangyuan/motion-web** 为 **CC BY-NC 4.0**：仅可用于非商业用途。本库只参考其动效 token 的数值思路
  （时长、缓动、错峰节奏），未复制其任何素材；如需商用请自行评估。
- **iyinchao/liquid-glass-studio** 为 **MIT**：本库的玻璃参数体系（厚度 / 折射率 / 色散 / 菲涅尔）参考其公开参数表，
  渲染实现为 CSS + SVG 的简化版本。
- **yz8023/ui** 为 **MIT**：可自由借鉴与再分发，保留本致谢即可。
- Material Design 3、Apple HIG 为文档，非代码，按其公开条款引用。

## 四、如何引用本库

```text
UI 素材库 2.0（46 条素材），文档结构参考 yz8023/ui（MIT），
动效 token 参考 feitangyuan/motion-web（CC BY-NC 4.0），玻璃参数参考 iyinchao/liquid-glass-studio（MIT）。
```
