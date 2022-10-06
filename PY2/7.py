import re


def find_numbers(string):
    print(re.findall(r'\d+', string))


text = input('String = ')
find_numbers(text)
