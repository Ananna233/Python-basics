

# 用来处理字符串，对字符串进行检索和替换的
# 1.查找  2.替换

import re

x = 'hello\\nworld'
print(x)  # hello\nworld
# 在正则表达式里，想要匹配一个 \ 需要使用 \\\\

# 第一个参数就是正则匹配规则
# 第二个参数表示需要匹配的字符串
# m = re.search('\\\\', x)

# 还可以在字符串前面加r，\\ 就表示 \
m = re.search(r'\\', x)

# match:匹配  和 search方法的执行结果是一个Match类型的对象
print(m)  # <re.Match object; span=(5, 6), match='\\'>
