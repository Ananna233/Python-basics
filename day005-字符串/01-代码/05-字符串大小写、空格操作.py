# 修改大小写

# capitalize 让字符串第一个单词的首字母大写
print('hello world\ngood morning'.capitalize())  # Hello world
# good morning
# upper 所有字母大写
print('hello123'.upper())  # HELLO123

# lower 全小写
print('HeLLo WoRlD'.lower())  # hello world

# title 每个单词首字母大写
print('good morning'.title())  # Good Morning

# ljust(width,fillchar)
# width 长度  fillchar 填充字符，默认是空格
# 让字符以指定长度显示，如果长度不够，默认在右边使用空格补齐
print('Monday'.ljust(10, '+'))  # Monday++++
print('helloworld!!!'.ljust(10, '+'))  # helloworld!!!
print('Tuesday'.rjust(10, '-'))  # ---Tuesday

# center 居中填充
print('Ananna233'.center(20, '*'))  # *****Ananna233******

# lstrip rstrip 去掉左/右的空格 strip 去掉左右空格
# lstrip('?') 可以指定删除某种字符
print('   hahaha    '.lstrip())  # hahaha    <==
print('   apple     '.rstrip())  # apple
print('   banana    '.strip())  # banana

# 以某种固定格式显示的字符串 ，我们可以将它切割成为一个列表
name = 'zhangsan+lisi+tony+make'
newname = name.split('+')
print(newname)  # ['zhangsan', 'lisi', 'tony', 'make']
# 将列表转换为字符串
# join() iterable 可迭代对象-
fruits = ['apple','banana','pear','tomato','orange']
print('-'.join(fruits))  # apple-banana-pear-tomato-orange
print('*'.join('hello')) # h*e*l*l*o

# 字符串的运算符
