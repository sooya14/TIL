import sys
sys.stdin = open('1493.txt', 'r')

def sf(a):
    s = 1
    f = 1
    n = 1
    while not s <= a <= f:
        s += n
        f += n +1
        n += 1

    for i in range(f-s+1):
        if a == s+i:
            x = i+1
            y = f - s + 1 -i
            break

    return [x, y]

def cal(x, y):

    s = 1
    n = 1
    while n != x:
        s += n+1
        n += 1

    r = 0
    while r != y-1:
        s += x + r
        r += 1

    return s


T = int(input())
for tc in range(T):
    a, b = list(map(int, input().split()))

    x = sf(a)[0] + sf(b)[0]
    y = sf(a)[1] + sf(b)[1]

    res = cal(x, y)


    print('#{} {}' .format(tc+1, res))