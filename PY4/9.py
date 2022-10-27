"""
 Write a function that receives a variable number of positional arguments and a variable number of keyword arguments
 and will return the number of positional arguments whose values can be found among keyword arguments values.

Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return return 3
"""


def my_f(*positions, **args):
    count = 0
    for p in positions:
        if p in args.values():
            count += 1
    return count


if __name__ == '__main__':
    print(my_f(1, 2, 3, 4, x=1, y=2, z=3, w=5))