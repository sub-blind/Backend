import requests
from bs4 import BeautifulSoup

header_user = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Whale/3.24.223.21 Safari/537.36"
}

# 접속하고자 하는 주소 입력
base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
search_url = input("검색어를 입력해주세요 : ")

url = base_url + search_url
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

titles = soup.select(".keyword_box_wrap.type_color")

for i in titles:
    name = i.select_one(".name.elss")
    category = i.select_one(".etc_area")
    etc = i.select_one(".title_link._cross_trigger._foryou_trigger")

    print(f"블로그 작성자는 : {name.text}")
    print(f"카테고리 : {category.text}")
    print(f"제목 : {etc.text}")
    print()
