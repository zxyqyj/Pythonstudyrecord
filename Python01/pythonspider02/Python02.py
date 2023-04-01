#自己尝试从qq音乐爬取周杰伦的歌曲
#他妈的，太难了，搞不到
import requests

url='https://u.y.qq.com/cgi-bin/musics.fcg?_=1648817022664&sign=zzbd7a5d2c75vgrfck33zlptdp7nxpseg945d2833'
headers={
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
}
reponse=requests.get(url=url,headers=headers)

print(reponse.text)