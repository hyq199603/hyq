'''
import json
import requests
import multiprocessing
import os
def A():
    with open('C:\\Users\\Administrator\\Desktop\\top_500.txt',mode='r') as f:
        res = f.readlines()[0].strip('\n').split('}')
        b = []
        for json_ in res[:-1]:
            _json = json_ + '}'
            _json = json.loads(_json)
            song_play_url = _json['song_play_url']
            song_name = _json['song_name']
            if song_play_url is not None:
                b.append(song_play_url)
                for i in b[0:23]:
                    path = i
                    response = requests.get(path)
                    mp3_ = response.content
                    with open('C:\\Users\\Administrator\\Desktop\\music\\'+song_name+'.mp3',mode='wb') as f:
                        f.write(mp3_)

def B():
    with open('C:\\Users\\Administrator\\Desktop\\top_500.txt',mode='r') as f:
        res = f.readlines()[0].strip('\n').split('}')
        b = []
        for json_ in res[:-1]:
            _json = json_ + '}'
            _json = json.loads(_json)
            song_play_url = _json['song_play_url']
            song_name = _json['song_name']
            if song_play_url is not None:
                b.append(song_play_url)
                for i in b[23:47]:
                    path = i
                    response = requests.get(path)
                    mp3_ = response.content
                    with open('C:\\Users\\Administrator\\Desktop\\music\\'+song_name+'.mp3',mode='wb') as f:
                        f.write(mp3_)                

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=A) 
    p2 = multiprocessing.Process(target=B)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('ok')

2.想办法把 https://www.17k.com/list/3015690.html 页面中章节详情的内容URL给拿到
2.1 做进程划分,爬取章节页面详情存储到本地,一个章节一个html文件.
2.2 html = response.text
2.3 如果你的请求返回出来的是乱码,设置response.encoding='utf-8'/'gbk'...
2.4 你把文章的内容给拿出来存到本地.
'''
import requests
from lxml import etree
path = ('https://www.17k.com/list/3015690.html')
response = requests.get(path)
response.encoding='utf-8'
tree = etree.HTML(response.text)
list_1 = tree.xpath('//html/body/div[@class="Main List"]/dl[@class="Volume"]/dd/a')
for i in list_1[0:40]:
    hyq = requests.get(path)
    hyq.encoding='utf-8'
    tree1 = etree.HTML(hyq.text)
    list_2 = tree1.xpath('//html/body/div[@class="area"/div[@class="read"]/div[@class="readArea"]/div[@class="readAreaBox content]')
    print(list_2) 
   