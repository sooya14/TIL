import sys
sys.stdin = open ('1952.txt', 'r')

T = int(input())
for tc in range(T):
    price = list(map(int, input().split()))
    month = list(map(int, input().split()))

    mini = price[3]

    for i in range(12):
        result = 0

        result += month[i] * price[0]
        if result < mini:
            mini = result

        result = 0
        if

    print(price, month)