class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class X(object):
    pass


class Y(object):
    pass


class Student(Person, X):
    pass


p1 = Person('zhangsan', 18)
p2 = Person('zhangsan', 18)

s = Student('lisi', 20)
# 获取两个对象的内存地址  id(p1) == id(p2)
print(p1 is p2)  # is 身份运算符是用来 比较是否是同一个对象

# type(p1） # 其实就是获取的就是类对象
if type(p1) == Person:
    print('p1是Person类创建的实例对象')

# s这个实例对象是否是由Student类创建的？
print(type(s) == Student)  # True
print(type(s) == Person)  # False

# isinstance 用来判断一个对象是否是由 指定的类（或者父类类）实例化出来的
print(isinstance(s, Student))  # True
print(isinstance(s, Person))  # True

print(isinstance(s, (Person, X)))  # True  多个继承，可以判断是否继承自里面的类
print(isinstance(s, (Person, X, Y)))  # True  多个继承，可以判断是否继承自里面的类

print('-----------------------')
# issubclass 用来判断一个类是否是另一个类的子类
print(issubclass(Student, Person))  # True
print(issubclass(Person, Student))  # False

print(issubclass(Student, (Person, X)))  # True
