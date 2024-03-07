#아래 코드를 실행한 결과를 예상하라.
def n_plus_1 (n) :
    result = n + 1
    print (result)
n_plus_1(3)
#print (result)

#이러한 코드가 있다면 이 코드는 실행되지 않을 것이다.
#왜냐하면 함수 내부에서 result라는 이름으로 사용된 변수를 함수 밖에서 접근하는 것은 불가 하기때문디다.

#문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
def make_url(string):
  url = "www." + string + ".com"
  return url

result = make_url("naver")
print(result)

#문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
def make_list(string):
  list = []
  for i in string:
    list.append(i)
  return list

result = make_list("abcd")
print(result)

#숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.

def pickup_even(string):
  list = []
  for i in string:
    if i % 2 == 0:
      list.append(i)
  return list

result = pickup_even([3,4,5,6,7,8])
print(result)

#콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.

def convert_int(string):
  return int(string.replace(',',''))

a = convert_int("1,234,567")
print (a)

#아래 코드의 실행 결과를 예측하라.

def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)

#  4번 라인에서 함수로 10이 입력돼서 14가 반환됩니다. a 변수에는 14가 저장됩니다.
#  5번 라인에서 함수로 14가 입력돼서 18이 반환됩니다.
#  변수 b에는 18이 바인딩됩니다.
#  6번 라인에서 함수로 18가 입력돼서 22가 반환됩니다.
#  변수 c에는 22가 바인딩됩니다.


#아래 코드의 실행 결과를 예측하라.

def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)

#  함수가 여러번 중첩돼 있습니다. 안쪽 부터 차례로 해석하면 됩니다.
#  함수(10)의 결과 14, 함수(14) 결과 18, 함수(18) 결과 22 가 반환됩니다.
#  결국 36번과 동일한 코드를 축약해서 작성해 놓은 겁니다.


#아래 코드의 실행 결과를 예측하라.

def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)

#  7번 라인에서 함수1으로 10이 입력돼서 14가 반환됩니다.
#  a 변수에는 14가 저장됩니다.
#  8번 라인에서 함수2로 a에 저장된 14가 입력돼서 140이 반환됩니다.
#  변수 c에는 140이 바인딩됩니다.


#아래 코드의 실행 결과를 예측하라.

def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)

#  8번 함수2가 호출됩니다. 4번 라인으로 파이썬 인터프리터는 이동하고 이때 num에는 10이 바인딩됩니다.
#  5번 라인 코드를 실행하면 num이 12로 업데이트 됩니다.
#  6번라인의 코드를 실행하려고 하는데, 함수1이 호출됩니다.
#  1번 라인의 함수 정의부로 이동하며 num 값은 12로 바인딩됩니다.
#  2번 라인의 코드가 실행돼서 16이 반환됩니다.
#  함수1의 동작을 끝마치고 함수 2의 6번 라인으로 돌아오고 함수2도 return을 만나면서 16을 반환합니다.
#  8번 라인으로 돌아와 c 변수에는 16을 바인딩합니다.