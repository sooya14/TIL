# n = 13
# data = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
#
#
# def find(a):
#
#     print(a)
#     find(nodes[a][1])
#     find(nodes[a][2])
#
#
#     # for i in range(len(nodes)):
#     #     if nodes[i][0] == a:
#     #         for j in range(1, len(nodes[i])):
#     #             return find(nodes[i][j])
#
#
# nodes = []
# for i in range(1, n+1):
#     tree = [i]
#     for j in range(0, len(data), 2):
#         if data[j] == i:
#             tree.append(data[j+1])
#     nodes.append(tree)
#
# for z in range(len(nodes)):
#     if len(nodes[z]) != 3:
#         nodes[z].append(0)
#
#
# find(1)
# print()

######################################

def ans(T):
    if T:
        print('%d' % T, end=' ')
        ans(tree[T][0])
        ans(tree[T][1])

n = 13
tree = [[0] * 2 for _ in range(n+1)]

temp = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

for i in range(len(temp) // 2):
    parent, child = temp[i*2], temp[i*2+1]
    if not tree[parent][0]:
        tree[parent][0] = child
    else:
        tree[parent][1] = child

ans(1)
print()