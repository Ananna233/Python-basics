# open 参数介绍
# file：用来指定打开的文件（不是文件的名字，而是文件的路径）
# mode：打开文件的模式，默认是 r 表示只读
# encoding：打开文件时的编码方式

# 路径分为两种：
# 1.绝对路径：从电脑盘符开始的路径
# 2.相对路径：
import os
print(os.sep)  # Windows系统里，文件夹之间使用 \ 分割   在Python的字符串里， \ 表示转义字符
# 在非Windows，文件之间使用 / 分割

# 路径书写的三种方式：1. \\   2.r'\'  3.'/'  (推荐使用3)
file = open('D:\\Python基础学习\\day013-文件操作\\01-代码\\xxx.txt',encoding='utf-8')
# 或者 file = open(r'D:\Python基础学习\day013-文件操作\01-代码\xxx.txt')
# file = open('D:/Python基础学习/day013-文件操作/01-代码/xxx.txt')
print(file.read())

# 相对文件：当前文件所在的文件夹开始的路径
# ../表示返回上一级
# ./ 可以省略不写，表示当前文件夹
# /  不能随便使用
# file = open('xxx.txt',encoding='utf-8')
# file = open('demo/sss.txt',encoding='utf-8')
file = open('../ppp.txt',encoding='utf-8')

print(file.read())

file.close()