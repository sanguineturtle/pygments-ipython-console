================
pygments-ipython-console
================
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

In Sphinx_ documents the lexer is selected with the ``highlight`` directive::

    .. highlight:: ipython

.. _Pygments: http://pygments.org/
.. _Sphinx: http://sphinx-doc.org/

Installation
============

TBA

