# Python里的for循环是指for...in 循环，和C语言里的for不一样
# for语句格式：for 变量名 in 可迭代对象
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)


# range(a,b) 内置类 用来生成指定区间[a,b)的整数序列
# 注意：in的后面必须要是一个可迭代对象！！！
# 目前接触的可迭代对象：字符串、列表、字典、元组、集合、range
for i in range(0,10):
    print(i)  # 0,1,2,3,4,5,6,7,8,9

for x in 'hello':  # 实际上是一个遍历操作
    print(x)       # h/n  e/n  l/n  l/n  o/n