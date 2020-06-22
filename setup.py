#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for FireHole

You can install FireHole with

python setup.py install
"""
from setuptools import setup
from os import path

DIR = path.dirname(path.abspath(__file__))

DESCRIPTION = "FireHole (fh) is a Python package for Data Analyst."

AUTHORS = 'Xia Tian'

URL = 'https://github.com/xSumner/firehole'

EMAIL = 'xsumner@hotmail.com'

with open(path.join(DIR, 'requirements.txt')) as f:
    INSTALL_PACKAGES = f.read().splitlines()

with open(path.join(DIR, 'README.md'), encoding='UTF-8') as f:
    README = f.read()


VERSION = "0.4.0"

packages = ["firehole",
            "firehole.algorithms",
            "firehole.algorithms.ahp",
            "firehole.algorithms.ahp.hierarchy",
            "firehole.algorithms.ahp.methods",
            "firehole.algorithms.flashtext",
            "firehole.algorithms.similarity"]

# add the tests
package_data = {
    "firehole": ['tests/*.py'],
    "firehole.firehole": ['tests/*.py']
    }


setup(
    name='firehole',
    packages=packages,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type='text/markdown',
    install_requires=INSTALL_PACKAGES,
    version=VERSION,
    url=URL,
    author=AUTHORS,
    author_email=EMAIL,
    keywords=['Data Analysis', 'AHP'],
    tests_require=['pytest'],
    package_data=package_data,
    include_package_data=True,
    python_requires='>=3'
)
