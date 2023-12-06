#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted = a_dictionary.keys()
    list(map(lambda key: print(a_dictionary[key]), sorted))
