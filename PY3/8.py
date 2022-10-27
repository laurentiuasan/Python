"""
Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True.
For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag is set
to True, otherwise it should contain characters that have the ASCII code not divisible by x.

 Example:
     x = 2, ["test", "hello", "lab002"], flag = False will return (["e", "s"], ["e" .
     Note: The function must return list of lists.
"""


def f(strings, x=1, flag=True):
    ans = []
    sublist = []
    for string in strings:
        for i in string:
            print(i, ord(i))
            if flag and ord(i) % x == 0:
                sublist.append(i)
            elif not flag and ord(i) % x != 0:
                sublist.append(i)
        ans.append(sublist[:])
        sublist.clear()

    return ans


if __name__ == '__main__':
    print(f(["test", "hello", "lab002"], x=2, flag=False))
