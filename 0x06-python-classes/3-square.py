#!/usr/bin/python3
"A module for a class that defines a square"


class Square:
    "a square class"
    def __init__(self, size=0):
        "initialaize a square"
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """A method that returns the are of a square"""
        return (self.__size ** 2)
