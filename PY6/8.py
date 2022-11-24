"""
a) Write a function called print_arguments with one parameter named function.
The function will return one new function which prints the arguments and the keyword arguments received
and will return the output of the function receives as a parameter.
"""


def multiply_by_two(x):
    return x * 2


def print_arguments(function):
    def another_f(f):
        print(globals())
        return f
    return another_f(function)


if __name__ == '__main__':
    aug_multiplied_by_two = print_arguments(multiply_by_two)
    x = aug_multiplied_by_two(10)
