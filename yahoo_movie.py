"""
Yahoo電影排行
['本週', '上週', '片名', '上映日期', '預告片', '網友滿意度']
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
r = requests.get('https://movies.yahoo.com.tw/chart.html')
movie = BeautifulSoup(r.text,'html.parser')

all = movie.find('div', class_='rank_list table rankstyle1')

rows = all.find_all('div', class_='tr') # parser columns 
columns = list(rows.pop(0).stripped_strings)  # get strings and convert into list
print (columns)   # ['本週', '上週', '片名', '上映日期', '預告片', '網友滿意度']

content = []
for row in rows:
	thisweek_rank = row.find_next('div', attrs = {'class':'td'})
	updown = thisweek_rank.find_next('div', attrs = {'class':'td'})
	lastweek_rank = updown.find_next('div', attrs = {'class':'td'})

	if thisweek_rank.string == str(1):
		movie_title = lastweek_rank.find_next('h2')
	else:
		movie_title = lastweek_rank.find_next('div', class_='rank_txt')

	release_date = movie_title.find_next('div', attrs = {'class':'td'})
	trailer = release_date.find_next('div', attrs = {'class':'td'})
	trailer_address = trailer.find('a').get('href')
	stars = row.find('h6', attrs = {'class':'count'})
	# replace None with empty string ''
	lastweek_rank = lastweek_rank.string if lastweek_rank.string else ''
	c = [thisweek_rank.string, lastweek_rank, movie_title.string, release_date.string, trailer_address, stars.string]
	#print(c)
	content.append(c)
# convert to panda 
df = pd.DataFrame(content, columns=columns)
print(df)


