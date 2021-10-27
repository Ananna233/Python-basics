# p229
# 1.数字和字母都表示它本身
# 2.很多字母前面添加 \ 会有特殊含义（重点1）
# 3.绝大多数标点符号都有特殊含义（重点）
# 4.如果想使用标点符号，需要加 \ 转义字符

import re

# 表示字母数字本身
re.search(r'x', 'hello xyz')
re.search(r'5', 'sf56879')

print(re.search(r'd', 'good'))  # 字母d是普通的字符  <re.Match object; span=(3, 4), match='d'>
print(re.search(r'\d', 'good'))  # \d 有特殊含义，不再表示字母d  None
print(re.search(r'\d+', 'afsfw65ef25'))  # <re.Match object; span=(5, 7), match='65'>
# re.search('+','1+2')  # 不能直接使用，+ 有特殊含义
print(re.search('\+', '1+2'))  # <re.Match object; span=(1, 2), match='+'>