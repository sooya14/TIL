# Python 과목평가

* 객관식 20문제 + 주관식 5문제 (단답형) = 25문제

* 시험범위 : 01, 02, 03, 04, 07, 08 (05, 06 시험 범위 X)

* 코드의 오류 파악할 줄 알기 

* dict => value 접근, `.get` 

* list => `sort`, `sorted` 차이 / `return` 의 유무 차이 

* type 잘 파악하기 

* `range` 함수 : 0부터 센다. ex) `range(1, 45)` => 45 포함 ㄴㄴ 

* 슬라이식 마니 해보기 

* 재귀함수 => 읽을 줄 알아야한다. 그림 그려서 해보기 

* ★함수 : `return` 파악 

* ☆ mutable : [], {}, () => 원본이 바뀐다. return 이 없다. 

  ​	immutable : 나머지 => 원본이 바뀌지 않는다. return gksek. 



![1564307217298](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1564307217298.png)



## 01.python_intro



#### 식별자 

* 첫 글자에는 숫자, '_' 는 올 수 없다. 
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



### 문자형(string)

* Single quotes(`'`)나 Double quotes(`"`) 사용 => 하나의 문장부호를 선텍히리고 유지 (PEP-8)
* `input()` => 사용자에게 받은 입력은 기본적으로 str 이다. 
* 그러나 문자열 안에 문장부호가  있으면 오류가 발생한다. 

```python
print('철수가 말했다. '안녕?'')  #=> 오류발생

# 오류 해결 
print('철수가 말했다. "안녕?"')  # 큰따움표 사용
print('철수가 말했다. \'안녕?\'')  # \ 사용

```

* 긴 문자열은 """ 을 사용 => 긴 str 도 타입은 그냥 str



### 이스케이프 문자열 

![1564287950848](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1564287950848.png)

```python
print('개행문자(backslash n) 말고도 가능합니다.', end='!')
print('기본값이 엔터일 뿐', end='!')

# 개행문자(backslash n) 말고도 가능합니다.!기본값이 엔터일 뿐!
```



### String interpolation

1) `%-formatting`  : c 언어에서 사용한다. 

2) [`str.format()`](https://pyformat.info/)

3) [`f-strings`](https://www.python.org/dev/peps/pep-0498/) : 파이썬 3.6 버전 이후에 지원 되는 사항입니다.

```python
name = '수경'

# 2번 
'Hello, {} {} {}' .format(name, 100, True)  
# 'Hello, 수경 100 True'

# 3번
f'Hello, {name}'
# 'Hello, 수경'
```

* `"""` 도 가능 
* f-string 은 형식을 지정할 수 있다. 

```python
f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}'   
```

* 연산도 가능 



### 산술 연산자

![1564288479089](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1564288479089.png)

* 나눗셈 

  * `/` : 일반적인 나눗셈
  * `//` : 나누었을 때 몫의 값만 추출 ex) 5 // 2 => 2
  * `%` : 나누었을 때 맞아 떨어지지 않을 때 나오는 값 => 5 % 2 => 1 

  ```python
  print(int(5 / 2))
  
  # 2 추출 => 기본적으로 int 는 내림이다.(소숫점 뒷자리 버려버림)
  ```

  * `divmod` 함수 : 몫과 나머지를 알려주는 함수

  ```python
  print(divmod(5, 2))
  # (2, 1) => class tuple 형태로 추출 
  ```

* 양수 음수 표현도 가능 => 배웠던 수학처럼 그냥 간단히



### 비교 연산자 

![1564288891802](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1564288891802.png)

* 부등호가 앞이고 = 이 뒤에 있다. 
* `3 == 3.0` 은 같은 숫자이다. => True 
* 문자열에서 대소문자가 다르면 당연히 같은 str 이 아니다!! 



### 논리 연산자 

![1564289011857](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1564289011857.png)

* 우리가 보통 알고 있는 `&` `|`은 파이썬에서 비트 연산자이다. => 2진법에서 사용하는 것이다. (그러나 쉅 시간에 쌤이 알려주시지 않은 것 같음 )
* ` a or b` : 둘중 하나라도 True 면 True 이다. 둘다 False 여야지만 False 값이 추출



