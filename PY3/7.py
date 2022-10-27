"""
Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
The first element of the tuple will be the number of palindrome numbers found in the list
and the second element will be the greatest palindrome number.
"""


def is_palindrome(x):
    temp = x
    rev = 0
    while x > 0:
        rev = rev * 10 + x % 10
        x = int(x / 10)

    if rev == temp:
        return True
    else:
        return False


def palindroms(numbers):
    count = 0
    max_palindrome = 0

    for i in numbers:
        if is_palindrome(i):
            count += 1
            if i > max_palindrome:
                max_palindrome = i

    return count, max_palindrome


if __name__ == '__main__':
    n = [15, 10, 121, 11511, 21, 11, 22, 34]
    print(palindroms(n))
