numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = len(numbers)

for i in range(1 << n):
    for j in range(n + 1):
        if i & (1 << j):
            print(numbers[j], end=',')
    print()
print()

