"""
The validate_dict function that receives as a parameter a set of tuples
( that represents validation rules for a dictionary that has strings as keys and values) and a dictionary.
A rule is defined as follows: (key, "prefix", "middle", "suffix").
A value is considered valid if it starts with "prefix", "middle" is inside the value (not at the beginning or end)
and ends with "suffix". The function will return True if the given dictionary matches all the rules, False otherwise.

Example: the rules  s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
and d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} => False
because although the rules are respected for "key1" and "key2" "key3" that does not appear in the rules.
"""


def validate_dit(tuples_set, a_dict):
    for rule in tuples_set:
        value = a_dict.get(rule[0])
        if value is None:
            return False
        if not value.startswith(rule[1]) or not value.endswith(rule[3]) \
                or not rule[2] in value or value.startswith(rule[2]) or value.endswith(rule[2]):
            return False
    return True


if __name__ == '__main__':
    d = dict({"key1": "come inside, it's too cold out", "key3": "this is not valid"})
    s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
    print(validate_dit(s, d))
