# -*- coding: utf-8 -*-
"""生成 glass-demos 6 个演示页 + 目录页"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import _libg
from _libg import render, INDEX_HEAD, INDEX_EXTRA
from _glass_js import GLASS_JS
import _pg_1, _pg_2

PAGES = [
    (_pg_1.L01, {}),
    (_pg_1.L02, {}),
    (_pg_1.L03, {}),
    (_pg_2.L04, {}),
    (_pg_2.L05, {}),
    (_pg_2.L06, {}),
]

CARD = {
    "refraction": ("边缘 20px 带", "中心不偏移，边缘拼命偏移——玻璃厚度的全部秘密",
                   "Snell 边缘因子 · RGB 折射率 0.98/1.0/1.02 · debug 步骤"),
    "fresnel-glare": ("方向光源", "菲涅尔是环，眩光是弧：一个均匀、一个有方向",
                      "pow5 菲涅尔 · 法线×光源方向 · 对侧弱反光"),
    "superellipse-blob": ("n = 2 → 7", "圆角矩形和 squircle 的区别，就是 n 从 2 走到 5",
                          "超椭圆角部 · smin 融合 · 弹簧跟随副形状"),
    "blur-pipeline": ("31 × 2 取样", "可分离卷积：两次一维，等于一次二维",
                      "sigma = r/3 · 31 tap · blurEdge · SDF 阴影"),
    "spring-follow": ("0 帧 → 过冲", "玻璃有质量，所以它会追鼠标、也会冲过头",
                      "none / lerp / spring · 速度驱动尺寸回弹"),
    "render-steps": ("8 个切面", "把 4 个 pass 一层层剥开，看参数到底作用在哪一层",
                     "8 个正交切面 · 中间纹理直出 · 自动播放"),
}

COMMON_REQ = [
    "改成深色背景，玻璃整体压暗一档",
    "做成可直接复用的卡片组件（含 3 个图标按钮）",
    "加移动端适配：390px 竖屏下单列、画布高度 260px",
    "参数面板收成 3 组预设（清透 / 磨砂 / 浓彩）",
    "加一个「导出当前画布为 PNG」按钮",
    "换成浅色背景，验证文字与玻璃的可读性",
]
EXTRA_REQ = {
    "refraction": ["加 GPU 计时：显示 4 个 pass 各自耗时（ms）"],
    "fresnel-glare": ["把眩光染成品牌色（不改变方向性）"],
    "superellipse-blob": ["两块玻璃都能用指针拖拽，不只是跟随"],
    "blur-pipeline": ["模糊质量两档：低（9 tap）/ 高（31 tap）"],
    "spring-follow": ["支持拖拽甩出后带惯性继续滑行"],
    "render-steps": ["加「八宫格」模式：一次并排显示全部 8 个步骤"],
}


def build(pages):
    total = len(pages)
    cards = []
    for i, (p, extra) in enumerate(pages):
        p = dict(p)
        p.update(extra)
        d, w, h = CARD[p["slug"]]
        p["dur"] = d; p["card_what"] = w; p["card_how"] = h
        no = int(p["no"])
        prev = pages[i - 1][0] if i > 0 else None
        nxt = pages[i + 1][0] if i < total - 1 else None
        pager = ""
        if prev:
            pager += '<a href="l%02d-%s.html"><div class="k">← 上一页 · %s</div><div class="t">%s</div></a>' % (
                int(prev["no"]), prev["slug"], prev["no"], prev["short"])
        else:
            pager += '<a href="index.html"><div class="k">← 返回</div><div class="t">全部 6 个演示</div></a>'
        if nxt:
            pager += '<a class="next" href="l%02d-%s.html"><div class="k">下一页 · %s →</div><div class="t">%s</div></a>' % (
                int(nxt["no"]), nxt["slug"], nxt["no"], nxt["short"])
        else:
            pager += '<a class="next" href="index.html"><div class="k">看完了 →</div><div class="t">返回目录</div></a>'
        p["pager"] = pager
        rel = COMMON_REQ[:3] + EXTRA_REQ.get(p["slug"], []) + COMMON_REQ[3:5]
        html = render(p, rel, GLASS_JS)
        out = os.path.join(HERE, "l%02d-%s.html" % (no, p["slug"]))
        open(out, "w", encoding="utf-8").write(html)
        print("wrote", os.path.basename(out), len(html))
        cards.append(
            '<a class="vcard" href="l%02d-%s.html">\n'
            '      <div class="vtop"><span class="vno">%s</span><span class="vtags">%s</span>'
            '<span class="vdur">%s</span></div>\n'
            '      <h3>%s</h3>\n'
            '      <p class="vwhat">%s</p>\n'
            '      <p class="vhow">%s</p>\n'
            '      <span class="vgo">进入演示 + 提示词 →</span>\n'
            '    </a>' % (int(p["no"]), p["slug"], p["no"], p["layer"], p["dur"], p["title"],
                           p["card_what"], p["card_how"]))
    html = (INDEX_HEAD.replace("{css}", _libg.SHARED_CSS + _libg.MOTION_CSS + _libg.GLASS_CSS)
                      .replace("{extra}", INDEX_EXTRA)
                      .replace("{cards}", "\n    ".join(cards)))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(html)
    print("wrote index.html", len(html))


if __name__ == "__main__":
    build(PAGES)
