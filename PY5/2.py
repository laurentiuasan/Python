"""
Să se scrie o funcție ce primește ca argumente două căi: director si fișier.

Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie,
calea absolută a fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A.
"""
import os


def f(dir, fisier):
    write_file = open(fisier, mode='w')
    for root, directories, files in os.walk(dir):
        for file in files:
            if file.startswith('A'):    # la test nu am fisiere care incep cu 'A'
                write_file.write(file)
                write_file.write("\n")


if __name__ == '__main__':
    f("C:\\Users\\laula\\Desktop\\Python", "C:\\Users\\laula\\Desktop\\Python\\PY5\\ex2_output.txt")
