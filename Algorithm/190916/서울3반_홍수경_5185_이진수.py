import sys
sys.stdin = open('5185.txt', 'r')


data = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15 }


def Bbit_print(i):
    output = ''
    for j in range(3, -1, -1):
        output += '1' if i & (1 << j) else '0'

    print(output, end='')


T = int(input())

for tc in range(T):
    n, number = list(input().split())


    print('#{}' .format(tc+1) , end=' ')
    for i in range(len(number)):
        Bbit_print(data[number[i]])
    print()




