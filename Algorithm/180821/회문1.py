import sys
sys.stdin = open ('회문1.txt', 'r')

for tc in range(10):
    number = int(input())
    texts = [list(map(str, input())) for _ in range(8)]

    # 세로 리스트
    seros = []
    for xx in range(8):
        sero = []
        for yy in range(8):
            sero.append(texts[yy][xx])
        seros.append(sero)

    #  가로
    result_g = 0
    for i in range(8):
        for x in range(8-number+1):
            check = []
            check2 = []
            for j in range(number):
                check.append(texts[i][j+x])

            check2 = check[::-1]
            if check == check2:
                result_g += 1

    # 세로
    result_s = 0
    for a in range(8):
        for b in range(8 - number + 1):
            chch = []
            chch2 = []
            for c in range(number):
                chch.append(seros[a][c+b])

            chch2 = chch[::-1]
            if chch == chch2:
                result_s += 1

    result = result_g + result_s

    print('#{} {}' .format(tc+1, result))
