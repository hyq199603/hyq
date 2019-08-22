import requests
import re
import numpy as np 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
url = 'https://www.baidu.com/s?wd=%E7%95%99%E4%B8%8B%E9%82%AE%E7%AE%B1'
response = requests.get(url,headers=headers)
html = response.text
regex = re.compile("[a-zA-z]+://[^\s]*")
res = regex.findall(html)

new_res = []
for i in res:
    if '//cache.baiducontent.com/c?m=9' in i:
        new_res.append(i)
        for j in new_res:
            response = requests.get(j,headers=headers)
            html_1 = response.text
            regex = re.compile("[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?")
            res_1 = regex.findall(html_1)
            list_2 = str(list(set(res_1)))
            with open('C:\\Users\\lenovo\\Desktop\\html\\emile.txt',mode='a',encoding='utf8') as f:
                f.write(list_2)
