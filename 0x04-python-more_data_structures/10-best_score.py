#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is not None:

        keys = list(a_dictionary.keys())
        max = a_dictionary[keys[0]]
        maxkey = keys[0] 
        for key in keys:
            if max < a_dictionary[key]:
                max = a_dictionary[key]
                maxkey = key
        return maxkey

    return None
