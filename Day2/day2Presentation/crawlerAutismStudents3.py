import requests
import sys
from bs4 import BeautifulSoup  #html passer
import xlwt #pip install xlwt
import sqlite3
#pip list | grep requests

print("--- Command Line:", sys.argv)

api_url = "https://www.collegechoice.net/rankings/best-colleges-for-students-with-autism/"
print("--- api_url:", api_url)

#grab data from website
def retrieveData(api_url):
    try:
        response = requests.get(api_url)
    except requests.exceptions.ConnectionError as e:
        print('Error', e.args)
        exit(1)

    html = response.content
    # print('--- html:', html)

    # parsing html with BS
    soup = BeautifulSoup(html, 'html.parser')

    elements = soup.findChild("ol").findChildren("li")
    # print(elements)

    datalist = []
    j=0
    for i in range(0, len(elements)):
        row = []
        try:
            univ_name = elements[i].find('span').getText()
        except AttributeError:
            # print("Error!")
            continue
        # print("span:", elements[i].find('span'))
        print(univ_name)
        row.append(univ_name)
        location = elements[i].find('p').getText()
        print(location)
        row.append(location)
        ranking = j+1
        row.append(ranking)
        print(ranking)
        desc = ""
        descElements = elements[i].findChild("div", class_="inner-content").findChildren() ### findChildren() and make this a list, then do for each loop on list and append to desc on each iteration
        # print(descElements)
        for n in range(2, len(descElements)):
            desc += descElements[n].getText()
        row.append(desc)
        print(desc)
        url = elements[i].findChild('a')["href"]
        row.append(url) #url of the university
        print(url)
        row.append(api_url) #url of the site/source
        j += 1
        # print(row)
        datalist.append(row)

    return datalist

datalist = retrieveData(api_url)
print(datalist)

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
                insert into autism_universities3(
                univ_name,location,ranking,description,url,source_url)
                values (?,?,?,?,?,?)'''
        # print(sql)
        cur.execute(sql, (data[0], data[1],data[2],data[3],data[4],data[5]))
        conn.commit()
    cur.close
    conn.close()


def init_db(dbpath):
    sql = '''
        create table autism_universities3
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
    '''      
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    conn.close()

saveToDataBase(datalist, "autismUniversitiesDB.db")