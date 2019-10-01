import sys
sys.stdin = open('1.txt', 'r')

def hing(k):
    global visited, ans
    if k == m:
        for i in ans:
            print(i, end=' ')
        print()

    else:
        for i in range(n):
            if visited[i] == 1:
                continue
            visited[i] = 1
            ans.append(i+1)
            hing(k+1)
            visited[i] = 0
            ans.pop()


n, m = list(map(int, input().split()))
visited = [0] * n
ans = []

hing(0)

