#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    if my_list == None:
        return 0

    counter = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            counter += 1
        print()
    except IndexError:
        print()
        pass
    return counter
