#coding=utf-8
# from traceback import format_exception_only
from turtle import width
import jieba
from wordcloud import WordCloud
# 处理图片模块
import imageio
mk = imageio.imread("download.jpg")
w = wordcloud.WordCloud(mask=mk)

w = worldcloud.WorldCloud(width=1000,
                            height = 700,
                            background_color = 'white',
                            font_path = 'C:\Windows\Fonts\Sitka Banner\msyh.ttc',
                            mask = mk,
                            scale = 15)
words = open('wyy.txt',encoding='gbk').read()
new_words = ' '.join(jieba.cut(words))
worldcloud.generate(new_words)
wordcloud.to_file('wyy_pic.jpg')#保存到图片