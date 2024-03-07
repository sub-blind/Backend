#/
#num = input("주민등록번호: ")
#계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
#        int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
#        int(num[11])* 4 + int(num[12]) * 5
#계산2 = 11 - (계산1 % 11)
#계산3 = str(계산2)
#
#if num[-1] == 계산3[-1]:
#    print("유효한 주민등록번호입니다.")
#else:
#    print("유효하지 않은 주민등록번호입니다.")
#

#for문

과일 = ["사과", "배", "복숭아", "자두"]
for fruit in 과일:
  print(fruit)
  #과일의 자료수는 4이기 때문에
  # ####이 4번 출력됨
  print("####")

변수 = "A"
print("출력", 변수)
변수 = "B"
print("출력", 변수)
변수 = "C"
print("출력", 변수)

변수 = "A"
print("출력", 변수.lower())
변수 = "B"
print("출력", 변수.lower())
변수 = "C"
print("출력", 변수.lower())


for 배열 in [10,20,30]:
  print(배열)
  print("-----")

for 배열2 in ["----",10,20,30]:
  print(배열2)

for 리스트 in [100,200,300]:
  print(리스트 + 10)

for 음식 in ["피자", "치킨", "짜장면"]:
  print("제가 좋아하는 음식은 " + 음식)
  #음식글자수 = len(음식)
  #print(음식글자수)
  print(음식, len(음식))
  print(음식[0])
