import requests
from bs4 import BeautifulSoup

# 접속하고자 하는 주소 입력
url = "https://www.naver.com"


# get방식을 이용홰 서버에게 resource(자원 = html, css)을 보내도록 요청한다. 데이터 수신이 가능하게 됨.
# request의 경우 거의 처음에 사용되고 이후에는 잘 사용되지 않음, 왜냐면 정적인 사이트에서는 HTML 코드가 변하지 않기 떄문이다.
# requests로 넘어오는 내용은 예를 들어 네이버 화면에서 마우스 오른쪽 버튼을 누른 뒤 페이지 소스 보기로 보이는 내용과 동일
req = requests.get(url)


# GET방식을 통해 가져온 많은 데이터 중 우리가 필요한건 텍스트 형태의 자료(HTML 포함되어 있음)
html = req.text


# beautifulsoup이라는 함수에는 2가지 파라미터를 넣는데 html, "html.parser" 를 넣는다.
# 이걸 넣으면 파서(컴퓨터가 이해할 수 있도록 html을 분해해서 트리구조로 변경하는것을 진행
soup = BeautifulSoup(html, "html.parser")

# select_one  원하는 태그를 찾을 수 있는데 기준은 클래스명, id, 태그도 가능하다. 클래스 경우 앞에 . 을 넣고 ID는 앞에 #을 넣는다.
query = soup.select_one("#query")
print(query)
