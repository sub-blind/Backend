data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
#수수료를 0.014 %로 가정할 때, 각 가격에 수수료를 포함한 가격을 한라인에 하나씩 출력하라.

for line in data:
  for column in line:  
    print(column * 1.00014)
  print("-----")  


#위의 결과물을 일차원 배열로 저장하는 방법
result =  [] #빈 배열을 만들어준다.
for line in data:
  for column in line:  
    #데이터를 0번부터 배열에 하나씩 넣어준다.
    result.append(column * 1.00014)
print(result)

#맨위 결과물을 2차원 배열로 저장하는 방법.
result = []
for line in data:
  sub = []
  for column in line:  
    sub.append(column * 1.00014)
  result.append(sub)
print(result)

#각 배열에서 [3]의 값만 출력하는 방법
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for row in ohlc:
  print(row[3])

#[3]이 150원보다 큰 경우를 출력하는 방법.
for row in ohlc[1:]:
  if (row[3] > 150):
    print(row[3])

#같거나 클때
for row in ohlc[1:]:
  if (row[3] >= row[0]):
    print(row[3])

#고가 - 저가 출력
volatility = []#빈 배열을 만들어준다.
for row in ohlc[1:]:
    #데이터를 0번부터 배열에 하나씩 넣어준다.
    volatility.append(row[1]-row[2])
print(volatility)

#종가가 시가보다 높은 날만 출력
for row in ohlc[1:]:
  if (row[3] > row[0]):
    print(row[1]-row[2])

#시가에 매수 해서 종가에 팔앗을때의 수익금을 계산
sum = 0
for row in ohlc[1:]:
  sum += row[3]-row[0]
print(sum)