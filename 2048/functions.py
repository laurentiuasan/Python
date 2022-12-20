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


def check_state(matrix):
    check_win = np.where(matrix, matrix == 2048)
    if check_win != 0:
        return 1    # 1 representing win
    print(check_win)

    check_over = np.all(matrix)     # case for matrix full


def move(matrix, direction):
    new_matrix = np.zeros((4, 4), dtype=int)
    if direction == "up":
        for j in range(0, e.SIZE):
            temp = 0
            for i in range(0, e.SIZE):
                if matrix[i][j] != 0:
                    new_matrix[temp][j] = matrix[i][j]
                    temp += 1
    return new_matrix, True


def restart():
    matrix = init_game()
    return matrix, True


