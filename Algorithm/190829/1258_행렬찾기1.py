import sys
sys.stdin = open ('1258_행렬찾기.txt', 'r')


T = int(input())

for tc in range(T):
    num = int(input())

    arr = [list(map(int, input().split())) for _ in range(num)]

    result = []

    for i in range(num):
        for j in range(num):
            garow = 0
            sero = 0

            if arr[i][j] != 0:

                for x in range(num -j):
                    if arr[i][j+x] != 0:
                        garow += 1
                    else:
                        break
                for y in range(num -i):
                    if arr[i+y][j] != 0:
                        sero += 1
                    else:
                        break

                for w in range(sero):
                    for z in range(garow):
                        arr[i+w][j+z] = 0

                result.append([sero * garow, sero, garow])


    result.sort()

    ans = [len(result)]
    for n in range(len(result)):
        ans.append(result[n][1])
        ans.append(result[n][2])



    ansss = list(map(str, ans))

    print('#{} {}'.format(tc + 1, ' '.join(ansss)))


    # res = []
    # for n in range(len(result)):
    #     res.append(result[n][2])
    #
    # res.sort()
    #
    # real = [len(result)]
    # for m in range(len(res)):
    #     for v in range(len(result)):
    #         if res[m] == result[v][2]:
    #
    #             real.append(result[v][0])
    #             real.append(result[v][1])
    #
    # ans = list(map(str, real))
    #
    #
    # print('#{} {}' .format(tc+1, ' '.join(ans)))

