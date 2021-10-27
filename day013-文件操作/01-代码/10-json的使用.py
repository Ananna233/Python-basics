# 序列化：将数据从内存持久化保存到硬盘的过程
# 反序列化：将数据从硬盘加载到内存的过程

# write 只能写入字符串或者二进制
# 字典、列表、数字都不能直接写入到文件里

# 将数据装换成为字符串：repr/str  使用json模块
# json本质就是字符串，区别在于json里要用双引号表示字符串
# 将数据装换成二进制:使用pickle模块

import json

file = open('names.txt', 'w', encoding='utf-8')
names = ['zhangsan', 'lisi', 'wangwu', 'tony']
x = json.dumps(names)  # dumps的作用是将数据转换成为字符串
print(x)  # '["zhangsan", "lisi", "wangwu", "tony"]'

file.write(x)

# json里将数据持久化有两个方法：
# dumps：将数据转换成为json字符串，不会将数据保存到文件里
# dump：将数据转换成为json字符串的同时写入指定文件
# json.dump(names, file)

file.close()

# json 反序列化也有两个方法
# loads:将json字符串加载成为Python里的数据
# load：读取文件，把读取的内容加载成为Python里的数据

x = '{"name":"zhangsan","age":18}'  # 符合json规则的字符串

p = json.loads(x)
print(p, type(p))  # {'name': 'zhangsan', 'age': 18} <class 'dict'>
print(p['name'])  # zhangsan

# load 读取一个文件，并把文件里的json字符串加载成为一个对象
file1 = open('names.txt', 'r', encoding='utf-8')
y = json.load(file1)
print(y)  # ['zhangsan', 'lisi', 'wangwu', 'tony']
print(y[0])  # zhangsan

file1.close()


class Penson(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃东西')


p = Penson('Anan', 21)
x = json.dumps(p.__dict__)
y = json.loads(x)

print(x)  # {"name": "Anan", "age": 21}
print(y)  # {'name': 'Anan', 'age': 21}
