# mode 指的是文件的打开方式
# r  只读模式，默认，打开文件后，只能读取，不能写入  如果文件不存在会报错
# w  写入模式，打开文件以后，只能写入，不能读取  如果文件存在，会覆盖文件；如果文件不存在，会创建文件
# b  以二进制形式打开文件  可以用来操作非文本文件
# rb 以二进制读取  rw 以二进制写入

# a 追加模式，会在最后追加内容。如果文件不存在，会创建文件，如果文件存在，会追加
# r+ 可读写  如果文件不存在会报错
# w+ 可读写  如果文件存在，会覆盖文件；如果文件不存在，会创建文件


# file = open('xxx.txt','r',encoding='utf-8')
# print(file.read())
# file.write('hello')  不能执行写入操作，会报错

# file = open('xxx.txt','w')
# # file.read()  # 不能执行读取，会报错
# file.write('hello')
# file = open('yyy.txt','w')

# file = open('xxx.txt','rb')
# print(file.read())  # 读取的结果是二进制  ？？

# file = open('xxx.txt','wb')
# # file.write('今天是10月9日')  # 会报错，只能写入二进制
# file.write('今天是10月9日'.encode('utf8'))
#
# file = open('xxx.txt','rb')
# print(file.read())  # 读取的结果是二进制

file = open('yyy.txt', 'w+', encoding='utf8')
file.write('hahaha')
file.seek(0, 0)  # 写入后，文件指针到最后，需要调用seek将文件指针置到开头
print(file.read())

file.close()
