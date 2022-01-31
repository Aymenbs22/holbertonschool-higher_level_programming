#!/usr/bin/python3
"""define is_kind_of_clas"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance"""
    if (isinstance(obj, a_class)):
        return (True)
    else:
        return (False)
