import sys
sys.stdin = open('5176.txt', 'r')


def find(a):
    global cnt
    if arr[a]:
        find(a * 2)
        cnt += 1
        t = cnt
        tree[a] = t
        find(a * 2 + 1)


T = int(input())
for tc in range(T):
    n = int(input())
    arr = [i for i in range(n+1)] + [0] * (n+1)

    tree = [0] * (n+1)

    cnt = 0
    find(1)

    print('#{} {} {}' .format(tc+1, tree[1], tree[n//2]))




# def func(t):
#     global count
#     if arr[t]:
#         func(2 * t)
#         count += 1
#         temp = count
#         tree[t] = temp
#         func(2 * t + 1)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [i for i in range(N + 1)] + [0] * (N + 1)
#     print(arr)
#     tree = [0] * (N + 1)
#
#     count = 0
#     func(1)
#     # print(tree)
#     print('#%d %d %d' % (tc, tree[1], tree[N // 2]))