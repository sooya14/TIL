# list slicing

my_list = [4, 3, 7, 5, 3, 1, 2, 3]
# [x 시작점(포함됨): y끝(포함안됨)]
# [3:5] : index 3 <= i < 5 결국 index 3, 4
# [:y] : index 0 (시작) <= index < y
# [시작:] : x <= index ~ 리스트의 마지막을 포함하여

sl = my_list[2, 5]  # index 2 <= ... < 5 
# [7, 5, 3] => 갯수는 예상할 수 있다. len(sl)=> 5 - 2 = 3

my_list[-1]  # 무조건 마지막 요소 
my_list[:-1]  # 마지막을 제외한 모든 요소 
my_list[:]  # my_list 와 다를게 없음 

my_list[::1]  # my_list 와 다를게 또 없음 
# [시작:끝:스텝]
my_list[::2]  # 쉼표를 2개 건너뛴다. 
my_list[::-1]  # my_list 를 뒤집은 것이다. 
print(my_list[::-2])
print(my_list[3:2])  # if n>=3 and 2 > n  이것을 만족하는 수는 없으니깐 비어있는 list 가 나온다. 

