# for 
# 안전하다 / 반드시 끝난다 / 무조건 돌릴 수 있는 것들을 처음 부터 끝까지 모두 순회하며 돌아요.
# for ? in ??: ? 내가 짓고 싶은 이름 / ?? 돌릴 수 있는 것 : (우선순위) list, strind, range, dict, tuple,  

for i in range(10):
    # 1부터 10을 출력
    print(i+1)

total = 0  # 더할 곳을 뚫어놓는다
for n in [1, 2, 3, 4, 5]:
    total = total + n

# while => 내가 끝을 지정해야한다. 자유도가 상대적으로 높음. 
# while T/F:  => 필수

# 파이썬 내맘대로 T/F 변환 법칙
# F : 0, '', [], {}, (), None
# T : 그 외의 모든 값

flag = True

while flag:
    
    flag = False  # flag 는 조정할 수 있다. 

x = 0
while x < 10:
    print('열번말하기')
    x = x + 1