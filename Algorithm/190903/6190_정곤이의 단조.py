import sys
sys.stdin = open('6190_정곤이의 단조.txt', 'r')

from collections import deque

def danjo(numbers):

    mult = []
    for i in range(n):
        for j in range(i, n):
            if i == j:
                pass
            else:
                mult.append(numbers[i] * numbers[j])

    a = list(map(str, mult))

    result = []
    for i in range(len(a)):
        if len(a[i]) == 1:
            result.append(mult[i])
        cnt = 0
        for j in range(len(a[i]) -1):
            if int(a[i][j]) <= int(a[i][j+1]):
                cnt += 1
                if cnt == len(a[i]) - 1:
                    result.append(mult[i])
                    break
            else:
                break


    if len(result) == 0:
        return -1
    else:
        result.sort()
        return result[-1]


T = int(input())

for tc in range(T):
    n = int(input())

    numbers = deque()
    numbers = list(map(int, input().split()))


    print('#{} {}' .format(tc+1, danjo(numbers)))