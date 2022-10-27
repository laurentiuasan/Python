"""
 Write a function that receives a variable number of lists and returns a list of tuples as follows:
 the first element from tuple contains the first items in the lists,
 the second element contains the items on the position 2 in the lists, etc.
 Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")].
Note: If input lists do not have the same number of items,
    missing items will be replaced with None to be able to generate max ([len(x) for x in input_lists]) tuples.
"""


def f(*lists):
    ans = []
    max_index = 0

    for i in range(len(lists)):
        if len(lists[i]) > max_index:
            max_index = len(lists[i])

    for i in range(len(lists)):
        if len(lists[i]) != max_index:
            while len(lists[i]) < max_index:
                lists[i].append(None)
        sublist = [index[i] for index in lists]
        ans.append(tuple(sublist))


    print(ans)


if __name__ == '__main__':
    f([1, 2, 3], [5, 6, 7], ["a", "b"])
