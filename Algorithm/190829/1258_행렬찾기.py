import sys
sys.stdin = open ('1258_행렬찾기.txt', 'r')

def find(arr):

    while sum(arr, []) != 0:

        check = []
        y = 0

        for i in range(num):
            x = 0
            for j in range(num):
                if arr[i][j] != 0:
                    x += 1
                    arr[i][j] = 0
                else:
                    check.append(x)
                    y += 1
                    break
            return


T = int(input())

for tc in range(T):
    num = int(input())

    arr = [list(map(int, input().split())) for _ in range(num)]

    result = []
    while sum(arr, []) != 0:

        check = []
        y = 0

        for i in range(num):
            x = 0
            for j in range(num):
                if arr[i][j] != 0:
                    x += 1
                    arr[i][j] = 0
                else:
                    check.append(x)
                    y += 1
                    break


        for z in range(len(check)):
            if check[z] == 0:
                pass
            else:
                a = check.count(check[z])
                b = check[z]
                result.append([a, b])
                for w in range(a+1):
                    if check[w] == b:
                        check[w] = 0




    print(result)


