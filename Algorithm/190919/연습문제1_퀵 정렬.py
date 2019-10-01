
# def merge(arr):
#     if len(arr) > 1:
#         p = arr[len(arr) // 2]
#         left = []
#         right = []
#         mid = []
#
#         for i in range(len(arr)):
#             if arr[i] < p:
#                 left.append(arr[i])
#             elif arr[i] > p:
#                 right.append(arr[i])
#             else:
#                 mid.append(arr[i])
#         # mid.append(p)
#         return merge(left) + mid + merge(right)
#     else:
#         return arr

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

# def p(arr, p, r):
#     x = arr[r]
#     i = p -1
#
#     for j in range(p. r):
#         if arr[j] <= x:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i+1], arr[r] = arr[r], arr[i+1]
#
#     return i + 1


def quick(arr, l, r):
    if l < r:
        s = p(arr, l, r)
        quick(arr, l, s -1)
        quick(arr, s+1, r)
    return arr




arr1 = [11, 45, 23, 81, 28, 34, 99, 22, 17, 8]

result = quick(arr1, 0, len(arr1)-1)
print(result)