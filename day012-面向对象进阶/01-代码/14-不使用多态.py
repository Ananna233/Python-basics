# 多态是基于继承，通过子类重写父类的方法
# 达到不同的子类对象调用相同的父类方法，得到不同的结果
# 提高代码的灵活度

class PoliceDog(object):
    def attack_enemy(self):
        print('警犬正在攻击坏人')


class BlindDog(object):
    def lead_road(self):
        print('导盲犬正在领路')


class DrugDog(object):
    def search_drug(self):
        print('缉毒犬正在搜毒')


class Person(object):
    def __init__(self, name):
        self.name = name

    def work_with_pd(self):
        self.dog.attack_enemy()  # self.dog => pd

    def work_with_bd(self):
        self.dog.lead_road()  # self.dog => bd

    def work_with_dd(self):
        self.dog.search_drug()  # self.dog => dd


p = Person('张三')
pd = PoliceDog()
p.dog = pd  # 往Person里添加属性dog
p.work_with_pd()

pd = BlindDog()
p.dog = pd  # 往Person里添加属性dog
p.work_with_bd()

pd = DrugDog()
p.dog = pd  # 往Person里添加属性dog
p.work_with_dd()
