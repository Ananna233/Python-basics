import socket
# 不同电脑之间的通信需要使用socket
# socket可以在不同的电脑间通讯，还可以在同一个电脑的不同程序之间通信

# 1.创建socket，并连接
# AF_INET:表示这个socket是用来进行网络连接
# SOCK_DGRAM: 表示连接是一个UDP连接
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 2.发送信息
# data:要发送的数据，它是二进制的数据
# address:发送给谁  参数是一个元组，元组里有两个元素 第0个是目标的IP地址 ，第一个是表示程序的端口号

# 给172.18.54.73这台主机的9000端口上发送了 hello
# 端口号: 0~65536  0~1024不要用，系统   找一个空闲的端口号
s.sendto('hello'.encode('utf8'),('172.18.54.73',9000))

# 3.关闭socket
s.close()