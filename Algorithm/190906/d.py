def power(s):
    r = [[]]

    for e in s:
        t = [x+[e] for x in r]
        r += t

    return r