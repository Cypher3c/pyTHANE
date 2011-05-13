from distutils.core import setup
import py2exe


options = {
    'py2exe': {
        'dll_excludes': [
            'MSVCP90.dll'
         ],
        "packages": ["lxml", "gzip"]
     }
}


setup(windows=['src/asset_gui.py'], options=options)

