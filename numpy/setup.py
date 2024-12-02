'''
    setup.py file for spammodule.c

    Calling
    $python setup.py build_ext --inplace
    will build the extension library in the current file.

    Calling
    $python setup.py build
    will build a file that looks like ./build/lib*, where
    lib* is a file that begins with lib. The library will
    be in this file and end with a C library extension,
    such as .so

    Calling
    $python setup.py install
    will install the module in your site-packages file.

    See the setuptools section 'Building Extension Modules'
    at setuptools.pypa.io for more information.
'''

from setuptools import setup, Extension
import numpy as np

module1 = Extension('spam', sources=['spammodule.c'])

setup(name='spam', version='1.0', ext_modules=[module1])