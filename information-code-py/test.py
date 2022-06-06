#coding=utf-8
import jieba
from wordcloud import WordCloud #导入词云模块
words = open('wyy.txt',encoding='gbk').read()#打开歌词文件，获取到歌词
new_words = ' '.join(jieba.cut(words))#使用jieba.cut分词，然后把分好的词变成一个字符串，每个词用空格隔开
wordcloud = WordCloud(width=1000, #图片的宽度
                      height=860,  #高度
                      margin=2, #边距
                      background_color='black',#指定背景颜色
                      font_path='C:\Windows\Fonts\Sitka Banner\msyh.ttc'#指定字体文件，要有这个字体文件，自己随便想用什么字体，就下载一个，然后指定路径就ok了；刚才的字体适用于英文字体，用在中文字体上会报错，所以换了一个中文字体
                      )
wordcloud.generate(new_words) #分词
wordcloud.to_file('ylxb2.jpg')#保存到图片