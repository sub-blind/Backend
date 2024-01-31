import requests
from bs4 import BeautifulSoup

header_user = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}

base_url = "https://www.melon.com/chart/month/index.htm"

req = requests.get(base_url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

# num = 1 << 곡 순위 할 수 있는 다른 방법
lst_all = soup.find_all(class_=["lst50", "lst100"])

for i in lst_all:
    up = i.select_one(".up")

    if up:
        title = i.select_one(".ellipsis.rank01 a")
        name = i.select_one(".ellipsis.rank02 a")
        rank = i.select_one(".wrap.t_center .rank")
        album = i.select_one(".ellipsis.rank03 a")

        print(f"순위: {rank.text}위")
        print(f"전 달 대비: {up.text}순위 상승")
        print(f"제목: {title.text}")
        print(f"가수: {name.text}")
        print(f"앨범: {album.text}")
        print()
