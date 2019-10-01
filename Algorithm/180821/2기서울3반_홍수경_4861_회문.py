import sys
sys.stdin = open ('4861_회문.txt', 'r')

T = int(input())

for tc in range(T):
    n, m = map(int, input().split())  # n * n / m 회문의 글자수

    texts = [list(input()) for _ in range(n)]

    # 세로 리스트
    seros = []

    for xx in range(n):
        sero = []
        for yy in range(n):
            sero.append(texts[yy][xx])
        seros.append(sero)

    result_g= []
    # 가로
    for i in range(n):
        for x in range(n-m+1):
            check = []
            check2 = []
            for j in range(m):
                check.append(texts[i][j+x])
                check2.append(texts[i][m-1-j-n+x])
            if check == check2:
                result_g = check

    # 세로
    result_s = []
    for i in range(n):
        for a in range(n - m + 1):
            chch = []
            chch2 = []
            for b in range(m):
                chch.append(seros[i][b + a])
                chch2.append(seros[i][m - 1 - b - n + a])
            if chch == chch2:
                result_s = chch

    if len(result_s) == 0:
        result = result_g
    else:
        result = result_s



    print('#{} {}' .format(tc+1, ''.join(result)))


    # # 망한 세로
    # for b in range(m):
    #     chch = []
    #
    #     for a in range(n):
    #         chch.append(texts[a][b])
    #     chch2 = chch[::-1]
    #     if chch == chch2:
    #         result = chch
    #
    #
    # print('#{} {}' .format(tc+1, ''.join(result)))
    #