![1564289465290](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1564289465290.png)

=> `and` : True 이면 뒤의 값을 추출 / 둘 중 하나라도 False 이면 Fasle 에 해당하는 값 추출 

=> `or` : 둘다 True 면 앞의 값을 추출 (이미 하나의 값이라도 Ture 면 True 니깐) / 둘다 False 면 뒤에 것 /

```python
print(3 and 5)  # 5
print(3 and 5 and 10 and 15 and 0)  # 0
print(3 or 5)  # 3
print(3 or 0)  # 3
print(3 or 5 or 10 or 15 or 0)  # 3
```



### 복합 연산자 

![1564289681590](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1564289681590.png)



### 기타 연산자 

Concatenation : 숫자가 아닌 자료형은 `+` 연산자를 통해 합칠 수 있다.

```python
[1, 2, 3] + [4, 5, 6]  
# [1, 2, 3, 4, 5, 6] => list 도 가능하다. 
```



Containment Test : `in` 연산자를 통해 속해있는지 여부를 확인할 수 있다.

Identity : `is` 연산자를 통해 동일한 object인지 확인할 수 있다.

Indexing/Slicing : `[]`를 통한 값 접근 및 `[:]`을 통한 슬라이싱



* 파이썬 에서는 **-5 부터 256 까지만** `id` 가 동일하다.  그 이상은 다른 id 를 부여받는다. 

```python
a = 3  
b = 3
print(a == b)  # True

print(a is b)  # True    
print(id(a), id(b))  # => id 가 같다. 

x = 300
y = 300
print(x == y)  # True
print(x is y)  # False 
print(id(x), id(y))  # id 가 서로 다르다. 
```



### 연산자 우선순위 

1. `()`을 통한 grouping
2. Slicing `[:]`
3. Indexing `[0]`
4. 제곱연산자 `**`
5. 단항연산자 `+`, `-` (음수/양수 부호)
6. 산술연산자 `*`, `/`, `%`
7. 산술연산자 `+`, `-`
8. 비교연산자, `in`, `is`
9. `not`
10. `and`
11. `or`

=> 영어로 된 연산자들이 뒤에 있다.



### 기초 형변환(Type conversion, Typecasting)

### 암시적 형변환(Implicit Type Conversion)

파이썬 내부에서 알아서 자동으로 형변환이 이루어진다. 

- bool
- Numbers (int, float, complex)

```python
True + 3  # 4
```

* int + float => float

  int + complex => complex



### 명시적 형변환(Explicit Type Conversion)

 위의 상황을 제외하고는 모두 직접적을 타입을 변경할 수 있다. 

```python
1 + '등' # => 오류발생
str(1) + '등'  # '1등'
```

* 숫자를 문자로 바꿀 수는 있지만 문자를 숫자로 바꿀 수는 없다.  / 숫자들끼리는 얼마든지 가능

```python
int('a')  # 오류발생

a = '3.5'  # str 이기 때문에 int 로 변경 ㄴㄴ
int(a)
```



### 시퀀스자료형 



### list

* 리스트 만드는 방법

```python
list_1 = []   # 방법1
list_2 = list()   #방법2  

# 리스트의 값 찾는 방법
location[0]
```

* 리스트 안에는 모든 것이 들어갈 수 있다.  => int, bool, str, list, tuple, (set), range, 



### tuple

* immutalbe 
* 직접사용하기 보단 내부에서 사용하고 있다. 

```pyth
x, y = 1, 2
```



### range()

ragne(a, b) => a 부터 b-1 까지 (b 는 포함되지 않는다.) / a 없으면 0부터!

```python
range(0, 1, 0.01) # 마지막 부분(step) 에는 소숫점은 올 수가 없다. 에러 뜬다. 
```



#### 시퀀스에서 활용할 수 있는 연산자/함수

![1564291125075](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1564291125075.png)

