import sys
sys.stdin = open('1979.txt', 'r')

T = int(input())

for tc in range(T):
    n, k = list(map(int, input().split()))

    puzzle = [list(map(int, input().split())) for _ in range(n)]

    result = 0

    for i in range(len(puzzle)):
        garo = 0
        for j in range(n):
            if puzzle[i][j] == 1:
                garo += 1
                if j == n-1:
                    if garo == k:
                        result += 1
                        garo = 0

            elif puzzle[i][j] == 0:
                if garo == k:
                    result += 1
                    garo = 0
                else:
                    garo = 0

    for i in range(len(puzzle)):
        sero = 0
        for j in range(n):
            if puzzle[j][i] == 1:
                sero += 1
                if j == n-1:
                    if sero == k:
                        result += 1
                        sero = 0

            elif puzzle[j][i] == 0:
                if sero == k:
                    result += 1
                    sero = 0
                else:
                    sero = 0




    print('#{} {}' .format(tc+1, result))