#!/usr/bin/python3
def uppercase(str):
    string = ""
    for letter in str:
        if ord(letter) <= 122 and ord(letter) >= 97:
            string += chr(ord(letter) - 32)
        else:
            string += letter
    print("{}".format(string))
