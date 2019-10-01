import sys
sys.stdin = open('1865.txt', 'r')

# def first(dch):
#
#     res = 1
#     chk = [0] * n
#
#     for i in range(n):
#         t = 0
#         for j in range(n):
#             if not chk[i]== 1 and t < dch[i][j]:
#                 t = j
#         chk[t] = 1
#         res *= dch[i][j]
#
#     return res

def dongch(k, v):
    global res

    if k == n:
        if v > res:
            res = v

    else:
        for i in range(k, n):
            check[k], check[i] = check[i], check[k]
            if v * dch[k][check[k]] > res:
                dongch(k + 1, v * dch[k][check[k]])
            check[k], check[i] = check[i], check[k]


T = int(input())

for tc in range(T):
    n = int(input())

    data = [list(map(int, input().split())) for _ in range(n)]
    dch = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            dch[i][j] += data[i][j] / 100

    check = [i for i in range(n)]
    res = 0

    dongch(0, 1)

    print('#{} {:.6f}' .format(tc+1, res * 100))