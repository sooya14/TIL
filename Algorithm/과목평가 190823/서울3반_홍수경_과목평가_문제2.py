import sys
sys.stdin = open('문제2.txt', 'r')

T = int(input())

for tc in range(T):
    nmk = list(map(int, input().split()))
    n = nmk[0]
    m = nmk[1]
    k = nmk[2]

    arr = [list(map(int, input().split())) for _ in range(n)]


    plus = []
    result = []
    for i in range(len(arr)):
        if i != n -k + 1:
            for x in range(len(arr)):
                if x != m - k + 1:
                    for j in range(k):
                            plus.append(arr[i][j+x])
                    for z in range(k - 2):
                        plus.append(arr[i+1 + z][x])
                        plus.append(arr[i+1 + z][x + k - 2 +1])
                    for y in range(k):
                        plus.append(arr[i + k -1][y + x])
                    result.append(sum(plus))
                    plus = []
                if x == m - k + 1:
                    break
        if i == n - k +1 :
            break


    print('#{} {}' .format(tc+1, max(result)))