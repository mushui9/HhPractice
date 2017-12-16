# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import os

def click_num(av_num):
    url='http://interface.bilibili.com/player?id=cid:3881817&aid='+str(av_num)
    web_data=requests.get(url)
    soup=BeautifulSoup(web_data.text,"html.parser")
    click=soup.click
    if click==None:
        num='0'
    else:
        num=click.get_text()
    return num

file=open('click_num.txt','a')
for i in range(10000,20000):
    num=click_num(i)
    print(i,num)
    if int(num)>1000000:
        file.write('\n'+str(i)+'\t'+num)
file.close()

