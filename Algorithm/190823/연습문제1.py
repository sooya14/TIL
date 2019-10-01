cal = [2, '+', 3, '*', 4, '/', 5,]

stack = []
result = []

for c in cal:
    if c in range(10):
        result.append(c)
    if c == '+' or c == '-' or c == '*' or c == '/':
        stack.append(c)

for _ in range(len(stack)):
    result.append(stack.pop())

result = list(map(str, result))

print(' '.join(result))