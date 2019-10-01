import sys
sys.stdin = open('5186.txt', 'r')

def change(input_number):

    cnt = 0
    res = ''
    n = input_number
    while True:
        mult = float(n) * 2
        res += str(mult)[0]
        cnt += 1
        n = mult - int(str(mult)[0])
        if mult == 1:
            return res
        if cnt >= 13:
            return 'overflow'


T = int(input())

for tc in range(T):
    input_number = input()

    result = change(input_number)

    print('#{} {}' .format(tc+1, result))




