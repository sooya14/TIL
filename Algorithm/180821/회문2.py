import sys
sys.stdin = open ('회문2.txt', 'r')


for _ in range(10):
    tc = int(input())
    # 가로 리스트
    texts = [list(map(str, input())) for _ in range(100)]

    # 세로 리스트
    seros = []
    for i in range(100):
        sero = []
        for j in range(100):
            sero.append(texts[j][i])
        seros.append(sero)


    result = []

    # 가로
    for i in range(100):
        for n in range(100, -1, -1):
            for x in range(100 - n+1):
                check = []
                for j in range(n):
                    check.append(texts[i][x+j])
                if check == check[::-1]:
                    result.append(n)
    # 세로
    for i in range(100):
        for n in range(100, -1, -1):
            for x in range(100 - n+1):
                chch = []
                for j in range(n):
                    chch.append(seros[i][j + x])
                if chch == chch[::-1]:
                    result.append(n)



    print('#{} {}' .format(tc, max(result)))
