"""
Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director.

Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din directorul dat ca parametru.

Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’
"""

import os


def f(dir):
    ans = []
    for root, directories, files in os.walk(dir):
        for file in files:
            file_name, file_extensions = os.path.splitext(file)
            if file_extensions != '':
                ans.append(file_extensions)
    return ans


if __name__ == '__main__':
    print(f("C:\\Users\\laula\\Desktop\\Python"))