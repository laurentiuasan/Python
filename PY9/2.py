"""
Write a function that receives as a parameter a regex string, a text string and a whole number x,
and returns those long-length x substrings that match the regular expression.
"""
import re


def do_the_thing(regex_str, text_str, x):
    return [i for i in re.findall(regex_str, text_str) if len(i) == x]


if __name__ == '__main__':
    my_regex = r"\d+"
    text = "S0 11   y a1sd3 _32_ .4 sdds aswhrwhkj214hk46jka"
    x = 2
    print(do_the_thing(my_regex, text, x))
