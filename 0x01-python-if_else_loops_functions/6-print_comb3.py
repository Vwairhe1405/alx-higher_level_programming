#!/usr/bin/python3
for i in range (0, 99):
    if (i % 10 > i / 10):
        if (i == 1):
            print("{:02d}".format(i), end="")
        else:
            print(", {:02d}".format(i), end="")
            print()
