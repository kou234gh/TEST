# http://books.toscrape.com/
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.keys import

# def test_eight_components():
driver = webdriver.Chrome()
time.sleep(3)

driver.get("http://books.toscrape.com/")

# chromedriver = 'chromedriver.exe'
# driver = webdriver.Chrome(executable_path=chromedriver, )
try:
    wait = WebDriverWait(driver, 30)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
except TimeoutException:
    print("アラートは発生しませんでした")
except Exception as e:
    print(e)
# serch_box = driver.find_element(by=By.ID, value="twotabsearchtextbox")
# serch_box.send_keys(search_word)
# submit_button = driver.find_element(by=By.ID, value="nav-search-submit-button")
# submit_button.click()
# 検索結果出てくる

# 商品リストを取得する
tag_body = driver.find_element(by=By.TAG_NAME, value="body")
# tag_divs = tag_body.find_elements(by=By.TAG_NAME, value="div")
tag_divs = tag_body.find_elements(by=By.CSS_SELECTOR, value="div[data-index]")
title_links = tag_body.find_elements(
    by=By.CSS_SELECTOR, value="div > ol > li > article > h3 > a")

with open('readme.txt', 'a') as f:

    for title_link in title_links:
        new_page = title_link.click()

        full_title = driver.find_element(
            by=By.CSS_SELECTOR, value="#content_inner > article > div > div > h1").text
        upc = driver.find_element(
            by=By.CSS_SELECTOR, value="#content_inner > article > table > tbody > tr:nth-child(1) > td").text
        price = driver.find_element(
            by=By.CSS_SELECTOR, value="#content_inner > article > div > div > p.price_color").text

        f.write(
            "Title : "+full_title+"\n" +
            "Price : "+price+"\n" +
            "UPC : "+upc+"\n" +
            "--------------------------------"+"\n"
        )
        driver.back()
driver.quit()
