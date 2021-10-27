class Singleton(object):
    __instance = None  # 私有变量
    __is_first = True  # 类属性只能通过类对象修改

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            # 申请内存，创建一个对象，并把对象的类型设置为cls
            cls.__instance = object.__new__(cls)  # 这个是申请内存
        return cls.__instance

    def __init__(self, a, b):
        if self.__is_first:
            # 第一次修改允许，，后面就不允许修改覆盖了
            # 实际上，是创建了一个对象属性__is_frist = False，而不是修改了上面的类属性__is_first
            self.__is_first = False
            self.a = a
            self.b = b

    @classmethod
    def aaa(cls):
        return cls.__is_first

# 调用__new__方法申请内存  （先调用__new__方法  再调用__init__方法)
# 如果不重写__new__方法，会调用object的__new__方法
# object的__new__方法会申请内存
# 如果重写了__new__方法，需要自己手动的申请内存
s1 = Singleton('哈哈', 'abc')
s2 = Singleton('呵呵', 'ABC')

print(s1 is s2)
print('s1=', s1.a, s1.b)  # s1= 呵呵 ABC
print('s2=', s2.a, s2.b)  # s2= 呵呵 ABC
# 覆盖了  可以不让覆盖,设置类属性  __is_first = True

print(Singleton.aaa())  # True   没有被修改！！！！！！