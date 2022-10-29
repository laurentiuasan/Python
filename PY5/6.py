"""
Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior,
cu diferența că primește un parametru în plus: o funcție callback, care primește un parametru, iar pentru fiecare
eroare apărută în procesarea fișierelor, se va apela funcția respectivă cu instanța excepției ca parametru.
"""
import os


def callback(exception):
    print(exception)


def f(target, to_search, callback):
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

    except Exception as e:
        callback(e)


if __name__ == '__main__':
    print(f("C:\\Users\\laula\\Desktop\\Python\\PY5\\asds", "an", callback))