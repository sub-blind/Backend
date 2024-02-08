from bs4 import BeautifulSoup
from selenium import webdriver

# 셀레니움에 다양한 옵션을 적용시키기 위한 패키지
from selenium.webdriver.chrome.options import Options

# 크롬 드라이버 매니저를 실행시키기 위해 설치해주는 패키지
from selenium.webdriver.chrome.service import Service

# 자동으로 크롬 드라이브를 최신으로 유지해주는 패키지
from webdriver_manager.chrome import ChromeDriverManager

# 클래스, 아이디, css_selector를 이용하고자 할때
from selenium.webdriver.common.by import By

# 키보드 입력
from selenium.webdriver.common.keys import Keys
import time

import pymysql
import re
from datetime import datetime

user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

options_ = Options()
options_.add_argument(f"User-Agent={user}")
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])


# 크롬 드라이버 매니저를 자동으로 설치되도록 실행시키는 코드
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options_)

url = "https://kream.co.kr/"
driver.get(url)
time.sleep(0.5)

driver.find_element(By.CSS_SELECTOR, ".search_btn_box").click()
time.sleep(0.5)

driver.find_element(
    By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus"
).send_keys("슈프림")
time.sleep(0.5)

driver.find_element(
    By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus"
).send_keys(Keys.ENTER)
time.sleep(0.5)


for i in range(50):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)


html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
items = soup.select(".item_inner")

num = 1

product_list = []
for i in items:
    product_name = i.select_one(".translated_name")
    if "후드" in product_name.text:
        category = "상의"
        product_brand = i.select_one(".product_info_brand.brand").text
        product_name_hood = i.select_one(".translated_name").text
        product_price = i.select_one(".amount").text

        print(num, product_name_hood, product_price)
        item = [category, product_brand, product_name_hood, product_price]
        product_list.append(item)
        num += 1


keywords = ["캡", "비니"]

for i in items:
    product_name = i.select_one(".translated_name")

    for keyword in keywords:
        if keyword in product_name.text:
            category = "모자"
            product_brand = i.select_one(".product_info_brand.brand").text
            product_name_hood = product_name.text
            product_price = i.select_one(".amount").text

            print(num, product_name_hood, product_price)
            item = [category, product_brand, product_name_hood, product_price]
            product_list.append(item)
            num += 1


keywords = ["백", "팩"]

for i in items:
    product_name = i.select_one(".translated_name")

    for keyword in keywords:
        if keyword in product_name.text:
            category = "가방"
            product_brand = i.select_one(".product_info_brand.brand").text
            product_name_hood = product_name.text
            product_price = i.select_one(".amount").text

            print(num, product_name_hood, product_price)
            item = [category, product_brand, product_name_hood, product_price]
            product_list.append(item)
            num += 1
driver.quit()

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="rla456852",
    db="kream",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)
conn.cursor()


def execute_query(conn, query, args=None):
    with conn.cursor() as cursor:
        cursor.execute(query, args or ())
        if query.strip().upper().startswith("SELECT"):
            return cursor.fetchall()
        else:
            conn.commit()


for i in product_list:
    execute_query(
        conn,
        "INSERT INTO kream (category, brand, product_name, price) VALUES (%s, %s, %s, %s)",
        (i[0], i[1], i[2], i[3]),
    )
