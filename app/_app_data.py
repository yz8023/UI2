# -*- coding: utf-8 -*-
"""素材库 App 的数据层：22 个素材（9 视频拆解 + 7 动效 + 6 玻璃）"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'motion-demos'))
sys.path.insert(0, os.path.join(ROOT, 'glass-demos'))
sys.path.insert(0, os.path.join(ROOT, 'video-demos'))

import _cases_1, _cases_2          # noqa
import _library                    # noqa
import _pg_1, _pg_2                # noqa
import _pages_a, _pages_c, _pages_d, _pages_e  # noqa


def _motion():
    out = []
    for mod in (_cases_1, _cases_2):
        for name, v in vars(mod).items():
            if isinstance(v, dict) and 'prompt' in v:
                out.append(v)
    out.sort(key=lambda v: v['no'])
    items = []
    for v in out:
        items.append(dict(
            id='m' + v['no'], num=v['no'], coll='motion', name=v['short'], title=v['title'],
            path='../motion-demos/m%s-%s.html' % (v['no'], v['slug']),
            src='motion-web · %s' % v['slug'],
            dur='canvas 2d' if 'canvas' in v.get('layer_cn', 'canvas') else 'dom',
            layer=v.get('layer_cn', ''), diff='★★☆',
            mech=v['mech'], params=v['params'], verify=v['verify'],
            prompt=v['prompt'].strip(), reqs=v.get('reqs') or [],
            demos=[],
        ))
    return items


def _glass():
    out = []
    for mod in (_pg_1, _pg_2):
        for name, v in vars(mod).items():
            if isinstance(v, dict) and 'prompt' in v and 'slug' in v:
                out.append(v)
    out.sort(key=lambda v: v['no'])
    items = []
    for v in out:
        items.append(dict(
            id='l' + v['no'], num=v['no'], coll='glass', name=v['short'], title=v['title'],
            path='../glass-demos/l%s-%s.html' % (v['no'], v['slug']),
            src='liquid-glass-studio · %s' % v['path'].split('/')[-1],
            dur='webgl2', layer=v['layer'], diff='★★★',
            mech=v['mech'], params=v['params'], verify=v['verify'],
            prompt=v['prompt'].strip(), reqs=[], demos=[],
        ))
    return items


VIDEO = [
    dict(
        no='01', short='弹窗选型', title='别把所有弹出来的东西都叫「弹窗」', tag='浮层 / 弹窗',
        mech='同一件事按「是否打断、是否可撤销」分三种承载：Toast（不打断、无操作）、Drawer（不打断、可操作）、Modal（打断、必须决策）。',
        params='三种承载 · 打断性 · 可撤销性 · 信息量',
        verify='删除等不可逆操作必须用 Modal；设置类用 Drawer；结果反馈用 Toast；三者不能互相替代。',
        prompt='''做一个单文件 HTML（零依赖），把「Toast / Drawer / Modal」三种承载放进同一块画布对比。
【做法】
- 一块 640×420 的舞台，三个按钮：Toast、Drawer、Modal。
- Toast：底部滑入，1.5s 自动消失，不带按钮，不抢焦点。
- Drawer：从右侧滑入，覆盖 45% 宽度，可关，页面其余部分仍可见可读。
- Modal：全屏压暗 + 卡片缩放进入，必须点确认/取消才关闭。
【必须给出选型判据】
- 打断性（是否阻断当前任务）· 可撤销性（操作是否可回退）· 信息量（是否需要承载表单）。
- 给一句结论：不可逆 → Modal；可回退的设置 → Drawer；只是告知结果 → Toast。
【自检】
- 三种都在 200ms 内给出视觉反馈；
- Toast 不能含需要点击的元素；
- Modal 打开后焦点必须锁在卡片内。
输出完整 HTML。'''),
    dict(
        no='02', short='6 种高级浮层', title='别只知道 Modal：6 种高级浮层', tag='浮层体系',
        mech='把「浮层」拆成 6 种语义：Popover（锚定、非模态）、Tooltip（只解释）、Sheet（底部可拖）、Dialog（必须决策）、Menu（命令集）、Lightbox（看大图）。',
        params='6 种浮层 · 锚点关系 · 模态层级 · 关闭方式',
        verify='每种浮层必须能回答「为什么不用 Modal」；关闭方式与层级不能混淆（Tooltip 不可点，Menu 选完即关）。',
        prompt='''做一个单文件 HTML，用 6 个可点的示例讲清「浮层」的 6 种语义。
【6 种】
1 Popover：锚定在按钮旁，点击外部关闭，非模态；
2 Tooltip：悬停出现，只解释，不可交互；
3 Sheet：从底部升起，可向下拖动关闭；
4 Dialog：压暗背景，必须决策；
5 Menu：一列命令，选中即关闭；
6 Lightbox：看大图，背景压暗，Esc 关闭。
【要求】
- 每个浮层旁边写一句「什么时候必须用它」，以及「什么时候不该用」；
- 所有浮层共用一套进入/退出曲线（如 cubic-bezier(.2,.9,.3,1.1)，180–260ms）；
- 必须处理 Esc 关闭、点击外部关闭、焦点返回触发按钮。
【自检】键盘可完整操作；同一时刻只允许一个模态浮层。
输出完整 HTML。'''),
    dict(
        no='03', short='大厂质感 5 招', title='扒了大厂源码，高级感全在这 5 招', tag='视觉质感',
        mech='质感不是滤镜，是 5 个可枚举的细节：分层阴影、内高光描边、统一圆角、留白节奏、低对比渐变。',
        params='分层阴影 2 层 · 内描边 1px 白 12% · 圆角同一套 scale · 8pt 间距 · 渐变对比 <8%',
        verify='逐条开关，关掉任意一条都能说出「哪里变廉价了」；关掉全部后必须明显掉档。',
        prompt='''做一个单文件 HTML，用一张卡片演示「高级感」的 5 个可开关来源。
【5 招（每条都能单独开合）】
1 分层阴影：一层紧贴 + 一层大范围（0 1px 2px rgba(0,0,0,.4), 0 14px 34px rgba(0,0,0,.55)）；
2 内高光描边：inset 0 1px 0 rgba(255,255,255,.22) + 1px 边框 rgba(255,255,255,.12)；
3 统一圆角：卡片/按钮/输入框共用一套圆角比例（如 16 / 12 / 10）；
4 留白节奏：内边距按 8 的倍数，文字行高 1.6；
5 低对比渐变：160deg 两个近似色，明度差不超过 8%。
【交互】5 个开关独立生效，右侧实时显示当前「质感分」（开几条），全部关掉时卡片必须明显变廉价。
【自检】截取全开 / 全关两张图，肉眼必须能看出档次差异。
输出完整 HTML。'''),
    dict(
        no='04', short='AI 界面 5 细节', title='大厂 AI 界面的 5 个隐藏细节', tag='AI 交互',
        mech='流式输出 + 可打断 + 复制/重试 + 状态可读 + 失败可恢复：AI 界面的体验差异全在这 5 个状态机里。',
        params='首字 <800ms · token 流 30–60/s · 停止按钮常驻 · 失败保留已生成内容',
        verify='任何时刻都能停止；停止后内容保留可复制；失败时必须给出重试且不清空已有输出。',
        prompt='''做一个单文件 HTML，复刻 AI 聊天界面的 5 个关键细节（可交互原型）。
【5 个细节】
1 首字延迟：请求后先出骨架/光标，800ms 内必须有第一个字；
2 流式输出：每帧追加 2–4 个字符，逐字光标闪烁，行高固定避免抖动；
3 可打断：生成中「停止」按钮常驻且可点，点后立即停在当前内容；
4 结果操作：复制 / 重新生成 / 好的反馈，位置固定在答案下方；
5 失败恢复：模拟失败时保留已生成内容，给「重试」而不是清空。
【要求】状态机写清楚：idle → requesting → streaming → done | stopped | error，用 DOM 属性体现当前状态。
【自检】生成中点停止，内容不丢；失败后点重试，从原位置续写。
输出完整 HTML。'''),
    dict(
        no='05', short='下拉 vs 选择器', title='别乱叫「下拉框」：Dropdown vs Select', tag='组件选型',
        mech='Dropdown 是「命令菜单」，点一项立刻执行，按钮文字不变；Select 是「取值控件」，点一项回填数值，不执行动作。',
        params='命令型 vs 取值型 · 是否回填 · 是否关闭 · 键盘行为',
        verify='Dropdown 选中后必须触发动作且标题不变；Select 选中后只改显示值，不触发任何副作用。',
        prompt='''做一个单文件 HTML，把 Dropdown（命令菜单）与 Select（取值控件）并排放在真实界面里各点一次。
【左边 Dropdown】一个「分享 ▾」按钮，菜单里是命令：复制链接 / 发送给… / 导出 PDF。
- 点任意一项：立刻执行（给出结果提示），按钮文字保持不变，菜单关闭。
【右边 Select】一个「城市 ▾」控件，列表是可选值：上海 / 杭州 / 成都。
- 点任意一项：只把按钮文字回填为所选值，不执行任何动作，菜单关闭。
【下方各写一行日志】说明刚刚发生的是「执行了命令」还是「回填了数值」。
【必须给出的判据表】动作是否发生 · 是否回填 · 是否记住上次选择 · 键盘是否支持上下选择。
【自检】Dropdown 不保存选择；Select 不产生副作用。
输出完整 HTML。'''),
    dict(
        no='06', short='热区与误触', title='为什么你总是点不中那个按钮', tag='可点性',
        mech='视觉尺寸 ≠ 命中尺寸：32px 视觉按钮要给 44–56px 命中半径，用透明外扩热区实现，而不是把按钮画大。',
        params='视觉 32px · 命中 44–56px · 外扩方式 = 伪元素/padding/pointer 判定',
        verify='把热区从 32 切到 56，同一批点击的落空率必须显著下降，而视觉尺寸保持不变。',
        prompt='''做一个单文件 HTML，用可点的实验说明「热区」与「误触」。
【实验】
- 画布上并排两个视觉尺寸 32px 的按钮，命中半径一个 16px（=视觉），一个 28px（外扩）。
- 用户每次点击都记录命中/落空，右上角实时显示「命中 N · 落空 M」与落空率。
- 一个开关切换「扩大热区」，切换后视觉尺寸必须一像素都不变，只改命中判定与虚线示意圈。
【必须解释】外扩热区不能用 transform: scale（会放大视觉），要用透明 padding / 伪元素 / 命中距离判定。
【自检】扩大热区后落空率明显下降；两个按钮视觉完全一致；相邻按钮热区不能重叠（重叠时要按最近距离分配）。
输出完整 HTML。'''),
    dict(
        no='07', short='全球化布局', title='界面走向全球化，按钮为什么总被外文撑爆', tag='国际化',
        mech='不同语言字宽差异可达 2–3 倍：定宽按钮必然截断/溢出，正确做法是自适应宽度 + 省略号 + 可换行 + 允许容器拉伸。',
        params='zh 4 字 ↔ de 18 字 ↔ ru 15 字 · 定宽 52px 必爆炸 · 弹性布局 + ellipsis',
        verify='切到德语时，定宽按钮必须溢出/截断（用来演示问题），自适应与换行两种方案必须保持可读。',
        prompt='''做一个单文件 HTML，演示多语言下按钮被撑爆与三种解法。
【场景】一行三个按钮，同一句文案，四种语言：中文「导出报表」/ 英文「Export report」/ 德语「Bericht exportieren」/ 俄语「Экспорт отчёта」。
【三种布局并排】
1 定宽 bad：固定 52px，德语必然溢出或截断 → 标红提示；
2 自适应 + 省略号：max-width + text-overflow: ellipsis，必须还能 hover 看到全文；
3 可换行：white-space: normal + 行高调整，按钮高度自适应。
【要求】语言切换即时生效；给一张判据表：是否溢出 / 是否可读 / 是否会改变布局高度。
【自检】德语下第 1 种必须肉眼可见地坏掉，第 2、3 种必须可用。
输出完整 HTML。'''),
    dict(
        no='08', short='虎先锋 · 无伤实录', title='无伤虎先锋：40 帧还能这么丝滑？', tag='帧率 / 手感',
        mech='低帧率下的「丝滑」来自：稳定的帧时间曲线 + 明确的闪避窗口（约 320–700ms）+ 命中反馈与镜头反馈对齐。',
        params='≈40fps · 帧时间 16–38ms 抖动 · 闪避窗口 320–700ms · 冲击反馈 1–3 帧',
        verify='帧时间曲线震荡但无长帧尖峰；闪避成功必须在窗口内且反馈立即出现。',
        prompt='''做一个单文件 HTML，用一张实时图解释「低帧率下为什么还能丝滑」。
【画面】
- 上方：最近 54 帧的帧时间柱状图，>30ms 标黄；旁边显示实时 FPS 与当前帧时间。
- 下方：一条时间轴，标出攻击起手 → 闪避窗口（320–700ms 高亮）→ 命中判定。
【交互】画面每 1.5s 发起一次攻击，用户在窗口内点击画面算闪避成功，计数 +1；窗口外点击记 MISS。
【必须解释】丝滑 ≠ 高帧率：帧时间稳定 + 输入在窗口内被响应 + 反馈在 3 帧内出现，玩家就会觉得跟手。
【自检】窗口内点击必成功；柱状图不能出现整段空白（长帧）；MISS 与成功必须视觉可区分。
输出完整 HTML。'''),
    dict(
        no='09', short='寅虎 · 无伤实录', title='寅虎：你礼貌吗？——无伤挑战里的节奏', tag='节奏 / 判定',
        mech='节拍类手感的三个参数：周期（620ms）、判定窗口（PERFECT ±70ms / GOOD ±140ms）、反馈层级（字 + 颜色 + 缩放）。',
        params='BPM ≈ 97（620ms/拍）· PERFECT ±70ms · GOOD ±140ms · 判定文字停留 620ms',
        verify='窗口外的点击必须是 MISS；连续命中时判定文字不能重叠（需要排队/淡出）。',
        prompt='''做一个单文件 HTML 的「打拍子」判定小游戏，用来讲清节奏手感。
【机制】
- 拍点以 620ms 周期向圆心收拢（同心圈从外向内），第 0 圈到达圆心瞬间即拍点；
- 用户点击画面打拍子，按时间误差判定：|Δ| < 70ms 为 PERFECT，< 140ms 为 GOOD，其余 MISS；
- 判定文字从圆心上方浮出并淡出，停留 620ms；连续命中时文字必须上移排队，不能互相压住。
【界面】左侧显示 PERFECT / GOOD / MISS 计数；圆圈用半透明描边，不使用贴图。
【自检】窗口外点击必为 MISS；同一拍内连点不能重复得分（要有冷却）；判定文字在 60fps 下不抖动。
输出完整 HTML。'''),
]

VIDEO_FILES = {
    '01': '01-弹窗选型.html',
    '02': '02-6-种高级浮层.html',
    '03': '03-大厂质感-5-招.html',
    '04': '04-AI-界面-5-细节.html',
    '05': '05-下拉-vs-选择器.html',
    '06': '06-热区与误触.html',
    '07': '07-全球化布局.html',
    '08': '08-虎先锋-·-无伤实录.html',
    '09': '09-寅虎-·-无伤实录.html',
}

VIDEO_MODS = [(_pages_a, ['P01', 'P02']), (_pages_c, ['P03', 'P04']),
              (_pages_d, ['P05', 'P06']), (_pages_e, ['P07', 'P08', 'P09'])]


def _video():
    meta = {}
    for mod, keys in VIDEO_MODS:
        for k in keys:
            v = getattr(mod, k)
            demos = re.findall(r'<h2[^>]*>(.*?)</h2>', v['demos'], re.S)
            meta[v['no']] = dict(demos=[re.sub(r'<[^>]+>', '', d).strip() for d in demos],
                                 lede=v['lede'])
    items = []
    for v in VIDEO:
        m = meta.get(v['no'], dict(demos=[], lede=''))
        items.append(dict(
            id='v' + v['no'], num=v['no'], coll='video', name=v['short'], title=v['title'],
            path='../video-demos/' + VIDEO_FILES[v['no']],
            src='视频拆解 · %s' % v['tag'],
            dur='dom + css', layer='对比演示', diff='★☆☆',
            mech=v['mech'], params=v['params'], verify=v['verify'],
            prompt=v['prompt'].strip(), reqs=[], demos=m['demos'],
            lede=m['lede'],
        ))
    return items


REQ_LIB = {
    'video': ['改成深色配色，与素材库 App 一致', '补移动端 390px 布局', '给每种方案加一行「什么时候不该用」'],
    'motion': ['把交互从鼠标改成触摸优先', '加一个「慢放 0.25×」开关', '参数收成 3 个预设（柔和 / 标准 / 夸张）'],
    'glass': ['降低一点亮度，适配浅色页面', '加 FPS 读数验证性能', '做成可复用的组件并保留参数面板'],
}


def all_items():
    items = _video() + _motion() + _glass()
    for it in items:
        if not it['reqs']:
            it['reqs'] = REQ_LIB[it['coll']]
    items.sort(key=lambda x: (x['coll'] != 'video', x['coll'] != 'motion', x['num']))
    return _library.items() + items


if __name__ == '__main__':
    its = all_items()
    print(len(its))
    for it in its:
        print(it['id'], it['coll'], it['name'], '|', it['title'][:28], '| prompt', len(it['prompt']), '| demos', len(it['demos']))
