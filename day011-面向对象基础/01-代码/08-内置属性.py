class Person(object):
    '''
    这是一个人类
    '''
    __slots__ = ('name', 'age')  # 约束，规定可以出现的属性

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃饭')


# 'name':'zhangsan','age':18,'eat':<function>
p = Person('zhangsan', 18)
# print(dir(p))  # 把对象所有支持的属性列出
print(p.__class__)  # <class '__main__.Person'>
print(p.__dict__)  # {'name': 'zhangsan', 'age': 18}  把对象属性和值转换为字典

#     这是一个人类  文档说明
print(p.__doc__)  # 对象名.__doc__
print(Person.__doc__)  # 类名.__doc__

print(p.__module__)  # __main__
