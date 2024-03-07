
from ast import Num
from locale import currency

print(3==5)
print(1<2)

if 4<3:
  print("hi")
else:
  print("bye")
  
#입력받은 문자열 출력하기--

user = input("입력:")
if user.islower():
  print(user.upper())
else:
  print(user.lower())


score = int(input("당신의 점수는 몇점 입니까:"))
#/score = int(score)

if 81 <= score <=100 :
  print("당신의 학점은 A")
elif 61 <= score <= 80 :
  print("당신의 학점은 B")
elif 41 <= score <= 60 :
  print("당신의 학점은 C")
elif 21 <= score <= 40 :
  print("당신의 학점은 D")
else : 
  print("당신의 학점은 F")

#/
#환율 = {"달러": 1167, "엔": 1.096, "유로": 1268, "위안": 171}
#man = input("입력:")
#Num, currency = user.split()
#print(float(Num) * 환율[currency],"원")

a = input("입력:")
b = input("입력:")
c = input("입력:")
if a<b and b>c:
  print(b)
elif b<c and c>a:
  print(c)
else :
  print(a)


phonecompany = input("당신의 전화번호를 입력해 주세요.")
phonecompany = phonecompany.split("-")[0]
if phonecompany == "011":
  print("당신은 SKT 사용자입니다.")
elif phonecompany == "016":
  print("당신은 KT 사용자입니다.")
elif phonecompany == "019":
  print("당신은 LGU 사용자입니다.")
else :
  print("알 수 없습니다.")


우편번호 = input("우편번호 : ")
우편번호 = 우편번호[:3]
if 우편번호 in ["010", "011", "012"]:
  print("강북구")
elif 우편번호 in ["013", "014", "015"]:
  print("도봉구")
else :
  print("노원구")



num = input("주민등록번호: ")
계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
        int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
        int(num[11])* 4 + int(num[12]) * 5
계산2 = 11 - (계산1 % 11)
계산3 = str(계산2)

if num[-1] == 계산3[-1]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")

import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")