# 将数据写入到内存涉及到 StringIO和BytesIO两个类
from io import StringIO, BytesIO

s_io = StringIO()
s_io.write('hello')  # 把数据写入到了内存里缓存起来
s_io.write('good')

print(s_io.getvalue())  #

# file 需要的是一个文件流对象
# print('hello', file=open('sss.txt', 'w'))

print('hello', file=s_io)
print('world', file=s_io)
print('good', file=s_io)

print(s_io.getvalue())
s_io.close()

# ByteIO
b_io = BytesIO()
b_io.write('你好'.encode('utf8'))
print(b_io.getvalue())  # b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(b_io.getvalue().decode('utf-8'))  # 你好
b_io.close()
