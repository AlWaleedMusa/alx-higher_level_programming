#!/usr/bin/python3

def roman_to_int(roman_string):

    if not roman_string or type(roman_string) != str:
        return 0

    simps = [x for x in roman_string]
    num = 0
    for simp in simps:
        if simp == "I":
            num += 1
        elif simp == "V":
            num += 5
        elif simp == "X":
            num += 10
        elif simp == "L":
            num += 50
        elif simp == "C":
            num += 100
        elif simp == "D":
            num += 500
        elif simp == "M":
            num += 1000

    return num
