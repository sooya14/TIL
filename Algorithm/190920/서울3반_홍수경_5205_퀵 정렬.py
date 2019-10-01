import sys
sys.stdin = open('5205.txt')

def p(arr, l, r):
    p = arr[l]
    i = l
    j = r

    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]
    return j


def quick(arr, l, r):
    if l < r:
        s = p(arr, l, r)
        quick(arr, l, s -1)
        quick(arr, s +1, r)
    return arr

T = int(input())
for tc in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    result = quick(arr, 0, len(arr)-1)

    print('#{} {}' .format(tc+1, result[n//2]))