# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('src','src')],#存放资源的位置
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='BTD6多功能脚本免费版',#文件名字
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,#打包的时候是否进行压缩
    upx_exclude=[],
    runtime_tmpdir=".\Temp",#临时目录的路径
    # runtime_tmpdir=None,
    console=True,#制定可执行程序执行时显示控制台窗口
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],#exe的图标
)