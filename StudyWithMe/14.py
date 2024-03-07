#함수를 알아보도록 하겠습니다.
def 함수 (string):
  print(string)

함수("안녕")
함수("Hi")

#더하기 함수
def 함수(a,b):
  print(a+b)

함수(43, 43)
함수(3524, 23)

#예를 들어
# def함수(문자열):
# print(문자열)
# 함수()를 실행시키면
# 함수에 정의와 다르게 함수를 호출하고 있기 때문에
# 이 함수를 호출할 땐 하나의 파라미터를 입력해줘야 한다.



#def 함수(a, b) :
#    print(a + b)

#함수("안녕", 3)

# TypeError: must be str, not int
# 또 위와 같은 함수가 실행되지 않는 이유는
# 위와같이 정의된 함수는 같은 타입 2개만을 받아 
# 덧셈을 하는 의도로 정의된 함수다.
# 하지만 위와같이 문자열인 안녕과 3을 더할 경우엔
# 더할 수 없다는 에러가 발생합니다.

#하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.

def print_with_smile(mystr):
  print(mystr  + ":D")
print_with_smile("hi")

#현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.

def print_upper_price(price):
  print(price + (price*0.3))

print_upper_price(300)

#두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라

def print_sum(a, b):
  print(a + b)

#두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.

def print_arithmetic_operation(a,b):
  print(a+b)
  print(a-b)
  print(a*b)
  print(a/b)

print_arithmetic_operation(50, 10)

#세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.

def print_max(a,b,c):
  maximum = 0
  if a>maximum:
    maximum = a
  if b>maximum:
    maximum = b
  if c>maximum:
    maximum = c
  print(maximum)

print_max(10, 2, 30)
    
  
    
  

