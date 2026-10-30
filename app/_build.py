# -*- coding: utf-8 -*-
"""生成 素材库 App：/home/user/app/index.html"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'glass-demos'))

from _shell import APP_CSS, APP_HTML
from _minis import MINI_CSS, MINIS_JS
from _minis_glass import MINIS_GLASS_JS
from _app_js import APP_JS
from _app_data import all_items
from _library import css as LIB_CSS, js as LIB_JS
from _xp import TYPES, ANIMS, SETTINGS, GESTURES, XP_CSS, XP_JS
from _mw import RECIPE_DEMOS, TOKENS
from _spec import SPECS, RECIPES, SPEC_ZH
from _proj import PLATFORMS, FEATURES, PROMPT
from _exp_css import EXP_CSS
from _exp_js import EXP_JS
from _glass_js import GLASS_JS


def build():
    items = all_items()
    slim = []
    for it in items:
        slim.append({k: it.get(k, '') for k in
                     ('id', 'num', 'coll', 'name', 'title', 'path', 'src', 'dur', 'diff',
                      'mech', 'params', 'verify', 'prompt', 'reqs', 'demos', 'use')})
    data = json.dumps(slim, ensure_ascii=False, indent=0)
    js = APP_JS.replace('__DATA__', data)
    rec = []
    for d in RECIPE_DEMOS:
        rec.append({'html': d['html'], 'css': d['css'], 'js': d['js']})
    payload = (
        '<script>window.__XPTYPES=' + json.dumps(TYPES, ensure_ascii=False) + ';'
        'window.__XPANIMS=' + json.dumps(ANIMS, ensure_ascii=False) + ';'
        'window.__XPSET=' + json.dumps(SETTINGS, ensure_ascii=False) + ';'
        'window.__XPGEST=' + json.dumps(GESTURES, ensure_ascii=False) + ';'
        'window.__MSPECS=' + json.dumps(SPECS, ensure_ascii=False) + ';'
        'window.__MRECIPES=' + json.dumps(RECIPES, ensure_ascii=False) + ';'
        'window.__SPECZH=' + json.dumps(SPEC_ZH, ensure_ascii=False) + ';'
        'window.__MTOKENS=' + json.dumps(TOKENS, ensure_ascii=False) + ';'
        'window.__MPROJ=' + json.dumps({'platforms': PLATFORMS, 'features': FEATURES, 'prompt': PROMPT},
                                       ensure_ascii=False) + ';'
        '</script>')
    recjs = ('<script>window.__REC=' + json.dumps(rec, ensure_ascii=False) +
             ';window.__ANIM=' + json.dumps(ANIMS, ensure_ascii=False) + ';</script>')
    html = (APP_HTML
            .replace('__CSS__', APP_CSS + MINI_CSS + LIB_CSS() + XP_CSS + EXP_CSS)
            .replace('__GLASS__', GLASS_JS)
            .replace('__PAYLOAD__', payload)
            .replace('__RECJS__', recjs)
            .replace('__XPJS__', XP_JS)
            .replace('__EXPJS__', EXP_JS)
            .replace('__MINIS__', MINIS_JS + LIB_JS())
            .replace('__GLASSMINIS__', MINIS_GLASS_JS)
            .replace('__APPJS__', js))
    out = os.path.join(HERE, 'index.html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print('wrote', out, len(html), 'bytes /', len(items), 'items')


if __name__ == '__main__':
    build()
