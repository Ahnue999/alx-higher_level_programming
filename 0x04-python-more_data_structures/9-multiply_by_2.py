#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    newdict = {}
    keys = list(a_dictionary.keys())
    for key in keys:
        newdict[key] = a_dictionary[key] * 2

    return (newdict)
