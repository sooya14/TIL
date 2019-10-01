import sys
sys.stdin = open('1861.txt', 'r')

T = int(input())
for tc in range(T):
    n = int(input())

    rooms = [list(map(int, input().split())) for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    ans = [1, 0]

    for i in range(n):
        for j in range(n):
            visited = [[0] * (n) for _ in range(n)]

            start = rooms[i][j]
            cnt = 1
            stack = []
            stack.append([i, j])
            visited[i][j] = 1

            while stack:
                a = stack[-1][0]
                b = stack[-1][1]
                point = rooms[a][b]
                stack.pop()

                for x in range(4):
                    xx = a + dx[x]
                    yy = b + dy[x]
                    if 0 <= xx < n and 0 <= yy < n and visited[xx][yy] == 0:
                        if abs(point - rooms[xx][yy]) == 1:
                            stack.append([xx, yy])
                            visited[xx][yy] = 1
                            cnt += 1

            if ans[1] < cnt:
                ans[0] = start
                ans[1] = cnt
            elif ans[1] == cnt:
                if ans[0] < start:
                    ans[0] = start
                    ans[1] = cnt
            break


    print(ans)