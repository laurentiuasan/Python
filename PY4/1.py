"""
Write a function that receives as parameters two lists a and b and returns a list of sets containing:
(a intersected with b, a reunited with b, a - b, b - a)   
"""


def do_all(a, b):
    intersection = a.intersection(b)
    union = a.union(b)
    a_differenced = a.difference(b)
    b_differenced = b.difference(a)

    return [intersection, union, a_differenced, b_differenced]


if __name__ == '__main__':
    print(do_all({1, 2, 3, 5}, {2, 4, 5, 7}))
