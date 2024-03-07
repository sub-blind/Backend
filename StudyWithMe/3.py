print("python study")
#오늘은 다양한 메서드에 대해 알아보고자 한다.

text = "btc_krw"
#upper 메서드는 소문자를 대문자로 바꾸어 주는 메서드이다
new_text = text.upper()
print(new_text)

#upper 메서드는 대문자를 소문자로 바꾸어 주는 메서드이다
new_text2 = text.lower()
print(new_text2)

#capitalize 첫글자만 대문자로 다음은 소문자로 반환하는 메서드
text = text.capitalize()
print(text)

#split은 스플릿을 기준으로 문자열을 나누는 것이다.
a = "hi my name is jaeseob"
new_a = a.split()
print(new_a)

b = "hi-my-name-is-jaeseob"
new_b = b.split("-")
print(new_b)

#rstrip은 문자열의 오른쪽 공백을 제거해준다.
c = "abcd        "
new_c = c.rstrip()
print(new_c)



#파이썬의 리스트에 대해 알아보자
movie_list = ["김", "재", "섭"]
print(movie_list)

#insert는 원소를( 인덱스의 위치에 추가 시켜 줍니다.)
movie_list.insert(1, "유")
print(movie_list)

#del은 원소를 삭제 시켜줍니다
del movie_list[1]
del movie_list[1]
print(movie_list)

#리스트끼리의 덧셈
list1 = ["오", "늘", "도"]
list2 = ["힘", "내", "자"]

list3 = list1+list2
print(list3)

#list의 최댓값과 최솟값 함계
#max(), min(), sum()

list_num = [12, 23, 7, 34, 2]
print("작은 수 :",min(list_num))
print("큰 수 :",max(list_num))
print("합계 :",sum(list_num))

#리시트의 저장되어 있는 데이터의 개수를 구하는 메서드
#len()

list_len = [12, 23, 7, 34, 2, 2, 1, 12, 12, 33, 23, 3]
print("리스트의 길이는:", len(list_len))

#리시트의 원소들이 숫자일때 평균을 구하는 메서드는 없기에 sum/ len를 쓴다
#sum/len
list_aver = [12, 23, 7, 34, 2, 2, 1, 12, 12, 33, 23, 3, 333]

average = sum(list_aver)/len(list_aver)
print(int(average))

#슬라이싱
price = ['123', 1, 2, 3, 4, 5]
print(price[1:])

#골라서 출력하기.
company = ["삼성", "LG", "kakao"]
print(company[0], company[2])

#바인딩 되어 있는 것들을 바꿔주는 메서드
#join
print(company)
print(" ".join(company))
print("/".join(company))
print(" 그리고 ".join(company))
print("\n".join(company))

#string으로 되어 있는 문자열을 리스트로 저장하는 법
string = "삼성전자/네이버/카카오/쿠팡/배달의민족"
solution = string.split("/")
print(solution)

#리스트의 있는 값을 오름차순으로 정렬하는 메서드
#sort()
#sorted()
data = [1, 3, 6, 1, 21, 4]
data.sort()
print(data)
data2 = sorted(data)
print(data2)

#튜플은 ()로 정의하는 것이다.
variable = ()
print(type(variable))

myname = ("김", "재", "섭")
print(type(myname))

mytuple = (1)
print(type(mytuple))

#튜플은 원소의 값을 변경할 수 없다.
myinterest = ('책읽기', '차마시기', '음악감상')
data = list(myinterest)
print(data)

data = tuple(data)
print(data)

#range 함수
data = tuple(range(2,100,2))
print(data)