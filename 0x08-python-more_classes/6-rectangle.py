#!/usr/bin/python3
""" class rectangle
"""


class Rectangle:
    """ class rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and heigth"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ width
        """
        return self.__width

    @property
    def height(self):
        """height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ width  setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height  setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """are of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter of the rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """prints the rectangle"""

        if self.__width is 0 or self.__height is 0:
            return ""

        for i in range(self.__height):
            [print("#", end="") for j in range(self.__width)]
            if i < self.__height - 1:
                print()
        return ("")

    def __repr__(self):
        """repr"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """del"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
