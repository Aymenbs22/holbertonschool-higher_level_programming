#!/usr/bin/python3
"""module create Rectangle class"""


class Rectangle:
    """New Class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        """set width of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        """set height of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):

        if (self.__width == 0 or self.__height == 0):
            return (0)

        return((self.__width + self.__height) * 2)

    def __str__(self):

        """Print rectangle"""
        rect = ("")
        if (self.__width == 0 or self.__height == 0):
            return (rect)

        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    rect += "#"
                if i < self.__height - 1:
                    rect += "\n"
                return (rect)

    def __repr__(self):

        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
