import sys
sys.stdin = open ('GNS.txt', 'r')

T = int(input())

for _ in range(T):
    tc_number = list(map(str, input().split()))
    text = list(map(str, input().split()))
    tc = tc_number[0]
    number = int(tc_number[1])

    e_num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    cnts = []

    for e in e_num:
        cnt = 0
        for t in text:
            if e == t:
                cnt += 1
        cnts.append(cnt)

    result = []
    for i in range(len(e_num)):
        for j in range(cnts[i]):
            result.append(e_num[i])


    print('{} {}' .format(tc, ' '.join(result)))



