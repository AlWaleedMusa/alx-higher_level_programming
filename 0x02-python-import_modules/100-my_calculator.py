#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys

    cal_list = ["+", "-", "*", "/"]
    length = len(sys.argv)

    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        exit(1)

    if argv[2] not in cal_list:
        print("Unknown operator. Available operators: +, -, * and /\n")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == "+":
        print("{} {} {} = {}".format(a, argv[2], b, add(a, b)))
    elif argv[2] == "-":
        print("{} {} {} = {}".foramt(a, argv[2], b, sub(a, b)))
    elif argv[2] == "*":
        print("{} {} {} = {}".format(a, argv[2], b, mul(a, b)))
    elif argv[2] == "/":
        print("{} {} {} = {}".foramt(a, argv[2], b, div(a, b)))