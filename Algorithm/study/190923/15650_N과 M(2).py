import sys
sys.stdin = open('15650.txt', 'r')

def hing(k, j):
    global ans

    if k == m:
        for i in range(m):
            # if ans[i] > ans[i+1]:
            #     continue
            # print(ans[i], end=' ')
            print(ans[i], end=' ')
        print()

    else:
        for i in range(j, n):
            if visited[i] == 1:
                continue
            visited[i] = 1
            ans.append(i+1)
            hing(k+1, i)
            visited[i] = 0
            ans.pop()



n, m = list(map(int, input().split()))

visited = [0] * n
ans = []

hing(0, 0)