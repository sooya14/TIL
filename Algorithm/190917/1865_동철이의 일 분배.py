import sys
sys.stdin = open('1865.txt', 'r')


# T = int(input())
#
# for tc in range(T):
#     n = int(input())
#     dch = [list(map(int, input().split())) for _ in range(n)]


def grid_ans():
    global ans
    val = 1
    chk = [0] * N
    for i in range(N):
        tmaxi = 0
        for j in range(N):
            if not chk[j] and tmaxi < mat[i][j]:
                tmaxi = j
        chk[tmaxi] = 1
        val *= mat[i][tmaxi]

    ans = val


def solve(k, val):
    global ans
    global cnt
    cnt += 1
    if k == N:
        if val > ans:
            ans = val
    else:
        for i in range(k, N):
            perm[k], perm[i] = perm[i], perm[k]
            if val * mat[k][perm[k]] > ans:
                solve(k + 1, val * mat[k][perm[k]])
            perm[k], perm[i] = perm[i], perm[k]


for tc in range(1, int(input()) + 1):
    N = int(input())

    mat = [0.0] * N
    for i in range(N):
        mat[i] = list(map(lambda x: int(x) / 100, input().split()))

    cnt = 0
    ans = 0
    perm = [x for x in range(N)]

    grid_ans()

    solve(0, 1)
    print("#%d %.6f" % (tc, ans * 100))