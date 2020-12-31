"""
目標：從 Dcard 論壇中，找出 1 篇 (可以 人工 先選好) 
超過 5000 心情數的文章，然後爬取裡面的留言，並選擇性地做基本分析。
由於每一則留言都有兩個部分：使用者名稱、留言。

爬取自己選定的該篇文章所有留言，並裝入字典，
key 為使用者名稱，value 為清單中裝著 該使用者的所有留言內容。

最後以這樣的資料結構，依照 使用者名稱的 留言數 排行出來，即可看看是哪個使用者名稱 留言數最多。
(分析目標不一定為個人，只以使用者名稱做歸類)
"""
import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.dcard.tw/f/mood/p/234511181")

soup = BeautifulSoup(html.text, 'html.parser')

names = soup.find_all('div', 'sc-7fxob4-4 eiOVFy')
leaves = soup.find_all('div', 'phqjxq-0 frrmdi')

dic1 = []
for name in names:
    n = name.text
    dic1.append(n.strip())

dic2 = []
for leave in leaves:
    l = leave.text
    dic2.append(l.strip())

data = dict(zip(dic1, dic2))

for d in data:
    print(d,len(data[d]))