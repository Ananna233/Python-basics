# *args表示可变参数
# **kwargs 表示可变的关键字参数
# args和kwargs可以改成其他变量名字

def add(a, b, *args, **kwargs):
    # print('a = {},b = {}'.format(a, b))
    # print('args = {}'.format(args))  # 多出来的参数会以元组的形式保存到args
    print('kwargs = {}'.format(kwargs))  # 多出来的关键字参数会以字典的形式保存 kwargs = {'x': 34, 'y': 54}
    c = a + b
    for arg in args:
        c += arg
    return c


# add(1, 3)
# add(1, 3, 5, 7, 9, 0)  # a = 1,b = 3    args = (5, 7, 9, 0)  只有args这个

print(add(1, 2, 9, 78, 3, 56, x=34, y=54))  # kwargs = {'x': 34, 'y': 54}

print(add(1, 2, 9, 78, 3, 56, 34, 54))  # 237
