#!/usr/bin/python3
for c in range(97, 123):
    if c == ord("e") or c == ord("q"):
        continue
    print("{:c}".format(c), end="")
