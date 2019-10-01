data = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

def bfs(node, start):

    queue = []
    visited = [0] * 8
    visited[start] += 1
    queue.append(start)


    while queue:
        x = queue.pop()
        for i in range(node):









node = [[0] * 8 for _ in range(8)]

for i in range(0, len(data) - 1, 2):
    node[data[i]][data[i + 1]] += 1

start = 1
result = bfs(node, start)

print(result)

