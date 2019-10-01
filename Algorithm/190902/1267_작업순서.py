import sys
sys.stdin = open ('1267_작업순서.txt', 'r')

for tc in range(10):
    v, e = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    node = []

    for i in range(0, len(arr), 2):
        node.append([arr[i], arr[i+1]])

    work = [[0] * (v+1) for _ in range(v+1)]

    for i in range(len(node)):
        work[node[i][0]][node[i][1]] += 1

    cnt = [0] * (v+1)

    for i in range(v+1):
        for j in range(v+1):
            if work[i][j] == 1:
                cnt[j] += 1

    queue = []
    visited = [0] * (v+1)
    front = -1
    rear = -1

    for i in range(1, v+1):
        if cnt[i] == 0:
            queue.append(i)
            rear += 1
            visited[i] = 1
    while front != rear:
        front += 1
        x = queue[front]
        for n in range(v+1):
            if work[x][n] == 1:
                cnt[n] -= 1
            if cnt[n] == 0 and visited[n] == 0 and work[x][n] ==1:
                queue.append(n)
                rear += 1
                visited[n] = 1
                cnt[n] -= 1

    print('#{} {}' .format(tc+1, ' '.join(map(str, queue))))













