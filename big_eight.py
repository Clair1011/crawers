'''
表格類型: 八大官股行庫買賣超爬蟲
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []
r = requests.get('https://chart.capital.com.tw/Chart/TWII/TAIEX11.aspx')
soup = BeautifulSoup(r.text, 'lxml')

#print(soup.prettify())

tables = soup.find_all('table', attrs = {'cellpadding': '2'})
for table in tables:
	trs = table.find_all('tr')
	for tr in trs:
		date, value, price = [td.text for td in tr.find_all('td')]
		if date == '日期':
			continue
		data.append([date, value, price])
# 轉成pd,以excel輸出
pf = pd.DataFrame(data, columns = ['日期', '八大行庫買賣超金額', '台指期'])
pf.to_excel('big_eight.xlsx')
pf.to_html('big_eight.html')