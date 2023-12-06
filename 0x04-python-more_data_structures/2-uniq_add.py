#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    uniq = []
    for i in range(len(my_list)):
        if i in uniq:
            continue
        else:
            sum += i
            uniq.append(i)
    return sum
