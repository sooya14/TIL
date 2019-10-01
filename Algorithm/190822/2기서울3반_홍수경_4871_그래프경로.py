import sys
sys.stdin = open ('4871_그래프경로.txt', 'r')

T = int(input())

for tc in range(T):
    p, num = list(map(int, input().split()))
    lines = [list(map(int, input().split())) for _ in range(num)]
    find_s, find_f = list(map(int, input().split()))

    check = [[0] * p for _ in range(p)]

    for i in range(len(lines)):
        x = lines[i][0]
        y = lines[i][-1]
        check[x-1][y-1] = 1



    result = 0
    stack = []
    for i in range(len(check[find_s - 1])):
        if check[find_s - 1][i] == 1:
            n = find_s

    stack.append(find_s -1)
    n = find_s


    while n != find_f-1:
        n = stack[-1]
        for i in range(p):

            if check[n][i] == 1:
                stack.append(i)
                if i == find_f-1:
                    result = 1
                    n = i
                    break

                if sum(check[n]) == 0:
                    stack.pop()

            if len(stack) == 0:
                result = 0
                break


    print('#{} {}' .format(tc+1, result))
