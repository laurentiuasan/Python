"""
Using functions, anonymous functions, list comprehensions and filter,
 implement three methods to generate a list with all the vowels in a given string.

For the string "Programming in Python is fun" the list returned will be ['o', 'a', 'i', 'i', 'o', 'i', 'u'].
"""
import re


def f(string):
    return [ch for ch in string if ch in 'aeiou']


if __name__ == '__main__':
    example = "Programming in Python is fun"
    # Function
    print(f(example))

    # Anonymous function
    anon_f = lambda string: [ch for ch in string if ch in 'aeiou']
    print(anon_f(example))

    # List comprehensions & filter
    a_list = filter(anon_f, [x for x in example])
    print(list(a_list))

    another_way = re.findall('[aeiou]', example)
    print(another_way)