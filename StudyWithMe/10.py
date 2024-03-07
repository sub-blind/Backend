#리스트 데이터를 출력하는 방법.
#for문을 섞어서 출력하는 법.
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
  print(price_list[i])

price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
  print(i,price_list[i])

#숫자를 역순으로 출력하는 법.
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
  print((len(price_list)-1)-i,price_list[i])

#100부터 10씩 더해서 출력하는 방법.
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
  for i in range(1,4):
    print(90 + 10*i ,price_list[i])

#리스트를 2개씩
list = ["가", "나", "다", "라"]
for i in range(1, len(list)):
  print(list[i-1], list[i])

# 리스트를 3개씩
list = ["가", "나", "다", "라", "마"]
for i in range(2, len(list)):
  print(list[i-2], list[i-1], list[i])

#우측값과의 차분값을 두하는 것
list = [100, 200, 400, 800]
for i in range(1, len(list)):
  print(abs(list[i]-list[i-1]))

#3개의 평균을 출력하는 방법
list = [100, 200, 400, 800, 1000, 1300]
for i in range(1, len(list)-1):
  print(abs(list[i-1] + list[i] + list[i+1]) / 3)

#두개의 고가와 저가가 정해져 있을때
#그 둘의 차이를 하나의 리스트에 저장한뒤
#그것을 출력한다.
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility =[]
for i in range(len(low_prices)):
  volatility.append(high_prices[i]- low_prices[i])
  print(volatility[i], end=' ')
  


