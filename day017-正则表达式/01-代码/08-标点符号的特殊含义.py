# p230

import re

# \s 表示任意的非打印(空白)字符
print(re.search(r'\s', 'hello world'))  # 空格 <re.Match object; span=(5, 6), match=' '>
print(re.search(r'\s', 'hello\nworld'))  # 换行 <re.Match object; span=(5, 6), match='\n'>
print(re.search(r'\s', 'hello\tworld'))  # 制表符 <re.Match object; span=(5, 6), match='\t'>
print(re.search(r'\n', 'hello\nworld'))  # <re.Match object; span=(5, 6), match='\n'>

# \S  表示非空白字符
print(re.search(r'\S', '\t\n af'))  # <re.Match object; span=(3, 4), match='a'>

print('---------------')
# 标点符号的使用
# () : 用来表示一个分组
m = re.search(r'h(\d+)x', 'sh8269xaffg')
print(m.group())  # h8269x
print(m.group(1))  # 8269
# 如果要表示括号，需要使用\
m1 = re.search(r'\(.*\)', '(1+2)*3+4')
print(m1.group())  # (1+2)

# . 表示匹配除换行以外的其他任意字符
# 如果想匹配. 需要使用\.

# [] 用来表示可选项范围  [x-y] 从x到y的区间，包含x和y
# m2 = re.search(r'f[0-5]m', 'asf5md')  # <re.Match object; span=(2, 5), match='f5m'>
# m2 = re.search(r'f[0-5]+m', 'asf43305md')  # <re.Match object; span=(2, 9), match='f43305m'>
# m2 = re.search(r'f[a-d]+m', 'asfacbmd')  # <re.Match object; span=(2, 7), match='facbm'>
m2 = re.search(r'f[0-5a-dx]+m', 'asfa2cxbmd')  # 0<=value<=5  或者 a<=value<=d 或者 value=x
# <re.Match object; span=(2, 9), match='fa2cxbm'>
print(m2)

# | 用来表示或者  和 [] 有一定的相似，但有区别
# [] 里的值表示的是区间，而且是当个字符  r'0|5|d'  可等价为 [05d]
# | 就是可选值，可以出现多个值，如下x|y|prz  中的prz
m3 = re.search(r'f(x|y|prz)m', 'hello fprzm')  # <re.Match object; span=(6, 11), match='fprzm'>
# m3 = re.search(r'f(x|y|prz)+m', 'hello fxxprzm')
print(m3)

# {} 用来限定前面元素出现的次数
# {n}: 表示前面的元素出现n次
print(re.search(r'go{2}d', 'good'))  # <re.Match object; span=(0, 4), match='good'>
# {n,}:表示前面元素出现n次以上
print(re.search(r'go{2,}d', 'gooooood'))  # <re.Match object; span=(0, 8), match='gooooood'>
# {,n}:表示前面的元素出现n次以下
print(re.search(r'go{,2}d', 'gd'))  # <re.Match object; span=(0, 2), match='gd'>
# {m,n}:表示前面的元素出现m到n次  包含m,n  ==>[m,n]
print(re.search(r'go{3,5}d', 'goood'))  # <re.Match object; span=(0, 5), match='goood'>

print('**************************')

# *:表示前面的元素出现任意次(0次及以上) 等价于{0,}
print(re.search(r'go*d', 'gd'))  # <re.Match object; span=(0, 2), match='gd'>
# print(re.search(r'go*d', 'gooooooooooooooood'))  # <re.Match object; span=(0, 18), match='gooooooooooooooood'>

# +: 表示前面的元素至少出现一次，等价于{1,}
print(re.search(r'go+d', 'good'))  # <re.Match object; span=(0, 4), match='good'>

# ?:两种用法:
# 1.规定前面的元素最多只能出现一次，等价于{,1}
# 2.将贪婪模式转换成为非贪婪模式
print(re.search(r'go?d', 'gd'))  # <re.Match object; span=(0, 2), match='gd'>

print('|||||||||||||||||||||')

# ^: 以指定的内容开头  $: 以指定的内容结尾
# ^ 除了表示已指定的内容开始以外，在[]里还可以表示取反
print(re.search(r'^a.*i$', 'aofi'))  # <re.Match object; span=(0, 4), match='aofi'>
print(re.search(r'^a.*i$', 'dfsd\naofi\n fee', re.M))  # <re.Match object; span=(5, 9), match='aofi'>
