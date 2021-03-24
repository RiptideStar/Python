import requests
import sys
from bs4 import BeautifulSoup
import sqlite3

print("--- Command Line:", sys.argv)

api_url = "https://www.greatvaluecolleges.net/best-colleges-for-students-with-autism/"
print("--- api_url:", api_url)


def retrieveData(api_url):
    try:
        response = requests.get(api_url)
    except requests.exceptions.ConnectionError as e:
        print('Error', e.args)
        exit(1)

    html = response.content

    # parsing html with BS
    soup = BeautifulSoup(html, 'html.parser')

    parentClass = soup.findChild("div", class_="entry-content clearfix")
    ranking_AND_names = parentClass.findChildren("h3")
    ranking_AND_names.pop(0)
    ranking_AND_names.pop(len(ranking_AND_names)-1)
    # print(ranking_AND_names)
    location = parentClass.findChildren("h4")
    # print(location)
    pList_Link_Desc = parentClass.findChildren('p')
    datalist = []
    for i in range(0, 17):
        pList_Link_Desc.pop(0)
    # print(pList_Link_Desc)
    # for i in range(0, len(ranking_AND_names)):

retrieveData(api_url)


def saveToDataBase(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in datalist:
        # print(data)
        for index in range(len(data)):
            if index == 2:
                continue
            data[index] = '"'+data[index]+'"'
            print(data[index])
        sql = '''
                insert into autism_universities(
                univ_name,location,ranking,description,url,source_url)
                values (?,?,?,?,?,?)'''
        # print(sql)    
        cur.execute(sql, (data[0],data[1],data[2],data[3],data[4],data[5]))
        conn.commit()
    cur.close
    conn.close()



def init_db(dbpath):
    sql = '''
        create table autism_universities
        (
        id integer primary key autoincrement,
        univ_name varchar,
        location varchar,
        ranking integer,
        description text,
        url text,
        source_url text,
        misc text
        );
    '''      # 创建数据表
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    conn.close()    