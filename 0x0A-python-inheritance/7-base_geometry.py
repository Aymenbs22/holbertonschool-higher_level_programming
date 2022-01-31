#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """area"""
    def area(self):
        raise Exception("area() is not implemented")
        """integer_validator"""
    def integer_validator(self, name, value):
        """integer_validator"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
