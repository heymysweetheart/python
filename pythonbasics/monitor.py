__author__ = 'leo'


import urllib.request
import re
import requests
from bs4 import BeautifulSoup


pages= [1,2,3,4,5]
url = "http://lr.com:99/hot_cac/graph_view.php?action=tre&tre_id=243&leaf_id=159&page="
for page in pages:
    htmltext = urllib.request.urlopen(url + str(page)).read()
    soup = BeautifulSoup(htmltext)
    tables = soup.findChildren('table')
    mytable = tables[0]
    monitorRows = mytable.findChildren('tr',{'style':'background-color: #f9f9f9;'})
    monitorRows += mytable.findChildren('tr',{'style':'background-color: #ffffff;'})
    resultlist = []
    resultlist_with_comment = []
    for monitorRow in monitorRows:
        monitorName = monitorRow.findChild('strong').get_text()
        table = monitorRow.findChild('table')
        comment = table.findChild('div', {'style':'text-align:left;background:#fff;border:1px solid #ccc;line-height:22px;'}).get_text().strip()
        if(comment == ''):
            resultlist.append(monitorName)
    for relt in resultlist:
        print(relt)
