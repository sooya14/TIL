import sys
sys.stdin = open('2578.txt', 'r')

# 빙고판
pan = [list(map(int, input().split())) for _ in range(5)]

call = [list(map(int, input().split())) for _ in range(5)]

# 사회자가 숫자 부르는 숫자
numbers = []
for i in range(len(call)):
    for j in range(len(call)):
        numbers.append(call[i][j])

check = [[0] * 5 for _ in range(5)]

nn = 1
for n in numbers:
    cnt = 0
    for x in range(5):
        for y in range(5):
            if n == pan[x][y]:
                check[x][y] = 1

                # 가로
                for g in range(5):
                    if sum(check[g]) == 5:
                        cnt += 1
                # 세로
                    sero = []
                    for s in range(5):
                        sero.append(check[s][g])
                        if sum(sero) == 5:
                            cnt += 1
                # xy 같은 대각선
                xydae = []
                bandae = []
                for i in range(len(check)):
                    if check[i][i] == 1:
                        xydae.append((check[i][i]))
                        if sum(xydae) == 5:
                            cnt += 1
                    # 반대 대각선
                    if check[i][4-i] == 1:
                        bandae.append(check[i][4-i])
                        if sum(bandae) == 5:
                            cnt += 1

    if cnt >= 3:
        break
    else:
        nn += 1

print(nn)

