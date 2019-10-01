import sys
sys.stdin = open('5102.txt', 'r')

def bfs(node):
    visited = [0] * (v+1)

    queue = []
    queue.append(s)
    visited[s] = 1

    front = -1
    rear = 0

    while front != rear:
        front += 1
        x = queue[front]

        for i in range(1, v+1):
            if node[x][i] == 1 and visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                rear += 1

                if i == g:
                    return len(queue) -1
        else:
            front -=1
            break



T = int(input())

for tc in range(T):
    v, e = list(map(int, input().split()))

    arr = [list(map(int, input().split())) for _ in range(e)]

    s, g = list(map(int, input().split()))

    node = [[0] * (v+1) for _ in range(v+1)]

    for i in range(len(arr)):
        node[arr[i][0]][arr[i][1]] += 1
        node[arr[i][1]][arr[i][0]] += 1

    res = bfs(node)

    cnt = []
    for i in range(len(res)):
        if not res[i] in cnt:
            cnt.append(res[i])

    print('#{} {}' .format(tc+1, len(cnt)))