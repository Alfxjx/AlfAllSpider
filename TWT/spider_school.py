# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 21:21:44 2018

@author: alfred
"""

import requests

from bs4 import BeautifulSoup
from datetime import datetime

url="http://news.gzcc.cn/html/xiaoyuanxinwen/"
res=requests.get(url)
res.encoding="utf-8"

soup=BeautifulSoup(res.text,"html.parser")
for news in soup.select("li"):
    if len(news.select(".news-list-title")) > 0:
        print(news.select(".news-list-title"))
print(1)
for news in soup.select("li"):
    if len(news.select(".news-list-title")) > 0:
        t=news.select('.news-list-title')[0].text
        dt=news.select('.news-list-info')[0].contents[0].text
        a = news.select('a')[0].attrs['href']
        print(t,dt,a,'\n')
for news in soup.select("li"):
 if len(news.select(".news-list-title")) > 0:
        a = news.select('a')[0].attrs['href']#新闻链接
        t = news.select('.news-list-title')[0].text#标题
        res1=requests.get(a)
        res1.encoding='utf-8'
        soup1=BeautifulSoup(res1.text,'html.parser')
        dt=soup1.select('.show-info')[0].text#时间
        print(t,'\n',dt,'\n')
        print(soup1.select('#content')[0].text)#内容
        t1=dt.lstrip('发布时间:')[:19]
        i=dt.find('摄影：')
        s=dt[dt.find('来源：'):].split()[0].lstrip('来源：')
        a = dt[dt.find('作者：'):].split()[0].lstrip('作者：')
        if i>0:
            p = dt[dt.find('摄影：'):].split()[0].lstrip('摄影：')
            print(t1,a,s,p)
        break
str = '2018-03-30 17:10:12 '
datetime.strptime(str,'%Y-%m-%d %H:%M:%S ')
print('\n\n',str)