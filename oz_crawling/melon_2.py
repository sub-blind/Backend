from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(2)

url = "http://www.melon.com/chart/"
driver.get(url)
time.sleep(5)

html_str = driver.page_source

soup = BeautifulSoup(html_str, "html.parser")

# 차트 항목을 가져와서 출력합니다.
chart_items = soup.select(".lst50")

print("Melon 차트 순위:")
for item in chart_items:
    # strip()은 공백을 제거해줍니다.
    rank = item.select_one(".rank").text.strip()
    title = item.select_one(".ellipsis.rank01").text.strip()
    artist = item.select_one(".checkEllipsis").text.strip()
    print(f"{rank}위 제목:{title}  가수:{artist}")


driver.quit()
