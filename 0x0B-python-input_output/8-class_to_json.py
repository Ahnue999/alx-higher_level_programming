#!/usr/bin/python3
""" class to json """


def class_to_json(obj):
    """ class to json """

    data = {}

    if hasattr(obj, "__dict__"):
        data = obj.__dict__.copy()

    return data
