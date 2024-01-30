from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

options = Options()
user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
options.add_argument(f"User-Agent={user}")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("incognito")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "https://kream.co.kr/"
driver.get(url)

driver.find_element(By.CSS_SELECTOR, ".btn_search").click()
time.sleep(0.5)

driver.find_element(
    By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus"
).send_keys("슈프림")
time.sleep(0.1)

driver.find_element(
    By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus"
).send_keys(Keys.ENTER)
time.sleep(0.1)

for i in range(30):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".item_inner")
num = 1
for i in items:
    product_name = i.select_one(".translated_name")

    if "후드" in product_name.text:
        brand = i.select_one(".product_info_brand")
        names = i.select_one(".translated_name")
        price = i.select_one(".amount")

        print(f"Num.{num}")
        print(f"브랜드 :{brand.text}")
        print(f"제품명 : {names.text}")
        print(f"가격 : {price.text}")
        print()
        num += 1

driver.quit()
