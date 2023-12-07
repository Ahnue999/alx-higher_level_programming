#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return (0)

    up = 0
    down = 0

    for tuple in my_list:
        up += tuple[0] * tuple[1]
        down += tuple[1]

    return (up / down)
