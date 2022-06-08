# 说明

这个文件夹是2022信息实践课程python方向的作业集合，包含了个人对于python基本语法和爬虫、词云的一些学习。

## homework1.ipynb

编写于jupyter notebook。

主要实现的功能有：

- 列表的建立与其中元素的删除
- 字符串子串的提取（展示了从头提取和自尾部提取两种索引方式）
- 两个整数的加法（我尝试了很大数字的相加，但似乎没有越界）

## homework2.ipynb

编写于jupyter notebook

主要实现的功能是：

- 处理一个json格式的字典类型
- 并按需求输出对应键位的值

## 文件夹 spider-learn

参考网上的例程，爬取了豆瓣前100的高分电影，输出到json里，利用正则表达式处理数据，并命名为格式相对统一的样式。

blog是另一个爬虫程序的结果，但是源程序已经不在了。

## 文件夹 worldcloud-learn

主要参考同济子豪兄的github教程：https://github.com/TommyZihao/zihaopython。

分两步走，先出词云worldcloud_test1.py，再加上模板定制词云worldcloud_test2.py。

蒙版图片为download.png。词云图片分别为：wyy.jpg，wyy_pic.jpg。

## 文件夹 spider-do

主要是用爬虫爬取我想要的歌词，输出到文件。

实现的是从http://music.163.com/api/song/lyric?1949119429爬取歌曲《记念》的歌词，test1是输出到终端，test2是输出到jinian.txt。

## 文件夹 zhomework3

这个文件夹是我的作业。

主要是就是spider-do和worldcloud-learn两个文件夹的融合。

这一步很简单。

输出就是jinian_pic.jpg和jinian_pics.jpg。
