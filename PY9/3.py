"""
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


if __name__ == '__main__':
    text = "Wrong do poi45*nt avo*id by f;ruit34 learn or in de7ath. So 546passage however! " \
           "besides invited comfo;rt elderly be me."
    regex_list = [r"[0-5]+", r"[a-m]+", r"[;,.!?]+"]
    print(a_function(text, regex_list))