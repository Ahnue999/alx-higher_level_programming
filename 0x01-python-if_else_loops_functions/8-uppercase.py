#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if 97 <= ord(str[i]) <= 122:
            c = ord(str[i]) - 32
        else:
            c = ord(str[i])
        print("{:c}".format(c), end="")
    else:
        print()
