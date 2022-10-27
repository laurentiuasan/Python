"""
Write a function that receives as a parameter a variable number of lists and a whole number x.
Return a list containing the items that appear exactly x times in the incoming lists.

Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2
lists [1,2,3 ]
(1 is in list 1, 4) , (2 is in list 1, 2), (3 is in lists 1, 2)
"""


def appearances(x, *lists):
    ans = []
    containing = []
    unique_numbers = []

    for lista in lists:
        for number in lista:
            containing.append(number)

    for n in containing:
        if n not in unique_numbers:
            unique_numbers.append(n)

    for i in unique_numbers:
        if containing.count(i) == x:
            ans.append(i)

    return ans


if __name__ == '__main__':
    print(appearances(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))
