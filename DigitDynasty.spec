# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/Users/liaud/2212/group21/mainMenu.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/liaud/2212/group21/ArithmeticEmperor.py', '.'), ('C:/Users/liaud/2212/group21/Button.py', '.'), ('C:/Users/liaud/2212/group21/CookingGame.py', '.'), ('C:/Users/liaud/2212/group21/data.csv', '.'), ('C:/Users/liaud/2212/group21/GameMap.py', '.'), ('C:/Users/liaud/2212/group21/Player.py', '.'), ('C:/Users/liaud/2212/group21/Question.py', '.'), ('C:/Users/liaud/2212/group21/RunningArmy.py', '.'), ('C:/Users/liaud/2212/group21/SandwichStack.py', '.'), ('C:/Users/liaud/2212/group21/SnakeSums.py', '.'), ('C:/Users/liaud/2212/group21/fonts', 'fonts/'), ('C:/Users/liaud/2212/group21/images', 'images/'), ('C:/Users/liaud/2212/group21/sound', 'sound/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='DigitDynasty',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\liaud\\Downloads\\dd_logo.ico'],
)
