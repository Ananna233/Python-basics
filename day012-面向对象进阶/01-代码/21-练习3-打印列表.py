class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '姓名:{},年龄:{}'.format(self.name, self.age)


p1 = Person('zhangsan', 18)
p2 = Person('lisi', 21)

print(p1)  # 调用__str__ 或 __repr__方法
persons = [p1, p2]

# 直接打印列表，会调用列表元素的__str__或者__repr__方法
print(persons)  # 直接打印一个列表，会把列表里的每一个对象的内存地址打印出来
# 实际上应该是调用__repr__方法  重写__repr__方法