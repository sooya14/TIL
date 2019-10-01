import sys
sys.stdin = open ('5178.txt', 'r')

def nodesum(a):
    global tree
    if a == 1:
        return
    elif a % 2:
        tree[a // 2] = tree[a-1] + tree[a]
        nodesum(a-2)
    else:
        tree[a // 2 ] = tree[a]
        nodesum(a-1)


T = int(input())

for tc in range(T):
    n, m, l = list(map(int, input().split()))

    data =  [list(map(int, input().split())) for _ in range(m)]

    tree = [0 for _ in range(n+1)]

    for i in range(m):
        tree[data[i][0]] = data[i][1]

    nodesum(n)

    result = tree[l]


    print('#{} {}' .format(tc+1, result))