"""
Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
"""


def is_prime(x):
    if x < 2 or x != 2 and x % 2 == 0 or x != 3 and x % 3 == 0:
        return False
    for d in range(5, 1 + int(x ** 0.5), 6):
        if x % d == 0 or x % (d + 2) == 0:
            return False
    return True


def check_primes(lista):
    only_primes = []
    for number in lista:
        if is_prime(number):
            only_primes.append(number)

    return only_primes


if __name__ == '__main__':
    numere = [0, -1, 23, 1435, 1239897, 29, 6, 81, 589, 301, 43, 101]
    print(check_primes(numere))
