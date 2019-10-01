import sys
sys.stdin = open('1961.txt', 'r')

T = int(input())

for tc in range(T):
    n = int(input())

    numbers = [list(map(int, input().split())) for _ in range(n)]

    result = [[0] * 3 for _ in range(n)]


    for i in range(n):
        ans1 = ''
        for j in range(n):
            ans1 += str(numbers[n-j-1][i])
        result[i][0] = ans1


    for i in range(n):
        ans2 = ''
        for j in range(n):
            ans2 += str(numbers[n-i-1][n-1-j])
        result[i][1] = ans2


    for i in range(n):
        ans3 = ''
        for j in range(n):
            ans3 += str(numbers[j][n-i-1])
        result[i][2] = ans3


    print('#{}' .format(tc+1))


    for i in range(len(result)):
        for j in range(3):
            print(result[i][j], end=' ')
        print()


