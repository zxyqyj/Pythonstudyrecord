import urllib.parse
import json
import requests
import jsonpath
import os

filename='../picture\\'

if not os.path.exists(filename):
    os.mkdir(filename)

url = 'https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}'

label = '美女'
label = urllib.parse.quote(label)

num = 1
for index in range(0,2400,24):
    u = url.format(label,index)
    we_data = requests.get(u).text
    html = json.loads(we_data)
    print(html)
    photo = jsonpath.jsonpath(html, "$..path")
    for i in photo:
        a = requests.get(i)
        # print(a.content)
        with open(str(num)+'.jpg', mode='wb') as f:
            f.write(a.content)  # 二进制
        num += 1
        if num ==5 :
            break
    break