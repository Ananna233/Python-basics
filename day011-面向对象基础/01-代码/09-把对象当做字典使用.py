class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setitem__(self, key, value):  # key = 'zhangsan'
        # print('setitem方法被调用了，key={}，value={}'.format(key,value))
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]


p = Person('zhangsan', 18)
print(p.__dict__)  # 将对象转换成为字典 {'name': 'zhangsan', 'age': 18}

# 改变值
# 可以转为字典，但不能直接把一个对象当做字典来使用
p['name'] = 'jack'  # []语法会调用对象的__setitem__方法
p['age'] = 22

print(p.name, p.age)  # jack  22

# 获取值
print(p['name'])  # 会调用__getitem__方法

# 这个也可以改？？！！
p.name = 'anan'
print(p.name)