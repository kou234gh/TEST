# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:23:14 2022

@author: Tomita
"""

# import
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import chromedriver_binary
from selenium.common.exceptions import NoSuchElementException

# wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# selenium 4.0 ↑
from selenium.webdriver.common.by import By
from time import sleep


chrome_options = Options()
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options) 

HREFS = []

# URL開く
driver.get("https://www.amazon.co.jp/ref=nav_logo")
# 待機処理
# driver.implicitly_wait(10)
sleep(10)
wait = WebDriverWait(driver=driver, timeout=60)
 #検索窓 
Word = "キーボード"
driver.find_element(By.ID, "twotabsearchtextbox").send_keys(Word)
sleep(1)
driver.find_element(By.ID,"nav-search-submit-button").click()
 #商品URLの取得 
URLS = driver.find_elements(By.CSS_SELECTOR,"a.a-link-normal.s-no-outline")

for URL in URLS:
    URL = URL.get_attribute("href")
    print("[INFO] URL :", URL)
    HREFS.append(URL)
     #商品詳細の取得 

for HREF in HREFS:
    driver.get(HREF)
    # title
    title = driver.find_element(By.ID, "productTitle").text
    print("[INFO]  title :", title)
    # price 
    price = driver.find_element(By.CSS_SELECTOR, 'div.aok-align-center > span > span > span.a-price-whole').text
    print("[INFO]  price :", price)
    # img
    img = driver.find_element(By.XPATH, '//div[@id="imgTagWrapperId"]/img').get_attribute("src")
    print("[INFO]  img :", img)
    