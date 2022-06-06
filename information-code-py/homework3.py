# import wordcloud
# w = wordcloud.WordCloud()
# x = 'and that government of the people, by the people, for the people, shall not perish from the earth.'
# w.generate(x)
# w.to_file('output1.png')

import urllib.request
import re

url='http://www.cnblogs.com/over140/p/4440137.html'
req=urllib.request.Request(url)
resp=urllib.request.urlopen(req)
html_page=resp.read().decode('utf-8')
print(html_page)
title_pattern=r'(<a.*id="cb_post_title_url".*>)(.*)(</a>)'
title_match=re.search(title_pattern,html_page)
print(title_match)
#title=title_match.group(2)
#print(title)