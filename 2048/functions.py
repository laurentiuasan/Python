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




