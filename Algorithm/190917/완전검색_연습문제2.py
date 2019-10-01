
def swap(i, j):
    arr[i], arr[j] = arr[j], arr[i]

def perm(n, k):

    if k == n:
        print(arr)

    else:
        for i in range(k):
            swap(k, i)
            perm(n, k+1)
            swap(k, i)


arr = [1, 2, 4, 7, 8, 3]
perm(6, )

