#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

string = str(number)
last_digit = int(string[-1])

if last_digit > 5:
    print(f"Last digit of {number:d} is {last_digit:d} and is greater than 5")
elif last_digit < 6 and last_digit > 0:
    print(f"Last digit of {number:d} is {last_digit:d} and is less than 6 and not 0")
elif last_digit < 6 and last < 0:
    n_digit = last_digit * -1
    printf(f"Last digit of {number:d} is {n_digit:d} and is less than 6 and not 0")
elif last_digit == 0:
    print(f"Last digit of {number:d} is {last_digit:d} and is 0")
