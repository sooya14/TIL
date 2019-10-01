import sys
sys.stdin = open('2001_파리퇴치.txt', 'r')

T = int(input())

for tc in range(T):
    n, m = list(map(int, input().split()))

    arr = [list(map(int, input().split())) for _ in range(n)]


    result = []
    for z in range(n-m+1):
        for j in range(n-m+1):
            die = []
            for i in range(m):
                die.append(arr[i+z][j:j+m])
            result.append(sum(sum(die, [])))


    print('#{} {}' .format(tc+1, max(result)))