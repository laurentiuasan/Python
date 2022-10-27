"""
Write a function that receives a string as a parameter
and returns a dictionary in which the keys are the characters in the character string
and the values are the number of occurrences of that character in the given text.
Example: For string "Ana has apples." given as a parameter the function will return the dictionary:
{'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1} .
"""


def string_to_dictionary(s):
    split_string = [ch for ch in s]
    occurances = [s.count(i) for i in split_string]
    dictionary = dict(zip(split_string, occurances))

    return dictionary


if __name__ == '__main__':
    print(string_to_dictionary("Ana has apples."))


