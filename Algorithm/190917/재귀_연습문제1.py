def seletionsort(A):
    n = len(A)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if A[j] < A[min]:
                min = j
        temp = A[min]
        A[min] = A[i]
        A[i] = temp

    return A

def seletionsort2(A, s, e):
    if s == e:
        return

    mini = s
    for j in range(s+1, e):
        if A[j] < A[mini]:
            mini = j

    A[s], A[mini] = A[mini], A[s]
    seletionsort2(A, s+1, e)



A = [4, 6, 2, 7]
n = len(A)

print(seletionsort(A))
seletionsort2(A, 0, n-1)
print(A)