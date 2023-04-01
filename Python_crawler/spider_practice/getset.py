import requests
import re

html=requests.get('https://exercise.kingname.info/exercise_requests_get.html').content.decode('utf-8')
# print(html)
# html_bytes=html.content
# print(html_bytes)
# html_str=html_bytes.decode()
# print(html_str)

data={
    'name':'123',
    'password':'123'
}

html01=requests.post('https://exercise.kingname.info/exercise_requests_post',data=data).content.decode()
title=re.findall('<title>(.*?)</title>',html01,re.S)
content_list=re.findall('<p>(.*?)</p>',html01,re.S)
content_str='\n'.join(content_list)
print(f'页面标题为：{title}')
print(f'正文内容为：{content_str}')



html02=requests.post('https://exercise.kingname.info/exercise_requests_post',json=data).content.decode()
# print(html02)