* slicing

  ```python
  l = list(range(10))
  
  print(l[3:])   # 3 <= index <= 마지막
  print(l[3::2])  # 3 <= ind & step 2 <= 마지막
  print(l[:])   # 처음 <= index <= 마지막
  print(l[::-1])   # 뒤집기
  
  'apple'[::-1] # 시퀀스 자료형엔 모두 대괄호를 붙일 수 있다. 
  ```



### dict

* list 든  dict 든 꺼낼때는 항상 [] 이다. 
* 붕족된 key 값을 가질 수 없다. 
* `key`는 immutable한 모든 것이 가능하다. (불변값 : string, integer, float, boolean, tuple, range)



★ list, dict, set 은 mutable 하다. 그 외 나머지는 모두 immutable 하다. 

mutable 한 것은 모두 원본값이 바뀐다. 때문에 return 이 되지 않는다. 

immutable 한 것은 원본값이 바뀌지 않고 return 된다. 



## 02.control_of_flow

 

<조건문>

### if 문

* 반드시 if 뒤에는 조건식이 함께 해야한다. 그리고  :  도 필수 / 들여쓰기(4스페이스)

**조건 표현식**

```python
print('양수') if a > 0 else print('음수') 
```

* 가운데에 조건을 적고 맞을때의 조건을 왼쪽 틀렸을 때를 오른쪽에 적는다. 



<반복문>

### `while` 문

* 조건식이 True 의 경우을 반복해서 코드를 실행
* 반드시! 종료 조건을 설정해야한다. 안그러면 터진다. 
* 



### `for` 문

```python
for i in seq: 
    
# seq : sequence 순서가 있는 것이어야 한다. 
# => list, range, set, str
```



* `enumerate()` : 추가적인 변수 활용이 가능하다.  ??
* dict 일 때는 기본적으로 우선 key 이 출력된다. value 값을 출력하기 위해서는 [key] 하면된다. 



### `break`, `continue`, `else`



## 03.function  함수

* 함수는 짧아야하고 간결해야하고 자신의 것을 반복하고 있으면 안된다. 
* 매개변수 == parameter 파라미터 == 변수 == 인자
* return 값이 없으면 None을 반환한다. 
* `dir` 을 통해서 함수 목록을 확인 할 수 있다. 
* 함수에서 `print()` 로만으로 끝내면 타입은 `NoneType` 이 뜬다.  => `return` 이 있어야한다. 없으면 답은 0이다. 
* `return` == 반환하다 
* 위치를 통해서 인수를 파악한다. 
* 기본값을 주는 것을 뒤에 두어야한다. 기본값이 앞에 있으면 에러 발생 => 함수를 사용할 때, 변수를 지징했으면 다 지칭해야한다. 
* sep 다음에 end
* `*args` 가변인자 : class 'tuple'
* `**kwargs` 정의되지 않은 키워드 인자 : class 'dict' ??



* 함수의 인자(parameter)는 함수를 선언할 때 설정한 값이며, 인수(argument)는 함수를 호출할 때 넘겨주는 값이다. (HW)



### 이름공간 및 스코프(scope)??

L

E

G

B



### 재귀함수 recursive function

base case 가 있어야 하고 이것은 점점 범위가 줄어들어야한다. 또한 마지막으로 base case 는 n 이 1 될때 함수가 아니라 정수를 반환해야한다! 

=> for 문이 시간계산적으로는 더 빠르다 

​	그러나 재귀함수는 변수사용을 줄여줄 수 있다. 



## 04.data_structure

* `.()` 이렇게 생긴게 메소드



### 문자열 메소드

* `.join()` 

 괄호 안에는 for 문을 할 때 돌아갈 수 있는  list, range, set, str 이 가능 => 맨 앞뒤를 빼고 사이사이에 들어가게 된다. 



* `.find(a)` 

a 의 위치를 추출한다. (인덱스 자리) 

만약 없으면 -1 이 반환된다. 

​	`.index()` 

find() 랑 똑같은데 찾는 것이 없으면 오류 발생



* `split()` 

문자열을 띄어쓰기를 통해서 리스트로 반환한다.  



### 리스트 메소드 => mutable / return 없이 원본값이 바뀐다. 

