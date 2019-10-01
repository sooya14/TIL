stack = []

def push(v):
    stack.append(v)

def pop():
    if len(stack) == 0:
        return 'pop 을 할 수 없습니다.'
    else:
        return stack.pop(-1)

push('a')
push('b')
push('c')
pop()
print(stack)