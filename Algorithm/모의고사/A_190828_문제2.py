import sys
sys.stdin = open('190828_문제2.txt', 'r')



T = int(input())

for tc in range(T):
    n = int(input())
    onejas = [list(map(int, input().split())) for _ in range(n)]

    stack = onejas[:]

    check = []

    while len(stack) != 0:

        for i in range(n):
            if onejas[i][2] == 0:
                onejas[i][1] += 0.5
            if onejas[i][2] == 1:
                onejas[i][1] -= 0.5
            if onejas[i][2] == 2:
                onejas[i][0] -= 0.5
            if onejas[i][2] == 3:
                onejas[i][0] += 0.5

        x = 0
        k = []
        while x != n-1 :
            for j in range(n-x-1):
                if onejas[x][0] == onejas[x+1 +j][0] and onejas[x][1] == onejas[x +1 +j][1]:
                    check.append(onejas[x])
                    check.append(onejas[x +1 +j])
                    stack.pop(x)
                    stack.pop(x + 1 + j)
                    x += 1
                else:
                    x += 1
                    pass


                k.append(check[x][3])
                k.append(onejas[x+1 +j][3])
                x += 1

                break



    result = sum(k)

    print(tc+1, result)













    print(tc+1, onejas)

