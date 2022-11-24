"""
Write another variant of the function from the previous exercise that returns those elements that
have at least one attribute that corresponds to a key-value pair in the dictionary.
"""
import re


def a_function(path, attrs_dic):
    with open(path, "r") as fd:
        data = fd.read()
        search_string = r"(<(\w+) [^>]*(" + r"|".join(
            [" {key}=\"{value}\"".format(key=key, value=value) for key, value in attrs.items()]
        ) + r")[^>]*>[^(<\2>)]*</\2>)"
        print(search_string)
        match_list = [x[0] for x in re.findall(search_string, data)]
    return match_list


if __name__ == '__main__':
    attrs = {"class": "url", "name": "url-form", "data-id": "item"}
    print(a_function("example.xml", attrs))
