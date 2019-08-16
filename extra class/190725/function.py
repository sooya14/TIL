# return value
# 인자가 있다, 인자가 없다
# 리턴이 있다, 리턴이 없다

# yes in yes out
def yes_in_yes_out(x):  # immutable
    return x + 1

yiyo = yes_in_yes_out(100)
yiyo  # 101

def yes_in_no_out(x):  # mutable 의 형태이다. 
    a = 1 + 1

yino = yes_in_no_out(100)
yino  # None => 파이썬이 우리에게 하는 대답 : 없는데요 ㅇㅅㅇ 

def no_in_yes_out():  # immutable
    return ':)'

niyo = no_in_yes_out()
niyo  # :)

def no_in_no_out():
    1 + 1

nino = no_in_no_out():
nino  # None 