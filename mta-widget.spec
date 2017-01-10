# -*- mode: python -*-

block_cipher = None


a = Analysis(['mta-widget.py'],
             pathex=['/home/dobro/Python-Sandbox/widget'],
             binaries=None,
             datas=[('index.html','text/html')],
             hiddenimports=['gi.repository.WebKit','gi.repository.Gtk','gi.repository.Gdk','gi.repository.GLib','signal'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='mta-widget',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='mta-widget')
