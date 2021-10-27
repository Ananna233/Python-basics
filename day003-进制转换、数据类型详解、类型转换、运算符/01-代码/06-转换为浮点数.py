a = '12.34'
# 使用内置float 类可以将其他类型数据转换成为float浮点数
b = float(a)
print(b + 1)

# 如果字符串不能转换为有效的浮点数，会报错

c = 102
d = float(c)
print(d) #102.0