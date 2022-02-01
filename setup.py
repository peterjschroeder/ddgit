#!/usr/bin/env python3

from distutils.core import setup

setup(
        name='ddgit', 
        version='0.1', 
        description='DuckDuckGo search TUI', 
        author='Peter J. Schroeder', 
        author_email='peterjschroeder@gmail.com', 
        url='https://github.com/peterjschroeder/ddgit',
        scripts=['ddgit'],
        install_requires=['duckduckgo_search gallery-dl @ git+https://github.com/mikf/gallery-dl.git', 'pyperclip', 'urwid', 'pyxdg', 'youtube-dl']
)

