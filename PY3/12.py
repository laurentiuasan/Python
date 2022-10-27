"""
Write a function that will receive a list of words as parameter and
will return a list of lists of words, grouped by rhyme.
Two words rhyme if both of them end with the same 2 letters.
Example:
group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte'])
will return [['ana', 'banana'], ['carte', 'parte'], ['arme']]
"""


def group_by_rhyme(words):
    rhymes = []
    sublist = []
    found_rhyme = [0 for i in range(len(words))]

    for i in range(len(words)):
        sublist.append(words[i])
        for j in range(i + 1, len(words)):
            if found_rhyme[i] == 0 and found_rhyme[j] == 0:
                if words[i][-2] == words[j][-2]:
                    sublist.append(words[j])
                    found_rhyme[i] = 1
                    found_rhyme[j] = 1
        if len(sublist) == 1 and found_rhyme[i] == 0:
            found_rhyme[i] = 1
            rhymes.append(sublist[:])
        elif len(sublist) > 1:
            rhymes.append(sublist[:])
        sublist.clear()

    return rhymes


if __name__ == '__main__':
    print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))