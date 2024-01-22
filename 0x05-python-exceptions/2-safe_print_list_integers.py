#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    if my_list is None:
        return 0

    counter = 0
    for i in range(x):
        try:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                counter += 1
        except (ValueError, TypeError):
            pass
    print()
    return counter
