class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    # def __next__(self):  # 使用！=运算符会自动调用这个方法
    #     pass
    def __gt__(self, other):  # greater than 使用>会自动调用这个方法
        return self.age > other.age

    # def __ge__(self, other):  # 使用 >= 运算符会自动调用
    # def __it__(self, other):  # less than p1 < p2
    # def __le__(self, other):  # <=
    def __add__(self, other):  # + 加法会自动调用
        return self.age + other.age

    def __sub__(self, other):  # - 减法会自动调用
        return self.age - other.age  # 传什么参数  关键在于函数内部怎么实现

    # def __mul__(self, other):  # 乘法会自动调用
    # def __truediv__(self, other):  # / 除法会自动调用
    # def __pow__(self, power, modulo=None):  # ** 幂运算
    # def __str__(self):
    def __int__(self):
        return 10  # 使用int()时会调用它，，，是自己定义规则

    # def __float__(self):  # 使用float


p1 = Person('zhangsan', 18)
p2 = Person('zhangsan', 18)
p3 = Person('李四', 20)

print(p1 is p2)  # False
# print(p1 == p2)  # False
# ==运算符本质其实是调用对象的__eq__方法，获取__eq__方法的返回结果
# a == b  --> a.__eq__(b)

print(p1 == p2)  # True  （列表==比较会有他自己的内置方法）

# != 本质是调用__ne__方法（not equa） 或者__eq__方法取反
print(p1 != p2)  # False

print(p1 > p3)  # False

print(p1 + p2)  # 36

print(p1 - p2)  # 0

# str()将对象转换成为字符串，会自动调用__str__方法
# 1.str()  2.打印对象也会调用
print(str(p1))  # 转换成为字符串，默认转换成为类型+内存地址

# int() ==》调用对象的__int__方法
print(int(p1))  # 10
