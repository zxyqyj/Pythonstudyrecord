#爬取网易云音乐并下载歌曲
import requests #数据请求模块 第三方模块 pip.exe install requests
import re   #正则表达式模块
import os #文件操作模块

filename= '../music\\'

if not os.path.exists(filename):
    os.mkdir(filename)

url='https://music.163.com/discover/toplist?id=3778678'
#headers请求头，用来伪装python代码的 把python代码伪装成
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
}
reponse=requests.get(url=url,headers=headers)
print(reponse.text)
# html_data=re.findall('<li><a href="/song\?id=(\d+)">(.*?)</a>',reponse.text)
# print(html_data)
# for num_id,title in html_data:
#     #http://music.163.com/song/media/outer/url?id=3778678.mp3
#     music_url=f'http://music.163.com/song/media/outer/url?id={num_id}.mp3'
#     #对于音乐播放地址发送请求，获取二级制数据内容
#     music_content=requests.get(url=music_url,headers=headers).content
#     with open(filename+title+'.mp3',mode='wb') as f:
#         f.write(music_content)
#     print(num_id,title)