#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

from setuptools import find_packages, setup

if 'register' in sys.argv or 'upload' in sys.argv:
    raise Exception("I don't want to be on PyPI!")

curdir = os.path.dirname(os.path.abspath(__file__))

setup(
    name = 'oldchap',
    description = 'Static blog engine',
    license = 'gpl',
    version = '0.1',
    author = 'Òscar Vilaplana',
    author_email = 'hi@oscarvilaplana.cat',
    url = '',
    install_requires = ['opster', 'docutils', 'pytest'],
    packages=find_packages(curdir),
    entry_points = {'console_scripts': ['oldchap=oldchap.tool:main',
                                       ]},
    )
    
