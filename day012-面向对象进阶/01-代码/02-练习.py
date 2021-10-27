# 定义一个类属性，记录通过这个类创建了多少个对象

class Person(object):
    __count = 0

    def __init__(self, name, age):
        Person.__count += 1
        self.name = name
        self.age = age

    @classmethod
    def get_count(cls):
        return cls.__count

# 每次创建对象，都会调用__new__和 __init__方法
# 调用__new__方法，用来申请内存
# 如果不重写__new__方法，它会自动找object的__new__
# object的__new__方法，默认实现是申请一段内存，创建一个对象

p1 = Person('zhangsan', 18)
p2 = Person('lisi', 19)
p3 = Person('wangwu', 20)

print(Person.get_count())  # 3

# 申请了内存，创建了一个对象，被设置他的类型是Person
p4 = object.__new__(Person)
print(p4)  # <__main__.Person object at 0x000001DBF271F250>
p4.__init__('tony', 22)
