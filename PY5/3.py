"""
Să se scrie o funcție ce primește ca parametru un string my_path.

Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului.
Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count),
sortată descrescător după count, unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere cu acea
extensie. Lista se obține din toate fișierele (recursiv) din directorul dat ca parametru.
"""
import os


def f(my_path):
    extensions = []
    ans = []
    if os.path.isdir(my_path):
        for root, directories, files in os.walk(my_path):
            for file in files:
                file_name, file_extension = os.path.splitext(file)
                if file_extension != '':
                    extensions.append(file_extension)
        unique_extensions = set(extensions)
        for ext in unique_extensions:
            ans.append((ext, extensions.count(ext)))
        return ans

    elif os.path.isfile(my_path):
        fd = open(my_path, 'r').read()
        for i in range(len(fd) - 20, len(fd)):
            ans.append(fd[i])
        return ans


if __name__ == '__main__':
    print(f("C:\\Users\\laula\\Desktop\\Python\\PY5\\ex2_output.txt"))