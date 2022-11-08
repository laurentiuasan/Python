"""
Write a function with one parameter which represents a list.
The function will return a new list containing all the numbers found in the given list.
"""


def my_function(a_list):
    return [x for x in a_list if type(x) == int or type(x) == float]


if __name__ == '__main__':
    print(my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
