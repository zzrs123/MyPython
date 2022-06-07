#coding=utf-8

import jieba
import wordcloud #导入词云模块
# 处理图片模块
import imageio
mk = imageio.imread("download.png")
w = wordcloud.WordCloud(mask=mk)

w = wordcloud.WordCloud(width=1000,
                            height = 700,
                            background_color = 'white',
                            font_path = 'C:\Windows\Fonts\Sitka Banner\msyh.ttc',
                            mask = mk,
                            scale = 15)
words = open('wyy.txt',encoding='gbk').read()
new_words = ' '.join(jieba.cut(words))
w.generate(new_words)
w.to_file('wyy_pic.jpg')#保存到图片