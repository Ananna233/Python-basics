#
# 定义类：类名怎么定义？使用class来定义一个类
# class 类名：类名一般需要遵守大驼峰命名法，每一个单词的首字母都大写
# 1.class <类名>:
# 2.class <类名>(object):

class Student(object):  # 关注这个类有哪些特征和行为
    # 在__init__方法里，以参数形式定义特征，我们称之为属性
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    # 行为定义为一个个函数
    def run(self):
        print('正在跑步')

    def eat(self):
        print('正在吃东西')

# 小明今天18岁，身高175，明天早上跑完步，会去吃东西
# 小红今天17岁，身高165，不跑步，喜欢吃东西
# Student() ==>会自动调用 __init__方法

# 使用Student类创建了两个实例对象 s1  s2
# s1 s2 都会有name，age，height属性，同时都有run和eat方法
s1 = Student('小明', 18, 175)
s2 = Student('小红', 17, 165)

# 根据 业务逻辑  让不同的对象执行不同的行为
s1.run()
s1.eat()

s2.eat()

# print(s2.__init__())