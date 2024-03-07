#음수를 출력한다.
리스트 = [3, -20, -3, 44]
for 음수 in 리스트:
  if 음수 < 0:
    print(음수)

#조건을 주어 3의 배수이면서 20이하인 것을 출력
리스트2 = [13, 21, 12, 14, 30, 18]
for 음수 in 리스트2:
  if 음수 % 3 == 0 and 음수 < 20:
    print(음수)

#길이가 3이상인 리스트만 출력한다.
리스트3 = ["I", "study", "python", "language", "!"]
for 음수 in 리스트3:
  if len(음수) >= 3:
    print(음수)


#isupper를 통해 대문자를 판별해 출력한다.
리스트4 = ["A","b","c","D"]
for 대문자 in 리스트4:
  if 대문자.isupper():
    print(대문자)

#소문자를 출력할때에는 not을 써주면 된다.
리스트5 = ["A","b","c","D"]
for 대문자 in 리스트5:
  if not 대문자.isupper():
    print(대문자)

#첫글자를 대문자로 변경해서 출력하는 방법.
리스트6 = ['dog', 'cat', 'parrot']
for 변수 in 리스트6:
  첫글자 = 변수[0]
  대문자 = 첫글자.upper()
  print(대문자 + 변수[1:])

#split()을 이용해 .을 기준으로 앞부분만 출력해낸다.
리스트7 = ['hello.py', 'ex01.py', 'intro.hwp']
for 변수 in 리스트7:
  첫부분 = 변수.split('.')
  print(첫부분[0])

#.h인 파일을 split으로 자른 뒤에 찾아낸다.
리스트8 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트8:
  부분 = 변수.split('.')
  if 부분[1] == 'h':
    print(변수)

#조건을 2가지 준다 .h 이거나 .c인 파일을 출력
리스트9 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트9:
  split = 변수.split(".")
  if (split[1] == "h") or (split[1] == "c"):
    print(변수)


