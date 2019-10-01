import sys
sys.stdin = open('2805.txt', 'r')

T = int(input())

for tc in range(T):
    n = int(input())

    farm = [list(map(int, input())) for _ in range(n)]

    p = n // 2

    for i in range(p):
        for j in range(p-i):
            farm[i][j] = 0
            farm[i][-j-1] = 0

    for i in range(1, p+1):
        for j in range(i):
            farm[p+i][j] = 0
            farm[p+i][-j-1] = 0

    result = sum(sum(farm, []))


    print('#{} {}' .format(tc+1, result))