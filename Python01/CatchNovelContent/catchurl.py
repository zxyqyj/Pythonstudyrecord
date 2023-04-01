import lxml.html
import redis
import requests
import selector
from redis import client

html = requests.get('https://www.bbiquge.net/book/24881/').content.decode('gbk')

# print(html)
# 检查是否爬取到源文件
url_list=[]
selector=lxml.html.fromstring(html)
#xml.html.fromstring是一个函数，用于将HTML字符串转换为可操作的Element对象。它是lxml库中的一个函数，可以用于解析HTML文档并提取其中的数据。
#Element对象对应网页的 HTML 元素。每一个 HTML 元素，在 DOM 树上都会转化成一个Element节点对象（以下简称元素节点）。
url_list_part = selector.xpath('//dl[@class="zjlist"]/dd/a/@href')
#/html/body/div[4]/dl/dd[1]/a 完整的xpath
for url in url_list_part:
    url_list.append('https://www.bbiquge.net/book/24881/'+url)

# print(url_list)
client=redis.StrictRedis()
#redis.StrictRedis()函数是Python Redis客户端库中的一个函数，用于创建一个连接到Redis服务器的StrictRedis对象，该
# 对象提供了对Redis命令的执行和数据操作的方法。StrictRedis对象是线程安全的，可以在多个线程中共享。它支持多个Redis数据库的连接和操作。
for url in url_list:
    client.lpush('url_quene', url)

# print(client)
# print(client.llen('url_quene'))
