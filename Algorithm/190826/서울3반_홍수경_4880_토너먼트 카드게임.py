import sys
sys.stdin = open('4880_토너먼트 카드게임.txt', 'r')


def gbb(people):



T = int(input())
for tc in range(T):

    num = int(input())
    people = list(map(int, input().split()))

    print(tc+1, num, people)


