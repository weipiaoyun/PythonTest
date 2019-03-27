#!/bin/usr/python
# coding:UTF-8
# 单行注释，上面注释coding为utf8,第一行只有对linux有效。最好设置成为#!/bin/usr/even python
"""
使用三个双引号的多行注释
使用三个双引号的多行注释
使用三个双引号的多行注释
"""
'''
使用三个单引号的多行注释
使用三个双引号的多行注释
使用三个双引号的多行注释
'''

# name = raw_input("Please input your name:")
# print("hello" + name)

if True:
    print "Answer"
    print "True"

else:
    print "False"

str1 = "List of name:\
        Hua Li\
        Chao Deng"
print str1

str2 = """
    List of Name:
    Hua li #liHua
    Chao Deng
    """

print str2;

# 输出换行
print "aaa"
print "bbb",  # 这里表示不换行
print "ccc"

# 变量赋值
a, b, c = 1, 2, "john"
print a, b, c

# 截取一段字符串; 前面的数必须要小于后面的数。如s[-2:-5]输出为空。下标要么全部为正，要么全部为负。
s = "012345678"
print s[1:5]  # 第一到第四个字符 (四个字符)
print s[-5:-2]  # -1为最后一个，-2为7. -5位4 .5-7 (三个字符)
print s[:5]  # 从第一到第5-1个字符
print s[2:]  # 从第二个到最后一个字符
print s[2:] * 2  # 乘以2,表示输出两遍。*是重复操作
print s[1:5:3]  # 第三个参数，步长，步长为3表示跳3-1 = 2。中间有两个跳过。

"""
import wx
app = wx.App()
frame = wx.Frame(None, -1, "Hello, World!");
frame.Show(True)
app.MainLoop()
"""
