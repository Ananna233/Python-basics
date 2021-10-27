# p205
from collections.abc import Iterable


class Demo(object):
    def __init__(self, x):
        self.x = x
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):

        self.count += 1
        if self.count <= self.x:
            return self.count - 1
        else:
            raise StopIteration  # 让迭代器停止

d = Demo(10)

# i = d.__iter__()
# i.__next__()

i = iter(d)  # 内置函数iter 可以获取一个可迭代对象的迭代器
print(next(i))
print(next(i))
print(next(i))
print(next(i))