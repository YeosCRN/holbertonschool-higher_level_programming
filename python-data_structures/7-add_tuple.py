#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = []
    for x, y in zip(tuple_a, tuple_b):
        result.append(x + y)
    result.extend(tuple_a[len(result):] or tuple_b[len(result):])
    return tuple(result)
