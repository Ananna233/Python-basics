a = 20
b = 12
# 方法一：使用第三个变量

# 方法二：使用运算符
# a = a + b
# b = a - b
# a = a - b

# 方法三：使用亦或运算符
# a = a ^ b
# b = a ^ b
# a = a ^ b
# 原理 a ^ b ^ b = a

# 方法四：Python特有方法
a,b = b,a

print(a)
print(b)