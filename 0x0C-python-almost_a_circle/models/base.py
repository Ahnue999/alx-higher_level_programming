#!/usr/bin/python3
""" base class """


class Base:
    """ base class """

    __nb_objects = 0
    def __init__(self, id=None):
        """ init """
        if id is not None:
            self.id = id
        else:
            __nb_objets += 1
            self.id = __nb_objects
