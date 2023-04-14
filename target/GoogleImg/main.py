import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Google画像検索のURL
search_url = "https://www.google.com/imghp"

# 画像ファイル名
image_file = "280923391_811114413611397_929858969864101237_nのコピー.jpg"


# Chromeドライバーのオプション
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# Chromeドライバーの起動
driver = webdriver.Chrome(options=chrome_options)

# Google画像検索のウェブページにアクセス
driver.get(search_url)
driver.find_elements(by=By.XPATH, value="//div[@aria-label='画像で検索']")[0].click()

# 要素が表示されるまで待つ
wait1 = WebDriverWait(driver, 10)
upload_box = wait1.until(EC.presence_of_element_located((By.XPATH, "//input[@name='encoded_image']")))
upload_box.send_keys(os.getcwd() + "/" + image_file)
# 画像をアップロードする
  
time.sleep(10)
# 類似画像のリンクを取得する

similar_images_link = driver.find_element(by=By.XPATH ,value="//a[text()='Visually similar images']")
similar_images_link.click()
time.sleep(15)

# 類似画像のウェブページにアクセス
similar_images_url = driver.current_url
driver.get(similar_images_url)
time.sleep(15)

# 画像を保存するdriver.
images = driver.find_elements(by=By.XPATH ,value="//img[@class='rg_i']")
for i, image in enumerate(images):
    src = image.get_attribute('src')
    if src.startswith('http') and i < 10:
        with open(f"similar_image_{i}.jpg", "wb") as f:
            f.write(driver.execute_script("return arguments[0].src", image).split(",")[1].decode('base64'))
time.sleep(5)

# ブラウザを終了する
driver.quit()
