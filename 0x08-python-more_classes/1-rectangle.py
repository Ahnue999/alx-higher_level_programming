#!/usr/bin/python3
"""A simple rectangle"""


class Rectangle:
    """Rectangle"""
    def __init__(self, width=0, height=0):
        """init"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """width
        """
        return slef.__width

    @property
    def height(self):
        """height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """width setter.
        """
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter.
        """
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
