

def print_spiral_order(matrix):

    ans = []
    seen = [[[0, 0, 0, 0]], [[0, 0, 0, 0]], [[0, 0, 0, 0]], [[0, 0, 0, 0]]]

    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, di = 0, 0, 0

    # Iterate from 0 to R * C - 1
    for i in range((len(matrix) * len(matrix[0][0]))):
        ans.append(matrix[x][0][y])
        seen[x][0][y] = 1
        cr = x + dr[di]
        cc = y + dc[di]
        if 0 <= cr < len(matrix) and 0 <= cc < len(matrix[0][0]) and not(seen[cr][0][cc]):
            x, y = cr, cc
        else:
            di = (di + 1) % 4
            x = x + dr[di]
            y = y + dc[di]

    return ans


# Driver code
if __name__ == "__main__":
    words = [["firs"], ["n_lt"], ["oba_"], ["htyp"]]

    for i in print_spiral_order(words):
        print(i, end="")


