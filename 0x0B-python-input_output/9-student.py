#!/usr/bin/python3
""" a student """


class Student:
    """ student class """

    def __init__(self, first_name, last_name, age):
        """ init """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ dictionary representaion """

        data = {}

        if hasattr(self, "__dict__"):
            data = self.__dict__.copy()

        return data
