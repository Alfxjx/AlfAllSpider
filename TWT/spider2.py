# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 21:10:10 2018

@author: alfred
"""



import requests
from bs4 import BeautifulSoup
res=requests.get('http://news.gzcc.cn/html/xiaoyuanxinwen/')
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')
print(soup.text)
'''for news in soup.select("li"):
    if len(news.select(".news-list-title")) > 0:
        t=news.select('.news-list-title')[0].text
        dt=news.select('.news-list-info')[0].contents[0].text
        a = news.select('a')[0].attrs['href']
        print(t,dt,a,'\n')'''

for news in soup.select('li'):
    if len(news.select(".news-list-title")) > 0:
        a=news.select('.news-list-title')[0].text
        print(a)
    if(len(news.select('h3'))>0):
        h3= news.select('h3')[0].text
        time=news.select('.time')[0].text
        a=news.select('a')[0]['href']
        print(time,h3,a)




