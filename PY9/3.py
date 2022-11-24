""" OLD
Write a function that receives as a parameter a string of text characters and a list of regular expressions
and returns a list of strings that match on at least one regular expression given as a parameter.
"""
import re


def a_function(text, list_of_regex):
    match_list = []
    for reg in list_of_regex:
        temp = re.findall(reg, text)
        for i in temp:
            if i not in match_list:
                match_list.append(i)
    return match_list


""" NEW
3. Write a function that receives two parameters: a list of strings and a list of regular expressions. The function 
will return a list of the strings that match on at least one regular expression from the list given as parameter.
"""


def f(list_strings, list_regex):
    match_list = []
    for string in list_strings:
        for reg in list_regex:
            temp = re.findall(reg, string)
            for i in temp:
                if i not in match_list:
                    match_list.append(i)
    return match_list


if __name__ == '__main__':
    text = "Wrong do poi45*nt avo*id by f;ruit34 learn or in de7ath. So 546passage however! " \
           "besides invited comfo;rt elderly be me."
    list_strings = ["Wrong", "do", "poi45*nt", "avo*id", "by f;ruit34", "learn or in de7ath."]

    regex_list = [r"[0-5]+", r"[a-d]+", r"[;,.!?]+"]
    print(a_function(text, regex_list))     # OLD
    print(f(list_strings, regex_list))      # NEW
