# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
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
a.datas += [
            ('bg.png', 'assets/img/background/bg.png', 'DATA'), 
            ('bullet0.png', 'assets/img/bullet/bullet0.png', 'DATA'),
            ('bullet1.png', 'assets/img/bullet/bullet1.png', 'DATA'),
            ('enemy0.png', 'assets/img/enemy/enemy0.png', 'DATA'),
            ('enemy1.png', 'assets/img/enemy/enemy1.png', 'DATA'),
            ('enemy2.png', 'assets/img/enemy/enemy2.png', 'DATA'),
            ('enemy3.png', 'assets/img/enemy/enemy3.png', 'DATA'),
            ('enemy4.png', 'assets/img/enemy/enemy4.png', 'DATA'),
            ('explosion0.png', 'assets/img/explosion/explosion0.png', 'DATA'),
            ('explosion1.png', 'assets/img/explosion/explosion1.png', 'DATA'),
            ('explosion2.png', 'assets/img/explosion/explosion2.png', 'DATA'),
            ('explosion3.png', 'assets/img/explosion/explosion3.png', 'DATA'),
            ('explosion4.png', 'assets/img/explosion/explosion4.png', 'DATA'),
            ('player0.png', 'assets/img/player/player0.png', 'DATA'),
            ('player1.png', 'assets/img/player/player1.png', 'DATA'),
            ('player2.png', 'assets/img/player/player2.png', 'DATA'),
            ('bgm.mp3', 'assets/sound/bgm.mp3', 'DATA'),
            ('explosion.mp3', 'assets/sound/explosion.mp3', 'DATA'),
            ('shot.mp3', 'assets/sound/shot.mp3', 'DATA')
            ]
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Shooting Game v1.0.0',
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
    icon='favicon.ico'
)
