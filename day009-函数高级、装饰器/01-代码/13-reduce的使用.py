from functools import reduce  # 导入模块的语法


# reduce 以前是一个内置函数
# 内置函数和内置类都在builtins.py文件里

def foo(x, y):  # reduce 函数调用过程：x=100,y=99 ==>x=100+99=199,y=36 ==>x=199+36=235,y=75==>...
    return x + y


scores = [100, 99, 36, 75]
print(reduce(foo, scores))  # 310

# 求所有学生的年龄
students = [
    {'name': 'zhangsan', 'age': 18, 'score': 98, 'height': 180},
    {'name': 'lisi', 'age': 20, 'score': 95, 'height': 182},
    {'name': 'wangwu', 'age': 21, 'score': 100, 'height': 175},
    {'name': 'tony', 'age': 23, 'score': 94, 'height': 185},
    {'name': 'xiaohhua', 'age': 19, 'score': 99, 'height': 181},
    {'name': 'make', 'age': 20, 'score': 90, 'height': 178},
]


def bar(x, y):
    # 没有初始化
    # x = {'name':'zhangsan','age':18,'score':98,'height':180},
    # y = {'name':'lisi','age':20,'score':95,'height':182}

    # 初始化x=0
    # x = 0
    # y = {'name':'zhangsan','age':18,'score':98,'height':180}
    return x + y['age']


print(reduce(bar, students, 0))  # 121
print(reduce(lambda x, y: x + y['age'], students, 0))  # 121
