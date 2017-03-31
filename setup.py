#!/usr/bin/env python3



try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'stager',
    version = '0.0.1',
    description = 'the perfect Gentoo installer',
    url = 'https://github.com/gentoo/stager',
    author = 'Matthew Marchese',
    author_email = 'maffblaster@gentoo.org',
    license = 'To be determined...',
    keywords = 'gentoo installer development',
    packages = ['stager'],
    install_requires = [''],
    py_modules=['stager'],
)
