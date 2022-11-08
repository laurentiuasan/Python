"""
1a) Write a module named utils.py that contains one function called process_item.
The function will have one parameter, x, and will return the least prime number greater than x.
When run, the module will request an input from the user, convert it to a number
and it will display the output of the process_item function.
"""


def is_prime(x):
    if x < 2 or x != 2 and x % 2 == 0 or x != 3 and x % 3 == 0:
        return False
    for i in range(5, int(x**0.5) + 1, 6):
        if x % i == 0 or x % (i + 2) == 0:
            return False
    return True


def process_item(x):
    while not is_prime(x+1):
        x += 1
    return x + 1


if __name__ == '__main__':
    try:
        x = int(input("Insert number x: "))
        print(process_item(x))
    except Exception as e:
        print("Error! ", e)



