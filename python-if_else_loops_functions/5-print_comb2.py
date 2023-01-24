#!/usr/bin/python3
for i in range(0, 99 + 1):
    if i < 10:
        print("0{}, " .format(i), end="")
    elif i >= 10 and i < 99:
        print("{}, " .format(i), end="")
    else:
        print(f"{i}")
