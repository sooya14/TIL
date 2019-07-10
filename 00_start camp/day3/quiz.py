#string = input('숫자를 입력하세요: ')
#number = int(string)

number = int(input('숫자를 입력하세요: '))


# 1 ~ number까지 출력
# 그와중에 3배수 fizz/ 5배수 buzz/ 15배수 fizz buzz


for i in range(1, number + 1):
    if i % 15 == 0:         
        print('Fizz Buzz') 
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz') 
    else:
        print(i)



