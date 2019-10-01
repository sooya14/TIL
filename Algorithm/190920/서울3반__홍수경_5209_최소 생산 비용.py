import sys
sys.stdin = open('5209.txt', 'r')

def produce(k, result):
    global mini, n, factory

    if k == n:
        if mini > result:
            mini = result

    else:
        for i in range(n):
            if visited[i] == 1:
                continue
            visited[i] = 1
            if result+factory[k][i] < mini:
                produce(k + 1, result + factory[k][i])
            visited[i] = 0


T = int(input())
for tc in range(T):
    n = int(input())

    factory = [list(map(int, input().split())) for _ in range(n)]


    mini = 99999
    visited = [0] * (n)
    produce(0, 0)

    print('#{} {}'.format(tc+1, mini))