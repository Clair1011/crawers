#爬取pchome 曲面螢幕名稱及價格

import requests
import pprint

r = requests.get('https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=%E6%9B%B2%E9%9D%A2%E8%9E%A2%E5%B9%95&page=1&sort=sale/dc')

data = r.json()

#print(data['prods'][0]['name'])

for d in data['prods']:
	print(d['name'])
	print(d['price'])