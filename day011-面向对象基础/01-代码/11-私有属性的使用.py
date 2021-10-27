import datetime


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 1000  # 以两个下划线开始的变量是私有变量

    def test(self):
        self.__money += 10  # z这里可以访问私有变量

    def get_money(self):
        print('{}查询了余额'.format(datetime.datetime.now()))
        return self.__money

    def set_money(self, qian):
        if type(qian) != float and type(qian) != int:
            print('设置不合法')
            return
        print('{}修改了余额为{}'.format(datetime.datetime.now(), qian))
        self.__money = qian
        return self.__money

    def __demo(self):  # 以两个下划线开始的函数，是私有函数，在外部无法调用
        print('我是demo函数，name={}'.format(self.name))

    def test(self):
        self.__demo()  # 内部可以调用

p = Person('zhangsan', 18)
print(p.name, p.age)  # zhangsan 18 可以直接获取
# print(p.__money)  # 不能直接获取到私有变量

# 获取私有变量的方式：
# 1.使用 对象_类名__私有变量名获取
print(p._Person__money)  # 1000 通过这种方式也能获取到私有变量

# 2.定义get和set方法获取
print(p.get_money())
print(p.set_money(125.6))
# 3.使用property方法可以获取
# 暂不了解

# p.__demo()  # 不能直接调用  私有方法
p._Person__demo()  # 我是demo函数，name=zhangsan