#!/usr/bin/python3
"A module for a class that defines a square"


class Square:
    "a square class"
    def __init__(self, size=0):
        "initialaize a square"
        self.__size = size

    @property
    def size(self):
        """returns the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size"""
        if type(value) == int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """A method that returns the are of a square"""
        return (self.__size ** 2)

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
