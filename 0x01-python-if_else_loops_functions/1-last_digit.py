#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
minus = False

print("Last digit of {:d}".format(number), end=" ")

if number < 0:
    minus = True
    number = number * -1

l = number % 10
if minus:
    l = l * -1


if l > 5:
    print("and is greater than 5")
elif l == 0:
    print("and is 0")
elif l < 6:
        print("and is less than 6 and not 0")
