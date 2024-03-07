#딕셔너리
#우선 비어있는 딕셔너리를 만들어준다
temp = {}

icecream = {"바밤바":1500, "죠스바":1700, "월드콘":2300}
print(icecream)
#위 딕셔너리에 정보를 추가하는 방법
icecream["빠삐코"]=500
icecream["옥동자"]=1000

print(icecream)
print("조스바의 가격은 :",icecream["죠스바"])

#딕셔너리 안에 있는 값을 변경하는 방법

icecream["죠스바"] = 2500

print(icecream)

#딕셔너리 안에 있는 것을 삭제하는 법
del icecream["옥동자"]
print(icecream)

#딕셔너리 안에 원소를 2개씩 넣은 것이다.
mybag = {"바밤바":[1000, 20], "아이스바":[1500, 5], "스크류바":[1200, 15]}
print(mybag)

#이 원소 2 개중 하나만 출력하기를 원한다면.
print(mybag["바밤바"][0],"원")
print("남은 바밤바의 재고는",mybag["바밤바"][1],"개입니다.")

#원소를 추가하는 법
mybag["월드콘"] = [2000, 10]
print(mybag)

#딕셔너리의 keys() 메서드이다.
#결과를 보면 뒤에 value값이 아닌 key값만 리스트에 저장되어 나온다.
problem = {'빨강':100,'파랑':200, '노랑':300, '초록': 4000}
solution = list(problem.keys())
print(solution)

#딕셔너리 values() 메서드이다.
#결과를 보면 keys의 값이 아닌 뒤에 values들이 나온다,
problem2 = {'빨강2':200,'파랑2':400, '노랑2':600, '초록2':5000}
solution2 = list(problem2.values())
print(solution2)

#value들의 합계를 구했다.
print(sum(solution2))

#딕셔너리 update 메서드이다.
problem.update(problem2)
print(problem)

#zip과 dict 메소드

keys =("apple", "pear", "peach")
vals = (300,250,400)

result = dict(zip(keys,vals))
print(result)