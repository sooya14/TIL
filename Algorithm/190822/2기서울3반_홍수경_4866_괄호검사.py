import sys
sys.stdin = open ('4866_괄호검사.txt', 'r')

T = int(input())
for tc in range(T):
    text = list(map(str, input()))
    result = 1

    stack = []

    for t in text:
        if t == '(' or t == '{':
            stack.append(t)
        else:
            if t == '}':
                if len(stack) == 0:
                    result = 0
                else:
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        result = 0

            if t == ')':
                if len(stack) == 0:
                    result = 0
                else:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        result = 0

    if text[0] == ')' or text[0] == '}':
         result = 0
    elif len(stack) == 0 and result == 1:
        result = 1
    else:
        result = 0

    print('#{} {}' .format(tc+1, result))

    #
    # if len(stack) == 0 and text[0] != ')' and text[0]!= '}':
    #     result = 1
    # else:
    #     result = 0





