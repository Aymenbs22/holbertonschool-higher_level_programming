#!/usr/bin/python3
"""module create class"""


class Square:
    """New Class"""

    def __init__(self, size=0):
        """def"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif (size <= 0):
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)