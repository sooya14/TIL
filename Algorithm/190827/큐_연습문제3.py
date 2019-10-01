arr = [[1, 2], [1, 3], [2, 4], [2, 5], [4, 6], [5, 6], [6, 7], [3, 7]]

q = [[0] * 7 for _ in range(7)]

for i in range(len(arr)):
    q[arr[i][0] -1][arr[i][1] -1] += 1
    q[arr[i][1] -1][arr[i][0] -1] += 1


def bfs(q):
    visited = [1]
    queue = [1]

    while queue:

        x = queue.pop(0)

        for j in range(len(q)):
            if q[x-1][j] == 1 and not j+1 in visited:
                visited.append(j+1)
                queue.append(j+1)
            if len(queue) == 7:
                break
    return visited

print(bfs(q))
