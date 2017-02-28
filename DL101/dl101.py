#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入正则表达式模块 re
import re
# 引入 collections 的计数器
from collections import Counter

# 打开文件；简单将文件名写死，用于读出
# 在 vim 中用:set fileencoding 查看，文件编码是 utf-8
rawfile = open("happiness_seg.txt")
# 打开文件；作为输出英文标点的目标文件
# 编码依然是 utf-8
outputfile = open("e_happiness_seg.txt",'a')


# 将所有中文标点转化为英文标点
table = {ord(f):ord(t) for f,t in zip(
u'，。：；！？《》【】（）％＃＠＆’‘“”、―',
u',.:;!?<>[]()%#@&\'\'\"\"\\-')}

# 逐行读出文件中每行，line 是 str 类型，注意编码转换
# 替换标点后，写入 outputfile 中
for line in rawfile.readlines():
    inputline = line.decode('utf-8')
    outputline = inputline.translate(table)
    outputfile.write(outputline.encode('utf-8'))

# 关闭文件
rawfile.close()
outputfile.close()


# 打开 outputfile 作为只读输入
# 用正则表达式，以标点符号分割句子
outputfile = open("e_happiness_seg.txt")
tempfile = open("tempfile.txt",'a')
# 建立一个数组类型变量，存储分出的句子
senlist = []
# 逐行读出，以标点符号分割成句子，将句子存放在数组 senlist 中
for line in outputfile.readlines():
    #senitem = str(re.split(r'[,.:;!?<>[]()%#@&\'\"\"\\-]\s*', line)).decode('string_escape')
    senitem = re.split(r'[,.:;!?<>()\'\"\\-]\s*', line)
    senlist.extend(senitem)

# 关闭文件
outputfile.close()

# 看一下 senlist，发现有些 item 为空；非空的 item 最后都有个空格
# 删除空 item

cleanlist = []

for item in senlist:
    if str(item) <> '':
        cleanitem = str(item)[:-1]
        cleanlist.append(cleanitem)

# 将清理过的文字内容写入 tempfile
tempfile.write(str(cleanlist).decode('string_escape'))

tempfile.close()

# 在句子数组 senlist 中，遍历每个 item
# 将每个 item 再以空格 split 成 item 建立临时list
# 将临时 linst 中的 item， join 成二分词组数组
# 最终结果存储在新 list bialist 中

# 建立临时list templist
templist = []

# 建立二分词组list
bialist = []

# 建立 desfile 存放所有二分词组
desfile = open("desfile.txt",'a')

# 遍历 cleanlist，拆开每个词
# 放在临时 list 中
for item in cleanlist:
    tempitem = item.split(" ")
    templist.append(tempitem)

# 遍历临时 list
# 建立所有二元词组
for item in templist:
    for i in range(len(item) - 1):
        biaitem = str(item[i]) + " " + str(item[i + 1])
        bialist.append(biaitem)

# 将二元词组写入 desfile
desfile.write(str(bialist).decode('string_escape'))

desfile.close()

# 建立 resultfile 存储结果

resultfile = open("resultfile.txt",'w')

count = Counter(bialist)

result = str(count.most_common(10)).decode('string_escape')

resultfile.write(result)

print result
