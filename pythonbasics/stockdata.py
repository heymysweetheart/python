__author__ = 'leo'


import urllib.request
import re


symble = "AAPL"
symblelist = ["AAPL","SPY","GOOG","NFLX"]
for symb in symblelist:
    url = "http://finance.yahoo.com/q?s=" + symb
    regex = '<span id="yfs_l84_[*]">(.+?)</span>'
    htmltext = urllib.request.urlopen(url).read()
    price = re.findall('<span id="yfs_l84_' + symb + '">(.+?)</span>', htmltext)

    print("price of " + symb + " is: " + price[0].decode("utf-8"))
    # todo read param from file and write results to files.