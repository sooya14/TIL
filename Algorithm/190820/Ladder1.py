import sys
sys.stdin = open ('Ladder1.txt', 'r')


for tc in range(10):
    T = int(input())
    ladders = [list(map(int, input().split())) for _ in range(100)]

    # 2의 위치
    for i in range(100):
        if ladders[-1][i] == 2:
            a = i

    x = 0
    y = 0
    dx = [0, 0, -1]  # 좌 우 상
    dy = [-1, 1, 0]
    xx = len(ladders) -2

    visitied = []

    while xx != 0:
        for j in range(len(dx)):
            x = xx + dx[j]
            y = a + dy[j]
            if 0 <= x < len(ladders) and 0 <= y < len(ladders):
                if [x, y] not in visitied:
                    if ladders[x][y] == 1:
                        visitied.append([x, y])
                        xx = x
                        a = y

    print('#{} {}'.format(T, a))
#############################################################

    # n = 1
    # result = a
    # visited = []
    # while n < 98:
    #
    #     # 좌
    #     if 0 <= result - 1 <= 99:
    #         if ladders[-1 -n][result - 1] == 1:
    #             if not [-1-n, result-1] not in visited:
    #                 ladders[-1 - n][result - 1] == 0
    #                 visited.append([-1-n, result-1])
    #                 result -= 1
    #
    #     # 우
    #     if 0 <= result + 1 <= 99:
    #         if ladders[-1 -n][result + 1] == 1:
    #             if [-1-n, result +1] not in visited:
    #                 ladders[-1 - n][result + 1] == 0
    #                 visited.append([-1-n, result+1])
    #                 result += 1
    #
    #     # 위
    #     if ladders[-1 - n][result] == 1:
    #         if  [-1-n, result] not in visited:
    #             ladders[-1 - n][result] == 0
    #             visited.append([-1-n, result])
    #             n += 1


    # print('#{} {}' .format(T, result))