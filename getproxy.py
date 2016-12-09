import requests
import re
import threading
import time
import random
from bs4 import BeautifulSoup
#beginurl='http://www.xicidaili.com/'
beginurl='http://www.youdaili.net/Daili/http/'
linkfirst=[]
semaphore=threading.Semaphore(9)


def getfirstlink(beginurl):
    proxies = {
        "http": "http://115.198.143.72:8118",
        "https": "http://211.103.250.145:80",
    }
    heads={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/5.7.16400.812 Safari/537.36'}
    r = requests.get(beginurl,headers=heads)
          #print(r.content.decode('utf-8'))
    soup=BeautifulSoup(r.content.decode('utf-8'),'html.parser')
    result=soup.select('div[class="chunlist"] > ul > li > p > a')  #CSS选择器

    for i in result:
       #print(i.get('href'),i.get('title')) #取链接
        linkfirst.append(i.get('href'))
    return linkfirst



class Gettext(threading.Thread):
#print(t)
    def __init__(self,urls):
        self.urls=urls
        threading.Thread.__init__(self)
    def run(self):
        self.gettext(self.urls)
    def gettext(self,urls):
        semaphore.acquire()
        heads = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/5.7.16400.812 Safari/537.36'}
        proxies = {
            "http": "http://115.198.143.72:8118",
            "https": "http://211.103.250.145:80",
        }
        try:
            r = requests.get(urls, headers=heads,timeout=15)
            relink=re.compile('\d+\.\d+\.\d+\.\d+:\d+@\w+')
            result=relink.findall(r.content.decode('utf-8'))
            # soup=BeautifulSoup(r.content.decode('utf-8'),'html.parser')
            # #print(soup.prettify())
            # result=soup.select('span[style="font-size: 14px;"]')
            nextpagere=re.compile('\d{4}_\d.html')
            nextlast=nextpagere.findall(r.content.decode('utf-8'))
            s=set(nextlast)
            for i in s:
                nextpage='http://www.youdaili.net/Daili/guonei/'+i
                #print(nextpage)
                linkfirst.append(nextpage)


            for i in result:
                pass
                #print(i.get_text())
                print(i)
        except Exception as e:
            print(e)

        semaphore.release()

if __name__=='__main__':
    linkfirst=getfirstlink(beginurl)
    for link in linkfirst:
        t=Gettext(link)
        t.start()
    t.join()