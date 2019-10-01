import sys
sys.stdin = open('IM_개미의 이동거리.txt', 'r')

T = int(input())

def ant(arr):

    # dx = [-1. 1, 0 0]  # 상 하 좌 우
    # dy = [0, 0, -1, 1]

    result =0

    x = 0
    y = 1

    check = 3
    while 0 <= x < len(arr) and 0 <= y < len(arr):

        if arr[x][y] == 0:
            if check == 3:
                y += 1
            elif check == 0:
                x -= 1
            elif check == 1:
                x += 1
            elif check == 2:
                y -= 1

        elif arr[x][y] == 2:
            if check == 0:
                y -= 1
                check = 2
            elif check == 1:
                y += 1
                check = 3
            elif check == 2:
                x -= 1
                check = 0
            elif check == 3:
                x += 1
                check = 1

        elif arr[x][y] == 1:
            if check == 0:
                y += 1
                check = 3
            elif check == 1:
                y -= 1
                check = 2
            elif check == 2:
                x += 1
                check = 1
            elif check == 3:
                x -= 1
                check = 0

        result += 1

    return result



for tc in range(T):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(10)]

    print(tc+1, ant(arr))


########################################################

for tc in range(1, 4):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
​
    x, y = 0, 0
    dx, dy = 0, 1
    cnt = 0
    while 0 <= x + dx < n and 0 <= y + dy < n:
        x += dx
        y += dy
        if arr[x][y] == 1:
            dx, dy = -dy, -dx
        if arr[x][y] == 2:
            dx, dy = dy, dx
        cnt += 1
​
    print('#%d %d' % (tc, cnt))


