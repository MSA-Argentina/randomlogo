#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='randomlogo',
    version='0.0.1',
    author='Felipe Lerena',
    description='Random Logo Generator',
    author_email='felipelerena@gmail.com',
    packages=['randomlogo'],
    scripts=[],
    url='http://github.com/MSA-Argentina/randomlogo',
    license='LICENSE.txt',
    long_description=open('README.rst').read(),
    install_requires=['jinja2',
                      'pillow'],
    entry_points={
        'console_scripts': ['randomlogo = randomlogo.__init__:main']
    },
    package_data={
        'randomlogo': ['templates/*'],
    }
)
