import requests
import sys
from bs4 import BeautifulSoup  #html passer
import xlwt #pip install xlwt
import sqlite3
#pip list | grep requests

print("--- Command Line:", sys.argv)

api_url = "https://www.bestvalueschools.com/rankings/students-with-autism/"
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

    datalist = []
    for i in range(0, len(elements)):
        row = []
        univ_name = elements[i].find('span').getText()
        # print(univ_name)
        row.append(univ_name)
        location = elements[i].find('p').getText()
        # print(location)
        row.append(location)
        ranking = i+1
        row.append(ranking)
        # print(ranking)
        desc = elements[i].findChild("div", class_="inner-content").find('p').getText()
        row.append(desc)
        # print(desc)
        url = elements[i].findChild('a')["href"]
        row.append(url) #url of the university
        row.append(api_url) #url of the site/source
        # print(row)
        datalist.append(row)

    return datalist

datalist = retrieveData(api_url)

# save to excel
def saveToExcel(datalist, name):

    #create book
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)

    #create sheet
    sheet = book.add_sheet('universitiesForStudentsAutism', cell_overwrite_ok=True)

    # create column names
    columns = ('Univ Name', 'Location', 'Rankings', 'Description', 'URL', 'Source', 'Misc')

    #write all column names into the top row
    for i in range(0, len(columns)):
        sheet.write(0, i, columns[i])

    #write data into the excel sheet into columns (per row)
    for i in range(0, len(datalist)):
        data = datalist[i]
        for j in range(0, len(data)):
            sheet.write(i+1, j, data[j])

    #save the book to a file
    book.save(name)      

# saveToExcel(datalist, "UniForStudentswAutism1.xls")


def init_db(name):
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
        '''
    conn = sqlite3.connect(name)
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    conn.close()

def saveToDataBase(datalist, name):
    init_db(name)
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            if index == 2:
                continue
            data[index] = '"'+data[index]+'"'
            print(data[index])
        sql = '''
            insert into autism_universities(
                univ_name, location, ranking, description, url, source_url
            )
            values (?,?,?,?,?,?)
            '''
        cur.execute(sql, (data[0], data[1], data[2], data[3], data[4], data[5]))
        conn.commit()
    cur.close
    conn.close()

saveToDataBase(datalist, "autismUniversitiesDB.db")  