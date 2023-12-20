#!/usr/bin/python3
"A module for a class that defines a square"


class Square:
    "a square class"
    def __init__(self, size=0, position=(0, 0)):
        "initialaize a square"
        self.__size = size
        self.__position = position

        @property
        def size(self):
            """get size"""
            return (self.__size)

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        @property
        def position(self):
            """get position"""
            return (self.__position)

        @position.setter
        def position(self, value):
            if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
                raise TypeError("position must be a \
                        tuple of 2 positive integers")
            self.__position = value

    def area(self):
        """A method that returns the area of a square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints a square"""

        if self.__size == 0:
            print()
            return

        for i in range(0, self.__position[1]):
            print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()

    def __str__(self):
        """ for print() """

        ret = []
        for i in range(0, self.__position[1]):
            ret.append('\n')
        for i in range(self.__size):
            for k in range(self.__position[0]):
                ret.append(' ')
            for j in range(self.__size):
                ret.append('#')
            if i < self.__size - 1:
                ret.append('\n')
        return "".join(ret)
