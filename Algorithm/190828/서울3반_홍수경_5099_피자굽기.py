import sys
sys.stdin = open('5099_피자굽기.txt', 'r')



T = int(input())

for tc in range(T):
    n, m = list(map(int, input().split()))

    p = list(map(int, input().split()))

    pizzas = []
    for i in range(len(p)):
        pizzas.append([i+1, p[i]])

    queue = []
    for i in range(n):
        queue.append(pizzas[i])

    i = 0
    while len(queue) != 1:
        queue[0][1] //= 2

        if queue[0][1] // 2 == 0:
            if n + i < m:
                queue.pop(0)
                queue.append(pizzas[n+i])
                i += 1
            elif n + i >= m:
                queue.pop(0)

        else:
            queue.append(queue.pop(0))


    print('#{} {}' .format(tc+1, queue[0][0],))

