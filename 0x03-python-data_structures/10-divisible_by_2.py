#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    length = len(my_list)
    if length <= 0:
        return None
    new = []
    for i in range(length):
        if my_list[i] % 2 == 0:
            new.append(True)
        else:
            new.append(False)

    return new
