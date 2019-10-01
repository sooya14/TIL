# num = 100
#
# ch = ord('0') + num
#
# print(chr(ch))


def atoi(str):
    value = 0

    for i in range(len(str)-1, -1, -1):
        if ord(str[i]) > ord('0') and ord(str[i]) <= ord('9'):
            digit = ord(str[i]) - ord('0')

        else:
            break

    value = (value * 10) + digit

    return value


def myitoa(num):
    s = ''
    while True:
        digit = num % 10
        s = s + chr(digit + ord('0'))
        num = num // 10
        if num == 0:
            break
    char = ''
    for i in range(len(s) - 1, -1, -1):
        char = char + s[i]
    return char

