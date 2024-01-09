#!/usr/bin/python3
""" a student """


class Student:
    """ student class """

    def __init__(self, first_name, last_name, age):
        """ init """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ dictionary representaion """

        data = {}

        if hasattr(self, "__dict__"):
            if isinstance(attrs, list):
                for attr in attrs:
                    if attr in self.__dict__:
                        data[attr] = self.__dict__[attr]
            else:
                data = self.__dict__.copy()

        return data

    def reload_from_json(self, json):
        """ replaces all attributres of student """

        for key, value in json.items():
            self.__dict__[key] = value
