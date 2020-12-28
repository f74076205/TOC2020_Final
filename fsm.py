from transitions.extensions import GraphMachine

import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage

from utils import send_text_message

load_dotenv()

import requests 
from bs4 import BeautifulSoup

# import matplotlib.pyplot as plt
# import pyimgur
import message_template
def get_latest_turtlesoup():
    response = requests.get("http://gameschool.cc/turtlesoup/latest/?o=date")
    soup = BeautifulSoup(response.text, "html.parser")
    title=[]
    content=[]
    url=""
    urlTurtleSoup="http://gameschool.cc"
    url_list=[]
    a_tags = soup.select('div.puzzle_title')
    for t in a_tags:
        title.append(t.text)
        # print(t.text)
    a_tags = soup.select('div.puzzle_snippet')
    for t in a_tags:
        content.append(t.text)
        # print(t.text)
    a_tags = soup.select('a.puzDiv')
    for t in a_tags:
        url=urlTurtleSoup+t['href']
        url_list.append(url)
        # print(t['href'])
    # print(soup.prettify()) 

    # for index in range(len(title)):
    #     print ("標題 :",title[index])
    #     print ("內容 :",content[index])
    #     print ("url :",url_list[index])
    #     print("===================================")
    return title,content,url_list

def get_rated_turtlesoup():
    response = requests.get("http://gameschool.cc/turtlesoup/best/?o=date")
    soup = BeautifulSoup(response.text, "html.parser")
    title=[]
    content=[]
    url=""
    urlTurtleSoup="http://gameschool.cc"
    url_list=[]
    a_tags = soup.select('div.puzzle_title')
    for t in a_tags:
        title.append(t.text)
        # print(t.text)
    a_tags = soup.select('div.puzzle_snippet')
    for t in a_tags:
        content.append(t.text)
        # print(t.text)
    a_tags = soup.select('a.puzDiv')
    for t in a_tags:
        url=urlTurtleSoup+t['href']
        url_list.append(url)
        # print(t['href'])
    # print(soup.prettify()) 

    # for index in range(len(title)):
    #     print ("標題 :",title[index])
    #     print ("內容 :",content[index])
    #     print ("url :",url_list[index])
    #     print("===================================")
    return title,content,url_list


