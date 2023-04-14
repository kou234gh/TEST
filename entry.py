import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import requests
import pandas as pd
import io
import gspread
import os
import numpy as np


"""
global variable======================================================================
"""

id = "477296"
pw = "entryentry"


def main(arg_date, driver):
    
    today = datetime.date.today()
    str_today = str(today)
    year = str_today.split("-")[0]
    month = str_today.split("-")[1]
    # date = str_today.split("-")[2]
    date = f"{arg_date:02}"
    
    items_list = ["Product Class", "銘柄", "Contract Issue", "売り順位", "参加者ID", "Participant", "ParticipantEN",
                  "売り取引高", "順位", "参加者ID", "Participant", "ParticipantEN", "買い取引高", f"{year}{month}{date}"]

    # ダウンロード先のディレクトリパスを指定
    download_dir = f"/Users/kou234/DEV/TEST/Selenium/target/jpx/strage/{year}-{month}-{date}"
    # print(download_dir)

    try:
        targets = driver.find_elements(
          by=By.XPATH, value=f"//tr/td[text()='{year}/{month}/{date}']/../td/a"
        )
        for i in range(4):
            # xl_file_names.append(str(targets[i].get_attribute("href")).split("/")[-1])
            xl_urls.append(targets[i].get_attribute("href")) 
    except:    
        return
    # print(xl_urls)

  
# arg_date = int(sys.argv[1])
options = webdriver.ChromeOptions()
# prefs = {'download.default_directory': download_dir}
# options.add_experimental_option('prefs', prefs)
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get(
    'https://www.jpx.co.jp/markets/derivatives/participant-volume/index.html')
time.sleep(2)

for the_date in range(arg_date,31):
    main(the_date, driver)
    
driver.quit()