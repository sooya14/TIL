import sys
sys.stdin = open ('4869_종이붙이기.txt', 'r')

def paper(x):

    if x == n:
        return 1
    if x > n:
        return 0
    return paper(x + 10) + paper(x + 20) * 2



T = int(input())
for tc in range(T):
    n = int(input())


    print('#{} {}' .format(tc+1, paper(0)))

