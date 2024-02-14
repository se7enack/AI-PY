"""
This build.py script is for py2applet to build a binary from python source code (cryptocreeper.py)

Usage:
    python3 build.py py2app
"""

from setuptools import setup

APP = ['cryptocreeper.py']
DATA_FILES = []
OPTIONS = {
    'iconfile':'icon.ico'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
