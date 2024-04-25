#!/usr/bin/python3
"""Find a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Find a peak in a list"""
    if not list_of_integers:
        return None

    num = len(list_of_integers)

    if num == 1:
        return list_of_integers[0]
    if num == 2:
        return max(list_of_integers)
    if list_of_integers[num // 2] < list_of_integers[num // 2 - 1]:
        return find_peak(list_of_integers[: num // 2])

    if list_of_integers[num // 2] < list_of_integers[num // 2 + 1]:
        return find_peak(list_of_integers[num // 2 + 1 :])

    return list_of_integers[num // 2]
