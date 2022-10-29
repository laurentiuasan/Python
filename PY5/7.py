"""
Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către un fișer si
returnează un dicționar cu următoarele cămpuri: full_path = calea absoluta catre fisier,
file_size = dimensiunea fisierului in octeti, file_extension = extensia fisierului (daca are) sau "",
can_read, can_write = True/False daca se poate citi din/scrie in fisier.
"""
import os


def f(path):
    keys = ['full_path', 'file_size', 'file_extension', 'can_read', 'can_write']
    values = []
    if os.path.isfile(path):
        values.append(os.path.abspath(path))
        values.append(os.path.getsize(path))
        values.append(os.path.splitext(path)[1])
        values.append(os.access(path, os.R_OK))
        values.append(os.access(path, os.W_OK))

    return dict(zip(keys, values))


if __name__ == '__main__':
    print(f("C:\\Users\\laula\\Desktop\\Python\\PY5\\examples\\abc.txt"))
