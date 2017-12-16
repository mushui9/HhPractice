# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import os
import pymysql

#实现数据库读写更新，待补充，（读取数据库值判断）控制循环退出，多线程，反爬虫技巧
#速度，10000/20min

'''
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

# 判断是否为数字
def isNum(value):
    try:
        value + 1
    except TypeError:
        return False
    else:
        return True

'''
def get_name(av_num):
    url='http://www.bilibili.com/video/av'+str(av_num)
    web_data=requests.get(url)
    soup=BeautifulSoup(web_data.text,'html.parser')
    av_name=soup.title.string[0:-14]
    #av_name=str(av_num)
    return av_name

def get_num(av_num):
    url='http://api.bilibili.com/x/web-interface/archive/stat?aid='+str(av_num)
    web_data=requests.get(url)
    x=[av_num,0,0,0,0,0,0,'']
    try:
        j=web_data.json()['data']
        view=j['view']
        x[1]=view+1-1
        x[2]=j['danmaku']
        x[3]=j['reply']
        x[4]=j['favorite']
        x[5]=j['coin']
        x[6]=j['share']
        #x=[av_num,view,danmu,reply,favorite,coin,share]
    except Exception as e:
        pass
    return x
    
def main():
    db=pymysql.connect('localhost','root','root','study',use_unicode=True, charset="utf8")
    cur=db.cursor()
    sql='select av_num from biliclick where id=1'
    cur.execute(sql)
    av_num=cur.fetchall()[0][0]
    amout=10000
    while(amout>0):
        av_num=av_num+1
        print(av_num)
        amout=amout-1
        x=get_num(av_num)
        if(x[1]>1000000):
            x[7]=get_name(av_num)
            sql='insert into biliclick(av_num,view,danmu,reply,favorite,coin,share,av_name) values("%s","%s","%s","%s","%s","%s","%s","%s")'
            cur.execute(sql % (x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))
    else:
        sql='update biliclick set av_num="%s" where id=1' % (av_num)
        cur.execute(sql)
        db.close()
            
    #print(get_num(av_num_begin))


if __name__=='__main__':
    main()
