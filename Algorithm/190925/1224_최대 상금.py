import sys
sys.stdin = open('1224.txt', 'r')

def cal(k, result):
    global maxi, n, visited, cnt, ind

    if cnt == n:
        if maxi < result:
            maxi = result

    else:
        for i in range(len(pan)):
            if visited[i] == 1:
                continue
            visited[i] = 1
            cnt += 1
            ind[i] = i
            cal(k + 1)
            cnt -= 1
            ind[i] = 0



T = int(input())
for tc in range(T):
    data = list(input().split())

    n = int(data[1])

    pan = [data[0][i] for i in range(len(data[0]))]

    visited = [0] * len(pan)
    ind = [0] * len(pan)
    maxi = 0
    cnt = 0
    cal(0)

    print(n, pan)