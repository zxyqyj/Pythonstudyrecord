from telnetlib import EC

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

b = webdriver.Chrome()
b.get('https://exercise.kingname.info/exercise_advanced_ajax.html')
# time.sleep(5)
# html=b.page_source
# print(html)
# input('按任意键结束')
try:
    WebDriverWait(b,30).util(EC.presence_of_element_located((By.CLASS_NAME,"content")))#参数是一个元组，元组第0项为By.XX，第一项为具体内容
    # WebDriverWait(b,30).util(EC.text_to_be_present_in_element((By.CLASS_NAME,"content"),'通关'))#两个参数：第一个参数是一个元组，元组第0项为By.XX，第一项为具体标签内容；第二个参数为部分
    #或者全部文本，又或是一段正则表达式
except Exception as _:
    print('网页加载太慢，不想等了。')
print(b.page_source)




 
# element = driver.find_element_by_id("passwd-id") #如果有多个符合条件的，返回第一个
# element = driver.find_element_by_name("passwd") #如果有多个符合条件的，返回第一个
# element_list = driver.find_elements_by_id("passwd-id") #以列表形式返回所有的符合条件的element
# element_list = driver.find_elements_by_name("passwd") #以列表形式返回所有的符合条件的element
# comment = driver.find_element_by_xpath('//div[@class="content"]')
# print(comment.text)
#
# comment = driver.find_elements_by_xpath('//p[starts-with(@id, "content_")]')
# for each in comment:
#     print(each.text)