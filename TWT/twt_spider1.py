# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 15:36:50 2018

@author: alfred
"""

import requests
from bs4 import BeautifulSoup
res=requests.get('https://news.twt.edu.cn/?c=default&a=secondpage&type=2')
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')
#print(soup)
for news in soup.select('.twt-card-block'):
    if len(news.select('a')) > 0:
        #print(news.select('a'))
        a=news.select('a')
        i=0
        for a[i] in a:
            for list in a[i]:
                print(a[i])
                #为什么只能爬侧边栏呢
            