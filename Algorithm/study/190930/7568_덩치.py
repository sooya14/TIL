import sys
sys.stdin = open('00.txt', 'r')

n = int(input())

people = [list(map(int, input().split())) for _ in range(n)]

result = []


for i in range(n):
    cnt = 1
    w = people[i][0]
    h = people[i][1]
    for j in range(n):
        if i != j:
            if w < people[j][0] and h < people[j][1]:
                cnt += 1

    result.append(cnt)

for i in range(len(result)):
    print(result[i], end=' ')