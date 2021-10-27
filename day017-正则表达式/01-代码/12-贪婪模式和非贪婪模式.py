import re

# 在Python的正则表达式里，默认是贪婪模式，尽可能多的匹配
# 在贪婪模式后面添加 ? 可以将贪婪模式转换成为非贪婪模式
m = re.search(r'm.*a', '03asjmdsadas')
print(m.group())  # mdsada

# 尽可能少的匹配
n = re.search(r'm.*?a', '03asjmdsadas')
print(n.group())  # mdsa

x1 = re.match(r'aa(\d+)', 'aa2324ddd')
print(x1.group(0))  # aa2324
print(x1.group(1))  # 2324

x2 = re.match(r'aa(\d+?)', 'aa2324ddd')
print(x2.group(0))  # aa2
print(x2.group(1))  # 2

x3 = re.match(r'aa(\d+)ddd', 'aa2324ddd')
print(x3.group(0))  # aa2324ddd
print(x3.group(1))  # 2324

x4 = re.match(r'aa(\d+?)ddd', 'aa2324ddd')  # 在满足匹配规则的情况下  尽可能最少匹配
print(x4.group(0))  # aa2324ddd
print(x4.group(1))  # 2324

x5 = re.match(r'aa(\d+?).*', 'aa2324ddd')
print(x5.group(0))  # aa2324ddd
print(x5.group(1))  # 2

x6 = re.match(r'aa(\d??)(.*)', 'aa2324ddd')
print(x6.group(0))  # aa2324ddd
print(x6.group(1))  # 空
print(x6.group(2))  # 2324ddd
