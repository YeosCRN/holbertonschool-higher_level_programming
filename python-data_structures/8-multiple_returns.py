#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    y = ord(sentence[:1])
    z = (x, chr(y))
    return z
