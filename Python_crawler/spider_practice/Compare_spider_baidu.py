import requests
import time
from multiprocessing.dummy import Pool

def query(url):
    requests.get(url)

start=time.time()
for i in range(100):
    query(' http://www.baidu.com')
end=time.time()
print(f'单线程访问100次时间：{end-start}')

start=time.time()
url_list=[]
for i in range(100):
    url_list.append(' http://www.baidu.com')
pool=Pool(5)
pool.map(query,url_list)#线程池的map()方法，第一个参数函数，第二个参数一个列表
end=time.time()
print(f'多线程访问100次时间：{end-start}')


