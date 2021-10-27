def calc(a, b, fn):
    c = fn(a, b)
    return c


# def add(x, y):
#     return x + y
#
#
# def minus(x, y):
#     return x - y
#
#
# # 回调函数
# x1 = calc(1, 3, add)  # a=1,b=3,fn=add
# x2 = calc(10, 5, minus)  # a=10,b=5,fn=minus

x3 = calc(5, 7, lambda x, y: x + y)
x4 = calc(10, 3, lambda x, y: x - y)
x5 = calc(5, 4, lambda x, y: x * y)
x6 = calc(8, 2, lambda x, y: x / y)
print('x3={},x4={},x5={},x6={}'.format(x3, x4, x5, x6))  # x3=12,x4=7,x5=20,x6=4.0
