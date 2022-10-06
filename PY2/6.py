
def is_palindrome(x):
    temp = x
    rev = 0
    while x > 0:
        rev = rev * 10 + x % 10
        x = int(x / 10)

    if rev == temp:
        print("It is palindrome")
    else:
        print("It is NOT palindrome")


is_palindrome(1234321)
