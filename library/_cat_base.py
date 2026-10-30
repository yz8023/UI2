# -*- coding: utf-8 -*-
"""素材库 · 数据基座：设计 token、demo 容器、条目构造器"""

# 所有组件 demo 共用的舞台与设计 token（深色，和 App 一致）
DEMO_CSS = r"""
.dz{
  --bg:#0d141b; --card:#161f28; --card2:#1d2731; --ink:#e9f0f8; --soft:rgba(233,240,248,.60);
  --dim:rgba(233,240,248,.34); --line:rgba(255,255,255,.14); --line2:rgba(255,255,255,.22);
  --acc:#9dccff; --acc-d:#164a70; --mint:#5fdba8; --ok:#5fdba8; --warn:#ffd28a; --danger:#ff8fa3; --violet:#9d8cff;
  --r:14px; --r-sm:10px; --pill:999px;
  --spring:cubic-bezier(.2,.9,.3,1.15); --ease:cubic-bezier(.2,.8,.3,1);
  position:relative; height:100%; min-height:150px; display:grid; place-items:center; padding:12px;
  background:
    radial-gradient(120% 100% at 18% 0%, rgba(157,204,255,.10), transparent 62%),
    radial-gradient(120% 100% at 92% 104%, rgba(95,219,168,.075), transparent 62%),
    var(--bg);
  color:var(--ink); font-size:13px; line-height:1.5; overflow:hidden;
  contain:layout paint style;
}
.dz *{box-sizing:border-box}
.dz .lbl{font-size:11px;color:var(--soft);letter-spacing:.04em}
.dz .cap{position:absolute;left:9px;bottom:7px;font-size:9px;line-height:1.4;color:var(--dim);z-index:9;
  background:rgba(6,10,16,.55);border:1px solid rgba(255,255,255,.07);padding:2px 7px;border-radius:99px;
  pointer-events:none;max-width:calc(100% - 18px)}
.dz .row{display:flex;align-items:center;gap:8px}
.dz .col{display:flex;flex-direction:column;gap:8px}
.dz .card{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:12px}
.dz button{font:inherit;color:inherit;background:none;border:0;cursor:pointer}
.dz .t-press{transition:transform .16s var(--spring)}
.dz .t-press:active{transform:scale(.955)}
.dz .btn{display:inline-flex;align-items:center;justify-content:center;gap:6px;height:30px;padding:0 14px;
  border-radius:10px;font-size:12px;color:var(--ink);background:rgba(255,255,255,.08);
  border:1px solid var(--line);transition:transform .16s var(--spring),background .18s;cursor:pointer}
.dz .btn:active{transform:scale(.96)}
.dz .btn.pri{background:linear-gradient(180deg,#a9d4ff,#7fbdf5);color:#06121c;font-weight:700;border-color:transparent;
  box-shadow:0 6px 16px rgba(120,180,240,.28)}
.dz .btn.danger{background:rgba(255,143,163,.16);color:#ff8fa3;border-color:rgba(255,143,163,.4)}
.dz .dots i{display:inline-block}
@media (prefers-reduced-motion: reduce){ .dz *{transition-duration:.01ms!important;animation-duration:.01ms!important} }
"""


def item(**kw):
    """统一字段，缺省的走默认值"""
    d = dict(
        id='', slug='', name='', cat='', catname='', diff='★★☆',
        tag='', mech='', params='', verify='', steps=[], redline=[], fails=[],
        prompt='', html='', css='', js='', refs=[], env_deps='无第三方依赖（原生 HTML / CSS / JS）',
        env_files=None, env_notes='', demo_hint='',
    )
    d.update(kw)
    d.setdefault('slug', d['id'].lower())
    if d['env_files'] is None:
        d['env_files'] = ['代码/index.html（可直接双击运行的完整示例）']
    return d


REG = []


def add(*items):
    REG.extend(items)


