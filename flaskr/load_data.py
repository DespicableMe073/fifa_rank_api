import sqlite3
import re
from selenium import webdriver
from bs4 import BeautifulSoup
import bs4
from flaskr import group_model


pageuri = "http://2018.sina.com.cn/schedule/group.shtml"


# ------ 获取目标网页代码 ---
def gethtml():
    browser = webdriver.PhantomJS()
    browser.get(pageuri)
    return browser.page_source


# ------ 获取目标网页代码/解析数据---
def get_contents():
    ulist = []
    soup = BeautifulSoup(gethtml(),"html.parser")
    trs = soup.findAll('tr')
    for tr in trs:
        tds = tr.findAll('td')
        if len(tds) == 7:
            gm = group_model.GroupModel(tds[0].string,tds[1].string,tds[2].findAll('a')[0].string,tds[2].findAll('a')[1].string,tds[2].findAll('a')[2].string,
                 tds[3].string,tds[4].string)

            ulist.append(gm)



        else:
            pass

    return ulist


# 插入数据库
def insert_sqllite(ulist):
    con = sqlite3.connect("data.db3")
    cur = con.cursor()
    try:
        cur.execute('delete from groupsinfo')
        for gm in ulist:
            cur.execute("insert into groupsinfo(g1name,g2name,g1score,g2score,ggroupname,ggroup,gdatetime,isdelete) values(?,?,?,?,?,?,?,?)",(gm.g1name,gm.g2name,gm.g1score,gm.g2score,gm.groupname,gm.groupname[0],gm.gdate,0))
        con.commit()
        return True

    except Exception as e:
        con.rollback()
        return e

    finally:
        con.close()


if __name__ == "__main__":
    print(insert_sqllite(get_contents()))




