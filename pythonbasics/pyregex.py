__author__ = 'leo'


import urllib.request
import re

'''
This code is to how to use regular expression in python.
'''
symblelist = ["AAPL","SPY"]
for symb in symblelist:
    url = "http://finance.yahoo.com/q?s=" + symb
    htmltext = urllib.request.urlopen(url).read() # read() return a bytes objects
    #print(htmltext) #print a bytes object, result would be like this: b'<!DOCTYPE html PUBLIC "-//W3
    pattern = '<span id="yfs_l84_(.{1,6})">(.+?)</span>'
    #bellow pattern could also work well
    #pattern = '<span id="yfs_l84_' + symb.lower() + '">(.+?)</span>'
    price = re.findall(pattern, str(htmltext))
    matches = re.search(pattern,str(htmltext))
    print(price)
    print(matches.group(1))
    print(matches.group(2))
    #print("price of " + symb + " is: " + price[0].decode("utf-8"))
    # todo read param from file and write results to files.
