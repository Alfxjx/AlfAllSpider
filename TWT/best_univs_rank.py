# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 18:51:04 2018

@author: 58497_000
"""

import requests
from bs4 import BeautifulSoup
import bs4

def GetHtmlText(url):
    try:
        r=requests.get(url, timeout=30)
        r.raise_for_status() # 产生异常信息
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""
    
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string]) 
            #代表第几个td标签的内容

def PrintUnivList(ulist, num):
    tplt = '{0:^10}\t{1:{3}^10}\t{2:^10}'
    tplt0 = '{0:^10}\t{1:{3}^8}\t{2:^9}' #调整一下标题和下方列表使之对齐
    #{3}指用format变量的第三个来填充，中文空格
    print(tplt0.format('排名','学校名称','分数',chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
    print("Suc"+str(num))

def main():
    uinfo =[]
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html' 
    html = GetHtmlText(url)
    fillUnivList(uinfo,html)
    PrintUnivList(uinfo,20)
    
main()    