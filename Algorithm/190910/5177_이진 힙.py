import sys
sys.stdin = open ('5177.txt', 'r')

def heap(i):
    if i < 0:
        return
    if tree[i // 2] > tree[i]:
        tree[i // 2], tree[i] = tree[i], tree[i // 2]
        heap(i // 2)


T = int(input())
for tc in range(T):
    n = int(input())
    data = [0] + list(map(int, input().split()))

    tree = [0 for _ in range(n+1)]

    cnt = 0
    print(data, tree)
    for i in range(n+1):
        tree[i] = data[i]
        heap(i)


    # heap(n)


    ind = []
    while n != 1:
        ind.append(n // 2)
        n //= 2

    result = 0
    for i in range(len(ind)):
        result += tree[ind[i]]


    print('#{} {}' .format(tc+1, result))

    print(tc+1, data, tree, ind, result)

