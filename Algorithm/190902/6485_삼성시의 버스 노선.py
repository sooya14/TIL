import sys
sys.stdin = open ('6485_삼성시의 버스 노선.txt', 'r')

T = int(input())

for tc in range(T):
    n = int(input())

    ab = []
    for _ in range(n):
        ab.append(list(map(int, input().split())))

    p = int(input())

    c = []
    for _ in range(p):
        c.append(int(input()))

    bus = [0] * 5001

    for i in range(len(ab)):
        for j in range(ab[i][1] - ab[i][0]+1):
            bus[ab[i][0]+j -1] += 1

    result = []
    for z in range(len(c)):
        result.append(str(bus[c[z]-1]))


    print('#{} {}' .format(tc+1, ' '.join(result)))


