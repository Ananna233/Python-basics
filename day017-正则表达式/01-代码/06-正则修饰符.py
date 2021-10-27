# p228
import re

# 正则修饰符是对正则表达式进行修饰
# re.S  :让.  匹配换行\n
# re.I  :忽略大小写
# re.M  :让$能匹配到换行

# .  表示除换行以外的任意字符
x = re.search(r'm.*a', 'effdmsd\nafqw1af', re.S)
print(x)  # <re.Match object; span=(4, 14), match='msd\nafqw1a'>

y = re.search(r'x', 'good Xyz', re.I)
print(y)  # <re.Match object; span=(5, 6), match='X'>

# \w:表示的是字母和数字和_   +: 出现一次以上  $:以指定的内容结尾
z = re.findall(r'\w+$', 'i am boy\n you are girl\n he is man')
z2 = re.findall(r'\w+$', 'i am boy\n you are girl\n he is man', re.M)
print(z)  # ['man']
print(z2)  # ['boy', 'girl', 'man']
