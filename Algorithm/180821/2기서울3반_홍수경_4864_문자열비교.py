import sys
sys.stdin = open ('4864_문자열비교.txt', 'r')

T = int(input())

for tc in range(T):
    pattern = list(input())
    text = list(input())

    i = 0
    j = 0
    cnt = 0
    while i < len(text) and j < len(pattern):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            cnt += 1
        else:
            i += 1

    if cnt == len(pattern):
        result = 1
    else:
        result = 0

    print('#{} {}' .format(tc+1, result))
