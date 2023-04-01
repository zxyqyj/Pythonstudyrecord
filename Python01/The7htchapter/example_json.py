# import json
import json
import re

import lxml.html
import requests

# person = {
#     'basic_info': {'name': '青南',
#                    'age': 24,
#                    'sex': 'male',
#                    'merry': False},
#
#     'work_info': {'salary': 99999,
#                   'position': 'engineer',
#                   'department': None}
#     }

# person_json=json.dumps(person,indent=1)
#In the code snippet you provided, the person object is being converted into a JSON string with an indentation level of 4 using the json.dumps() method.
#indent=1,表示缩进空格为1，可更改

# print(person_json)

# html=requests.get('https://exercise.kingname.info/ajax_1_backend').content.decode('utf-8')

# print(html)
# data={'name':'火甲','age':26}
# data_l=json.dumps(data,indent=4)
# # print(data)
#
# html01=requests.post('https://exercise.kingname.info/ajax_1_postbackend',data_l).content.decode('utf-8')
# print(html01)

# data='{"success": true, "code": "\u884c\u52a8\u4ee3\u53f7\uff1a\u54ce\u54df\u4e0d\u9519\u54e6"}'
# data_dict=json.loads(data)

# # print(data_dict)
# first_url='https://exercise.kingname.info/ajax_3_backend'
# second_url='https://exercise.kingname.info/ajax_3_postbackend'
# first_ajax_url = 'http://exercise.kingname.info/ajax_3_backend'
# second_ajax_url = 'http://exercise.kingname.info/ajax_3_postbackend'

# url = 'http://exercise.kingname.info/exercise_ajax_3.html'
# page_html = requests.get(url).content.decode()
# secret_2 = re.search("secret_2 = '(.*?)'", page_html, re.S).group(1)
# print(secret_2)


# url_ajax='https://exercise.kingname.info/exercise_ajax_3.html'
# html_get_secret2=requests.get(url_ajax).content.decode()
# # print(html_get_secret2)
# selector=lxml.html.fromstring(html_get_secret2)
# secret2=selector.xpath('//head/script[1]/text()')
# /html/head/script
# secret2=re.search("secret_2 = '(.*?)'",html_get_secret2,re.S).group(1)#正则表达式空格也要匹配的
# print(secret2)
#re.search返回一个Match对象，如果找到匹配项，则包含匹配项的信息，如果没有找到，则返回None。Match对象可以用于进一步处理匹配项。
#match对象只包含的是一次匹配结果，只返回第一次匹配结果
# match对象的方法：
# .group(0) : 获得匹配后的字符串
# .start() : 匹配字符串在给定字符串的开始位置下标
# .end() : 匹配字符串在给定字符串的结束位置下标
# .span() : 返回一个元组类型，包含开始位置下标和结束位置下标

# html_get_secret1=requests.get(first_url).content.decode()
# ajax_1_dict=json.loads(html_get_secret1)
# secret1=ajax_1_dict['code']
#
# ajax_2_json=requests.post(second_url,json={'name':'xx','age':2323,'secret1':secret1,'secret2':secret2}).content.decode()
#
# ajax_2_dict=json.loads(ajax_2_json)
# code=ajax_2_dict['code']
#
# print(f'最终页面显示内容:{code}')

# html=requests.post('https://exercise.kingname.info/ajax_4_backend',json={'username': "kingname", 'password': "genius"}).content.decode()
# print(json.loads(html)['code'])

headers={
    'authority': 'exercise.kingname.info',
    'method': 'GET',
    'path': '/exercise_headers_backend',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate,br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'anhao': 'kingname',
    'content-type': 'application/json; charset=utf-8',
    'referer': 'https://exercise.kingname.info/exercise_headers.html',
    # 'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Windows',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
# headers = {
#     'Accept': '*/*',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
#     'anhao': 'kingname',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/json; charset=utf-8',
#     'DNT': '1',
#     'Host': 'exercise.kingname.info',
#     'Referer': 'http://exercise.kingname.info/exercise_headers.html',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
#     'X-Requested-With': 'XMLHttpRequest',
# }

url = 'http://exercise.kingname.info/exercise_headers_backend'
html=requests.get(url,headers=headers).content.decode()
print(json.loads(html))

# html_json = requests.get(url, headers=headers).content.decode()
# html_dict = json.loads(html_json)
#
# print(html_dict)