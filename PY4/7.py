"""
Write a function that receives a variable number of sets and returns a dictionary with the following operations
from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b",
where a and b are two sets, and op is the applied operator: |, &, -.
"""


def do_this(set1, set2, operation):
    if operation == "|":
        return str(set1) + " | " + str(set2), set2 | set1
    if operation == "&":
        return str(set1) + " & " + str(set2), set2 & set1
    if operation == "-":
        return str(set1) + " - " + str(set2), set1 - set2
    if operation == "/":
        return str(set2) + " / " + str(set1), set2 - set1


def f(*sets):
    keys, values = [], []
    for operation in "|&-/":
        for i in range(len(sets) - 1):
            for j in range(i + 1, len(sets)):
                for pair in [(sets[i], sets[j])]:
                    for key, value in [do_this(pair[0], pair[1], operation)]:
                        keys.append(key)
                        values.append(value)

    return dict(zip(keys, values))


if __name__ == '__main__':
    set1 = {1, 2}
    set2 = {2, 3}
    print(f(set1, set2))
