#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is not None:
        x = len(sentence)
        if x == 0:
            return(x, None)
        y = ord(sentence[:1])
        z = (x, chr(y))
    return z
