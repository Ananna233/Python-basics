# p227
# compile 编译
# 在re模块里，可以使用re.方法调用函数，还可以调用re.compile得到一个对象

import re

# 可以直接调用re.search方法
m = re.search(r'm.*a','jsifmsf5afjr')
print(m)

r = re.compile(r'm.*a')
x = r.search('jsifmsf5afjr')
y = r.search('gdjamewage')
print(x)
print(y)  # 常用于用一个正则规则匹配多个字符串
