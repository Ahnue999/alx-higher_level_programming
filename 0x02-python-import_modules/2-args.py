#!/usr/bin/python3

import sys

length = len(sys.argv)

if length == 1:
    print("{:d} argument".format(length), end="")
    print("{:d}: {:s}".format(1, sys.argv[0]))
else:
    print("{:d} arguments".format(length), end="")
    if length == 0:
        print(".")
    else:
        print(":")
        for i in range(length):
            print("{:d}: {:s}".format(i + 1, sys.argv[i]))
