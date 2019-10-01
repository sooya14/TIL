import sys
sys.stdin = open ('1224_계산기3.txt', 'r')

def hoo(cal):

    stack = []
    num = []

    for i in range(len(cal)):
        if cal[i] == '(' or cal[i] == '+' or cal[i] == '-' or cal[i] == '*' or cal[i] == '/':
            stack.append(cal[i])

        elif cal[i] == ')':
            if stack[-1] == '-':
                num.append(stack.pop())
                if stack[-1] == '(':
                    stack.pop()
                if stack[-1] == '+':
                    




        else:
            num.append(cal[i])







for tc in range(10):
    num = int(input())
    cal = list(input())

    print(tc+1, cal)

