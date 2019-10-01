import sys
sys.stdin = open('문제3.txt', 'r')

T = int(input())

for tc in range(T):
    n = int(input())

    sums = [list(map(int, input().split())) for _ in range(n)]

    dx = [-1, 1, 0, 0]  # 상 하 좌 우
    dy = [0, 0, -1, 1]

    for i in range(len(sums)):
        for j in range(len(sum[i])):
            for d in range(len(dx)):
                if i == 0 or i == n -1:
                if sums[i + d][i + y] > 0:



            sum[i][j]

    print(tc+1, sums)


