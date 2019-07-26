# Python 과목평가

* 객관식 20문제 + 주관식 5문제 (단답형) = 25문제
* 시험범위 : 01, 02, 03, 04, 07, 08 (05, 06 시험 범위 X)





## 01.python_intro



#### 식별자 

* 첫 글자에는 숫자가 올 수 없다. 
* 대소문자를 구별해야한다. 
* 아래는 사용할 수 없다.  => 내장함수나 모듈 등의 이름으로 만들면 안된다. 

```python
False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```

* 덮어 씌워지면 기존의 하마수를 사용할 수가 없다. 

```python
str = 'hi'   
str(5)  # 위에서 덮어씌워져 버려서 str 함수를 적용할 수가 없게 된다. => 오류발생
```



#### 기초 문법

* 인코딩 선언을 하지 않더라도 UTF - 8 이 기본설정



#### 주석

* 주석 : `#`
* doctring : `"""`



#### 코드라인

* 파이썬에서는 원래 `;` 를 잘 사용하지 않는다 그러나 딱 하나가 있는데

```python
print('happy');print('hacking') 
#happy
#hacking
```

​	원래 ; 없이 나란히 작성하면 오류가 뜨는데 ; 를 사용해서 나란히 print 를 굳이 둘 수가 있다. 

* 역슬래시 `\` 

```python
print('happy
      hacking')  # 에러
      
print('happy\
hacking')  # happyhacking
```

* `[]`, `{}`, `()` 은 \ 없어도 여러줄 가능 



#### 변수

* 변수의 갯수가 맞지 않으면 오류가 발생한다. (적어도 안되고 많아도 안되고)
* 



### 수치형

#### `int` (정수)

* 모든 정수는 `int` 이다. 
* 8진수 : `0o` / 2진수 : `0b` / 16진수 : `0x`

```python
0b10   #2 
0o10   #8 
0x10   #16 
```



#### arbitrary-precision arithmetc - Python ???



#### `float` (부동소수점, 실수) ??

* 컴퓨터가 2진수를 사용하고 있기 때문에 오류가 잘 발생한다. => 연산작업을 할 때, 답이 같지 않을 경우가 많이 발생
* 오류 방지 방법 2가지 

```python
# 방법 1
abs()  # 절대값 사용

# 방법 2
math.isclose()  # 
```



#### `complex` (복소수)

* 허수부 부분 : j => 제곱했을 때 마이너스가 나오는 수 

```python
a = 3- 4j

print(a.imag)  # -4.0
print(a.real)  #3.0
print(a.conjugate())  #(3+4j)
```



### BOOL

* 비교, 논리 연산을 할 떄 사용한다. 

```python
# 자동으로 F 가 결정되는 경우 
if  # 0, 0.0, '', [], (), {}, None
bool(
    # 0, 0.0, '', [], (), {}, None  
)

# 자동으로 T 가 결정되는 경우 => 위를 제외한 나머지 전부
if # 1, -1, -100, 1.1, ' '(스페이스 한칸이라도 있으면 비어있는 것이 아니다), [False], [None], [0]
bool(
    # 1, -1, -100, 1.1, ' ', [False], [None], [0]
)

```

* 띄어쓰기라도 있으면 뭐라도 있는 것이다! => True



### None

* 파이썬이 우리한테 없다라고 대답하는 것 
* 없어라는 값이다.



## 문자형(string)





## 08. OOP_advanced



#### 인스턴스 메서드

* 인스턴스가 사용할 메서드 
* 자동으로 인스턴스 객체가 self 가 된다.  



#### 클래스 메서드 

* 클래스가 사용할 메서드 
* `@classmethod` (데코레이터)
* 첫 번쨰 인자로 클래스(`cls`) 를 받는다. 자동으로 클래스 객체가 `cls` 가 된다. 
* ?클래스 속성을 통해서 메서드가 실행된다?



#### 스태틱(정적) 메서드

* 



