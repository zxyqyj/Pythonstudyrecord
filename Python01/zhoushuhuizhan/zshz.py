import os
import re
import time

import requests

html=requests.get('https://www.omyschool.com/article_list/521/%E5%92%92%E8%A1%93%E8%BF%B4%E6%88%B0/').content.decode('utf-8');
start_url='https://www.omyschool.com/'
# os.makedirs('咒术回站',exist_ok=True)

def get_url_comic(html):
    '''
    获取漫画每一章节的url
    :return: 返回一个装所有章节漫画的url的列表
    '''
    url_list=[]
    url_block=re.findall('<tbody>(.*?)</tbody>',html,re.S)[0] #先将大的框架爬下来
    # print(url_block)
    url_part=re.findall('<a href="(.*?)">',url_block,re.S)#获取每一章节的漫画url
    # print(url_part)
    for url in url_part:
        url_list.append(start_url+url)
    # print(url_list)
    return url_list

def get_content(html):
    '''
    获取每一章节的内容
    :param html: 每一章节的静态资源页面
    :return: 返回章节名+漫画名
    '''
    chapter=re.search('<span property="name">(\d*)話</span>',html,re.S).group(1)
    # print(chapter)
    content_block=re.search('<div class="uk-grid uk-grid-small">(.*?)<div class="uk-grid uk-grid-small">',html,re.S).group()
    contents=re.findall('src=\'(.*?)\'',content_block,re.S)#注意这里静态资源获取必须要将‘ 这个前面加反斜杠，进行转义
    pages=re.findall('alt="咒術迴戰: \d*話 - (.*?)"',content_block,re.S)
    # print(content)
    return chapter,contents,pages

def save(chapter,contents,pages):
    '''
    将获取的图片资源以及章节名保存下来
    :param chapter: 章节名
    :param content: 图片存放资源
    :return:
    '''
    dir=os.path.join('咒术回战',f'{chapter}')
    os.makedirs(dir,exist_ok=True)
    for page in pages:
        with open(os.path.join(dir,page+'.jpg'), 'wb') as f:
            i=0
            ++i
            r=requests.get(contents[i])
            f.write(r.content)
            time.sleep(10)#防止服务器因为太多请求涌入而拒绝连接，比较垃圾的一个做法


def get_html_content(url):
    '''
    将每一章节的url转换为静态html
    :param url: 每一章节的url
    :return: 返回每一章节的静态资源
    '''
    #需要线程池感觉
    return requests.get(url).content.decode('utf-8')

if __name__=='__main__':
    url_list=[]
    url_list=get_url_comic(html)
    # print(url_list)
    # for item in url_list:
    #     html1=get_html_content(item)
    #     print(html1)
    html01=get_html_content(url_list[0])
    chapter,contents,pages=get_content(html01)
    save(chapter,contents,pages)
    # chapter,content=get_content(html01)
    # print(chapter,content)
    # print(html01)
        # get_content(html1)