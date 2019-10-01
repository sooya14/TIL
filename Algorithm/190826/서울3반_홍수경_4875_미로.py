import sys
sys.stdin = open('4875_미로.txt' , 'r')


def mmm(miro):

    start = []
    for i in range(num):
        for j in range(num):
            if miro[i][j] == 2:
                start.append(i)
                start.append(j)
                break

    dx = [-1, 1, 0, 0]  # 상 하 좌 우
    dy = [0, 0, -1, 1]

    stack = []
    visited = []

    xx = start[0]
    yy = start[1]

    stack.append([xx, yy])

    while len(stack) != 0:
        xx = stack[-1][0]
        yy = stack[-1][1]

        for i in range(len(dx)):
            x = xx + dx[i]
            y = yy + dy[i]

            if 0 <= x < len(miro)  and 0 <= y < len(miro) and [x, y] not in visited:
                if miro[x][y] == 3:
                    return 1
                if miro[x][y] == 0 :
                    stack.append([x, y])
                    visited.append([x, y])
                    break

        else:
            stack.pop()
    return 0


T = int(input())

for tc in range(T):
    num = int(input())
    miro = [list(map(int, input())) for _ in range(num)]

    result = mmm(miro)

    print('#{} {}' .format(tc+1, result))