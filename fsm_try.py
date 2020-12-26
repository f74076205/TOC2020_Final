from bs4 import BeautifulSoup
import requests 
import re


x="你好I'am boy"
print(x.lower())
# print(y)
# urlYoutubeHorror="https://www.youtube.com/channel/UCGPlcnciT5KXLgVjLumGQgQ/videos"
# urlYoutubeTing="https://www.youtube.com/channel/UCmdc8oBXpYofxGC8s3J_aLQ/videos"
# urlBauxuan="https://www.youtube.com/playlist?list=PLKocQYCpz8DzVjRWQjImhNRhXsAEm47rn"

# urlScp="http://scp-zh-tr.wikidot.com/"



# string = "周杰倫"

# url = "https://www.youtube.com/results?search_query=" + string
# res = requests.get(url, verify=False)
# soup = BeautifulSoup(res.text,'html.parser')
# last = None

# for entry in soup.select('a'):
#     m = re.search("v=(.*)",entry['href'])
#     if m:
#         target = m.group(1)
#         if target == last:
#             continue
#         if re.search("list",target):
#             continue
#         last = target
#         print (target)

# response = requests.get("https://www.youtube.com/channel/UCGPlcnciT5KXLgVjLumGQgQ/videos")
# soup = BeautifulSoup(response.text, "html.parser")
# title=[]
# content=[]
# url=""
# urlptt="https://www.ptt.cc"
# url_list=[]
# print(soup.prettify()) 
# # print("===============================================")
# # a_tags = soup.select('div.title a')
# # for t in a_tags:
    
# #     title.append(t.text)
# #     ct=t.text
# #     if('刪除'not in ct ):
# #         print(t.text)
# #         print(t['href'])


# response = requests.get("https://www.ptt.cc/bbs/marvel/index.html")
# soup = BeautifulSoup(response.text, "html.parser")
# title=[]
# url=""
# urlptt="https://www.ptt.cc"
# url_list=[]
# # print(soup.prettify()) 
# print("===============================================")
# a_tags = soup.select('div.title a')
# for t in a_tags:
    
#     # title.append(t.text)
#     ct=t.text
#     if('刪除'not in ct ):
#         print(t.text)
#         print(t['href'])



# response = requests.get("http://gameschool.cc/turtlesoup/best/?o=date")
# soup = BeautifulSoup(response.text, "html.parser")
# title=[]
# content=[]
# url=""
# urlTurtleSoup="http://gameschool.cc"
# url_list=[]
# a_tags = soup.select('div.puzzle_title')
# for t in a_tags:
#     title.append(t.text)
#     # print(t.text)
# a_tags = soup.select('div.puzzle_snippet')
# for t in a_tags:
#     content.append(t.text)
#     # print(t.text)
# a_tags = soup.select('a.puzDiv')
# for t in a_tags:
#     url=urlTurtleSoup+t['href']
#     url_list.append(url)
#     # print(t['href'])
# # print(soup.prettify()) 

# for index in range(len(title)):
#     print ("標題 :",title[index])
#     print ("內容 :",content[index])
#     print ("url :",url_list[index])
#     print("===================================")


# response = requests.get("http://gameschool.cc/turtlesoup/all/?o=date")
# soup = BeautifulSoup(response.text, "html.parser")
# title=[]
# content=[]
# url=""
# urlTurtleSoup="http://gameschool.cc"
# url_list=[]
# a_tags = soup.select('div.puzzle_title')
# for t in a_tags:
#     title.append(t.text)
#     # print(t.text)
# a_tags = soup.select('div.puzzle_snippet')
# for t in a_tags:
#     content.append(t.text)
#     # print(t.text)
# a_tags = soup.select('a.puzDiv')
# for t in a_tags:
#     url=urlTurtleSoup+t['href']
#     url_list.append(url)
#     # print(t['href'])
# # print(soup.prettify()) 

# for index in range(len(title)):
#     print ("標題 :",title[index])
#     print ("內容 :",content[index])
#     print ("url :",url_list[index])
#     print("===================================")