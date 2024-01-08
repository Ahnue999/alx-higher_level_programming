#!/usr/bin/python3
""" square from rectangle """


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ square from rectangle """

    def __init__(self, size):
        """ init me """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
