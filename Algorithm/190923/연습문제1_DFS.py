arr = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

def dfs(node):

    stack = []
    vistied = []

    for i in range(len(node)):
        for j in range(8):
            


node = [[0] * 8 for _ in range(8)]
for i in range(0, len(arr)-1, 2):
    node[arr[i]][arr[i+1]] += 1

result = dfs(node)

print(node)





