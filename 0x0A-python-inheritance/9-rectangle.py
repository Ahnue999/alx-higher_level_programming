#!/usr/bin/python3
""" Geometry class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """ init method """
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height

    
    def area(self):
        """ for area """
        return self.__width * self.__height

    def __str__(self):
        """ str representation """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
