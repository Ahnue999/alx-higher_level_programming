#!/usr/bin/python3
""" returns true if an obj is a subclass of given class """


def inherits_from(obj, a_class):
    """ returns true if an obj is a subclass of given class """

    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
