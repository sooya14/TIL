import sys
sys.stdin = open ('4874_Forth.txt', 'r')

T = int(input())

for tc in range(T):
    hoo = list(input().split())

    mark = ['+', '-', '/', '*',]

    stack = []
    result = []
    for i in range(len(hoo)):
        if hoo[i] in mark:
            if len(stack) == 1:
                result.append('error')
                break
            else:
                if hoo[i] == '+':
                    stack.append(stack.pop() + stack.pop())
                if hoo[i] == '-':
                    stack.append(stack.pop(-2) - stack.pop(-1))
                if hoo[i] == '/':
                    stack.append(int(stack.pop(-2) / stack.pop(-1)))
                if hoo[i] == '*':
                    stack.append(stack.pop(-2) * stack.pop(-1))
        elif hoo[i] == '.':
            result.append(stack[0])
        else:
            stack.append(int(hoo[i]))

    if 'error' in result:
        print('#{} {}' .format(tc+1, 'error'))
    elif len(stack) > 1:
        print('#{} {}'.format(tc + 1, 'error'))
    else:
        print('#{} {}' .format(tc+1, result[0]))


