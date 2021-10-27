# p 245
import socket

# 基于TCP协议的socket链接
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# udp使用sendto发送数据

# 在发送数据之前必须要先和服务器建立链接
s.connect(('192.168.1.106',9090))  # 调用connect方法链接到服务器
s.send('hello'.encode('utf8'))
s.close()