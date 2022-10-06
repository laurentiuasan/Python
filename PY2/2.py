
sentence = input('input string: ').lower()

print(sum([sentence.count(v) for v in "aeiou"]))