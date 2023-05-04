import matplotlib.pyplot as plt
import requests
from PIL import Image
import jieba
import re

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

class tri:
    def __init__(self,bv):
        #获取三连数据需要aid，aid可直接由bv号从一个网上找到的算法转化来，一下为算法
        table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
        tr = {}
        for i in range(58):
            tr[table[i]] = i
        s = [11, 10, 3, 8, 4, 6]
        xor = 177451812
        add = 8728348608

        def bv2av(x):
            r = 0
            for i in range(6):
                r += tr[x[s[i]]] * 58 ** i

            return (r - add) ^ xor
        #获取cid
        self.cid = bv2av(list("BV"+bv))
        #使用api
        self.data = requests.get(url="https://api.bilibili.com/x/web-interface/archive/stat?aid="+str(self.cid),headers=headers).json()["data"]
        self.coin = self.data['coin']
        self.share = self.data['share']
        self.like = self.data['like']