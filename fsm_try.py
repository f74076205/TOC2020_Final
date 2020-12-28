import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.ptt.cc/bbs/marvel/index.html")
soup = BeautifulSoup(response.text, "html.parser")
title=[]
url=""
urlptt="https://www.ptt.cc"
url_list=[]
# print(soup.prettify()) 

a_tags = soup.select('div.title a')
for t in a_tags:
    
    # title.append(t.text)
    ct=t.text
    if('刪除'not in ct  ):
        title.append(t.text)
        url=urlptt+t['href']
        url_list.append(url)
        print(t.text)
        print(url)
    
   