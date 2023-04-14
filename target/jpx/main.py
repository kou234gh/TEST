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


    """
    スクレイピング======================================================================
    ウェブ上からローカルへ
    """
    # サイト上の該当箇所を日付を元に特定する
    xl_urls = []
   # ['https://www.jpx.co.jp/markets/derivatives/participant-volume/cg27su0000003sen-att/20230328_volume_by_participant_night.xlsx',
    # 'https://www.jpx.co.jp/markets/derivatives/participant-volume/cg27su0000003sen-att/20230328_volume_by_participant_night_J-NET.xlsx',
    # 'https://www.jpx.co.jp/markets/derivatives/participant-volume/cg27su0000003sen-att/20230328_volume_by_participant_whole_day.xlsx',
    # 'https://www.jpx.co.jp/markets/derivatives/participant-volume/cg27su0000003sen-att/20230328_volume_by_participant_whole_day_J-NET.xlsx']

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


    """
    保存したエクセルをDataframe、それからスプレッドシートに======================================================================
    """
     #   to spread sheet
    SPREADSHEET_ID = "1eULApo8M6wLKaUbS-m7Ai_LPGqH-UH1Qj7MIZUuBpmY"
    gc = gspread.service_account(filename = 'credentials.json')
    sh = gc.open_by_key(SPREADSHEET_ID)
    ss_name = f"{year}{month}{date}"
    try:
        worksheet = sh.add_worksheet(rows=1000, cols=30, title=ss_name)
        worksheet = sh.worksheet(ss_name)
    except:
        return

    for xl_url in xl_urls:
      response = requests.get(xl_url)
      content = response.content
      # バイナリデータをパースしてExcelファイルを読み込む
      xls = pd.ExcelFile(io.BytesIO(content))
      df_excel = pd.read_excel(xls, 0)
        # ファイル名の列を入れたい
      df = df_excel.assign(filename = str(xl_url).split("/")[-1])
        # 切り取り
      df = df.iloc[7:, :14]
      df.replace([np.inf, -np.inf, np.nan], "~", inplace=True)
      worksheet.append_rows(df.values.tolist())
   
    worksheet.insert_row(items_list)
  
arg_date = int(sys.argv[1])
options = webdriver.ChromeOptions()
# prefs = {'download.default_directory': download_dir}
# options.add_experimental_option('prefs', prefs)
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get(
    'https://www.jpx.co.jp/markets/derivatives/participant-volume/index.html')
time.sleep(2)

for the_date in range(arg_date,31):
    main(the_date, driver)
    
driver.quit()