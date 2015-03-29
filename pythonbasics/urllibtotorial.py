import urllib.request
import re
regex = '<title>(.+?)</title>'

urls = ['http://renren.com', 'http://sass.weibo.com/unfreeze', 'https://www.baidu.com/', 'https://www.yahoo.com/', 'http://www.sohu.com/']
for url in urls:
   htmlfile = urllib.request.urlopen(url)
   htmltext = htmlfile.read()
   titles = re.findall(b'<title>(.+?)</title>', htmltext)

   for title in titles:
      print(title.decode('utf-8'))
