#!/usr/bin/python3
def remove_char_at(str, n):
	li = list(str)
	li.pop(n)
	return("".join(li))
