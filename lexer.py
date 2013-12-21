"""Pygments lexer for IPython Console Files
"""

from IPython.sphinxext.ipython_console_highlighting import IPythonConsoleLexer
#Update IPythonConsole Lexer to recognise filenames *.ipy
IPythonConsoleLexer.filenames = ['*.ipy']







