#!/usr/bin/python3
""" Defines inherited class"""


def inherits_from(obj, a_class):
    """claas verify"""
    if issubclass(type(obj), a_class) and (type(obj) != a_class):
        return True
    else:
        return False
