import sys
sys.stdin = open ('4865_글자수.txt', 'r')

T = int(input())
for tc in range(T):
    str1 = list(input())
    str2 = list(input())

    strings = {}

    for i in range(len(str1)):
        strings[str1[i]] = 0

    # 딕셔너리 만드는 메서드
    # strings = strings.fromkeys(str1, 0)

    for k in strings.keys():
        strings[k] = str2.count(k)

    result = max(strings.values())

    print('#{} {}' .format(tc + 1, result))



