'''
第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
'''
import re

with open('test.txt','w') as f:
    f.write('Dear maintainer:\
//\n\
/ Once you are done trying to optimize this routine,\n\
/ and have realized what a terrible mistake that was,\n\
// please increment the following counter as a warning\n\
// to the next guy:\n\
// \n\
// total_hours_wasted_here = 42')

with open('test.txt','r') as file:
    strings=file.read()
reobj=re.compile('[a-zA-Z]+')
match=reobj.findall(strings)
i=0
word_dict={}

#以单词的小写作为键值进行统计，同时要
for word in match:
    if word.lower() in word_dict:
        word_dict[word.lower()]=word_dict[word.lower()]+1
    else:
        word_dict[word.lower()]=1
with open('result.txt','w') as f:
    for(word,num) in word_dict.items():
        f.write(word+":%d\n"%num)





