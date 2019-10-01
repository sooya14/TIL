import sys
sys.stdin = open('190827.txt', 'r')

T = int(input())

for tc in range(T):
    n, m, k = list(map(int, input().split()))

    color = [list(map(int, input().split())) for _ in range(k)]

    arr = [[0] * m for _ in range(n)]


    for i in range(len(color)):
        x = color[i][3] - color[i][1] + 1
        y = color[i][2] - color[i][0] + 1


        bs = 1
        for yy in range(y):
            for xx in range(x):
                if arr[color[i][0] + yy][color[i][1] + xx] > color[i][4]:
                    bs = 0
                    break

        if bs == 1:
            for yy in range(y):
                for xx in range(x):
                    arr[color[i][0] + yy][color[i][1] + xx] = 0
                    arr[color[i][0] + yy][color[i][1] + xx] += color[i][4]



    result = []
    for c in range(11):
        sum_color = 0
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == c:
                    sum_color += 1

        result.append(sum_color)


    print('#{} {}' .format(tc+1, max(result)))
