import requests  # 发送请求
import pandas as pd  # 保存csv文件
import os  # 判断文件是否存在
import time
from time import sleep  # 设置等待，防止反爬
import random  # 生成随机数
import re
from bs4 import BeautifulSoup as bs
import jieba
from wordcloud import WordCloud
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import logging

headers = {
    'authority': 'api.bilibili.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 需定期更换cookie，否则location爬不到
    'cookie': "buvid3=086E129A-F1C1-2C1A-C81C-81870A3EA9E254526infoc; b_nut=1674135254; _uuid=91DB1336-D132-C88E-A82B-BB618D2EA8CA55120infoc; buvid_fp=6fb6649ffd34ded69419db2e764759a0; buvid4=DB5507A2-FDF2-7D17-2D77-A87E03B6404C56108-023011921-EiMuj1RmAAwtT2bdqISiAw==; CURRENT_FNVAL=4048; rpdid=|(YYYJmmklR0J'uY~Rk|mR)m; fingerprint=e9a9a1372ac8f242bc5e5552ff3c73b0; innersign=0; i-wanna-go-back=-1; b_ut=7; b_lsid=FF466FC4_187611927CF; bsource=search_bing; header_theme_version=CLOSE; home_feed_column=4; SESSDATA=e27da95d,1696513306,3a017*41; bili_jct=29d250af5810ec3b2260dc38b3146fce; DedeUserID=1936784244; DedeUserID__ckMd5=2af8c1e1f942a63d; sid=74wnz720",
    'origin': 'https://www.bilibili.com',
    'referer': 'https://www.bilibili.com/video/BV1AL411D7Es/?spm_id_from=333.1007.tianma.8-3-25.click&vd_source=235b1d5e589d25c71a5d50e6201f88c6',
    'sec-ch-ua': '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'
}
url='http://comment.bilibili.com/1069297856.xml'
response = requests.get(url, headers=headers)
response.encoding= "utf-8"
r=response.text

#print(r)

pattern = re.compile('>(.*?)</d>',re.S)
items = re.findall(pattern,r)
# if not items:
#     print('fail')
# for item in items:
#     print(item)

#'<d.*？>(.*?)</d>' 不知道这个正则式错那？
# pattern = re.compile('>(.*?)</d>',re.S)
# items = re.findall(pattern,'<d p="1104.56400,5,25,16777215,1679670732,0,9369e1eb,1279929890682301440,10">发生甚么事了？</d>')
# print(items)
#KeyboardInterrupt是什么错？
#xpath：//*[@id="danmukuBox"]/div/div/div/div[1]/div/div/div[2]/div/div[2]/div[3]/div[1]/div/div/ul/li[1]/div/span[2]
#尝试其他方法，xpath与接口https://api.bilibili.com/x/player/pagelist?bvid=1AL411D7Es
#http://comment.bilibili.com/1080440412.xml
#https://api.bilibili.com/x/player/pagelist?bvid=ms4y1S7Q4
#
#http://comment.bilibili.com/1069297856.xml

litext =' '.join(items)
ls = jieba.cut(litext)
text=' '.join(ls)
#print(text)
jieba.setLogLevel(jieba.logging.INFO)
stopwords = ["的","是","了","不是","是","就","没","这","也"] # 去掉不需要显示的词
img = Image.open("D:\图库\图片\cybj.png") #打开图片
mask = np.array(img) #将图片装换为数组
wc = WordCloud(font_path="msyh.ttc",
               mask=mask,
               width = 1000,
               height = 700,
               background_color='white',
               max_words=200,
               stopwords=stopwords)

w = wc.generate_from_text(text)
wc.to_file("t1.png")
#plt.imshow(w,interpolation='bilinear')
#plt.axis("off")
#plt.show