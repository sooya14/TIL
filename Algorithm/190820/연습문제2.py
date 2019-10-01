
def check(g):
    stack = []
    stack2 = []
    gs = list(map(str, g))
    for i in gs:
        if i == '(':
            stack.append(i)
        else:
            stack2.append(i)

    if len(stack) == len(stack2):
        return 'ok'
    else:
        return 'ㄴㄴ'





print(check('()()((()))'))