from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.keys import

search_word = "アイス　美味しい"

# def test_eight_components():
driver = webdriver.Chrome()
time.sleep(3)

driver.get("https://sakura-eng.net")

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
# tag_body = driver.find_element(by=By.TAG_NAME, value="body")
# # tag_divs = tag_body.find_elements(by=By.TAG_NAME, value="div")
# tag_divs = tag_body.find_elements(by=By.CSS_SELECTOR, value="div[data-index]")
# 
# 
# # タイトル
# item_infos = {}
# 
# for tag_div in tag_divs:
# 
#     # タイトルの抽出
#     title_1 = tag_div.find_elements(by=By.CSS_SELECTOR, value="div>h2>a>span")
#     # 評価の抽出
#     reviews = tag_div.find_elements(
#         by=By.CSS_SELECTOR, value="div>span:nth-child(1)>span.a-size-base"
#     )
# 
#     if title_1 != [] and reviews != []:
#         #  titles.append(title_1[0])
#         item_infos.update({title_1[0].text: reviews[0].text})
# 
# 
# for info in item_infos:
#     print(
#         info + " : " + item_infos[info],
#         end="\n-------------------------------------------------\n",
#     )


driver.quit()