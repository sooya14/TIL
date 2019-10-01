# data = '0000000111100000011000000111100110000110000111100111100111111001100111'

data = '0000000'
# bit = []
# for j in range(len(data)/7):
#     b = ''
#     b += j
# print(bit)

res = []
for i in range(len(data)-1, 0, -1):
    result = 0
    if int(data[i]) == 1:
        result += 2 ** (7-i-1)

res.append(result)

print(res)

