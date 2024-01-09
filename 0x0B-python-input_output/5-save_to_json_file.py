#!/usr/bin/python3
""" loads a json """


import json


def save_to_json_file(my_obj, filename):
    """ loads a json """

    with open(filename, "w", encoding="utf-8") as fp:
        json.dump(my_obj, fp)
