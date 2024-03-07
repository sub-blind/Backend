#오늘의 파이썬의 모듈에 대해 알아보자.
#datetime 모듈을 사용해서 현재 시간을 화면에 출력해보세요.
import datetime
import time
import os


now = datetime.datetime.now()
print(now)

#datetime 모듈의 now 함수의 리턴 값의 타입을 화면에 출력해보세요.
print(now, type(now))

#datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.
for day in range (5, 0, -1):
  delta = datetime.timedelta(days=day)
  date = now - delta
  print(date)

#현재시간을 얻어온 후 다음과 같은 포맷으로 시간을 출력해보세요. strftime 메서드를 사용하세요.
print(now.strftime("%H:%M:%S"))

#datetime.datetime.strptime 메서드를 사용하면 문자열 형식의 시간을 datetime.datetime 타입의 시간 값으로 만들어줍니다. "2022-08-21"의 문자열을 시간 타입으로 변환해보세요.

day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))

#time 모듈, datetime 모듈을 사용해서 1초에 한 번 현재 시간을 출력하는 코드를 작성하세요.
while True:
  now = datetime.datetime.now()
 # print(now)
 # time.sleep(1)

#os 모듈의 getcwd 함수를 호출하여 현재 디렉터리의 경로를 화면에 출력해보세요.

#import os
#a = os.getcwd()
#print(a)

