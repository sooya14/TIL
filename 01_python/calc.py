# soo
def s_sum(num1, num2):
    return num1 + num2

def s_minus(num1, num2):
    if num1 > num2:
        return num1 - num2
    else:
        num2 - num1
        
def s_mul(num1, num2):
    return num1 * num2

def s_div(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print('0으로는 나눌 수 없습니다.')
    else:
        return result
    
# TCH
def add(x, y):
    return x + y

def sub(x, y):
    return x - y
        
def mul(x, y):
    return x * y

def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return '0으로는 나눌 수 없습니다.'  # s_div 랑 똑같다. 
    

