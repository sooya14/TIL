import sys
sys.stdin = open('4366.txt', 'r')

def change(a, num, i):

    if a == 2:






# def find(two, tree):
#
#     two_result = []
#     for i in range(len(two)):
#         if two[i] == 1:
#             two[i] = 0
#         else:
#             two[i] = 1
#
#         res = 0
#         for j in range(len(two)-1):
#             res += two[j] * (2 ** (len(two)-1 -j))
#
#         if two[i] == 1:
#             two[i] = 0
#         else:
#             two[i] = 1
#
#         two_result.append(res)
#
#
#
#     three_result = []
#     for i in range(len(three)):
#
#         check = [0, 1, 2]
#
#         for j in range(len(check)):
#             if i == j:
#
#
#
#         three_result.append(res)
#
#
#     for i in range(len(two_result)):
#         for j in range(len(three_result)):
#             if two_result[i] == three_result[j]:
#                 return two_result[i]


T = int(input())

for tc in range(T):
    two = list(map(int, input()))
    three = list(map(int, input()))

    two_result = []
    for i in range(len(two)):
        two_result.append(change(2, two, i))

    three_result = []
    for i in range(len(three)):
        three_result.append(change(3, three, i))


    print(tc+1, two, three, ans)