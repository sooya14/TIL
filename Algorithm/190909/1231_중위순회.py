import sys
sys.stdin = open ('1231.txt', 'r')


def ans(a):

    if a:
        ans(tree[a][0])
        for i in range(len(word)):
            if a == int(word[i][0]):
                print('{}' .format(word[i][1]) ,end='')
        ans(tree[a][1])


for tc in range(10):
    n = int(input())

    data = [list(input().split()) for _ in range(n)]

    tree = [[0] * 2 for _ in range(n+1)]


    for i in range(len(data)):
        if len(data[i]) == 3:
            tree[i+1][0] = int(data[i][2])
        elif len(data[i]) == 4:
            tree[i+1][0] = int(data[i][2])
            tree[i+1][1] = int(data[i][3])
        else:
            pass

    word = []
    for i in range(len(data)):
        word.append([data[i][0], data[i][1]])

    print('#{}'.format(tc + 1) ,end=' ')
    result = ans(1)
    print()

    print(data, tree, word)



