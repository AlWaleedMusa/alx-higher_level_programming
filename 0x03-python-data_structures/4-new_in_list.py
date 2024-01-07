#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0:
        cpy = my_list[:]
        return (cpy)
    if idx > len(my_list) - 1:
        cpy = my_list[:]
        return (cpy)

    new = my_list[:]
    new[idx] = element
    return (new)
