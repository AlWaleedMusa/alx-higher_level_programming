#!/usr/bin/python3
for i in range(0, 10):
    for m in range(1, 10):
        if i >= m:
            continue
        if i == 8 and m == 9:
            print("{}{}".format(i, m))
        else:
            print("{}{}".format(i, m), end=", ")
