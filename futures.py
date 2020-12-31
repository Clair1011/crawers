"""
期貨盤後資料爬取範例，更換日期。
"""
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def crawl(date):
    r = requests.get('https://www.taifex.com.tw/cht/3/?queryType=1&doQuery=1&dateaddcnt=1&queryDate={}%2F{}%2F{}'.format(date.year, date.month, date.day))
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'lxml')
        print('successfully got data from', date)
    else:
        print('connection error')

date = datetime.today()
while True:
    crawl(date)
    date = date - timedelta(days=1)
    if date < datetime.today() - timedelta(days=5):
        break 