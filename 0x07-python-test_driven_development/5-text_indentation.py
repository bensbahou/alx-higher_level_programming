#!/usr/bin/python3
"""
The 5-text_indentation module contains a single function called
text_indentation. This function takes a single string argument, text,
and prints the text with 2 new lines after each of these characters:
".", "?", and ":".
"""


def text_indentation(text):
    """splits a text into lines along "?", ":", "." followed by 2 new lines"""

    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for a in text:
        if flag == 0 and a != " ":
            flag = 1
        if flag == 1:
            if a in ".?:":
                print(a, end="\n\n")
                flag = 0
            else:
                print(a, end="")
