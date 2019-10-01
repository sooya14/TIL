
def comb(n, r):
    if r == 0:
        if sum(tr) == 0:
            return print(tr)
        else:
            return

    elif n < r:
        return

    else:
        tr[r - 1] = an[n - 1]
        comb(n - 1, r - 1)
        comb(n - 1, r)



an = [-1, 3, -9, 6, 7, -6, 1, 5, 4, 2]

n = len(an)
#
# for i in range(0, (1 << n)):
#     a = []
#     for j in range(0, n):
#         if i & (1<< j):
#             a.append(an[j])
#             # print('{}' .format(an[j]), end=' ')
#     if sum(a) == 0:
#         print(a)
#

for i in range(11):
    tr = [0] * i
    comb(n, i)