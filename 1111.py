import requests
from bs4 import BeautifulSoup
import pandas as pd



url = 'https://www.1111.com.tw/search/job?ks=%E9%9B%BB%E8%85%A6&fs=1&page='
html=requests.get(url)
soup = BeautifulSoup(html.text,'html.parser')
tem = soup.find('select',class_="custom-select").text #總頁數
page = int(tem.replace('1 / ','')) #取得page變數值150
if page > 15:# 最多取15頁資料
    page = 15 
for i in range(page):
    urla = url + str(i+1)
    html = requests.get(urla)
    soup = BeautifulSoup(html.text,'html.parser')
    job = soup.select('.it-md') #擷取職缺資料
    for j in job:
        work = j.find('div',class_='position0 jb-position0').a.text #擷取職務名稱
        
        site = j.find('a',class_='text-truncate position0Link mobileItemClick').get('href') #擷取工作網址
            
        company = j.find('div',class_='d-none').a.text #擷取公司名稱
        companysort = j.find('span',class_='d-none d-md-block').text.replace('｜','') #擷取公司類別 並將｜換成空白
        temp = j.find('div',class_='text-truncate needs').select('span') #擷取薪資、工作經驗、學歷
        area = temp[0].text #擷取工作地點
        salary = temp[1].text #月薪
        experiment = temp[2].text #經驗
        school = temp[3].text #學歷
        #擷取工作內容
        tema = j.find('div',class_='col-12 jbInfoTxt UnExtension').select('p')
        content = ''
        for k in range(len(tema)):
            content = content + tema[k].text
            
            dfmono = pd.DataFrame([{'職務名稱':work,
                                    '工作網址':site,
                                    '公司名稱':company,
                                    '公司類別':companysort,
                                    '薪資':salary,
                                    '工作經驗':experiment,
                                    '學歷':school,
                                    '工作內容':content }],
                                 
                                  
                                 )
            #df.append(dfmono) #將單筆pandas的DataFrame格式職缺加入df串列中
    #print(dfmono)
            df1 = dfmono[['職務名稱','薪資','學歷','工作內容','工作網址']]
            df2=df1.head(5)
            print(df2)