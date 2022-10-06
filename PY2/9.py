
import collections

s = "an apple is not a tomato"
print(collections.Counter(s.lower().replace(" ", "")).most_common(1))