#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    length = len(my_list)
    if length <= 0:
        return None
    if idx > length - 1 or idx < 0:
        return my_list

    new = []
    for i in range(length):
        if i == idx:
            continue
        new.append(my_list[i])

    my_list[:] = new

    return my_list
