from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


url = "https://naver.com/"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

query = soup.select_one("#query")
print(query)
