# 在Python里，可以使用一对单引号/双引号 或 3对单引号/双引号

a = 'hello'
b = "world!"
c = '''ahhh'''
d = """ooooo"""

print (d)
# 多种表示方式可以方便识别
m = 'xiaoming said:"i am xiaoming"'

# 字符串里的转义字符 \
x = 'I\'m xiaoming'  # \表示的是转义字符，作用是对\后面的1个字符进行转义
# '' 原义是字符串的开始，，使用\ 后吧'转为普通的单引号，显示一个普通的单引号
print(x)  # I'm xiaoming

y = "xiaoming said:\"I am xiaoming\" "
print(y) # xiaoming said:"I am xiaoming"
# 常见的
# \n ==>表示换行
# \t ==>表示一个制表符
# \\ ==>表示\
# 在字符串的前面添加 r 在Python里面表示的是原生的字符串

# \n表示换行  \\n==> 第一个\表示对第二个\转义，为普通的字符\
x1 = 'good mor\\ning' # good mor\ning
print(x1)

# 在字符串的前面添加 r 在Python里面表示的是原生的字符串
x2 = r'hello \teacher'
print(x2) # hello \teacher