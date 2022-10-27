"""
Write a function that receives as a parameter a list and returns a tuple (a, b),
a representing the number of unique elements in the list,
and b representing the number of duplicate elements in the list (use sets to achieve this objective).
"""


def f(a_list):
    return len(set(a_list)), len(a_list) - len(set(a_list))


if __name__ == '__main__':
    print(f([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 3, 5, 2, 7, 1]))