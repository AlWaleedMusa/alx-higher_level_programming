#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    length = len(sys.argv)
    sum_num = 0
    for i in range(1, length):
        sum_num += int(sys.argv[i])
    print(sum_num)
