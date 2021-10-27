class Person(object):
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('zhhangsan', 19)


# 。。。。啥也没有