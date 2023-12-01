#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = len(sys.argv) - 1

    if args == 1:
        print("{:d} argument".format(args), end="")
        print("{:d}: {:s}".format(args, sys.argv[args]))
    else:
        print("{:d} arguments".format(args), end="")
        if args == 0:
            print(".")
        else:
            print(":")
            for i in range(1, args + 1):
               print("{:d}: {:s}".format(i, sys.argv[i]))
