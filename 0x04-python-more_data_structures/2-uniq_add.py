#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    sum_num = 0
    for num in uniq_list:
        sum_num += num
    return sum_num
