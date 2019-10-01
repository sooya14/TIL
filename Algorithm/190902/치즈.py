
import sys
sys.stdin = open ('1267_작업순서.txt', 'r')
import copy
sys.setrecursionlimit(100000)


def oxinization(row2, col2):
    global row, col
    base[row2][col2] = 3
    if -1 < row2 < row + 2 and -1 < col2 < col + 2:
        # base[row2][col2] = 3
        for aa in range(4):
            if -1 < row2+dy[aa] < row + 1 and -1 < col2+dx[aa] < col + 1:
                if base[row2+dy[aa]][col2+dx[aa]] == 0:
                    oxinization(row2+dy[aa], col2+dx[aa])
                elif base[row2+dy[aa]][col2+dx[aa]] == 1:
                    base[row2 + dy[aa]][col2 + dx[aa]] = 7
            else:
                continue
        else:
            return
    return


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
row, col = map(int, input().split())
base = [0]*(row+3)
base[0] = [0 for _ in range(col+3)]
base[row+1] = [0 for _ in range(col+3)]
base[row+2] = [0 for _ in range(col+3)]
for i in range(1, row+1):
    base[i] = list(map(int, input().split()))
    base[i].insert(0, 0)
    base[i] += [0]
    base[i] += [0]
will_be_dead = 1
count = 0
result = 0
while will_be_dead != 0:
    base_copy = copy.deepcopy(base)
    oxinization(0, 0)
    will_be_dead = 0
    godgodcheesecheeese = 0

    for i in range(len(base)):
        for j in range(len(base[0])):
            if base[i][j] == 7:
                base_copy[i][j] = 0
                will_be_dead += 1
            elif base[i][j] == 1:
                godgodcheesecheeese += 1
    base = base_copy
    if will_be_dead != 0:
        result = will_be_dead
        count += 1
    if godgodcheesecheeese == 0:
        break
print(count)
print(result)