for i in range(100):
  print(i)

#print(list(range(2002, 2050, 4)))
for x in range(2002, 2050, 4):
  print(x)

#range를 이용해 범위 안에서 3의 배수를 찾는 것
for x in range(1, 30, 3):
  print(x)

#99부터 0까지 1씩 감소한는 방법
for y in range(100):
  print(99-y)

#소숫점값을 출력하는 방법
for z in range(10):
  print(z / 10)

#구구단
for i in range(1, 10):
  print(3,"*", i, "=", 3 * i)

#구구단에서 홀수 번째를 출력하는 방법
for i in range(1, 10, 2):
  print(3,"*",i,"=",3*i)

#또는
num = 3
for i in range(1, 10) :
    if i % 2 == 1 :
        print (num, "x", i, " = ", num * i)

#1 ~10 까지의 숫자 합을 구하는 방법
#들여쓰기를 잘 하자.
a=0
for i in range(1,11):
  a += i
print(a)

#1~10의 수중 홀수만을 더한다.
a=0
for i in range(1,11):
  if  i % 2 == 1:
    a += i
print(a)

#1~10의 수중 모든수를 곱한다.
a=1
for i in range(1,11):
    a *= i
print(a)
