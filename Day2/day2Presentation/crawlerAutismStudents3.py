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
        desc = elements[i].findChild("div", class_="inner-content").find('p').getText() ### findChildren() and make this a list, then do for each loop on list and append to desc on each iteration
        row.append(desc)
        # print(desc)
        url = elements[i].findChild('a')["href"]
        row.append(url) #url of the university
        row.append(api_url) #url of the site/source
        # print(row)
        datalist.append(row)

    return datalist

datalist = retrieveData(api_url)
print(datalist)