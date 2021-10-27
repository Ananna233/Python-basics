class Person(object):
    type = 'human'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):  # 对象方法有一个参数self，指的是实例对象
        print(self.name + '正在吃' + food)

    # 如果一个方法里没有用到实例对象的任何属性，可以将这个方法定义成static  静态
    @staticmethod
    def demo():
        print('hello')

    @classmethod
    def test(cls):  # 如果这个函数只用到了类属性，我们可以定义成为一个类方法
        # 类方法会有一个参数 cls,也不需要手动的传参，会自动传参
        # cls指的是类对象 cls == Person  ==》True
        print(cls.type)
        print('yes')

p1 = Person('zhangsan', 18)
p2 = Person('lisi', 19)

# 实例对象在调用方法时，不需要给形参self传参，会自动的吧实例对象传递给self
# eat对象方法，可以直接使用  实例对象.方法名(参数)  调用
# 使用  对象名.方法名(参数)  调用的方式，不需要传递self，会自动将对象名传递给self

p1.eat('泡面')  # 直接使用实例对象调用方法 zhangsan正在吃泡面

# 对象方法还可以使用类对象来调用  类名.方法名()
# 这种方法，不会自动给self传参，需要手动的指定self
Person.eat(p2, '西红柿炒鸡蛋')  # lisi正在吃西红柿炒鸡蛋

# 函数方法是存在类对象里面的  class Person
# 函数方法P1 p2没有自己保持  但是p1 p2会绑定eat函数  P1 p2的eat不是同一个

# print(p1.eat)  # <bound method Person.eat of <__main__.Person object at 0x000001E019296520>>
# print(p2.eat)  # <bound method Person.eat of <__main__.Person object at 0x000001E0192E00D0>>
# print(Person.eat)  # <function Person.eat at 0x000001E0192E83A0>
# print(p1.eat is p2.eat)  # False

# 静态方法
Person.demo()
p1.demo()

# 类方法：可以使用实例对象和类对象调用
p1.test()
Person.test()


# 静态方法：没有用到实例对象的任何属性
class Calculator(object):
    @staticmethod
    def add(a, b):
        return a + b


# 可以不创建对象直接使用方法 直接使用  类名.函数（）
print(Calculator.add(1, 5))  # 6



# 总结：
# 1.实例方法：会用到实例对象的属性，self指向这个方法的实例对象
# 两种调用方式：
#   A.实例对象.方法名() ==> 不需要手动给self传参，会自动将实例对象传递给self
#   B.类对象.方法名(, )  ==>需要手动的给self传参

# 2.类方法：会有一个参数cls，这个cls指的是类对象
# 如果一个方法只用到了类属性，可以将这个方法定义为类方法

# 3.静态方法：如果一个方法，既用不到实例对象，也用不到类对象，感觉就像和这个类没有关系一样，可以把这个方法定义为静态方法