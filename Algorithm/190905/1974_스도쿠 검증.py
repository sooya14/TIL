import sys
sys.stdin = open('1974.txt', 'r')

def play(puzzle):

    for i in range(9):
        cnt1 = 0
        for j in range(9):
            cnt1 += puzzle[j][i]
        if cnt1 != 45:
            return 0

    for i in range(9):
        if sum(puzzle[i]) != 45:
            return 0

    for z in range(0, 9, 3):
        cnt2 = 0
        for i in range(3):
            for j in range(3):
                cnt2 += puzzle[i][j+z]
        if cnt2 != 45:
            return 0

    return 1

T = int(input())

for tc in range(T):

    puzzle = [list(map(int, input().split())) for _ in range(9)]


    print('#{} {}' .format(tc+1, play(puzzle)))

