import sys
sys.stdin = open('00.txt', 'r')
import itertools


n, m = list(map(int, input().split()))
cards = list(map(int, input().split()))


combi = list(map(list, itertools.combinations(cards, 3)))

result = 0

for i in range(len(combi)):
    if 0 < sum(combi[i]) <= m:
        if sum(combi[i]) > result:
            result = sum(combi[i])

print(result)