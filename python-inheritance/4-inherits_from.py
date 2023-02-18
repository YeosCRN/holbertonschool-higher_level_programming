#!/usr/bin/python3
"""Fourth"""


def inherits_from(obj, a_class):
    if issubclass(type(obj), a_class):
        if type(obj) is not a_class:
            return True
    return False
