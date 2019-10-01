import sys
sys.stdin = open('5356.txt', 'r')

T = int(input())

for tc in range(T):
    arr = [list(input()) for _ in range(5)]

    maxi = 0
    for i in range(len(arr)):
        if maxi < len(arr[i]):
            maxi = len(arr[i])


    result = []
    for i in range(maxi):
        for j in range(maxi):
            try:
                result.append(arr[j][i])
            except IndexError:
                pass

    print('#{} {}' .format(tc+1, ''.join(result)))