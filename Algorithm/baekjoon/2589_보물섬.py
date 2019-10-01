import sys
sys.stdin = open('2589.txt', 'r')

def find(i, j):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited =[]
    time = []
    queue = []

    queue.append([i, j])

    while queue:
        t = queue.pop(0)

        for z in range(4):
            x = t[0] + dx[z]
            y = t[1] + dy[z]
            cnt = 0
            if 0 <= x < g and 0 <= y < s and not [x, y] in visited:
                if mapp[x][y] == 'L':
                    cnt += 1
                    visited.append([x, y])
            time.append(cnt)

    return min(time)



s, g = list(map(int, input().split()))

mapp = [list(input()) for _ in range(s)]


result = []

for i in range(g):
    for j in range(s):
        if mapp[i][j] == 'L':
            result.append(find(i, j))


print(s, g, result)