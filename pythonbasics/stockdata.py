__author__ = 'leo'


import urllib.request
import re


symble = "AAPL"
url = "http://finance.yahoo.com/q?s=aapl"
regex = '<span id="yfs_l84_aapl">(.+?)</span>'
htmltext = urllib.request.urlopen(url).read()
price = re.findall(b'<span id="yfs_l84_aapl">(.+?)</span>', htmltext)

print("price of " + symble + " is: " + price[0].decode("utf-8"))
# todo read param from file and write results to files.