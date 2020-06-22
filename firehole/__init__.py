"""
FireHole
========

    FireHole is a Python package customized for data analysts.

    Website:
    Source: https://github.com/xSumner/firehole
    Bug reports: https://github.com/xSumner/firehole/issues

Using
-----

    Just write in Python

    >>> import firehole as fh
    >>> entropy = fh.Entropy()
    >>> cov = fh.COV()
    >>> ahp = fh.parse()

"""
#   Xia Tian <xsumner@hotmail.com>
#   All rights reserved.
#   Apache License.
#
# Add platform dependent shared library path to sys.path
#

from __future__ import absolute_import

import sys
if sys.version_info[:2] < (3, 5):
    m = "Python 3.5 or later is required for FireHole (%d.%d detected)"
    raise ImportError(m % sys.version_info[:2])
del sys

# These are import orderwise
from firehole.exception import *

import firehole.algorithms
from firehole.algorithms import *

