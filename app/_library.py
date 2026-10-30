# -*- coding: utf-8 -*-
"""把 ../library 的 46 条素材接进 App：数据 / CSS / JS 三件套。"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LIB = os.path.join(ROOT, 'library')
if LIB not in sys.path:
    sys.path.insert(0, LIB)

from _cat_base import REG, DEMO_CSS                     # noqa: E402
import _cat_a, _cat_b, _cat_c, _cat_d, _cat_e, _cat_f    # noqa: F401,E402
import re                                                # noqa: E402


def scope_css(css, iid):
    """与 library/gen_library.py 同款：keyframes 改名 + `.dz` 换成按条目隔离的选择器。"""
    for name in set(re.findall(r'@keyframes\s+([A-Za-z_][\w-]*)', css)):
        css = re.sub(r'(?<![\w-])' + re.escape(name) + r'(?![\w-])', f'{name}-{iid}', css)
    return css.replace('.dz', f'[data-item="{iid}"]')

CAT_OF = {'基础组件': '组件', '表单输入': '表单', '导航': '导航', '布局': '布局',
          '反馈': '反馈', '数据展示': '数据', '动效': '动效', '应用模板': '模板'}


USE = {
 'F01':'提交 / 取消 / 次要操作', 'F02':'单行文本、邮箱、密码', 'F03':'二元设置项',
 'F04':'连续数值：音量、模糊半径', 'F05':'多选与互斥选项', 'F06':'用户身份、未读数、在线态',
 'F07':'提交前校验与错误提示', 'F08':'数量加减', 'F09':'2–4 个互斥视图切换',
 'F10':'关键词检索与联想', 'F11':'拖拽 / 选择 / 上传进度', 'F12':'从列表里选一个值',
 'F13':'App 一级导航', 'F14':'长列表页的标题区', 'F15':'次级导航与设置入口',
 'F16':'层级位置与回退', 'F17':'同层级内容切换', 'F18':'平板 / 桌面的一级导航',
 'F19':'首页 Bento 与数据概览', 'F20':'设置页、账户页', 'F21':'高度不一的图文流',
 'F22':'多端自适应排版', 'F23':'分屏叙事、章节页', 'F24':'刘海屏与手势条适配',
 'F25':'操作结果反馈', 'F26':'需要用户决策的确认', 'F27':'多个操作选项',
 'F28':'加载中的占位', 'F29':'无数据时的引导', 'F30':'任务进度、完成度',
 'F31':'提交中的防重复', 'F32':'趋势随时间变化', 'F33':'分类对比',
 'F34':'占比构成', 'F35':'单个关键指标', 'F36':'多字段结构化列表',
 'F37':'版本、流程、事件顺序', 'F38':'可拖动元素的物理回弹', 'F39':'列表与网格的首屏入场',
 'F40':'左右滑动做取舍', 'F41':'列表 → 详情的共享元素', 'F42':'长页面的景深',
 'F43':'首次启动说明', 'F44':'账号登录 / 注册', 'F45':'偏好项与危险操作', 'F46':'用户资料与作品',
}

REQS = ['换成品牌主题色', '改成浅色模式', '缩到 360px 宽', '加键盘 / 无障碍支持']


def items():
    out = []
    for it in REG:
        first = it['mech'].split('：')[0].split('。')[0]
        title = first if len(first) <= 18 else first[:17] + '…'
        out.append(dict(
            id=it['id'], num=it['id'][1:], coll='lib',
            name=it['name'], title=title,
            path='../library/%s-%s/index.html' % (it['id'], it['slug']),
            src='UI 素材库 2.0', dur=CAT_OF.get(it['catname'], it['catname']),
            diff=it['diff'], mech=it['mech'], params=it['params'], verify=it['verify'],
            use=USE.get(it['id'], ''),
            prompt=it['prompt'].strip(), reqs=REQS, demos=[],
        ))
    return out


def css():
    base = DEMO_CSS.replace('.dz', '.libdz')
    base += """
.libfit{width:300px;height:210px;transform:scale(var(--s,.8));transform-origin:center center}
.libdz{width:100%;height:100%;min-height:0}
.mini.lib{height:196px}
"""
    return base + '\n'.join(scope_css(it['css'], it['id']) for it in REG)


def js():
    tpl = json.dumps({it['id']: it['html'] for it in REG}, ensure_ascii=False)
    fns = ','.join('"%s":%s' % (it['id'], it['js']) for it in REG)
    return """
window.__LIBTPL = %s;
window.__LIBJS = {%s};
(function(){
  var TPL = window.__LIBTPL, FN = window.__LIBJS;
  window.__MINI = window.__MINI || {};
  Object.keys(TPL).forEach(function(id){
    window.__MINI[id] = function(el){
      el.classList.add('lib');
      el.innerHTML = '<div class="libfit"><div class="libdz" data-item="' + id + '">' + TPL[id] + '</div></div>';
      var fit = el.firstChild, dz = fit.firstChild;
      function calc(){
        var w = el.clientWidth, h = el.clientHeight;
        if(!w || !h) return;
        var s = Math.min((w - 6) / 300, (h - 6) / 210);
        fit.style.setProperty('--s', Math.max(.3, Math.min(1.6, s)).toFixed(3));
      }
      calc();
      var ro = window.ResizeObserver ? new ResizeObserver(calc) : null;
      if(ro) ro.observe(el);
      try{ if(FN[id]) FN[id](dz); }catch(e){ console.warn('lib demo fail', id, e); }
      return function(){ if(ro) ro.disconnect(); el.innerHTML = ''; };
    };
  });
})();
""" % (tpl, fns)