def get_ptt_title():
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
            # print(t.text)
            # print(url)
    
    return title,url_list
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text== "主選單"
    def is_going_to_ghost_story_ptt(self, event):
        text = event.message.text.lower()
        return text == "看marvel版"
    
    def is_going_to_ghost_story_youtube(self, event):
        text = event.message.text
        return text == "看微鬼畫"
    
    def is_going_to_turtlesoup_choice(self, event):
        text = event.message.text
        return text == "看海龜湯謎題"
    def is_going_to_turtlesoup_latest(self, event):
        text = event.message.text
        return text == "看最新海龜湯"
    def is_going_to_turtlesoup_rated(self, event):
        text = event.message.text
        return text == "看高評等海龜湯"
    def is_going_to_turtlesoup_youtube(self, event):
        text = event.message.text.lower()
        return text == "看youtube海龜湯"
        

    def is_going_to_scp_web(self, event):
        text = event.message.text.lower()
        return text == "看scp作品"
    
    def is_going_to_scp_youtube(self, event):
        text = event.message.text.lower()
        return text == "看scpyoutube"

    def on_enter_menu(self, event):
        reply_token = event.reply_token
        message = message_template.main_menu
        message_to_reply = FlexSendMessage("開啟主選單", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
    

    def on_enter_ghost_story_ptt(self, event):
        reply_token = event.reply_token
        message = message_template.marvelBoard
        title_ptt,url_ptt=get_ptt_title()
        print(url_ptt[0])
        message["body"]["contents"][1]["contents"][0]["contents"][0]["text"]=title_ptt[0]
        message["body"]["contents"][1]["contents"][1]["contents"][0]["text"]=url_ptt[0]
        message["body"]["contents"][1]["contents"][1]["contents"][0]["action"]["uri"]=url_ptt[0]


        message["body"]["contents"][1]["contents"][2]["contents"][0]["text"]=title_ptt[1]
        message["body"]["contents"][1]["contents"][3]["contents"][0]["text"]=url_ptt[1]
        message["body"]["contents"][1]["contents"][3]["contents"][0]["action"]["uri"]=url_ptt[1]


        message["body"]["contents"][1]["contents"][4]["contents"][0]["text"]=title_ptt[2]
        message["body"]["contents"][1]["contents"][5]["contents"][0]["text"]=url_ptt[2]
        message["body"]["contents"][1]["contents"][5]["contents"][0]["action"]["uri"]=url_ptt[2]


        message["body"]["contents"][1]["contents"][6]["contents"][0]["text"]=title_ptt[3]
        message["body"]["contents"][1]["contents"][7]["contents"][0]["text"]=url_ptt[3]
        message["body"]["contents"][1]["contents"][7]["contents"][0]["action"]["uri"]=url_ptt[3]


        message["body"]["contents"][1]["contents"][8]["contents"][0]["text"]=title_ptt[4]
        message["body"]["contents"][1]["contents"][9]["contents"][0]["text"]=url_ptt[4]
        message["body"]["contents"][1]["contents"][9]["contents"][0]["action"]["uri"]=url_ptt[4]
        message_to_reply = FlexSendMessage("前往marvel版最新文章", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        self.go_back()

    def on_enter_ghost_story_youtube(self, event):
        reply_token = event.reply_token
        message = message_template.weiteng
        message_to_reply = FlexSendMessage("前往Youtube鬼故事推薦", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        self.go_back()

    def on_enter_turtlesoup_choice(self, event):
        reply_token = event.reply_token
        message = message_template.turtlesoup
        message_to_reply = FlexSendMessage("前往海龜湯謎題", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def on_enter_turtlesoup_latest(self, event):
        reply_token = event.reply_token
        message = message_template.latestturtlesoup
        
        title_latest,content_latest,url_latest=get_latest_turtlesoup()
        message["body"]["contents"][1]["contents"][0]["contents"][0]["text"]=title_latest[0]
        message["body"]["contents"][1]["contents"][0]["contents"][0]["action"]["uri"]=url_latest[0]
        message["body"]["contents"][1]["contents"][1]["contents"][0]["text"]=content_latest[0]

        message["body"]["contents"][1]["contents"][2]["contents"][0]["text"]=title_latest[1]
        message["body"]["contents"][1]["contents"][2]["contents"][0]["action"]["uri"]=url_latest[1]
        message["body"]["contents"][1]["contents"][3]["contents"][0]["text"]=content_latest[1]

        message["body"]["contents"][1]["contents"][4]["contents"][0]["text"]=title_latest[2]
        message["body"]["contents"][1]["contents"][4]["contents"][0]["action"]["uri"]=url_latest[2]
        message["body"]["contents"][1]["contents"][5]["contents"][0]["text"]=content_latest[2]
        message_to_reply = FlexSendMessage("前往海龜湯謎題", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def on_enter_turtlesoup_rated(self, event):
        reply_token = event.reply_token
        message = message_template.ratedturtlesoup
        title_rated,content_rated,url_rated=get_rated_turtlesoup()
        message["body"]["contents"][1]["contents"][0]["contents"][0]["text"]=title_rated[0]
        message["body"]["contents"][1]["contents"][0]["contents"][0]["action"]["uri"]=url_rated[0]
        message["body"]["contents"][1]["contents"][1]["contents"][0]["text"]=content_rated[0]

        message["body"]["contents"][1]["contents"][2]["contents"][0]["text"]=title_rated[1]
        message["body"]["contents"][1]["contents"][2]["contents"][0]["action"]["uri"]=url_rated[1]
        message["body"]["contents"][1]["contents"][3]["contents"][0]["text"]=content_rated[1]

        message["body"]["contents"][1]["contents"][4]["contents"][0]["text"]=title_rated[2]
        message["body"]["contents"][1]["contents"][4]["contents"][0]["action"]["uri"]=url_rated[2]
        message["body"]["contents"][1]["contents"][5]["contents"][0]["text"]=content_rated[2]
        message_to_reply = FlexSendMessage("前往海龜湯謎題", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        
    
    def on_enter_turtlesoup_youtube(self, event):
        reply_token = event.reply_token
        message = message_template.buaxian
        message_to_reply = FlexSendMessage("前往Youtube海龜湯推薦", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        self.go_back()
    
    
    def on_enter_scp_web(self, event):
        reply_token = event.reply_token
        message = message_template.scpWebsite
        message_to_reply = FlexSendMessage("前往SCP作品", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        self.go_back()

    def on_enter_scp_youtube(self, event):
        reply_token = event.reply_token
        message = message_template.scpTing
        message_to_reply = FlexSendMessage("前往YoutubeSCP介紹推薦", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        self.go_back()
    
    # def on_exit_menu(self):
    #     print("Leaving menu")

    # def on_exit_ghost_story_ptt(self):
    #     print("Leaving ghost_story_ptt")

    # def on_exit_ghost_story_youtube(self):
    #     print("Leaving ghost_story_youtube")
