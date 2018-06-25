import requests
from bs4 import BeautifulSoup
#import traceback
import re 

def gethtmlptext(url, code = 'utf-8' ):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""
        
def getstocklist(lst, stockurl):
	html = gethtmlptext(stockurl, 'GB2312')
	soup = BeautifulSoup(html, 'html.parser')
	a = soup.find_all('a')
	for i in a :
		try:
			href = i.attrs['href'] # attrs means to find all with href
			lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
		except:
			continue
	
def getstockinfo(lst, stockurl, fpath):
    count = 0
    for stock in lst :
        url = stockurl + stock + '.html'
        html = gethtmlptext(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockinfo = soup.find('div', attrs = {'class': 'stock-bets'})
            
            name = stockinfo.find_all(attrs = {'class' : 'bets-name'})[0]
            infoDict.update({'stock name': name.text.split()[0]})
            
            key_list = stockinfo.find_all('dt')
            value_list = stockinfo.find_all('dd')
            for i in range(len(key_list)):
                key = key_list[i].text
                val = value_list[i].text
                infoDict[key] = val
                
            with open(fpath, 'a', encoding = 'utf-8') as f: # 缩进错误导致一直输出stock.txt里面的情况
                    f.write(str(infoDict) + '\n')
                    count+=1
                    print('\r当前进度:{:.2f}%'.format(count*100/len(lst)), end='')
        except:
            #traceback.print_exc()
            count+=1
            print('\r当前进度:{:.2f}%'.format(count*100/len(lst)), end='')
            continue
			
def main():
	stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
	stock_info_url = 'https://gupiao.baidu.com/stock/'
	output_file = 'F://code//c//stock.txt'
	slist = []
	getstocklist(slist, stock_list_url)
	getstockinfo(slist, stock_info_url, output_file)

main()