import requests
from bs4 import BeautifulSoup

header_user = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Whale/3.24.223.21 Safari/537.36"
}
# 접속하고자 하는 주소 입력
base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
search_url = input("검색어를 입력해주세요 : ")

url = base_url + search_url
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

titles = soup.select(".title_area")
name = soup.select(".user_info > a")

area = soup.select(".view_wrap")

for i in zip(titles, name):
    print("블로그 제목" + i[0].text)
    print("블로거" + i[1].text)
    print("링크" + i[0].a["href"])
    print()
