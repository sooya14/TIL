import sys
sys.stdin = open('15650.txt', 'r')

def hing(k, j):
    global ans

    if k == m:
        for i in range(m):
            print(ans[i], end=' ')
        print()

    else:
        for i in range(j, n):
            if visited[i] == 1:
                continue
            ans.append(i+1)
            hing(k+1, i)
            ans.pop()

n, m = list(map(int, input().split()))

visited = [0] * n
ans = []

hing(0, 0)