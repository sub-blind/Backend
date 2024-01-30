from selenium import webdriver
import time
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


header_user = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Whale/3.24.223.21 Safari/537.36"
}
# 접속하고자 하는 주소 입력
base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
search_url = input("검색어를 입력해주세요 : ")

url = base_url + search_url

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

time.sleep(1)

# 스크롤 코드
# driver.execute_script("window.scrollTo(0,4000)")
# time.sleep(2)

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)


html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
area = soup.select(".view_wrap")
count = 1
for i in area:
    ad = i.select_one(".link_ad")
    if ad:
        continue
    else:
        title = i.select_one(".title_link._cross_trigger")
        name = i.select_one(".user_info > a")
        print(count)
        print(name.text)
        print(title.text)
        print(title["href"])
        print()
        count += 1
