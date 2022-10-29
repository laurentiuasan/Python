"""
Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument
la linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.

Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’, iar ‘fisier’ nu are extensie, deci nu va apărea în lista finală.
"""
import os


def f(path):
    ans = set()
    for root, directories, files in os.walk(path):
        for file in files:
            file_name, file_extension = os.path.splitext(file)
            if file_extension != '':
                ans.add(file_extension)
        break

    return sorted(ans)


if __name__ == '__main__':
    print(f("C:\\Users\\laula\\Desktop\\Python\\PY5"))