# -*- mode: python ; coding: utf-8 -*-
import sys
from pathlib import Path

block_cipher = None

# アプリケーションのルートディレクトリを取得 (Get the root directory of the application)
ROOT_DIR = Path().absolute()

# Adjusted relative paths to include necessary files
add_datas = [
    (str(ROOT_DIR / 'enties' / '*'), 'enties'),
    (str(ROOT_DIR / 'mapper' / '*'), 'mapper'),
    (str(ROOT_DIR / 'logs' / '*'), 'logs'),
    (str(ROOT_DIR / 'manager' / '*'), 'manager'),
    (str(ROOT_DIR / 'util' / '*'), 'util'),
    (str(ROOT_DIR / 'frame_gui.py'), '.'),
    (str(ROOT_DIR / 'run_app.py'), '.'),
]

a = Analysis(
    ['run_app.py'],
    pathex=[str(ROOT_DIR)],  # Make sure the path is correctly set
    binaries=[],
    datas=add_datas,
    hiddenimports=['psycopg2', 'python-dotenv','schedule', 'pandas', 'sqlalchemy', 'numpy', 'logging.config'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive= False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main_app',  # The name of the executable
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=str(ROOT_DIR / 'temp'), 
    console=False,  # Set to True for a console-based application
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
