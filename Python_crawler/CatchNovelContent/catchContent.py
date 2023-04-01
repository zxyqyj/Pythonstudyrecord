import requests
import redis
from lxml import html
from pymongo import MongoClient

client=MongoClient("mongodb://127.0.0.1:27017")
database=client['Chapter6']
collection=database['white']

client = redis.StrictRedis()

content_list=[]

while client.llen('url_quene')>0:
    flag=1
    url=client.lpop('url_quene').decode()
    while flag:
        try:
            source=requests.get(url,timeout=3).content.decode("gbk")
            print('已读网站')
            flag=0
        except:
            pass
    selector=html.fromstring(source)
    Chapter_name=selector.xpath('//div[@class="border"]/h1/text()')[0]
    #/html/body/div[3]/h1
    # 完整的xpath路径Chapter_name
    content=selector.xpath('//div[@id="readbox"]/div[@id="content"]/text()')
    #/*[@id="content"]/text()[3]
    # / html / body / div[3] / div[2] / div[1] / text()[3]
    content_list.append({'title':Chapter_name,'content':'\n'.join(content)})
    print("successful")
# print(content_list)
collection.insert_many(content_list)