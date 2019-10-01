import sys
sys.stdin = open('1220_magnetic.txt', 'r')

for tc in range(10):
    num = int(input())
    ns = [list(map(int, input().split())) for _ in range(num)]

    result = 0
    for i in range(100):
        stack = []
        for j in range(100):
            if ns[j][i] == 1:
                stack.append(ns[j][i])
            elif ns[j][i] == 2 and len(stack) != 0:
                stack.pop()
                result += 1
                stack = []

    print('#{} {}' .format(tc+1, result))




