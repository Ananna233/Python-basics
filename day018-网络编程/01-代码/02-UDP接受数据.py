import socket

# 创建一个基于UDP的网络socket连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定IP地址和端口号
s.bind(('172.18.54.73', 9000))

# recvfrom 接收数据
content = s.recvfrom(1024)  # 是一个阻塞的方法，会等待接收到信息
print(content)
# 接收到的数据是一个元组，元组里有两个元素
# 第0个元素数接受到的数据，第1个元素是发送方的IP地址和端口号
print('从{}地址{}端口号接收到了信息，内容是{}'.format(content[1][0], content[1][1],content[0].decode('utf8')))

s.close()
