import sys
sys.stdin = open('00.txt', 'r')


number = int(input())
ans = 0

for num in range(666, number):

    str_n = str(num)
    result = 0

    for i in range(len(str_n)):
        result += int(str_n[i])
    result += num

    if result == number:
        ans = num
        break


print(ans)
