#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    new = set()
    for num in set_1:
        if num in set_2:
            continue
        new.add(num)
    for num in set_2:
        if num in set_1:
            continue
        new.add(num)

    return (new)
