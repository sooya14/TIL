numbers = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

arr = [[0] * 7 for _ in range(7)]

# 인접행렬 만들기
# for i in range(len(numbers), 2):
#     arr[numbers[i]][numbers[i+1]] = 1
#     arr[numbers[i+1]][arr[i]] = 1


for i in range(len(numbers)):
    if i % 2 == 0:
        a = numbers[i]
        b = numbers[i+1]
        arr[a-1][b-1] += 1

#  완성몬함
n = 0
stack = [1]
result = []
while len(stack) > 0:
    for i, v in enumerate(arr[n]):
        if v == 1:
            stack.append(i+1)

            n += 1
            result.append(i+1)
    n = stack[-1]
    stack.pop()


print(arr)

######################################################
raw_data = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
​
data = []
length = max(raw_data)
while raw_data:
    temp = []
    temp.append(raw_data.pop(0))
    temp.append(raw_data.pop(0))
    data.append(temp)
​
adj_matrix = [[0 for _ in range(length+1)] for _ in range(length+1)]
​
for datum in data:
    adj_matrix[datum[0]][datum[1]] = 1
    adj_matrix[datum[1]][datum[0]] = 1
​
# for line in adj_matrix:
#     print(line)
​
stacks = [1]
check_visit = [0] + [1] + [0 for _ in range(length-1)]
route = [1]
​
while stacks:
    for idx, ver in enumerate(adj_matrix[stacks[-1]]):
        if ver and not check_visit[idx]:
            stacks.append(idx)
            route.append(idx)
            check_visit[idx] = 1
            break
    else:
        stacks.pop(-1)
​
print('-'.join(list(map(str, route))))