# 内置类 list tuple set
nums = [9, 8, 7, 5, 6]

# 使用tuple内置类转换成为元组
x = tuple(nums)
print(x)

# 使用set 内置类转换成为集合
y = set(nums)
print(y) # {5, 6, 7, 8, 9}

# python里有一个比较强大的内置函数eval，可以执行字符串里的代码
a = 'input("请输入你的名字")'  # a 是一个字符串
b = '1+1'
print(eval(b))  # a

# JSON的使用，把列表、元组、集合、字典等转换成为JSON字符串
person = {'name':'zhangsan','age':18,'gender':'female'}
# 想要把字典传给前端页面，或者把字典写入文件
# '{"name"":"zhangsan","age":18,"gender":"female"}'
import json
m = json.dumps(person)  # dumps将字典、列表、集合、元组等转换成为JSON字符串
print(m)  # {"name": "zhangsan", "age": 18, "gender": "female"}
print(type(m))  # <class 'str'>   m 是一个字符串，不能再根据key获取value

n = '{"name": "lisi", "age": 20, "gender": "male"}'
# p = eval(n)
# print(type(p))  # <class 'dict'>
s = json.loads(n)  # loads可以将json字符串转换成为Python里的数据
print(s)  # {'name': 'lisi', 'age': 20, 'gender': 'male'}
print(type(s))  # <class 'dict'>

# python        JSON
#  字符串        字符串
#  字典          对象
#  列表、元组     数组
#  Ture         true
#  False        false

# JSON 数据  ==》Python 列表