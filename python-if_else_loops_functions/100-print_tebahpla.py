#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 != 0:
        n = i - 32
    else:
        n = i
    print("{}" .format(chr(n)), end="")
