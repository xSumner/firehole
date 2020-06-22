#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
**********
Exceptions
**********

Base exception and errors for FireHole

"""
__author__ = '''Xia Tian (xsumner@hotmail.com)'''


# the root of all Exceptions
class FireHoleException(Exception):
    """Base class for exceptions in FireHole"""


class FireHoleAlgorithmError(FireHoleException):
    """Exception for unexpected termination of algorithms."""


class FireHoleUnfeasible(FireHoleAlgorithmError):
    """Exception raised by algorithm trying to solve a problem
    instance that has no feasible solution"""


class FireHoleNotArray(FireHoleAlgorithmError):
    """Exception raised by introducing data which is not a numpy
    n-dimension array"""
    def __init__(self, arg_name, data_type):
        self.name = arg_name
        self.type = str(data_type)

    def __str__(self):
        print("{} is {}, not a numpy array.".format(self.name, self.type))
