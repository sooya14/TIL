import sys
sys.stdin = open ('IM_토끼와 사냥꾼.txt', 'r')

def hunter(arr):

    result = []

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 3:

                cnt = 0

                dx = [-1, -1, -1, 0, 0, 1, 1, 1]
                dy = [-1, 0, 1, -1, 1, -1, 0, 1]

                for z in range(len(dx)):
                    x = i + dx[z]
                    y = j + dy[z]
                    if z == 0:
                        for a in range(10):
                            if 0<= x -a < len(arr) and  0 <= y-a < len(arr):
                                if arr[x-a][y-a] == 2:
                                    break
                                if arr[x-a][y-a] == 1:
                                    arr[x - a][y - a] = 0
                                    cnt += 1
                    if z == 1:
                        for a in range(10):
                            if 0<= x -a < len(arr) and  0 <= y < len(arr):
                                if arr[x-a][y] == 2:
                                    break
                                if arr[x-a][y] == 1:
                                    arr[x - a][y] = 0
                                    cnt += 1

                    if z == 2:
                        for a in range(10):
                            if 0<= x -a < len(arr) and  0 <= y+a < len(arr):
                                if arr[x-a][y+a] == 2:
                                    break
                                if arr[x-a][y+a] == 1:
                                    arr[x - a][y + a] = 0
                                    cnt += 1

                    if z == 3:
                        for a in range(10):
                            if 0<= x < len(arr) and  0 <= y-a < len(arr):
                                if arr[x][y-a] == 2:
                                    break
                                if arr[x][y-a] == 1:
                                    arr[x][y - a] = 0
                                    cnt += 1

                    if z == 4:
                        for a in range(10):
                            if 0<= x < len(arr) and  0 <= y+a < len(arr):
                                if arr[x][y+a] == 2:
                                    break
                                if arr[x][y+a] == 1:
                                    arr[x][y + a] = 0
                                    cnt += 1
                    if z == 5:
                        for a in range(10):
                            if 0<= x +a < len(arr) and  0 <= y-a < len(arr):
                                if arr[x+a][y-a] == 2:
                                    break
                                if arr[x+a][y-a] == 1:
                                    arr[x+a][y - a] = 0
                                    cnt += 1

                    if z == 6:
                        for a in range(10):
                            if 0<= x +a < len(arr) and  0 <= y < len(arr):
                                if arr[x+a][y] == 2:
                                    break
                                if arr[x+a][y] == 1:
                                    arr[x+a][y] = 0
                                    cnt += 1

                    if z == 7:
                        for a in range(10):
                            if 0<= x +a < len(arr) and  0 <= y+a < len(arr):
                                if arr[x+a][y+a] == 2:
                                    break
                                if arr[x+a][y+a] == 1:
                                    arr[x+a][y + a] = 0
                                    cnt += 1

                result.append(cnt)

    return sum(result)


arr = [list(map(int, input().split())) for _ in range(10)]

print(hunter(arr))


#####################################

forest = [list(map(int, input().split())) for _ in range(10)]
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]
​
catch = 0
for r in range(10):
    for c in range(10):
        if forest[r][c] == 3:
            for i in range(8):
                testr = r + dy[i]
                testc = c + dx[i]
                while 1:
                    if 0 <= testr < 10 and 0 <= testc < 10:
                        if forest[testr][testc] == 1:
                            catch += 1
                            forest[testr][testc] = 0
                            testr += dy[i]
                            testc += dx[i]
                        elif forest[testr][testc] == 2:
                            break
                        else:
                            testr += dy[i]
                            testc += dx[i]
                    else:
                        break
​
