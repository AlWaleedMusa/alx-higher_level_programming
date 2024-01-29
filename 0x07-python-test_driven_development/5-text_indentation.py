#!/usr/bin/python3


def text_indentation(text):
    """
    text_indentation prints text with 2 new lines after . ? or :
        
    Args:
        text (str): text to be formatted
        
    Return:
		Nothing
    """
    temp_string = ""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if len(text) is 0:
        return

    for letter in text:
        temp_string += letter
        if letter in ["?", ":", "."]:
            while temp_string[0] is " ":
                temp_string = temp_string[1:]
            print(temp_string)
            print()
            temp_string = ""

    if len(temp_string) != 0:
        try:
            while temp_string[0] is " ":
                temp_string = temp_string[1:]
        except:
            pass
        print(temp_string, end="")
