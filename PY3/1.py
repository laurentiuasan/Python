"""
Write a function to return a list of the first n numbers in the Fibonacci string.
"""
import sys


def fib(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        lista = fib(n - 1)
        lista.append((lista[-1] + lista[-2]))
        return lista


if __name__ == '__main__':
    a = int(input("a= "))
    print(sys.getrecursionlimit())
    print(fib(a))
