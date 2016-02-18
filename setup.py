# Version 0.2.4 - Update Lexer to new IPython location

from setuptools import setup, find_packages

version = '0.2.4'

setup(name='pygments-ipython-console',
      version=version,
      description='Syntax coloring for IPython Console (Same as Sphinx)',
      long_description=open('README.rst').read() + '\n' +
                       open('CHANGES.rst').read(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Plugins',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
      keywords='pygments ipython conf lexer',
      author='Matthew McKay',
      author_email='mamckay@gmail.com',
      url='',
      license='BSD',
      py_modules=['lexer'],
      zip_safe=True,
      install_requires=[
          'setuptools',
      ],
      entry_points={
          'pygments.lexers': 'ipython=lexer:IPythonLexer',
      },
)
