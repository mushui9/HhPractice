
from bs4 import BeautifulSoup
import requests
import os
import pymysql
from multiprocessing import Pool

#实现数据库读写更新，待补充，，多线程，反爬虫技巧(多线程失效）

def get_data(av_num):
    url='http://api.bilibili.com/x/web-interface/archive/stat?aid='+str(av_num)
    web_data=requests.get(url)
    x=[av_num,0,0,0,0,0,0,'','']
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
    if(x[1]>1000000):
        url='http://www.bilibili.com/video/av'+str(av_num)
        web_data=requests.get(url)
        soup=BeautifulSoup(web_data.text,'html.parser')
        titles=soup.title.string
        length=len(soup.select('option'))
        if(length==0):
            try:
                x[7]=titles[-16:-14]
                x[8]=titles[0:-14]
            except Exception as e:
                pass
            save_data(x)
        else:
            if(x[1]/length>1000000):
                try:
                    x[7]=titles[-16:-14]
                    x[8]=tiltles[0:-14]
                except Exception as e:
                    pass
                save_data(x)
    #return x[4]


def save_data(x):
    savedb=pymysql.connect('localhost','root','root','study',use_unicode=True, charset="utf8")
    savecur=savedb.cursor()
    sql="""insert into biliclick(av_num,view,danmu,reply,favorite,coin,share,tag,av_name) values("%s","%s","%s","%s","%s","%s","%s","%s","%s")"""
    savecur.execute(sql % (x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
    savedb.close()

def main():
    db=pymysql.connect('localhost','root','root','study',use_unicode=True, charset="utf8")
    cur=db.cursor()
    sql='select av_num from biliclick where id=1'
    cur.execute(sql)
    av_begin=cur.fetchall()[0][0]
    amout=100
    av_end=av_begin+amout
    sql='update biliclick set view=0 where id=1'
    cur.execute(sql)
    flag=0
    
    pool=Pool(processes=8)
    while flag==0:
        result=pool.map(get_data,range(av_begin,av_end))
        #print(result)
        #pool.close()
        #pool.join()
        #save_data(result)
        av_begin=av_begin+amout
        av_end=av_end+amout
        print(av_begin)
        sql='select view from biliclick where id=1'
        cur.execute(sql)
        flag=cur.fetchall()[0][0]               
    pool.close()
    pool.join()
    sql='update biliclick set av_num="%s" where id=1' % (av_begin)
    cur.execute(sql)
    db.close()

if __name__ == "__main__":
	main()
            
