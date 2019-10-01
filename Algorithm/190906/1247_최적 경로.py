import sys
sys.stdin = open('1247.txt', 'r')


T = int(input())

for tc in range(T):
    n = int(input())

    arr = list(map(int, input().split()))

    node = []
    for i in range(0, len(arr), 2):
        node.append([arr[i], arr[i+1]])

    C = node[0]
    H = node[1]

    print(tc+1, node)