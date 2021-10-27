import re

# 查找相关的方法
# match和search:     查找字符串，返回的结果是一个re.Match对象
# 共同点：1.只对字符串查询一次   2.返回值类型都是 re.Match
# 不同点：match是从头开始匹配，一旦匹配失败，就返回None；search是在整个字符串里匹配

# finditer:  查找到的所有的匹配数据放到一个可迭代对象里

# findall:  把查找到的所有字符串结果放到一个列表里

# fullmatch: 完整匹配，字符串需要完全满足正则规则才会有结果，否则就是None


m1 = re.match(r'hel', 'hello world good morning')
m2 = re.search(r'hel', 'hello world good morning')
m3 = re.match(r'good', 'hello world good morning')
m4 = re.search(r'good', 'hello world good morning')
# print(m1)  # <re.Match object; span=(0, 3), match='hel'>
# print(m2)  # <re.Match object; span=(0, 3), match='hel'>
# print(m3)  # None
# print(m4)  # <re.Match object; span=(12, 16), match='good'>


# finditer 返回的结果是一个可迭代对象
# 可迭代对象里的数据是匹配到的所有 结果，是一个re.Match类型的对象
print(re.search(r'x', 'aafsas xfsqfacxcxxx'))
m6 = re.finditer(r'x', 'aafsas xfsqfacxcxxx')

for t in m6:
    print(t)

m7 = re.findall(r'x\d+', 'aafsas x45fsqfacx6cx71xx9')
print(m7)  # ['x45', 'x6', 'x71', 'x9']

m8 = re.fullmatch(r'hello world','hello world')
print(m8)  # <re.Match object; span=(0, 11), match='hello world'>

m9 = re.fullmatch(r'h.*d','haa3a53s5s6 ld')
print(m9)  # <re.Match object; span=(0, 14), match='haa3a53s5s6 ld'>