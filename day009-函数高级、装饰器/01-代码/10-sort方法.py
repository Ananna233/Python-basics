# 有几个内置函数和内置类，用到了匿名函数
nums = [4, 8, 2, 3, 6, 9, 1]

# 列表的sort方法，会直接对列表进行排序
# nums.sort()
# print(nums)  # [1, 2, 3, 4, 6, 8, 9]

# sorted内置函数，不会改变原有的数据，而是生成一个新的有序的列表
x = sorted(nums)
print(x)  # [1, 2, 3, 4, 6, 8, 9]

ints = (3, 5, 6, 9, 7, 8, 1, 4)
y = sorted(ints)  # [1, 2, 3, 4, 6, 8, 9]

students = [
    {'name':'zhangsan','age':18,'score':98,'height':180},
    {'name':'lisi','age':20,'score':95,'height':182},
    {'name':'wangwu','age':21,'score':100,'height':175},
    {'name':'tony','age':23,'score':94,'height':185},
    {'name':'xiaohhua','age':19,'score':99,'height':181},
    {'name':'make','age':20,'score':90,'height':178},
]

# 字典和字典之间不能使用比较运算
# student.sort()

# foo() takes 0 positional arguments but 1 was given
# foo这个函数需要0个位置参数，但是在调用的时候传递了一个参数

# def foo(ele):
#     # print('ele={}'.format(ele))  会遍历一遍
#     return ele['age']  # 通过返回值告诉sort方法，按照元素的那个属性进行排序

# 需要传递参数key 指定比较规则
# key 参数类型是函数

# 在sort内部实现的时候，调用了foo方法，并且传入了一个参数，参数就是列表里的元素

# students.sort(key=foo)

students.sort(reverse=True,key=lambda ele:ele['score'])
print(students)