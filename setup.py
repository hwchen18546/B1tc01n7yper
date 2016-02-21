from distutils.core import setup 
import py2exe 

setup(
    windows = [
        {
            "script": "ObB!tc01n7yper.py",
            "icon_resources": [(1, "img\logo.ico")]
        }
    ],
)