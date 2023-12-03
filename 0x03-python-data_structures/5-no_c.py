#!/usr/bin/python3

def no_c(my_string):
    length = len(my_string)
    new_str = ""
    for i in range(length):
        if my_string[i] in ["c", "C"]:
            continue
        new_str += my_string[i]

    new = "{:s}".format(new_str)
    return new
