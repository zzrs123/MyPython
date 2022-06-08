# coding=utf-8
import requests
import json
import re
from bs4 import BeautifulSoup
import jieba
import wordcloud #导入词云模块
# 处理图片模块
import imageio
lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(1949119429) + '&lv=1&kv=1&tv=-1'
lyric = requests.get(lrc_url)
soup = BeautifulSoup(lyric.text, 'lxml')
# print(soup)
# 此时的输出其实很不好看，并不是需要的txt文件格式
# "lyric":"[00:00.000]
# 作词 : 雷雨心/蒋思涵\n
# [00:01.000] 作曲 : 雷雨心\n
# [00:02.000] 原唱 : 雷雨心\n
# [00:08.48]出品：网易飓风\n
# [00:10.63]【此版本为正式授权翻唱作品】\n
# [00:15.46]\n[00:19.39]时间一

# 进行数据的过滤
## 先变为json
json_obj = lyric.text
# print(json_obj)
json1 = json.loads(json_obj)
print(json1)
# print(type(json1)) 字典类型
lrc = json1['lrc']['lyric']
pat = re.compile(r'\[.*\]')
lrc = re.sub(pat, "", lrc)
lrc = lrc.strip()
print(lrc)
# print(type(lrc))字符串类型
# 我想对这个字符串进行截取，只取歌词
print(len(lrc))
print(lrc[-21])  # -20是倒数第二行的换行符，-21是“司”，
# for i in range(645):
#     if lrc[-i]=='远':
#         print(i)
#         break
# -206是歌词正文
# lrc_do = lrc[0:441]
# 0-441其实也不太好，前面还有一段碍眼
# for i in range(0,441):
#     if lrc[i] == '时':
#         print(i)
#         break
# 输出57
lrc_do = lrc[56:441]
# 这一版好很多
print(lrc_do)
# 把lrc_do写进去
with open('jinian.txt', "w")as jinian:
    jinian.write(lrc_do)

# 接下来就可以用前面尝试过的词云程序worldcloud_test2.py来制作词云

# mk = imageio.imread("download.png")# 这里想换一个蒙版图
# mk = imageio.imread("jinian.jpg") #后来感觉还不如五角星，以汉字六作为蒙版感觉效果不好
mk = imageio.imread("download.png")
w = wordcloud.WordCloud(mask=mk)

w = wordcloud.WordCloud(width=1000,
                            height = 700,
                            background_color = 'white',
                            font_path = 'C:\Windows\Fonts\Sitka Banner\msyh.ttc',
                            mask = mk,
                            scale = 15)
# 这里把txt文件改为jinian.txt
words = open('jinian.txt',encoding='gbk').read()
new_words = ' '.join(jieba.cut(words))
w.generate(new_words)
# w.to_file('jinian_pic.jpg')#保存到图片
w.to_file('jinian_pisc.jpg')#保存到图片