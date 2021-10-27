class Person(object):
    def __init__(self, name):
        self.name = name
        self.dog = None

    def work_with_dog(self):
        if self.dog is not None and isinstance(self.dog, Dog):
            self.dog.work()


class Dog(object):
    def work(self):
        print('狗正在工作')


class PoliceDog(Dog):
    def work(self):
        print('警犬正在攻击坏人')


class BlindDog(Dog):
    def work(self):
        print('导盲犬正在领路')


class DrugDog(Dog):
    def work(self):
        print('缉毒犬正在搜毒')


p = Person('张三')
pd = PoliceDog()
p.dog = pd  # 往Person里添加属性dog
p.work_with_dog()

pd = BlindDog()
p.dog = pd  # 往Person里添加属性dog
p.work_with_dog()

pd = DrugDog()
p.dog = pd  # 往Person里添加属性dog
p.work_with_dog()
