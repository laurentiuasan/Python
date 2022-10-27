"""
 Write a function that receives as parameters two lists a and b and returns:
    (a intersected with b, a reunited with b, a - b, b - a)
"""


def intersection(a, b):
    return [value for value in a if value in b]


def reunion(a, b):
    return a + b


def minus(a, b):
    return [value for value in a if value not in b]


if __name__ == '__main__':
    x = [1, 2, 3, 5, 9]
    y = [4, 5, 7, 8]

    print(intersection(x, y))
    print(reunion(x, y))
    print(minus(x, y))
    print(minus(y, x))
