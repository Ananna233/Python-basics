# p204
# 有很多可迭代对象：list/tuple/dict/str/set/range/filter/map
# for...in 可迭代对象
from collections.abc import Iterable


class Demo(object):
    def __init__(self, x):
        self.x = x
        self.count = 0

    def __iter__(self):  # 只要重写了 __iter__方法就是一个可迭代对象
        return self

    def __next__(self):
        # 每一次for...in都会调用一次__next__方法,获取返回值
        self.count += 1
        if self.count <= self.x:
            return self.count - 1
        else:
            raise StopIteration  # 让迭代器停止


d = Demo(10)
print(isinstance(d, Iterable))  # isinstance：用来判断一个实例对象是否是由指定的类创建出来的
names = list('hello')
print(isinstance(names, Iterable))

# for...in 循环的本质就是调用对象的__iter__方法，获取这个方法的返回值
# 这个返回值需要是一个迭代器对象，然后再调用这个对象__next__方法
# for x in d:
#     print(x)

for i in Demo(10):
    print(i)
