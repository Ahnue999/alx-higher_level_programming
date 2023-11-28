#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if 97 <= ord(str[i]) <= 122:
            i = ord(str[i]) - 32
        else:
            i = ord(str[i])
        print("{:c}".format(i), end="")
    else:
        print()
