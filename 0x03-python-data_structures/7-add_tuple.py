#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    t1_length = len(tuple_a)
    t2_length = len(tuple_b)

    if t1_length == 0:
        a1 = 0
        a2 = 0
    elif t1_length == 1:
        a1 = tuple_a[0]
        a2 = 0
    else:
        a1 = tuple_a[0]
        a2 = tuple_a[1]

    if t2_length == 0:
        b1 = 0
        b2 = 0
    elif t2_length == 1:
        b1 = tuple_b[0]
        b2 = 0
    else:
        b1 = tuple_b[0]
        b2 = tuple_b[1]

    new_tup = (a1 + b1, a2 + b2)
    return (new_tup)
