"""
Write a function that, for a text given as a parameter, censures words that begin and end with vowels.
 Censorship means replacing characters from odd positions with *.
"""
import re


def censor_it(a_text):
    a_text = a_text.group(0)
    return "".join(a_text[i] if i % 2 == 0 else "*" for i in range(len(a_text)))


def f(text):
    return re.sub(r"^(a|e|i|o|u)\w+(a|e|i|o|u)|(a|e|i|o|u)\w+(a|e|i|o|u)\s", censor_it, text)


if __name__ == '__main__':
    input_text = "alimonada asta este buna, ada a1b2c3d4e"
    print(f(input_text))