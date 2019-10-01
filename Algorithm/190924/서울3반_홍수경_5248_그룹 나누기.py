import sys
sys.stdin = open('5248.txt', 'r')

T = int(input())

for tc in range(T):
    n, m = list(map(int, input().split()))

    data = list(map(int, input().split()))

    students = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(0, m * 2, 2):
        students[data[i]][data[i + 1]] = 1
        students[data[i + 1]][data[i]] = 1

    visited = [0] * (n + 1)
    cnt = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if students[i][j] == 1 and visited[i] == 0:
                queue = []
                queue.append(i)
                front = -1
                rear = 0
                cnt += 1

                while front != rear:
                    front += 1
                    x = queue[front]
                    for z in range(1, n + 1):
                        if students[x][z] == 1 and visited[z] == 0:
                            queue.append(z)
                            rear += 1
                            visited[z] = 1

    for i in range(1, n + 1):
        if sum(students[i]) == 0:
            cnt += 1

    print('#{} {}' .format(tc+1, cnt))