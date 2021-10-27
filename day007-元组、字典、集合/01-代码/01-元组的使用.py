# 元组和列表很像，都是用来保存多个数据
#  使用一对小括号()来表示一个元组
# 元组和列表的区别在于，列表是可变的，而元组是不可变数据类型
words = ['hello', 'words', 'zhangsan']
nums = (1, 2, 3, 4, 5, 6, 6, 5, 6)

# 和列表一样，也是一个有序的储存数据的容器
# 可以通过下标来获取元素
print(nums[2])  # 3
# nums[3] = 10 # 元组是不可变数据类型，不能修改
print(nums.index(5))  # 查找第一个5的下标
print(nums.count(6))  # 3 计数，6出现的次数

# 特殊情况:如何表示只有一个元素的元组？
# age = (18) # 这种书写方式，age是一个整数，并不是一个元组
# print(type(age)) # <class 'int'>
age = (18,)  # 如果元组里只有一个元素，要在最后加,
print(type(age))  # <class 'tuple'>

# tuple() 内置类
# 里面是可迭代对象
print(tuple('hello'))  # ('h', 'e', 'l', 'l', 'o')

# 怎样把列表转换成为元组？/元组转换成为列表？
# tuple list set 都是这样使用的
print(tuple(words))  # ('hello', 'words', 'zhangsan')
print(list(nums))  # [1, 2, 3, 4, 5, 6, 6, 5, 6]

# 字符串拼接 join  ==》 ''.join()
# 元组，列表这些都可以拼接
print("".join(('h', 'e', 'l', 'l', 'o')))  # hello

# 元组也可以遍历
for i in nums:
    print(i)
