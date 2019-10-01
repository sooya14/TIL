import sys
sys.stdin = open('2819.txt', 'r')

T = int(input())

for tc in range(T):
    pan = [list(map(int, input().split())) for _ in range(4)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 0]

    queue = []

    for i in range(4):
        for j in range(4):
            for n in range(4):
                x = j + dx[n]
                y = i + dy[n]



    print(tc+1, pan)