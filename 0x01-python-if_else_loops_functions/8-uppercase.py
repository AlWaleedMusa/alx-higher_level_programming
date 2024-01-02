#!/usr/bin/python3
def uppercase(str):
	string = ""
	for letter in str:
		upper = ord(letter) - 32
		string += chr(upper)
	return (string)
