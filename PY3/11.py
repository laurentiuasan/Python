"""
Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple.
Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]
"""


def order_list(l):
    for i in range(1, len(l)):
        if l[i-1][1][2] > l[i][1][2]:
            l[i-1], l[i] = l[i], l[i-1]
    return l


if __name__ == '__main__':
    lista = [('abc', 'bcd'), ('abc', 'zza'), ('ast', 'qwf'), ('try', 'gfe')]
    print(order_list(lista))
