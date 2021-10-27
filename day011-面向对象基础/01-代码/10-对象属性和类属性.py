class Person(object):
    type = '人类'  # 这个属性定义在类里，函数之外，我们称之为类属性

    def __init__(self, name, age):
        self.name = name
        self.age = age


# p1和p2都是通过Person类创建出来的实例对象
# Person类存在哪个地方？
# Person我们称之为类对象
# p1和p2称呼他们为实例对象 只要创建了一个实例对象就有自己的name和age属性
# name和age 是对象属性,在__init__方法里，以参数的形式定义的
# 对象属性：每个实例对象都单独保存一份的属性 每个实例对象之间的属性没有关联，互不影响

p1 = Person('zhangsan', 18)
p2 = Person('lisi', 19)

print('0x%X   0x%X   0x%X' % (id(Person), id(p1), id(p2)))

# 类属性可以通过类对象和实例对象获取
print(Person.type)  # 人类

# 实例对象获取
print(p1.type)  # 人类
print(p2.type)  # 人类

# 类属性只能通过类对象修改，实例对象无法修改类属性
p1.type = 'human'  # 实际上是给P1加了一个属性 type = human
print(p1.type)  # human
print(p2.type)  # 人类

Person.type = 'HUMAN'  # 修改类属性
print(p2.type)  # HUMAN
print(p1.type)  # human P1自己有type属性 ，不会再找类属性