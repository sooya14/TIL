import sys
sys.stdin = open('6109.txt', 'r')


T = int(input())

for tc in range(T):
    ns = list(input().split())

    n = int(ns[0])
    s = ''
    for i in range(1, len(ns)):
        s += ns[i]

    game = [list(map(int, input().split())) for _ in range(n)]
    result = [[0] * n for _ in range(n)]

    if s == 'up':
        for i in range(n):
            stack = []
            for j in range(n):
                if game[j][i] != 0:
                    stack.append(game[j][i])

            z = 0
            while z < len(stack) -1:
                if stack[z] == stack[z + 1]:
                    stack[z] += stack.pop(z+1)
                z += 1
            for w in range(len(stack)):
                result[w][i] = stack[w]




    print(tc+1,  result)