def by_cat():
    cats = {}
    for it in REG:
        cats.setdefault(it['catname'], []).append(it)
    order = ['基础组件', '表单输入', '导航', '布局', '反馈', '数据展示', '动效', '应用模板']
    return [(c, cats[c]) for c in order if c in cats]


CAT_META = {
    '基础组件': ('01', '按钮、输入、开关、滑块、勾选、头像徽标', 'F01–F06'),
    '表单输入': ('02', '校验、步进、分段、搜索、上传、选择器', 'F07–F12'),
    '导航': ('03', '标签栏、顶栏、抽屉、面包屑、标签页、侧边栏', 'F13–F18'),
    '布局': ('04', '卡片网格、分组列表、瀑布流、栅格、粘性堆叠、安全区', 'F19–F24'),
    '反馈': ('05', 'Toast、对话框、底部弹层、骨架屏、空态、进度、加载按钮', 'F25–F31'),
    '数据展示': ('06', '折线、柱状、环形、统计卡、表格、时间线', 'F32–F37'),
    '动效': ('07', '弹簧拖拽、错峰入场、手势卡片、页面转场、滚动视差', 'F38–F42'),
    '应用模板': ('08', '引导页、登录页、设置页、个人中心', 'F43–F46'),
}

# 常用参考来源（全库统一引用，保证 CREDITS 与每篇 参考来源.md 对齐）
REF = {
    'miuix': ('Miuix · chibatching', 'https://github.com/chibatching/Miuix', 'Apache-2.0', 'MIUI 风格组件语义：开关、底栏、分组列表'),
    'shadcn': ('shadcn/ui', 'https://github.com/shadcn-ui/ui', 'MIT', '组件结构、变体命名（variant/size）与可访问性约定'),
    'radix': ('Radix Primitives', 'https://github.com/radix-ui/primitives', 'MIT', '对话框 / 弹层 / 焦点陷阱 / 键盘交互的无障碍模型'),
    'motion': ('Motion (Framer Motion)', 'https://github.com/motiondivision/motion', 'MIT', '弹簧参数 (stiffness, damping) 记法与预设'),
    'motionweb': ('feitangyuan/motion-web', 'https://github.com/feitangyuan/motion-web', 'CC BY-NC 4.0', '动效 token、错峰入场、滚轮与视差机制'),
    'glass': ('iyinchao/liquid-glass-studio', 'https://github.com/iyinchao/liquid-glass-studio', 'MIT', '液态玻璃 4-pass 渲染与参数体系'),
    'yzui': ('yz8023/ui', 'https://github.com/yz8023/ui', 'MIT', '素材库的「四件套」文档结构、深色极光 + 玻璃底栏视觉、AGENTS 红线写法'),
    'm3': ('Material Design 3', 'https://m3.material.io/', '文档（CC BY 4.0）', '组件尺寸、状态层、Elevation 与色调映射'),
    'hig': ('Apple Human Interface Guidelines', 'https://developer.apple.com/design/human-interface-guidelines/', '文档', '触控热区 44pt、分组列表、分段控件与安全区'),
    'antd': ('Ant Design', 'https://github.com/ant-design/ant-design', 'MIT', '表单校验、表格、统计卡与数据展示规范'),
    'vant': ('Vant', 'https://github.com/youzan/vant', 'MIT', '移动端 Toast / 弹层 / 步进器 / 选择器的交互细节'),
    'floating': ('Floating UI', 'https://github.com/floating-ui/floating-ui', 'MIT', '锚定浮层的定位与碰撞翻转'),
    'ionic': ('Ionic Framework', 'https://github.com/ionic-team/ionic-framework', 'MIT', '移动端手势（下拉关闭、滑动切页）的实现参考'),
    'wind': ('Tailwind CSS', 'https://github.com/tailwindlabs/tailwindcss', 'MIT', '间距 / 圆角 / 阴影的原子化尺度'),
}


def refs(*keys):
    return [REF[k] for k in keys]
