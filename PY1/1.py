'''
O functie care primeste 3 numere naturale mai mari decat 0. Returneaza TRUE daca numerele sunt laturile unui
triunghi dreptunghic, FALSE in caz contrar
'''


def check_triangle(a, b, c):
    if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
        return True
    else:
        return False


if __name__ == '__main__':
    x = int(input('a = '))
    y = int(input('b = '))
    z = int(input('c = '))
    if x > 0 or y > 0 or z > 0:
        print(check_triangle(x, y, z))
    else:
        print('Wrong input')
