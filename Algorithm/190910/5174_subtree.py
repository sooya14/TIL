import sys
sys.stdin = open ('5174.txt', 'r')


def find(a):
    global cnt

    if a:
        find(tree[a][0])
        find(tree[a][1])
        cnt += 1

T = int(input())

for tc in range(T):
    e, n = list(map(int, input().split()))
    data = list(map(int, input().split()))

    m = max(data)

    tree = [[0] * 2 for _ in range(m+1)]


    for i in range(len(data) // 2):
        parent, child = data[i * 2], data[i * 2 + 1]
        if not tree[parent][0]:
            tree[parent][0] = child
        else:
            tree[parent][1] = child

    cnt = 0
    find(n)


    print('#{} {}' .format(tc+1, cnt))

