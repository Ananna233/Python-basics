class Student(object):
    __slots__ = ('name', 'age', 'city')  # 这个属性直接定义在类里，是一个元组，用来规定对象可以存在的属性

    def __init__(self, x, y):
        self.name = x  # 出现橙色是waning  可能会有bug
        self.age = y

    def say_hello(self):
        print('hello，我是', self.name)


# Student('zhangsan', 18)这段代码具体做了什么呢？
# 1.调用__new__方法，用来申请内存空间
# 2.调用__init__方法，并让self指向申请好的那段内存空间
# 3.让s1也指向创建好的内存空间
s1 = Student('zhangsan', 18)

print('s1的名字是', s1.name)  # s1的名字是 zhangsan
s1.say_hello()  # hello，我是 zhangsan

s2 = Student('tony', 21)
s2.say_hello()  # hello，我是 tony

# 没有属性，会报错
# print(s1.height)

# 动态属性
# 直接使用等号给一个属性赋值
# 如果这个属性以前不存在，会给对象添加一个新的属性
# 如果这个属性以前存在，会修改这个属性对应的值
s1.city = '北京'  # 给对象添加了一个city属性
print(s1.city)  # 北京

s1.name = '张三'
print(s1.name)  # 张三
