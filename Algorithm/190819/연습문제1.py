s = 'Reverse this strings'

print(s[::-1])

ss = []
for i in range(1, len(s)+1):
    ss.append(s[-i])

print(''.join(ss))

for j in range(1, len(s)/2 +1):
    
