import random

import numpy
import numpy as np
import enums as e
import mainframe


def init_game():
    """
    Function used to initialise the game with random number of values of 2
    :return: numpy array
    """
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


def move_up(matrix):
    new_matrix = np.zeros((4, 4), dtype=int)
    for j in range(e.SIZE):
        x, y = j, 0
        for i in range(e.SIZE):
            if matrix[j][i] != 0:
                new_matrix[x][y] = matrix[j][i]
                y += 1
    return new_matrix


