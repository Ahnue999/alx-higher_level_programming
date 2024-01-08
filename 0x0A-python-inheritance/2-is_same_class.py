#!/usr/bin/python3
""" Checks if an obj is an instance of a specified class """


def is_same_class(obj, a_class):
    """ Checks an obj """

    return True if type(obj) == a_class else False

