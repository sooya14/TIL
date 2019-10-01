import sys
sys.stdin = open('5208.txt', 'r')

def bus(k, cnt):
    global mini

    if k >= n-1:
        if cnt < mini:
            mini = cnt

    else:
        for i in range(battery[k], 0, -1):
            if cnt < mini and k+i < n:
                bus(k+i, cnt+1)

T = int(input())

for tc in range(T):
    data = list(map(int, input().split()))

    n = data[0]

    battery = data[1:]

    # cnt = 0
    mini = 999999999

    bus(0, 0)
    print('#{} {}' .format(tc+1, mini-1))




