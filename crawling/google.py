import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
from itertools import repeat
import openpyxl
 
driver = webdriver.Chrome(executable_path='/Users/jangseojin/Desktop/service-playground/crawling/selenium/chromedriver')
url = 'https://www.melon.com/chart/index.htm' # 멜론차트 페이지
driver.get(url)

html = driver.page_source # 드라이버 현재 페이지의 html 정보 가져오기 
soup = BeautifulSoup(html, 'lxml')
    
titles = soup.select('div.ellipsis.rank01')
singers = soup.select('div.ellipsis.rank02 > span.checkEllipsis')

title = [title.text.strip('\n') for title in titles]
singer = [singer.text for singer in singers]

result = pd.DataFrame(data=zip(range(1,101),title, singer), columns=['Rank', 'Title', 'Singer'])
    
result['Site'] = 'Melon'
result = result[['Site', 'Rank', 'Title', 'Singer']]
print(result.head())

result.to_excel('멜론차트크롤링.xlsx', encoding='utf-8', index=False)
