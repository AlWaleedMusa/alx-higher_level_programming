#!/usr/bin/python3

def best_score(a_dictionary):
    max_v = 0
    key = ""
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v < max_v:
                continue
            else:
                max_v = v
                key = k
    else:
        return None
    return (key)
