
''' my fnct
import math


def is_prime(x):
    prime = True
    if x <= 1:
        prime = False
    else:
        for i in range(2, int(math.sqrt(x/2))+1):
            if x % i == 0:
                prime = False
    return prime


if __name__ == '__main__':
    print(is_prime(int(input())))
'''


## Program facut la clasa
def is_prime(numar):
    """"""
    if numar < 2:
        return False
    if numar == 2:
        return True
    if numar % 2 == 0:
        return False
    max = numar ** 0.5 + 1  # adica sqrt ( numar )
    i = 3
    while i < max:
        if numar % i == 0:
            return False
        i = i + 2
    return True


n = int(input("Numarul:"))
print(is_prime(n))

