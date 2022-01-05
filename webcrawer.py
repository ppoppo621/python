"""
Created on Mon Aug 19 21:37:11 2019

@author: Wu_xu
"""

## web crawler practice
import requests
from bs4 import BeautifulSoup
import re  #regular expression

s = 0
book = requests.get('https://book.douban.com/subject/33450028/?icn=index-latestbook-subject')
book.status_code
content = BeautifulSoup(book.text,'lxml')
a = content.find_all('span','short')
for item in a:
    print(item.string)
pattern_s = re.compile('<span class="user-stars allstar(.*?) rating"')
p = re.findall(pattern_s,book.text)  ### why use book.text, not content? content is an object of beautifulsoup; book.text is a string.
for i in p:
    s += int(i)
print(s)

### WebCrawler Tasks

###Q1 get top 50 comments and calculate avg score

import requests
from bs4 import BeautifulSoup 
import re

r = requests.get('https://book.douban.com/subject/33422832/comments/')
soup = BeautifulSoup(r.text,'lxml')
list = soup.find_all('p','comment-content')
for item in list[:50]:
    print(item.text)
pattern_sc = re.compile('<span class="user-stars allstar(.*?) rating"')
p = re.findall(pattern_sc,r.text)
s=0
for i in p:
    s += int(i)
print(s/len(p))



### Q2 Dow index top 30 company (code, name, latest price) into a list

import requests
import re

def retrieve_dji_list():
    r = requests.get('http://money.cnn.com/data/dow30/')
    # put the re expression on one line and pay attention to the '\n'
    search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span>.*?\n.*?class="wsod_stream">(.*?)<\/span>')
    dji_list_in_text = re.findall(search_pattern, r.text)
    return dji_list_in_text

dji_list = retrieve_dji_list()
print(dji_list,'\n')


### Q2 by BeautifulSoup
import requests
from bs4 import BeautifulSoup 
import re
r = requests.get('http://money.cnn.com/data/dow30/')
soup = BeautifulSoup(r.text,'lxml')
list = soup.find_all('a',class_='wsod_symbol')
for i in list[0][3]:
    print(i.text)


### Q3 webcrawler

import re
import requests
def crawler(url):
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as err:
        return err
    r.encoding = r.apparent_encoding
    pattern = re.compile('href="/en/vnl/2018/women/teams/.*?">(.*?)</a></figcaption>\s+</figure>\s+</td>\s+<td>(.*?)</td>\s+<td class="table-td-bold">(.*?)</td>\s+<td class="table-td-rightborder">(.*?)</td>')
    p = re.findall(pattern, r.text)
    return p

if __name__ == "__main__":
    url = 'http://www.volleyball.world/en/vnl/2018/women/results-and-ranking/round1'
    result = crawler(url)
    print(result)

