#!/usr/bin/python3
""" loads a json """


import json


def load_from_json_file(filename):
    """ loads a json """

    with open(filename, "r", encoding="utf-8") as fp:
        return json.load(fp)
