import lxml.html
import requests
from bs4 import BeautifulSoup

html=requests.get('https://tieba.baidu.com/f?kw=%E5%AD%99%E7%AC%91%E5%B7%9D').content

# print(html)

# selector=lxml.html.fromstring(html)

# info=selector.xpath('//div[@class="threadlist_abs threadlist_abs_onlyline "]/text()')
#
# for inf in info:
#     print(inf.strip())

# print(info)

soup=BeautifulSoup(html,'lxml')

info_2=soup.find(class_='threadlist_bright j_threadlist_bright')
# print(info_2)
# all_content=info_2.find_all('div class="threadlist_abs threadlist_abs_onlyline "')
all_content=info_2.find_all('div',{'class','threadlist_abs threadlist_abs_onlyline '},False)
print(all_content)


#BeautifulSoup(),find_all()方法不会用