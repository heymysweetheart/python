__author__ = 'leo'

#python example of parse titles of web pages
import requests
import re

urls = ["http://tao-yuan.com.cn/", "http://www.newsmth.net/","http://www.newsmth.net/nForum/#!board/PieLove","http://qunar.com"]
i = 0;
regex = '<title>(.+?)</title>'
#apply bytes pattern to a binary object
#TypeError: can't use a string pattern on a bytes-like object python
pattern = re.compile(b'<title>(.+?)</title>')

while i< len(urls) :
    urltext = requests.get(urls[i]).text
    title = re.findall(regex,urltext)
    print(title)
    i +=1
