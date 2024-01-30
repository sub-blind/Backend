from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = Options()
user = "Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36"
options.add_argument(f"User-Agent={user}")

options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("incognito")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "https://m2.melon.com/cds/main/mobile4web/main_list.htm"
driver.get(url)
time.sleep(1)

if driver.current_url != url:
    driver.get(url)

driver.find_element(By.LINK_TEXT, "닫기").click()
time.sleep(0.2)

driver.find_element(By.LINK_TEXT, "멜론차트").click()
time.sleep(0.2)

more_btn = driver.find_elements(By.CSS_SELECTOR, "#moreBtn")[1].click()

# 노래 순위
# 노래 제목
# 가수 이름
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".list_item")
num = 1
print("멜론차트 TOP100위")
for i in items:
    singer = i.select_one(".name.ellipsis")
    title = i.select_one(".title.ellipsis")
    print(f"{num}위")
    print(f"제목:{title.text.strip()}")
    print(f"가수:{singer.text.strip()}")
    print()
    num += 1

# driver.quit()
