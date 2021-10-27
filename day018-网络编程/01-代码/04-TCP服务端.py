# p 246
import socket
# 创建一个socket链接
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('192.168.1.106',9090))
s.listen(128)  # 把2socket变成被动监听的socket
# x = s.accept() # 接受客户端请求
# print(x)
# (<socket.socket fd=536, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('192.168.1.106', 9090), raddr=('192.168.1.106', 2141)>, ('192.168.1.106', 2141))
# 接收到的结果是一个元组，元组里面有两个数据
# 第0个数据是客户端的socket链接，第1个元素是客户端的ip地址和端口号
client_socket ,client_addr = s.accept()

# udp里接收数据使用recvfrom
data = client_socket.recv(1024) # tcp 里使用recv接收数据  1024指一次读1024字节
print('接收到了{}客户端 {}端口号 发送的数据，内容是{}:'.format(client_addr[0],client_addr[1],data.decode('utf8')))
# 接收到了192.168.1.106客户端 1960端口号 发送的数据，内容是hello: