import sys
sys.stdin = open('15650.txt', 'r')

def hing(k):
    global ans
    if k == m:
        for i in range(len(ans)):
            print(ans[i], end=' ')
        print()

    else:
        for i in range(n):
            ans.append(i+1)
            hing(k+1)
            ans.pop()

n, m = list(map(int, input().split()))

ans = []

hing(0)