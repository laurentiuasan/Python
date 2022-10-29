"""
Să se scrie o funcție care primește ca argumente două șiruri de caractere,
target și to_search și returneaza o listă de fișiere care conțin to_search. Fișierele se vor căuta astfel:
 dacă target este un fișier, se caută doar in fișierul respectiv iar dacă este un director se va căuta recursiv in
  toate fișierele din acel director. Dacă target nu este nici fișier, nici director,
   se va arunca o excepție de tipul ValueError cu un mesaj corespunzator.
"""
import os


def f(target, to_search):
    ans = []
    try:
        if os.path.isfile(target):
            data = open(target, 'r').read()
            if to_search in data:
                return [os.path.abspath(target)]

        elif os.path.isdir(target):
            for root, directories, files in os.walk(target):
                for file in files:
                    if to_search in open(os.path.join(root, file), 'r').read():
                        ans.append(os.path.abspath(os.path.join(root, file)))
            return ans
        else:
            raise

    except Exception as e:
        print("This is not a file nor directory\n")
        print(e)


if __name__ == '__main__':
    print(f("C:\\Users\\laula\\Desktop\\Python\\PY5\\examples", "an"))