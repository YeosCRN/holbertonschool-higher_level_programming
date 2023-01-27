#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(len(str)):
        str2 = str
        str2 = str2[0:n] + str2[n + 1:]
    return str2    
    

