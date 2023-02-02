#!/usr/bin/python3
def no_c(my_string):
    str2 = ""
    for i in range(len(my_string)):
        x = ord(my_string[i])
        if x == 99 or x == 67:
            pass
        else:
            str2 += my_string[i]
    return str2
