# 类型转换 将一个类型的数据转换为其他类型的数据
# int==>str、float、   str==>int …………
age = input("请输入年龄:")
print(type(age))  # <class 'str'>
#使用int 内置类可以将其他类型的数据转换成为整数-
new_age = int(age) #使用int 内置类可以将其他类型的数据转换成为整数
print(type(new_age))
print(new_age+1)
