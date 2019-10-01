import sys
sys.stdin = open('6190_정곤이의 단조.txt', 'r')

def danjo(numbers):

    mult = []
    for i in range(n):
        for j in range(i, n):
            if i == j:
                pass
            else:
                mult.append(numbers[i] * numbers[j])

    result = []
    for i in range(len(mult)):
        m = mult[i]
        if m // 10 == 0:
            result.append(m)

        check = False
        while m // 10:
            b = m % 10
            m //= 10
            a = m % 10

            if b < a:
                check = False
                break
            else:
                check = True

        if check:
            result.append(mult[i])


    if len(result) == 0:
        return -1
    else:
        result.sort()
        return result[-1]


T = int(input())

for tc in range(T):
    n = int(input())

    numbers = list(map(int, input().split()))

    print('#{} {}' .format(tc+1, danjo(numbers)))