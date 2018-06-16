# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 19:39:24 2018

@author: 58497_000
"""

#淘宝搜索接口与翻页功能
import requests 
import re

def gethtmltext(url):
    try:
        r=requests.get(url, timeout=30)
        r.raise_for_status() # 产生异常信息
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""
    
def parsepage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html) #*?最小匹配
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1]) #去掉字符串的双引号
            title = eval(tlt[i].split(':')[1]) #朋友 是split not spilt !
            ilt.append([price, title])
    except:
        print("")
def printgoodslist(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt :
        count+=1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods = 'iphoneX'
    depth = 2
    start_url = 'https://s.taobao.com/search?q='+goods
    infolist = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = gethtmltext(url)
            parsepage(infolist, html)
        except:
            continue
    printgoodslist(infolist)
    
main()
