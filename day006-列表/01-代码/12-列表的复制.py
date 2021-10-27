# 可变类型和不可变类型
a = 10
b = a
print('修改前：a的地址：%X,b的地址：%X'%(id(a),id(b))) # 修改前：a的地址：7FF8A58217C0,b的地址：7FF8A58217C0
a = 12
print('修改后：a的地址：%X,b的地址：%X'%(id(a),id(b))) # 修改后：a的地址：7FF8A5821800,b的地址：7FF8A58217C0
print(b) # 10 原a值

nums1 = [100,200,300]
nums2 = nums1
nums1[0] = 1
print(nums2) # [1, 200, 300] 修改nums1也会使nums2改变
'''
Python里的数据都是保存在内存里的，数据又分为可变类型和不可变类型；
不可变类型：字符串、数字、元组
可变类型：列表、字典、集合
不可变数据类型：如果修改值，内存地址会发生改变
可变数据类型：如果修改值，内存地址不会发生改变
# 使用内置函数id可以获取一个变量的内存地址：id(a)
'''
print('-------------')
# 列表的复制
x = [100,200,300]
y = x # 等号是内存地址的赋值
# x,y指向了同一块内存空间，会相互影响
z = x.copy()

x[0] = 1
print(y) # [1, 200, 300]
print(z) # [100, 200, 300]

# 除了使用列表自带的copy方法以外，还可以使用copy模块实现拷贝
import copy
p = copy.copy(x) # 效果等价于x.copy(),都是一个浅拷贝
print(p) # [1, 200, 300]
#

# 切片其实就是一个浅拷贝
names1 = ['zhangsan','lisi','wangwu','anan']
names2 = names1[::]
names1[0] = 'jack'
print(names2) # ['zhangsan', 'lisi', 'wangwu', 'anan']