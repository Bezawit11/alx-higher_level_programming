#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for s in text:
        if s == '.' or s == '?' or s == '!':
            print(s)
        else:
            print(s, end="")
