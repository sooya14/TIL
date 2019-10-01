
def Bbit_print(i):
    output = ''
    for j in range(15, -1, -1):
        output += '1' if i & (1 << j) else '0'

    return output



a = 0xDEC
print(Bbit_print(a))

