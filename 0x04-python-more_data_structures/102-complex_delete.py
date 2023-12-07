#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())

    for key in keys:
        if value == a_dictionary[key]:
            a_dictionary.pop(key)

    return a_dictionary
