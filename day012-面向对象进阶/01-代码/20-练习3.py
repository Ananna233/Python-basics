# 宠物店类 PetShop
# 属性：店名，店中的宠物【使用列表存储宠物】
# 方法：展示所有宠物的信息

class PetShop(object):
    def __init__(self, shopName, pets=None):
        self.shopName = shopName
        if pets is None:
            pets = []
        self.pets = pets

    def show_pers(self):
        if len(self.pets) == 0:
            print('本店还没有宠物')
            return
        print('{}有{}个宠物，他们是:'.format(self.shopName, len(self.pets)))
        for pet in self.pets:
            #     print('姓名:{}:性别{}，品种:{}，年龄:{}'.format(pet.name, pet.gender, pet.breed, pet.age))
            print(pet)


class Pet(object):
    def __init__(self, name, gender, age, breed):
        self.name = name
        self.gender = gender
        self.age = age
        self.breed = breed

    def bark(self):
        print(self.name + '正在叫')

    def eat(self):
        print(self.name + '正在吃东西')

    def __str__(self):
        return '姓名:{}:性别{}，品种:{}，年龄:{}'.format(self.name, self.gender, self.breed, self.age)


# 宠物狗类 PetDog
# 属性：昵称，性别，年龄，品种
# 方法：叫，拆家，吃饭

class PetDog(Pet):
    def __init__(self, name, gender, age, breed):
        super(PetDog, self).__init__(name, gender, age, breed)

    def bark(self):
        print(self.name + '正在汪汪汪')

    def build_home(self):
        print(self.name + '正在拆家')

    def eat(self):
        print(self.name + '正在啃骨头')


# 宠物猫类 PetCat
# 属性：昵称，性别，年龄，品种，眼睛的颜色
# 方法：叫，撒娇，吃饭

class PetCat(Pet):
    def __init__(self, name, gender, age, breed, eyes_color):
        super(PetCat, self).__init__(name, gender, age, breed)
        self.eyes_color = eyes_color

    def bark(self):
        print(self.name + '正在喵喵喵')

    def build_home(self):
        print(self.name + '正在撒娇')

    def eat(self):
        print(self.name + '正在吃鱼')

    def __str__(self):  # 重写父类方法
        x = super(PetCat, self).__str__()
        x += ',眼睛颜色:{}'.format(self.eyes_color)
        return x


# 注意：狗的叫声是汪汪  猫的叫声是喵喵
#      狗吃的是骨头    猫吃的是鱼

dog1 = PetDog('小黑', 'female', 2, '阿拉斯加')
dog2 = PetDog('小白', 'male', 3, '萨摩耶')

cat1 = PetCat('tom', 'male', 3, '英短', 'blue')
cat2 = PetCat('胖胖', 'male', 2, '加菲猫', 'black')

ps = PetShop('huahua宠物店', [dog1, dog2, cat1, cat2])
ps.show_pers()
