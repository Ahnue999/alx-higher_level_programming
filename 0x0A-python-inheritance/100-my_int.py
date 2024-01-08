#!/usr/bin/python3
""" My int """


class MyInt(int):
    """ MyInt class """

    def __eq__(self, other):
        """ equality """
        return int(self) != other

    def __ne__(self, other):
        """ equality """
        return int(self) == other
