#!/usr/bin/python3
""" A class that inherits from the list class """


class MyList(list):
    """ inherits from list"""

    def print_sorted(self):
        """ prints the sorted list """
        print(sorted(self))
