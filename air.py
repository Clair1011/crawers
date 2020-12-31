'''
爬取台灣空氣品質, 地區:AQI
'''
import requests
import pprint
import re

r = requests.get('https://airtw.epa.gov.tw/json/camera_ddl_pic/camera_ddl_pic_2020123012.json')
data = (r.json())
pprint.pprint(data)

try:
	for d in data:
		name = d['Name'] 
		if '(AQI=)' in name:  # 如AQI為空則跳下一迴
			continue

		elif 'AQI' not in name: 
			continue
		result = re.search(r'(.+)\(AQI=(\d+)', name) # 使用Regex

		site_name = result.group(1)  # 地區
		aqi = result.group(2)        # AQI

		print(site_name, aqi)
except AttributeError:
	print('sorry, site_name error')
