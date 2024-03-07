#함수를 정의 하는 방법이다.
def print_text():
  print("비트코인")

#위처럼 정의한 뒤 함수를 호출 하는 방법은.
print_text()

#함수를 여러번 호출 하고 싶을땐.
for i in range(100):
  print_text()

#이처럼 100번을 출력하는 함수 자체를 완성하고 싶을땐
def print_texts():
  for i in range(100):
    print("도지코인")

## 함수가 정의되기전 함수를 호출하면 오류가 발생한다.


