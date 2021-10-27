# split rsplit splitlines partittion rpartition

# split 可以将一个字符串切割成一个列表
x = 'zhangsan-lisi-make-tony-anan'
y = x.split('-')
print(y) # ['zhangsan', 'lisi', 'make', 'tony', 'anan']
print(x.split('-m')) # ['zhangsan-lisi', 'ake-tony-anan']
z = x.rsplit('-')
print(z) # ['zhangsan', 'lisi', 'make', 'tony', 'anan']
# 指定切割次数，split是从左往右、、、rsplit是从右往左
print(x.split('-',2))  # ['zhangsan', 'lisi', 'make-tony-anan']
print(x.rsplit('-',2)) # ['zhangsan-lisi-make', 'tony', 'anan']

# splitline 按照行分割，返回一个包含各行作为元素的列表
mystr1 = 'hello \nworld'
print(mystr1.splitlines())
''' >>>hello
       world   ==>['hello ', 'world']
'''

# partition 指定一个字符串作为分隔符，分为三部分(元组)
# 前面   分隔符   后面
print('abcdef-IJKL-MN'.partition('-'))  # ('abcdef', '-', 'IJKL-MN') 从左往右
print('abcdef-IJKL-MN'.rpartition('-')) # ('abcdef-IJKL', '-', 'MN') 从右往左，找到第一个'-'进行分割


