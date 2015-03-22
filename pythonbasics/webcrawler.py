import requests
from bs4 import BeautifulSoup

def spider(max_page):
    page = 1
    while page <= max_page:
        url = ""

def crawler():
    url = "https://www.thenewboston.com/tops.php?type=text&period=this-month"
    domain = 'https://www.thenewboston.com'
    content = requests.get(url)
    plain_text = content.text
    soup = BeautifulSoup(plain_text)

    for link in soup.findAll('a', {'class': 'index_singleListingTitles'}):
        href = domain + link.get('href')
        title = link.string
        # print(title)
        print(href)
        crawl_single_page(href)

def crawl_single_page(item_url):
    content = requests.get(item_url)
    soup = BeautifulSoup(content.text)
    links = soup.findAll('a')
    domain = 'https://www.thenewboston.com'
    for link in links:
        print(domain + link.get('href'))

crawler()




