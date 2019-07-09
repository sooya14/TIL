# 190708 start camp - day01

##  컴퓨터 프로그래밍 언어

### 컴퓨터

컴퓨터란 계산기다. 

### 프로그래밍 

명령어의 집합. 쉽게 일 시키는 것

### 언어

말, 약속



## python 기초 문법 3형식

* 시작하기 전에 명심할 것

  * 대/소문자 구분

  * 띄어쓰기 및 들여쓰기(indent)

  * 스펠링

    

1. 저장

   * 무엇을 어떻게 저장할 수 있는가?

   * = : 박스에 저장한다.

     == : ~는 ~와 같다.

   * 컴퓨터가 저장할 수 있는 것은?

     * 숫자
     * 글자: 글자는 반드시 "" 또는 ''를 붙여야한다.
     * True/False :  조건, 반복에서 사용된다. (0 또는 1)

   * 마지막 것만 인식되어 저장된다. 

2. 조건

   * `if` 뒤에 : 가 있어야 자동 들여쓰기가 다음으로 된다. 

   ```python
   dust = 60
   if dust>50:
       print("50초과")
   else:
       print("50이하")   
       
   50초과
   ```

   ```python
   if dust > 150:
       print('매우나쁨')
   elif dust > 80:
     print('나쁨')
   elif dust > 50:
       print('보통')
   elif dust > 30:		
       print('좋음')
   else:
       print('매우좋음')
   ```

   

3. 반복

   * `While` 

   ```python
   n = 0
   While n < 3:
       print('출력')
       n = n+1
       
       
     
   
   0,1이상, 이하(<=, >=)는 python에서 잘 사용하지 않는다. 
   ```

   * 0,1이상, 이하(<=, >=)는 python에서 잘 사용하지 않는다. 

     초과, 미만(<,>)을 자주 사용한다. 

     

   * `for`

     * 정해진 여러개의 박스 중에 그 안에서 반복하고 이 반복은 반드시 처음부터 시작해서 끝에서 끝난다. 

     * `for`를 많이 사용하게 될 것이다. 

       ```python
       dust = [59, 24, 102]
       for i in dust:   #i 에는 뭘 써도 상광없다. 대신 아래 프린트에 꼭 나와야한다. 
           print(i)
           
       59 24 102
       ```
     

   * `While True` :  조건이 트루일때까지 반복적으로 실행되기에 종료조건이 반드시 필요

     VS `for i in dus` : 정해진 범위를 반복하기에 종료조건이 필요없음. 

     

   ```python
   greeting = '안녕'
   
   n = 0		
   while n < 5:
     print(greeting)
     n = n+1
       
   for n in [0,0,0,0,0]:	#5개의 개수가 중요한 것이다. 각 회차 5번 돈다느 것이 포인트이다. 
       print(greeting)
       
   for n in range(5):		
       print(greeting)
   ```

   

## python 함수

파이썬 함수에는 내장 함수와 외장 함수가 있다. 

괄호() 가 붙으면 함수이다. 



* 내장 함수

  * `print()` : 출력하는 함수

    ​					`print('안녕')` 과 `print(안녕)`은 다르다.

  * `range()` : 리스트를 생성하는 함수 

  * `list()` : 범위(range)를 생성하는 함수

    * `list()` 는 0번부터 숫자가 시작된다.

      ```python
      dusts = [58, 40, 70]
      print(dusts[1])
      
      40
      ```

      ``` python
      dusts={"영등포구":58, "서초구":40, ...}	#Key:강남구, Value:58
      print(dust["영등포구"])	#꺼낼때는 무조건 대괄호[ ] 이다. 
      
      58
      ```

    * 복수일 때는 항상 복수형으로 적는 것이 좋다. 

      

* 외장함수

  * `'random()` : 랜덤 관련 함수들의 묶음

  * `random.choice()` : 리스트에서 1개 무작위 선택

  * `random.sample(p,n)`: 모집단에서 n개의 요소를 무작위를 비복원 선택

    

### 로또 번호 추첨하기

```python
# 서랍에서 꺼낸다
import random

#공 바구니 numbers 를 만든다 1~45
numbers = range(1,46) 

#랜덤하게 공 바구니에서 6개를 뽑아서 lucky_numbers 에 저장한다. 
lucky_numbers = random.sample(numbers, 6)     

#lucky_numbers 를 출력한다. 
print(lucky_numbers)
```

