"""
Compare two dictionaries without using the operator "==" returning True or False.
(Attention, dictionaries must be recursively covered because they can contain other containers,
such as dictionaries, lists, sets, etc.)
"""


def compare_dic(d1, d2):
    # Cazul in care d1,d2 dictionare
    if (type(d1) is dict) and (type(d2) is dict):
        if len(d1) > len(d2):
            return 1
        elif len(d1) < len(d2):
            return -1

        for k in d1:
            if k in d2:
                result = compare_dic(d1.get(k), d2.get(k))
                if result == -1:
                    return -1
                elif result == 1:
                    return 1
        return 0

    # Cazul in care di,d2 liste
    if type(d1) is list and type(d2) is list:
        if len(d1) == len(d2):
            for i in d1:
                for j in d2:
                    return compare_dic(i, j)
        elif len(d1) > len(d2):
            return 1
        else:
            return -1

    # Cazul de baza string
    if type(d1) is str and type(d2) is str:
        for ch1 in d1:
            for ch2 in d2:
                if ch1 > ch2:
                    return 1
                elif ch1 == ch2:
                    return 0
                else:
                    return -1
    # Cazul de baza int
    if type(d1) is int and type(d2) is int:
        if d1 > d2:
            return 1
        elif d1 == d2:
            return 0
        else:
            return -1


if __name__ == '__main__':
    a = {'a': [1, 2], 'b': [1, 3], 'c': [5, 4]}
    b = {'a': [1, 2], 'b': [1, 3], 'c': [3, 4]}

    print(compare_dic(a, b))
