"""
Write a function that receives a variable number of arguments and keyword arguments. The function
returns a list containing only the arguments which are dictionaries,
 containing minimum 2 keys and at least one string key with minimum 3 characters.
"""


def my_f(*args, **kwargs):
    ans = []
    for arg in args:
        at_least_one = False
        if type(arg) == dict:
            if len(arg.keys()) >= 2:
                for key in arg.keys():
                    if type(key) == str and len(key) >= 3:
                        at_least_one = True
            if at_least_one:
                ans.append(arg)

    for arg in kwargs.values():
        at_least_one = False
        if type(arg) == dict:
            if len(arg.keys()) >= 2:
                for key in arg.keys():
                    if type(key) == str and len(key) >= 3:
                        at_least_one = True
            if at_least_one:
                ans.append(arg)
    return ans


# Fancy writing of my_F
def my_other_f(*args, **kwargs):
    return [
               i for i in args if type(i) == dict and max([0] + [len(x) for x in i.keys() if type(x) == str]) >= 3
           ] + [
               j for j in kwargs.values() if
               type(j) == dict and max([0] + [len(y) for y in j.keys() if type(y) == str]) >= 3
           ]


if __name__ == '__main__':
    print(my_other_f({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5}, 3764,
               dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True}))
    
