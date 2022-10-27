"""
Write a function that receives as parameter a matrix and will return the matrix
obtained by replacing all the elements under the main diagonal with 0 (zero).
"""


def under_diagonal(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i > j:
                m[i][j] = 0

    return m


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(under_diagonal(matrix))
