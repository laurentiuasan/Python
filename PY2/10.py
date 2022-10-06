
def f(string):
    new_string = string.replace(' ', '_')
    string = string.split()
    if new_string.count('_') > len(string):
        return 0

    return len(string)


print(f("I have Python exam"))
