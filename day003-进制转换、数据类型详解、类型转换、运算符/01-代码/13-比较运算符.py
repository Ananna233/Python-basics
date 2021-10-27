# 大于>  小于<  大于等于>=  小于等于<==   不等于！=  等等与==
print(2 > 1)  # True
print(2 < 4)  # True
print(5 >= 6)  # False
print(1 <= 9)  # True
print(5 != 6)  # True
print('hello' == 'hello')  # True

# 比较运算符在字符串里的使用
# 字符串之间使用比较运算符，会根据各个字符的编码值逐一进行比较
# ASCII码
print('a' > 'b')  # False
print('abc' > 'b')  # False
print('b' > 'a')  # Ture

# 数字和字符串之间，做==运算符的结果是False，做！=运算结果是True，不支持其他的比较运算
print('a' == 97)  # False
print("a" != 97)  # True
