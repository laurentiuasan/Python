"""
Write a function that extracts the words from a given text as a parameter.
A word is defined as a sequence of alpha-numeric characters.
"""
import re


def extract_words(text):
    return re.findall(r"[a-zA-Z0-9]+", text)


if __name__ == '__main__':
    a_text = "Bla bla 23 asd sdqe sdad asd lorem ipsum 2asd 34r_     sad  233      '' asd ''"
    print(extract_words(a_text))