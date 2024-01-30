from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
from webdriver_manager.chrome import ChromeDriverManager

url = "https://section.cafe.naver.com/ca-fe/home"

# req = requests.get(url)
# html = req.text

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
html = driver.page_source

print(html)
