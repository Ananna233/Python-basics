# Python里使用open 内置函数用来打开一个文件
# file：文件的路径。相对路径和绝对路径
# mode：打开文件的模式  r:只读  w:只写  b:二进制  t:文本形式打开
# mode 默认使用的 rt
# encoding:用来指定文件的编码方式。Windows系统里默认是gbk

# 读
file = open('yyy.txt', encoding='utf8')
# print(file.read())  # 将所有的数据都读取出来
# print(file.readline())  # 只读取一行

# while True:
#     content = file.readline()
#     print(content)
#     if content == '':
#         break

# 读取所有行的数据，保存到一个列表里
# x = file.readlines()
# print(x)  # ['你好\n', 'hello\n', 'hihihi\n', '嘤嘤嘤\n', 'QAQ\n', '呜呜呜\n', '哈哈哈']

x = file.read(10)  # 读取指定长度
print(x)  # 你好ya,爱你呀，喵

file.close()

# 优化：没有绝对的优化，除非提升硬件
# 软件层面：时间  /  空间