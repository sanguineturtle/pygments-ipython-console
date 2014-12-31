========================
pygments-ipython-console
========================
-----------------------------------------
Syntax coloring for IPython Console Files
-----------------------------------------

Overview
========

This package provides a Pygments_ lexer for IPython Console Files.
The lexer is published as an entry point and, once installed, Pygments will
pick it up automatically.

You can then use the ``ipython`` language with Pygments::

    $ pygmentize -l ipython test.ipy

[Or use the standard sphinx import of ipython_console_highlight.py]
In Sphinx_ documents the lexer is selected with the ``highlight`` directive::

    .. highlight:: ipython

.. _Pygments: http://pygments.org/
.. _Sphinx: http://sphinx-doc.org/

Thanks to pygments-openssl project for providing a template [https://github.com/stefanholek/pygments-openssl]

Requirements
============
This needs IPython 2.0+ for sphinxext module

Installation
============

Use your favorite installer to install pygments-ipython into the same Python you have installed Pygments.
Constructing an egg from repository::

	$ git clone https://github.com/sanguineturtle/pygments-ipython-console.git
	$ cd pygments-ipython-console
	$ python setup.py bdist_egg

For example [change directory to dist/ folder to locate egg file]::

	$ easy_install pygments-ipython-console.egg

To verify the installation run::

	$ pygmentize -L lexer | grep -i ipython
	* ipython:
    	IPython console session (filenames *.ipy)

pygments-ipython-console
========================

IPython Console Installer for Pygments

Notes:
======
This will install IPythonLexer. There are other Lexers in IPython2.0 and can be changed through the simple lexer.py file
