"""
Write a function that receives as parameter a matrix which represents the heights of the spectators in a stadium
and will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game.
A spectator can't see the game if there is at least one taller spectator standing in front of him.
All the seats are occupied. All the seats are at the same level.
Row and column indexing starts from 0, beginning with the closest row from the field.
Example:
# FIELD
[[1, 2, 3, 2, 1, 1],
[2, 4, 4, 3, 7, 2],
[5, 5, 2, 5, 6, 4],
[6, 6, 7, 6, 7, 5]]
Will return : [(2, 2), (3, 4), (2, 4)]
"""


def check_vision(m):
    can_see = [[0 for col in range(len(m[0]))] for row in range(len(m))]

    for x in range(len(m[0])):
        can_see[0][x] = 1

    for i in range(1, len(m)):
        for j in range(len(m[0])):
            if can_see[i-1][j] == 1:    # parcurg matricea si intreb daca cineva e mai scund pe randul anterior
                if m[i][j] > m[i-1][j]:
                    can_see[i][j] = 1
                else:
                    can_see[i][j] = 0
            else:
                greater = True
                for k in range(0, j):   # chiar daca cel din fata nu vede, poate vede cel din spate
                    if m[i][j] <= m[i][k]:
                        greater = False
                if greater:
                    can_see[i][j] = 1
                else:
                    can_see[i][j] = 0

    ans = []
    for i in range(len(can_see)):
        for j in range(len(can_see[0])):
            if can_see[i][j] == 0:
                ans.append((i, j))

    return ans


if __name__ == '__main__':
    matrix = [[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]]
    print(check_vision(matrix))
