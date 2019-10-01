import sys
sys.stdin = open('5204.txt', 'r')

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    left = merge_sort(arr[0:len(arr)//2])
    right = merge_sort(arr[len(arr)//2:])



    return merge(left, right)


def merge(left, right):
    global cnt

    if left[-1] > right[-1]:
        cnt += 1

    i = 0
    j = 0
    s_arr = []


    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            s_arr.append(left[i])
            i += 1
        else:
            s_arr.append(right[j])
            j += 1

    while i < len(left):
        s_arr.append(left[i])
        i += 1

    while j < len(right):
        s_arr.append(right[j])
        j += 1

    return s_arr


T = int(input())
for tc in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    cnt = 0

    result = merge_sort(arr)
    print('#{} {} {}' .format(tc+1, result[n//2], cnt))