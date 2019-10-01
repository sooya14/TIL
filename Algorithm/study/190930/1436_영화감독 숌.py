import sys
sys.stdin = open('00.txt', 'r')

n = int(input())
cnt = 0
result = 0

for i in range(666, 10000000000000000000):
    if '666' in str(i):
        cnt += 1

        if cnt == n:
            result += i
            break

print(result)

