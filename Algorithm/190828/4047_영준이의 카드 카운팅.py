import sys
sys.stdin = open('4047_영준이의 카드 카운팅.txt', 'r')

def checkerror(yj):

    arr1 = []
    for i in range(0, len(yj), 3):
        arr1.append(yj[i] + yj[i+1] + yj[i+2])

    check = []
    for i in arr1:
        check.append(arr1.count(i))

    bs = 1
    for j in check:
        if j >= 2:
            bs = 0

    if bs == 0:
        result = 'ERROR'
        return result
    else:
        return cardcount(yj)

    #
    # for i in arr1:
    #     if arr1.count(i) >= 2:
    #         result = 'ERROR'
    #         return result
    #     else:
    #         return cardcount(yj)


def cardcount(yj):

    sdhc = ['S', 'D', 'H', 'C']

    arr2 = []
    for i in range(0, len(yj), 3):
        arr2.append(yj[i])
        arr2.append(yj[i+1] + yj[i+2])

    result = []
    for s in sdhc:
        result.append(str(13 - arr2.count(s)))

    res = ' '.join(result)
    return res


T = int(input())

for tc in range(T):
    yj = list(input())

    print('#{} {}' .format(tc+1, checkerror(yj)))


