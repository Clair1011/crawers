import requests
from bs4 import BeautifulSoup

#三種BeautifulSoup常用的function: find, find_all, select (CSS slector)
#第三種寫法 select
root_url = 'https://disp.cc/b/' # 根目錄網址

r = requests.get('https://disp.cc/b/pttHot')
soup = BeautifulSoup(r.text, 'html.parser')

for span in soup.select('#list span.listTitle'):
	href = span.find('a').get('href')
	if href =='796-59l9':  #跳過開版成功連結
		break
	title = span.text
	url = root_url + href
	print(f'{title}\n{url}')


# span = soup.find_all("span", class_="listTitle")
# for spans in span:
# 	url = root_url + spans.find('a').get('href')
# 	title = spans.text
# 	if spans.find('a').get('href') =='796-59l9':  #跳過開版成功連結
# 		break
# 	print(f'{title}\n, {url}')
	
#print([t.text for t in titles])

