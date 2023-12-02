#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    length = len(my_list)
    if length <= 0:
        return None
    new = []
    for i in range(length):
        if i == idx:
            continue
        new.append(my_list[i])

    return new
