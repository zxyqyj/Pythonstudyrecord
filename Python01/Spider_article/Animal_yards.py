import os
import re
import requests

html=requests.get('https://www.kanunu8.com/book3/6879/index.html').content.decode('gbk')
start_url = 'https://www.kanunu8.com/book3/6879/'

def get_toc(html):
    '''
    获取每一章链接，储存到一个列表并返回
    :param html: 目录页源代码
    :return: 每一章链接
    '''
    toc_url_list=[]
    toc_block=re.findall('<strong>正文</strong></td>(.*?)</tbody>',html,re.S)[0]
    # print(toc_block)
    #re.findall()后面跟[0]意味着从re.findall()返回的所有匹配项列表中取出第一个元素，即最先匹配到的那个结果。
    toc_url=re.findall('<a href="(.*?)">',toc_block,re.S)
    for url in toc_url:
        toc_url_list.append(start_url+url)
    # print(toc_url_list)
    return toc_url_list

def get_artical(html):
    '''
    # 获取每一章节的正文并返回章节名和正文
    :param html: 每一章的源代码
    :return: 章节名 正文
    '''
    chapter_name=re.search('size="4"> (.*?)</font>',html,re.S).group(1)
    text_block=re.search('<p>(.*?)</p>',html,re.S).group(1)
    text_block=text_block.replace('<br />','').strip()
    return chapter_name,text_block

def save(chapter,article):
    '''
    将每一章保存到本地
    :param chapter: 章节名
    :param article: 正文内容
    :return: None
    '''
    os.makedirs('动物农场',exist_ok=True)
    #如果有此文件夹就什么也不做
    with open(os.path.join('动物农场',chapter+'.txt'),'w',encoding='gbk') as f:
        f.write(article)


def query(url):
    return requests.get(url).content.decode('gbk')

def run():
    url_list=get_toc(html)
    for item in url_list:
        html1=query(item)
        chapter,text=get_artical(html1)
        save(chapter,text)

if __name__ == '__main__':
    run()
    # get_toc(html)