import requests
import sys
from bs4 import BeautifulSoup     # For html passer
import xlwt  # pip install xlwt
import sqlite3

print("--- Command Line:", sys.argv)

api_url = "https://www.bestvalueschools.com/rankings/students-with-autism/"
print("--- api_url: ", api_url)


#grab data from website
def retrieveData(api_url):
    try:
        response = requests.get(api_url)
        #print("--- response headers: ",response.headers)
    except requests.exceptions.ConnectionError as e:
        print('Error', e.args)
        exit(1)

    html = response.content
    # print("--- html: ", html)

    # parsing html with BS
    soup = BeautifulSoup(html, 'html.parser')

    elements = soup.findChild(
        "ol", id="accordion-rankings-184224").findChildren("li")
    datalist = []
    for i in range(0, len(elements)):
        row = []
        univ_name = elements[i].find('span').getText()
        # print (univ_name)
        row.append(univ_name)
        location = elements[i].find('p').getText()
        row.append(location)
        row.append(i+1)  # append ranking, which is the iteration
        desc = elements[i].findChild(
            "div", class_="inner-content").find('p').getText()
        row.append(desc)
        url = elements[i].findChild('a')["href"]
        row.append(url)  # url of university
        row.append(api_url)  # url of the site
        # print(row)
        datalist.append(row)
    return datalist    

datalist = retrieveData(api_url)
# print(datalist)

# save to excel
def saveToExcel(datalist, savepath):
    print('saving .......')
    # create a workbook
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)

    # create a sheet
    sheet = book.add_sheet('autism_university1', cell_overwrite_ok=True)

    # create column names
    columns = ('Univ Name', 'Location', 'Rankings',
               'Description', 'URL', 'Source', 'Misc')

    # Write all column labels
    for i in range(0, len(columns)):
        sheet.write(0, i, columns[i])

    # write data values into columns (per row)
    for i in range(0, len(datalist)):
        data = datalist[i]
        for j in range(0, len(data)):
            sheet.write(i+1, j, data[j])

    # save the excel book
    book.save(savepath)

# saveToExcel(datalist, "autismUniExcelBook1.xls")

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


# init_db("myDB.db")    
saveToDataBase(datalist, 'myDB.db')