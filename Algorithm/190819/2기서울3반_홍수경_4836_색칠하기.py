import sys
sys.stdin = open('4836_색칠하기.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    boxs = [[0] * 10 for _ in range(10)]
    result = 0
    for _ in range(n):
        x1, y1, x2, y2, color = map(int, input().split())
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if boxs[x][y] == 0:
                    boxs[x][y] = color
                elif boxs[x][y] == 1 and color == 2:
                    result += 1
                elif boxs[x][y] == 2 and color == 1:
                    result += 1

    print('#{} {}' .format(tc, result))

