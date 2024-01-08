#!/usr/bin/python3
""" Checks if an obj is an instance of a specified class """


def is_same_class(obj, a_class):
    """ Checks an obj """

    if type(obj) is a_class:
        return True
    return False

