text = 'a pattern matching algorothm'
pattern = 'rithm'

# Brute Force
t = len(text)
p = len(pattern)

i = 0
j = 0

while i < t and j < p:
    if text[i] != pattern[j]:
        i = i -j
        j = -1
    i = i + 1
    j = j + 1

if j == p:
    print i - p
else:
    print -1

