#!/usr/bin/python3
def islower(c):
    token = ord(c)
    for i in range(97, 122):
        if token == i:
            return True
    return False
