import lxml
import requests
import pymongo
import redis
from lxml import html

connection = pymongo.MongoClient()
db = connection.Chapter6
handler = db.white

client = redis.StrictRedis()

content_list=[]
url=client.lpop('url_quene')
source=requests.get(url,timeout=10).content.decode("gbk")
# print(source)
selector=lxml.html.fromstring(source)
Chapter_name=selector.xpath('//div[@class="border"]/h1/text()')[0]
print(Chapter_name)
content=selector.xpath('//div[@id="readbox"]/div[@id="content"]/text()').strip()
# /*[@id="content"]/text()[3]
# / html / body / div[3] / div[2] / div[1] / text()[3]
print(content)
# content_list.append({'title':Chapter_name,'content':'\n'.join(content)})
# print(content_list)
#
# handler.insert(content_list)