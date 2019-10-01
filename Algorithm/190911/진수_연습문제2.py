
def Bbit_print(i):
    output = ''
    for j in range(24, -1, -1):
        output += '1' if i & (1 << j) else '0'

    return output


data = 0xF97A3

a = str(Bbit_print(data))

result = []

for j in range(0, len(a), 7):
    res = 0
    cnt = 0
    for i in range(1, 8):
        res += int((2 ** (7 - i)) * int(a[i+j]))
        cnt += 1
        if cnt == 7:
            result.append(res)
        


print(result)






