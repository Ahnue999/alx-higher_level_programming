#!/usr/bin/python3
""" Geometry class """


class BaseGeometry:
    """Base Geometry class"""

    def area(self):
        """ area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """ init method """
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
