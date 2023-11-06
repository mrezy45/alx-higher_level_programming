#!/usr/bin/python3
"""
    module to return the list of available attributes
    and methods of an object
"""


def lookup(obj):
    """function to look out for all attributes and methods of an object"""
    return dir(obj)
