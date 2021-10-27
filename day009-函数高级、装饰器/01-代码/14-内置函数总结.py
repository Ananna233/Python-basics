# 数学相关函数函数
# abs()绝对值函数
print(abs(-12))  # 12
# divmod(x,y)求两个数相除的商和余数
shang, yushu = divmod(13, 7)
print(shang, yushu)  #　1 6
# max(可迭代对象) 求最大值
# min(可迭代对象) 求最小值
# pow() 幂运算 pow(2,3)==2**3=8
# round(a, b) 四舍五入保留到指定小数位
print(round(3.1415926535,3))  # 3.142
# sum() 用来求和

# 可迭代对象相关的方法
# all(可迭代对象) 将里面所有可迭代对象转换成为布尔值，所有是True则True，否则False
print(all(['hello', 'hi', 1]))  # True
print(all([False, 'word', 0]))  # Flase
# any(可迭代对象) 将里面所有可迭代对象转换成为布尔值，有一个是True则True，全False则False
print(any([0, 1, 'hello']))  # True
print(any([False, 0, []]))  # False
# len() 获取长度
# iter 获取到可迭代对象的迭代器
# next() for...in 循环本质就是调用迭代器的next方法
# sorted() 用来排序的

# 转换相关
# bin() 将数字转换成为二进制
# chr() 将字符编码转换成为对应的字符
print(chr(97))  # a
# ord() 将字符转换成为对应的编码
print(ord('a'))  # 97
# eval()执行字符串里的Python代码
# oct() 将数字转换成为八进制
# hex() 将数字转换成为十六进制


# 变量相关
# globals() 用来查看所有的全局变量
# locals() 用来查看所有的局部变量

# 输入输出相关
# print
# input

# 判断对象相关的方法
# isinstance() 判断一个对象是否是由一个类创建出来的
# issubclass() 判断一个类是否是另一个类的子类


# 其他
# dir() 列出对象所有的属性和方法
nums = [1, 2, 3]
print(dir(nums))  # ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# exit(int) 以指定的退出码退出程序
# help() 用来查看帮助文档的
# id() 获取一个数据的内存地址
# open() 用来打开一个文件