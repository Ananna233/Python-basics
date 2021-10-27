nums = [3,5,6,4,2,1,9,7,8]

# 调用列表的sort方法可以直接对列表进行排序
# 直接对原有的列表进行排序
nums.sort()
print(nums) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 倒序
nums.sort(reverse=True)
print(nums) # [9, 8, 7, 6, 5, 4, 3, 2, 1]

# 内置函数sorted，不会改变原有的列表数据，会生成一个新的有序数据
x = sorted(nums)
print(nums) # [9, 8, 7, 6, 5, 4, 3, 2, 1] 没有改变
print(x)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 反转
names = ['zhangsan','lisi','wangwu']
names.reverse()
print(names) # ['wangwu', 'lisi', 'zhangsan']
# 等同于 print(names[::-1])