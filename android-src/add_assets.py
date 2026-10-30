# -*- coding: utf-8 -*-
"""把 classes.dex 与 assets/** 追加进 aapt2 产出的 base.apk。
aapt2 -A 写中文文件名时不会置 UTF-8 标志位，会变成乱码，所以这里用 zipfile 自己写（置 0x800）。"""
import os, sys, zipfile

base, out, dex, assets_root = sys.argv[1:5]

with zipfile.ZipFile(base) as zin, zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as zout:
    for it in zin.infolist():
        data = zin.read(it.filename)
        info = zipfile.ZipInfo(it.filename, date_time=(2024, 1, 1, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        # 文件名本身就是 UTF-8（aapt2 已经这么写），这里补上标志位
        zout.writestr(info, data)
    # classes.dex
    info = zipfile.ZipInfo('classes.dex', date_time=(2024, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    with open(dex, 'rb') as f:
        zout.writestr(info, f.read())
    # assets
    n = 0
    for root, _dirs, files in os.walk(assets_root):
        for fn in sorted(files):
            full = os.path.join(root, fn)
            rel = os.path.relpath(full, assets_root).replace(os.sep, '/')
            arc = 'assets/' + rel
            info = zipfile.ZipInfo(arc, date_time=(2024, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            with open(full, 'rb') as f:
                zout.writestr(info, f.read())
            n += 1
print('packed dex + %d assets' % n)
