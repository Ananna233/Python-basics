# 魔法方法：也叫魔术方法，是类里的特殊方法
# 特点：
# 1.不需要手动调用，会在适合的时机自动调用
# 2.这些方法，都是以__开始，以__结束
# 3.方法名都是系统规定好的，在合适的时机自己调用

class Person(object):
    def __init__(self, name, age):
        # 在创建对象时，会自动调用这个方法
        print('__init__方法被调用了')
        self.name = name
        self.age = age

    def __del__(self):
        # 当对象被销毁时，会自动调用这个方法
        print('__del__方法被调用了')

    def __repr__(self):
        return 'hello'

    def __str__(self):
        return '姓名：{}，年龄：{}'.format(self.name, self.age)

    def __call__(self, *args, **kwargs):
        print('__call__方法被调用了')
        print('args={},kwagrs={}'.format(args, kwargs))
        fn = kwargs['fn']
        return fn(args[0], args[1])


p = Person('zhangsan', 18)
# del p  # 可以手动销毁

# 如果不做任何的修饰，直接打印一个对象，是对象的类型以及内存地址
print(p)  # <__main__.Person object at 0x000002131CBF5520>

# 当打印一个对象的时候，会调用对象的__str__ 或者__repr__ 方法
# 如果两个方法都重写了，选择__str__
# 总结：__str__ 方法的结果更在意可读性，__repr__方法的结果更在意正确性
# print(p)
print(repr(p))  # 调用内置函数repr会触发对象的__repr__方法
print(p.__repr__())  # 魔法方法一般不手动的调用
print(p)  # 姓名：zhangsan，年龄：18

# __str__  和 __repr__
# import datetime
# x = datetime.datetime(2020,9,28,11,52,15,258)
# print(x)  # 2020-09-28 11:52:15.000258 __str__
# print(repr(x))  # datetime.datetime(2020, 9, 28, 11, 52, 15, 258) __repr__

# p()  # 对象名()  ==> 调用这个对象的__call__方法  ==》p.__call__()

n = p(1, 2, fn=lambda x, y: x + y)  # 把对象当函数用
print(n)  # 3