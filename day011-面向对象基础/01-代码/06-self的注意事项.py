class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃东西')


p1 = Person('zhansan', 18)
p2 = Person('lisi', 22)
p1.eat()  # zhansan正在吃东西

# self 只有在调用的时候才会有指向