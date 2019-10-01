queue = [0] * 10

front = -1  
rear = -1

def enqueue(item):
    global front
    global rear

    if rear == len(queue) -1:  # full 일 때
        return 'error'
    else:
        rear += 1
        queue[rear] = item

def dequeue():
    global front
    global rear

    if front == rear:  # empty 일 때
        return 'error'
    else:
        front += 1
        return queue[front]

enqueue(1)
enqueue(2)
enqueue(3)
print(dequeue())
print(dequeue())
print(dequeue())
