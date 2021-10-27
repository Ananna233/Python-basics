# p231
# 字母表示它本身 ，很多字母前面加 \ 会有特殊含义

# \n: 表示换行  \t:表示一个制表符   \s:表示空白字符  \S:非空白字符
# \d: 表示数字 ,等价于[0-9]
import re

print(re.search(r'x\d+p', 'x456p'))  # <re.Match object; span=(0, 5), match='x456p'>
print(re.search(r'x[0-9]+p', 'x456p'))  # <re.Match object; span=(0, 5), match='x456p'>

# ^ 除了表示已指定的内容开始以外，在[]里还可以表示取反
# \D:表示非数字，等价于[^0-9]
print(re.search(r'\D+', 'hell0'))  # <re.Match object; span=(0, 4), match='hell'>
print(re.search(r'[^0-9]+', 'hell0'))  # <re.Match object; span=(0, 4), match='hell'>

# \w:表示数字、字母以及_  等价于[0-9a-zA-Z_]  汉字
print(re.findall(r'\w+', 'h*E-l2,l.o_w55'))  # ['h', 'E', 'l2', 'l', 'o_w55']

# \W : \w 取反
print(re.findall(r'\W+', 'h*E-l2,l.o_w55'))  # ['*', '-', ',', '.']
