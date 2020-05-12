#!/usr/bin/env python

from setuptools import setup

setup(
    name='singer-cloud',
    version='0.0.1',
    classifiers=['Programming Language :: Python :: 3 :: Only'],
    py_modules=['singer_cloud'],
    install_requires=[
        'click==7.1.2',
        'PyYAML==5.3.1'
    ],
    entry_points='''
      [console_scripts]
      singer-cloud=singer_cloud:main
    ''',
    packages=['singer_cloud']
)
