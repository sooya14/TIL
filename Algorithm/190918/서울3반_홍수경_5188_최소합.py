import sys
sys.stdin = open('5188.txt', 'r')


def ehyo(x, y, res):
    global mini

    if x == n-1 and y == n-1:
        mini = res

    else:
        dx = [0, 1]
        dy = [1, 0]
        for i in range(len(dx)):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n:
                if res + data[xx][yy] < mini:
                    ehyo(xx, yy, res + data[xx][yy])



T = int(input())
for tc in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    x = 0
    y = 0
    mini = 99
    res = data[0][0]
    ehyo(x, y, res)

    print('#{} {}' .format(tc+1, mini, ))