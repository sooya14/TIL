from collections import deque

result = deque()

def enqueue(num):


    if len(result) == 0:
        result.append(num)

    elif len(result) == 1:
        if result[0] > num:
            result.append(result[0])
            result[0] = num
        else:
            result.append(num)

    else:
        for i in range(len(result)):
            if result[0+ i] < num < result[1+i]:
                result.insert(1+i, num)

    return result

enqueue(1)
enqueue(5)
enqueue(2)
enqueue(4)
print(enqueue(3))


##########################################

def insert_sort(a):
    sd = deque()
    sd.append(a[0])

    for i in range(1, len(a)):
        pos = i
        for j in range(i-1, -1, -1):
            if sd[j] > a[i]:
                pos = j
        sd.insert(pos, a[i])

    return sd





