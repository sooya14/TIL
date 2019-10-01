import sys
sys.stdin = open('4873_반복문자지우기.txt', 'r')

T = int(input())

for tc in range(T):
    texts = list(map(str, input()))

    stack = []

    for i in range(0, len(texts)):
        if len(stack) == 0:
            stack.append(texts[i])
        else:
           if stack[-1] != texts[i]:
               stack.append(texts[i])
           else:
               stack.pop()




    print('#{} {}' .format(tc+1, len(stack)))