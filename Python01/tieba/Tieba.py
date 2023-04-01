import re
import csv

with open('source.txt','r',encoding='utf-8') as f:
    source=f.read()

result_list=[]
username_list=re.findall('img username="(.*?)" class',source,re.S)
content_list=re.findall('class="d_post_content j_d_post_content " style="display:;">(.*?)<',source,re.S)
reply_time_list=re.findall('楼</span><span class="tail-info">(.*?)</span>',source,re.S)

for i in range(len(username_list)):
    result={'username':username_list[i].strip(),
            'content':content_list[i].strip(),
            'replytime':reply_time_list[i].strip()}#去掉抓取内容前后的空格 .strip()方法
    result_list.append(result)

print(result_list)

with open('tieba.csv','w',encoding='utf-8') as f:
    writer=csv.DictWriter(f,fieldnames=['username','content','replytime'])
    writer.writeheader()
    writer.writerows(result_list)