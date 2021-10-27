# 使用int内置类可以将数据类型转换为整数
a = '35'
b = int(a)
print(a) #str 35
print(b) #int 35
print(b+1)#int 36
# 如果字符串不是合法数字，会直接报错
# c='a'
# print(int(c))

d = '2ac6'
e = int(d,16) #10950 把字符串 2ac6 当做十六进制转换成为整数
print(e)