# key - value / dict 
d = {'a': 1, 'b': 2, 'c': [1, 2, 3]}

d['a']  # 1 => dict 에서 꺼낼때는 언제나 []로 꺼낸다.

# for 를 돌릴 때 raw, .key(), .values(), .items()
d = {'a': 1, 'b': 2, 'c': [1, 2, 3]}

for key in d:  # d for를 돌리면 key 가 나온다. 
    if key == 'a':
        result = d[key]

print(result)
# 위아래가 같다;
d['a']


# key, value 같이 꺼내기 
for k, v in d.items():
    pass 


# key를 꺼내는 2가지 방법
for key in d:
    pass

for key in d.keys():
    pass

# value 를 꺼내는 방법

d = {
    'd_code': 1234, 
    'name': '봉준호', 
    '필모그래피':[
        '기생충', 
        '괴물'
    ]
}

bongs_code = 0 
for valus in d.values:
    if value == '봉준호':
        bongs_code = d['d_code']

for key in d:
    print(d[key])





