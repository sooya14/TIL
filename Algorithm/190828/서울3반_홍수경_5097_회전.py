import sys
sys.stdin = open ('5097_회전.txt' , 'r')


T = int(input())

for tc in range(T):
    n, m = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    que = numbers + [0  for _ in range(m)]

    front = 0
    rear = n

    while front < m :
        que[front], que[rear]  =  que[rear], que[front]
        front += 1
        rear += 1


    print('#{} {}' .format(tc+1, que[front]))