#!/usr/bin/python3
def remove_char_at(str, n):
    if len(str) < n:
        return (str)

    li = list(str)
    li.pop(n)
    return ("".join(li))
