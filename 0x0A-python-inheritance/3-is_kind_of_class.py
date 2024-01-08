#!/usr/bin/python3
""" returns true if the same class or superclass """


def is_kind_of_class(obj, a_class):
    """ returns true if the same class or superclass """

    return True if isinstance(obj, a_class) else False
