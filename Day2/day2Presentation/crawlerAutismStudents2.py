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

    children = parentClass.findChildren()
    print(children)
    h3Children = children.findChildren("h3")
    for i in range(0, len(children)):
        if (children[i] in h3Children): #and children[i] contains number at front
            #try if children[i].getText()[0:1] contains number in front using int(children[i]) and except ValueError (if value error, just "continue" on the loop)
            #do a cycle (get name [i], location[i+1]...)
            #post check if children[i] in h3Children for descripion

    # ranking_AND_names = parentClass.findChildren("h3")
    # ranking_AND_names.pop(0)
    # ranking_AND_names.pop(len(ranking_AND_names)-1)
    # # print(ranking_AND_names[0])
    # locationList = parentClass.findChildren("h4")
    # # print(location)
    # pList_Link_Desc = parentClass.findChildren('p')
    # print("Length of pList:", len(pList_Link_Desc))
    # datalist = []
    # for i in range(0, 17):
    #     pList_Link_Desc.pop(0)
    # # print(pList_Link_Desc)
    # # 34, 35, 36
    # j = 0
    # for i in range(0, len(ranking_AND_names)):
    #     row = []
    #     ranking_name = ranking_AND_names[i].getText().split(". ")
    #     ranking = ranking_name[0]
    #     univ_name = ranking_name[1]

    #     row.append(univ_name)
    #     location = locationList[i].getText()
    #     row.append(location)
    #     row.append(ranking)
    #     url = pList_Link_Desc[j].findChild('a')["href"]
        
    #     desc = ""
    #     desc += pList_Link_Desc[j + 1].getText()
    #     while (pList_Link_Desc[j + 2].findChild('a') is None or len(pList_Link_Desc[j + 2]) > 30):
    #         desc += pList_Link_Desc[j + 2].getText()
    #         j += 1
    #     j += 2    
    #     row.append(desc)
    #     row.append(url)
    #     row.append(api_url)
    #     print(row)


    #     ### the initial way of thought for extracting univ_name and ranking
    #     # if (i < 10):
    #     #     # "8. UniversityName"
    #     #     univ_name = ranking_AND_names[i][3:]
    #     #     ranking = ranking_AND_names[i][0:1]
    #     # else:
    #     #     # "12. UniversityName"    
    #     #     univ_name = ranking_AND_names[i][4:]
    #     #     ranking = ranking_AND_names[i][0:2]
        


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