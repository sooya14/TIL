# SOO
def find_one(*args):
    for num in args:
        if args.count(num) % 2 == 1:
            return num

# list comprehension
def find_one(*args):
    return [num for num in args if args.count(num) % 2 == 1][0]

# # TCH => 2진수 XOR
def find_one(*args):
    r = 0
    for n in args:
        r ^= n
    return r

# 숫자 set 이 들어옵니다. => 단 하나만 홀수개가 들어옵니다. 
print(find_one(1, 2, 1))  # 2
print(find_one(1, 1, 2, 2, 3, 3, 3))  # 3
print(find_one(4, 3, 2, 1, 10, 1, 2, 4, 3))  #10