"""
Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers)
and a start position (integer). The function will return the song composed by going though the musical notes beginning
with the start position and following the moves given as parameter.
Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"]
"""


def compose(notes, moves, start):
    ans = [notes[start]]
    pos = start

    for i in range(len(moves)):
        pos = (pos + moves[i]) % len(notes)
        ans.append(notes[pos])

    return ans


if __name__ == '__main__':
    n = ["do", "re", "mi", "fa", "sol"]
    m = [1, -3, 4, 2]
    s = 2
    print(compose(n, m, s))
