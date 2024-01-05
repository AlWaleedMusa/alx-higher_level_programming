#!/usr/bin/python3

def multiple_returns(sentence):

    length = len(sentence)
    if length == 0:
        a = 0
        b = None
        return ((a, b))
    else:
        return ((length, sentence[0]))
