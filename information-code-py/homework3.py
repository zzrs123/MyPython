import wordcloud
w = wordcloud.WordCloud()
x = 'and that government of the people, by the people, for the people, shall not perish from the earth.'
w.generate(x)
w.to_file('output1.png')