* index, count 는 원본이 바뀌지 않는다. 나머지는 다 원본이 바뀐다. 



* `.append()` : 하나로 그냥 담긴다. 

  `.extend()` : 알아서 분해해서 넣는다. 여러개가 담긴다. 

  `.insert(i, '배고파')` : i 위치에 '배고파' 가 추가된다. 



* `.remove(a)` :  a 를 하나만 삭제한다. 앞에서 부터 / 그러나 만약 a 값이 없으면 오류발생

  `.pop(i)` : i 위치의 값이 출력되고 원본에서 그 값이 없어진다. 



* `.count(a)` : a 의 갯수를 세준다. 



* `.sort()` :  작은 수 부터 차례대로 나열해준다. / 원본 list 변경 / None을 리턴한다. 

  `sorted()` : 원본이 바뀌지 않는다.  => 내장 함수이다. 



**call by value**

만만 : 문자 숫자 TF  => 만만하니깐 복사가 막되고 막 줄수도 있어서 가질수도 있다. (=승용님 이클립스)



**call bt reference**

list, tupl, set, range 는  복사가 되는 것이 아니라 똑같은 id 를 가르키고 있는 것일 뿐이다. => mutable 한 애들만 가르킨다.  (=티비가 무거우니깐 들고 댕길 수 없고 가르킨다.)

* 얕은 복사
  * `.copy()` 
  * 슬라이싱 [:] 
  * 생서자 함수  A = list(c)

* 깊은 복사
  * `.deepcopy()` 





**List Comprehension**

```python
리스트 = [for문 돌았을때 추가될 값 계산식 for문]
```



### 딕셔너리 메소드

* `.get()` 



**dictionary comprehension**



### 세트 메소드

* `.remove()` : 없는 값을 제거할려고 할 경우 에러 발생

  `.discard()` : 에러가 없다. 



`map()`, `zip()`, `filter()`





## 07.OOP_basic

객체 지향 프로그래밍



* `__init__` : 인스턴스 객체를 생성할 때 자동으로 호출되는 메서드 이다.
* `__del__` : 인스턴스 객체가 소멸할 때 자동으로 호출되는 메서드이다.
* `__str__` : print를 사용할 때 인스턴스 객체를 호출하는 메서드이다.  (객체의 비공식적인 문자열을 출력할 떄 사용 => 사용자가 보기 쉬운 형태로 보여줄 때 사용)

* `__repr__` : 인스턴스 객체를 return 할 때 객체의 모습을 호출하는 메서드이다.  (객체의 공식적인 문자열을 출력할 때 사용 => 시스템이 해당 객체를 인식할 수 있게 할 때 사용)

  ex) '내 리스트에는 [1, 2, 3] 이 담겨있다.'





## 08. OOP_advanced



* 클래스의 변수 == 클래스의 속성

  인스턴스의 변수 == 인스턴스의 속성



#### 인스턴스 메서드

* 인스턴스가 사용할 메서드 
* 자동으로 인스턴스 객체가 self 가 된다.  



#### 클래스 메서드 

=> 인스턴스도 이 매서드를 받을 수는 있지만 사용은 하지 않는다. 클래스만 이 매서드를 사용하는 것이 바람직하다. 

* 클래스가 사용할 메서드 
* `@classmethod` (데코레이터)
* 첫 번쨰 인자로 클래스(`cls`) 를 받는다. 자동으로 클래스 객체가 `cls` 가 된다. 
* ?클래스 속성을 통해서 메서드가 실행된다?



#### 스태틱(정적) 메서드

=> 인스턴스도 이 매서드를 받을 수는 있지만 사용은 하지 않는다. 

* 첫번째 인자를 받지 않고 어떠한 인자도 자동으로 넘어가지 않는다... 
* `@statusmethod` 
* 



### 연산자 오버로딩(중복정의)

![1564313582531](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1564313582531.png)

### 상속

```python
issubclass(Student, Person)  # Student는 진짜 Person의 서브 클래스입니까?
isinstance(s, Person)  # s 는 할아버지의 자식이기도 하다... 
```

* `.super()` 