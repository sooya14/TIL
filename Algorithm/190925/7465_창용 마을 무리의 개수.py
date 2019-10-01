import sys
sys.stdin = open ('7465.txt', 'r')

T = int(input())
for tc in range(T):
    n, m = list(map(int, input().split()))

    data = [list(map(int, input().split())) for _ in range(m)]

    people = [[0] * (n + 1) for _ in range(n+1)]



    for i in range(m):
        if len(data[i]) == 2:
            people[data[i][0]][data[i][1]] = 1
            people[data[i][1]][data[i][0]] = 1

    visited = [0] * (n + 1)

    cnt = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if people[i][j] == 1 and visited[i] == 0:
                queue = []
                queue.append(i)
                front = -1
                rear = 0
                cnt += 1

                while front != rear:
                    front += 1
                    x = queue[front]
                    for z in range(1, n+1):
                        if people[x][z] == 1 and visited[z] == 0:
                            queue.append(z)
                            rear += 1
                            visited[z] = 1

    for i in range(1, n+1):
        if sum(people[i]) == 0:
            cnt += 1

    print('#{} {}' .format(tc+1, cnt))