import numpy as np
import enums as e
import time

"""
Era prea haotic codul asa ca am facut functii din unele metode pentru a putea face partea de AI
"""


def calculate_score(matrix):
    best = -1
    for i in range(4):
        current = 0
        for row in range(e.SIZE):
            for col in range(e.SIZE - 1):
                if matrix[row][col] >= matrix[row][col + 1]:
                    current += 1
        for col in range(e.SIZE):
            for row in range(e.SIZE - 1):
                if matrix[row][col] >= matrix[row + 1][col]:
                    current += 1
        if current > best:
            best = current
        matrix = reverse(matrix)
        matrix = transpose(matrix)
    return best


# returns opposite move
def get_opposite_move(direction):
    if direction == "w":
        return "s"
    elif direction == "s":
        return "w"
    elif direction == "a":
        return "d"
    elif direction == "d":
        return "a"


# pulls all the tiles together
def compress(matrix):
    new_matrix = np.zeros((e.SIZE, e.SIZE), dtype=int)
    for i in range(e.SIZE):
        position = 0
        for j in range(e.SIZE):
            if matrix[i][j] != 0:
                new_matrix[i][position] = matrix[i][j]
                position += 1
    return new_matrix


# stacks any 2 adjacent tiles with the same value
def combine(matrix, score):
    for i in range(e.SIZE):
        for j in range(e.SIZE - 1):
            if matrix[i][j] != 0:
                if matrix[i][j] == matrix[i][j + 1]:
                    matrix[i][j] *= 2
                    matrix[i][j + 1] = 0
                    score += matrix[i][j]
    return matrix, score


# reverse the matrix
def reverse(matrix):
    return np.fliplr(matrix)


# transpose
def transpose(matrix):
    return np.transpose(matrix)


# functions used together multiple times
def gather_and_stack(matrix, score):
    matrix = compress(matrix)
    matrix, score = combine(matrix, score)
    matrix = compress(matrix)
    return matrix, score


def move(direction, matrix, score):
    if direction == "w":
        return move_up(matrix, score)
    elif direction == "s":
        return move_down(matrix, score)
    elif direction == "a":
        return move_left(matrix, score)
    elif direction == "d":
        return move_right(matrix, score)


def move_up(matrix, score):
    matrix = transpose(matrix)
    matrix, score = gather_and_stack(matrix, score)
    time.sleep(0.1)
    matrix = transpose(matrix)

    return matrix, score, True


def move_down(matrix, score):
    matrix = transpose(matrix)
    matrix = reverse(matrix)
    matrix, score = gather_and_stack(matrix, score)
    time.sleep(0.1)
    matrix = reverse(matrix)
    matrix = transpose(matrix)

    return matrix, score, True


def move_left(matrix, score):
    matrix, score = gather_and_stack(matrix, score)
    time.sleep(0.1)

    return matrix, score, True


def move_right(matrix, score):
    matrix = reverse(matrix)
    matrix, score = gather_and_stack(matrix, score)
    time.sleep(0.1)
    matrix = reverse(matrix)

    return matrix, score, True
