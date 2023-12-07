#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted = list(a_dictionary.keys())
    sorted.sort()
    list(map(lambda key: print(key, ": ", a_dictionary[key], sep=""), sorted))
