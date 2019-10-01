import sys
sys.stdin = open ('4866_괄호검사.txt', 'r')


def check(text):
    stack = []
    for t in text:

        if t == '{' or t == '(':
            stack.append(t)

        if t == '}':
            if len(stack) == 0:
                return 0
                break
            elif stack[-1] == '{':







T = int(input())
for tc in range(T):
    text = list(map(str, input()))

    stack = []


