#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

string = str(number)
last_digit = string[-1]

if int(last_digit) > 5:
    print(f"Last digit of {string} is {last_digit} and is greater than 5")
elif int(last_digit) < 6 and int(last_digit) != 0:
    if int(last_digit) < 0:
        nlast_digit = int(last_digit) * -1
        print(f"Last digit of {string} is {nlast_digit} and is less than 6 and not 0")
    else:
        print(f"Last digit of {string} is {last_digit} and is less than 6 and not 0")
elif int(last_digit) == 0:
    print(f"Last digit of {string} is {last_digit} and is 0")
