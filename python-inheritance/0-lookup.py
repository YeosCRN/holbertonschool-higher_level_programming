#!/usr/bin/python3
"""Zero"""


def lookup(obj):
    """
        lookup - Return a list with object's attributes and method
        Arguments:
            obj - Object to bild the list with
        Return:
            made list.
    """
    return dir(obj)
