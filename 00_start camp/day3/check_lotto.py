my = [1, 2, 3, 4, 5, 6]

real = [1, 2, 3, 4, 5, 7]
bonus = 8


match = set(my).intersection(set(real))   #교집합을 물어보는 것 #집합은 순서가 없다. 
                    #[1, 2, 3] => list / {1, 2, 3,} => set / (1, 2, 3) => tuple / {'a' : 'A'} => dict
match_count = len(match)    #갯수세는 것

if match_count == 6:
    result = '1등'      
elif match_count == 5:
    if bonus in my:
        result = '2등'
    else:
        result = '3등'
elif match_count == 4:
    result = '4등'
elif match_count == 3:
    result = '5등'
else:
    result = '꽝'


