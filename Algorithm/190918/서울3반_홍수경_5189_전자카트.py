import sys
sys.stdin = open('5189.txt', 'r')


def cart(k, v):
    global mini

    if k == n:
        if v < mini:
            mini = v

    else:
        for i in range(k, n):
            chk[k], chk[i] = chk[i], chk[k]
            if v + arr[k][chk[k]] < mini:
                cart(k + 1, v + arr[k][chk[k]])
            chk[k], chk[i] = chk[i], chk[k]



T = int(input())

for tc in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    chk = [i for i in range(n)]
    mini = 999

    cart(0, 0)

    print(n , arr, mini)
