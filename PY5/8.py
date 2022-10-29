"""
Să se scrie o funcție ce primește un parametru cu numele dir_path.
Acest parametru reprezintă calea către un director aflat pe disc.
Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina directorului dir_path.

Exemplu apel funcție: functie("C:\\director") va returna ["C:\\director\\fisier1.txt", "C:\\director\\fisier2.txt"]

Calea "C:\\director" are pe disc următoarea structură:
C:\\director\\fisier1.txt <- fișier
C:\\director\\fisier2.txt <- fișier
C:\\director\\director1 <- director
C:\\director\\director2 <- director
"""
import os


def f(dir_path):
    ans = []
    for root, directories, files in os.walk(dir_path):
        for file in files:
            ans.append(os.path.abspath(os.path.join(root, file)))
        break
    return ans


if __name__ == '__main__':
    print(f("C:\\Users\\laula\\Desktop\\Python\\PY5\\"))