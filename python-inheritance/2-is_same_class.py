#!/usr/bin/python3
"""Second"""


def is_same_class(obj, a_class):
    if type(obj).__name__ == a_class.__name__:
        return True
    return False
