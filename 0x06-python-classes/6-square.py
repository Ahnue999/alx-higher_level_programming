#!/usr/bin/python3
"A module for a class that defines a square"


class Square:
    "a square class"
    def __init__(self, size=0, position=(0,0)):
        "initialaize a square"
        self.__size = size
        self.__position = position

    def __getattr__(self, name):
        """get attributes"""
        return self.__dict__[f"__{name}"]

    def __setattr__(self, name, value):
        """set values"""
        if name == "__size":
            if type(value) == int:
                if value >= 0:
                    self.__size = value
                else:
                    raise ValueError("size must be >= 0")
            else:
                raise TypeError("size must be an integer")
        if name == "__position":
            if type(value) != tuple or (type(value[0]) != int or type(value[1]) != int):
                    raise TypeError("position must be a tuple of 2 positive integers")
        self.__dict__[f"__{name}"] = value

    def area(self):
        """A method that returns the are of a square"""
        return (self.__size ** 2)

    def my_print(self):
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
