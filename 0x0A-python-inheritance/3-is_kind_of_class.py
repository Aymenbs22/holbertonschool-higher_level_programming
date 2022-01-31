#!/usr/bin/python3
"""define is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    if type(obj) is a_class:
        return (True)
    else:
        return (False)
