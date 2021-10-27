print("hello world!")

# 数据类型的概念
# 在Python里面数据有各自对应的类型

# 数字类型：  整数类型int 、浮点型 float  、复数 complex
print(4)  # int 整数类型         4
print(3.1415)  # float类型      3.1415
print((-1) ** 0.5)  # complex类型 (6.123233995736766e-17+1j)

# 字符串类型：其实就是一段普通的文字
# Python里的字符串要求使用一对单引号、或者双引号来包裹
print("早上好")  # 早上好
print('555')  # 555

# 布尔类型：用来表示真/假
# 布尔类型里面只有两个值  True  False
print(4 > 1)  # True
print(1 > 4)  # False

# 列表类型
names = ['张三', '李四', 'wangduoyu', 'ananna233']
print(names)  # ['张三', '李四', 'wangduoyu', 'ananna233']
# 字典类型
person = {'name': '陈冬冬', "age": 18, 'addr': '广东', '身高': '175cm'}
print(person)  # {'name': '陈冬冬', 'age': 18, 'addr': '广东', '身高': '175cm'}

# 元组类型
nums = (3, 1, 5, 9, 7)
print(nums)  # (3, 1, 5, 9, 7)

# 集合类型
X = {5, 'hello', 'hi', 'haha', True}
print(X)  # {True, 5, 'haha', 'hello', 'hi'}
