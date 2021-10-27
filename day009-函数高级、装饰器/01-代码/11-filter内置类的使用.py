# filter 对可迭代对象过滤，得到的是一个filter对象
# Python2的时候是内置函数，Python3修改成了一个内置类

ages = [12, 25, 31, 16, 17, 21, 28, 3]
# filter可以给定两个参数，第一个参数是函数，第二个参数是可迭代对象
# filter结果是有一个filter类型的对象，filter对象也是一个可迭代对象
x = filter(lambda ele: ele > 18, ages)
# print(x)  # <filter object at 0x000001377DA95AF0>
for i in x:
    print(i)
