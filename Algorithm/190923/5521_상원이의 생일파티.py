import sys
sys.stdin = open('5521.txt', 'r')



T = int(input())
for tc in range(T):
    n, m = list(map(int, input().split()))

    ab = [list(map(int, input().split())) for _ in range(m)]

    friends = [[0] * (n+1) for _ in range(n+1)]

    for i in range(len(ab)):
        friends[ab[i][0]][ab[i][1]] = 1
        friends[ab[i][1]][ab[i][0]] = 1

    visited = [0] * (n+1)
    real = []

    for i in range(len(friends)):
        if friends[1][i] == 1:
            real.append(i)
            visited[i] = 1

    for i in range(len(real)):
        for j in range(len(friends)):
            if friends[real[i]][j] == 1 and visited[j] == 0:
                visited[j] = 1

    result = 0
    if sum(visited) == 0:
        result = 0
    else:
        result = sum(visited) -1


    print('#{} {}' .format(tc+1, result))