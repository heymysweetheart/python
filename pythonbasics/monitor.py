__author__ = 'leo'


import urllib.request
import re
import requests
from bs4 import BeautifulSoup


pages= [1,2,3,4,5]
url = "http://yahoo.com/ti/ew.php?action=tree&tree_id=243&leaf_id=11901820&page="
for page in pages:
    htmltext = urllib.request.urlopen(url + str(page)).read()
    soup = BeautifulSoup(htmltext)
    tables = soup.findChildren('table')
    mytable = tables[0]
    #print(mytable)
    monitorRows = mytable.findChildren('tr',{'style':'background-color: #f9f9f9;'})
    resultlist = []
    for monitorRow in monitorRows:
        monitorName = monitorRow.findChild('strong').get_text()
        table = monitorRow.findChild('table')
        comment = table.findChild('div', {'style':'text-align:left;background:#fff;border:1px solid #ccc;line-height:22px;'}).get_text().strip()
        if(comment == ''):
            #list.append(monitorName.get_text())
            #print(monitorName)
            resultlist.append(monitorName)
    print(resultlist.__sizeof__())
    #wrappernames = re.findall(b'<strong>(.+?)<br></strong>', htmltext)
    #monitorIds = re.findall(b'<strong>(.+?)<br></strong>', htmltext)
    #for wrappername in wrappernames:
    #    print(wrappername)
    #print(wrappernames.__sizeof__())
    #print("price of " +k symb + " is: " + price[0].decode("utf-8"))
    # todo read param from file and write results to files.