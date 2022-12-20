import random

import numpy
import numpy as np
import enums as e
import mainframe


def init_game():
    no_values = random.randint(2, 6)
    matrix = np.zeros((e.SIZE, e.SIZE), dtype=int)
    for i in range(no_values):
        temp_x = random.randint(0, e.SIZE - 1)
        temp_y = random.randint(0, e.SIZE - 1)
        matrix[temp_x][temp_y] = 2

    return matrix


def reverse(matrix):
    return np.fliplr(matrix)


def transpose(matrix):
    return np.transpose(matrix)


def compress(matrix):
    new_matrix = np.zeros((4, 4), dtype=int)
    for i in range(e.SIZE):
        position = 0
        for j in range(e.SIZE):
            if matrix[i][j] != 0:
                new_matrix[i][position] = matrix[i][j]
                position += 1
    return new_matrix


def combine(matrix):
    for i in range(e.SIZE):
        for j in range(e.SIZE - 1):
            if matrix[i][j] != 0:
                if matrix[i][j] == matrix[i][j + 1]:
                    matrix[i][j] *= 2
                    matrix[i][j + 1] = 0
    return matrix


def move(matrix, command):

    if command == "up":
        matrix = transpose(matrix)
        print(matrix)

        matrix = compress(matrix)
        print(matrix)
        matrix = combine(matrix)
        print(matrix)
        matrix = compress(matrix)
        print(matrix)

        matrix = transpose(matrix)
        print(matrix)

    elif command == "down":
        matrix = transpose(matrix)
        matrix = reverse(matrix)

        matrix = compress(matrix)
        matrix = combine(matrix)
        matrix = compress(matrix)

        matrix = reverse(matrix)
        matrix = transpose(matrix)

    return matrix



