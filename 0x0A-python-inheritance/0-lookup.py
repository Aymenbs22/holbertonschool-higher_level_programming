#!/usr/bin/python3
"""define lookup"""


def lookup(obj):
    """function that returns the list of available attributes"""
    list = obj
    return(dir(list))
