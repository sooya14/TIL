import sys
sys.stdin = open('4615.txt', 'r')

T = int(input())

for tc in range(T):
    n, m = list(map(int, input().split()))

    pan = [[0] * (n+1) for _ in range(n+1)]

    a = int(n / 2)
    pan[a][a] = 2
    pan[a][a+1] = 1
    pan[a+1][a] = 2
    pan[a+1][a + 1] = 1


    dx = [-1, 1, 0, 0, 1, -1, -1, 1]  # 상하 좌우 /
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    for i in range(m):
        x, y, color = list(map(int, input().split()))
        if color == 1:
            another = 2
        else:
            another = 1

        pan[y][x] = color
        for i in range(8):
            xx = x + dx[i]
            yy =  y + dy[i]
            if xx < 0 or yy < 0 or xx >= n or yy >= n:
                continue
            if pan[yy][xx] == another:
                cnt = 0
                while pan[yy][xx] == another:
                    cnt += 1
                    xx += dx[i]
                    yy += dy[i]
                    if xx < 0 or yy < 0 or xx >= n or yy >= n or pan[yy][xx] == 0:
                        cnt = 0
                        break
                xx = x + dx[i]
                yy = y + dy[i]

                while cnt != 0:
                    pan[yy][xx] = color
                    xx += dx[i]
                    yy += dy[i]
                    cnt -= 1

    b = 0
    w = 0
    for i in range(1, n):
        for j in range(1, n):
            if pan[i][j] == 1:
                b += 1
            elif pan[i][j] == 2:
                w += 1

    print('#{} {} {}' .format(tc+1, b, w))