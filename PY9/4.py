"""
Write a function that receives as a parameter the path to an xml document and an attrs dictionary
 and returns those elements that have as attributes all the keys in the dictionary and values the corresponding values.
For example, if attrs={"class": "url", "name": "url-form", "data-id": "item"} the items selected
 will be those tags whose attributes are class="url" si name="url-form" si data-id="item".
"""
import re


def a_function(path, attrs_dic):
    with open(path, "r") as fd:
        data = fd.read()
        search_string = r"(<(\w+)"
        for key, value in attrs_dic.items():
            search_string += r"".join(" {key}=\"{value}\"".format(key=key, value=value))
        search_string = search_string + r">[^</\2>]*</\2>)"
        print(search_string)
        match_list = [x[0] for x in re.findall(search_string, data)]
    return match_list


if __name__ == '__main__':
    attrs = {"class": "url", "name": "url-form", "data-id": "item"}
    print(a_function("example.xml", attrs))
