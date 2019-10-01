# import sys
#
# sys.stdin = open('회문2.txt', 'r')
#
# for _ in range(10):
#     tc = int(input())
#     # 가로 리스트
#     texts = [list(map(str, input())) for _ in range(100)]
#
#     # 세로 리스트
#     seros = []
#     for i in range(100):
#         sero = []
#         for j in range(100):
#             sero.append(texts[j][i])
#         seros.append(sero)
#
#     number = 0
#     result_g = []
#     while number < 100:
#         # 가로
#         for i in range(100):
#             for x in range(number + 1):
#                 check = []
#                 check2 = []
#                 for j in range(100 - number):
#                     check.append(texts[i][j + x])
#
#                 check2 = check[::-1]
#                 if check == check2:
#                     result_g.append(number)
#                     number += 1
#                 else:
#                     number += 1
#     number_s = 0
#     result_s = []
#     while number < 100:
#         # 세로
#         for a in range(100):
#             for b in range(number_s + 1):
#                 chch = []
#                 chch2 = []
#                 for c in range(100 - number_s):
#                     chch.append(seros[a][c + b])
#
#                 chch2 = chch[::-1]
#                 if chch == chch2:
#                     result_s.append(number_s)
#                     number_s += 1
#                 else:
#                     number_s += 1
#
#     result = max(result_s + result_g)
#
#     print('#{} {}'.format(tc, result))