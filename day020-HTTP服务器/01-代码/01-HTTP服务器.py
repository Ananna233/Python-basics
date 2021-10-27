 # 1-21.01
import socket

# HTTP 服务器都是基于TCP的socket链接的
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('0.0.0.0', 9090))
server_socket.listen(128)  # 128排队长度

# 获取到的数据是一个元组，元组里有两个元素
# 第0个元素是 客户端的socket链接
# 第1个元素是 客户端的IP和端口号
client_socket, client_addr = server_socket.accept()

# 客户端的socket 里获取数据
data = client_socket.recv(1024).decode('utf8')
print(data)

# 返回内容之前，需要先设置HTTP相应头
#设置一个响应头就换一行
client_socket.send('HTTP/1.1 200 OK\n'.encode('utf8'))

# 所有的响应头设置完以后再换行
client_socket.send('\n'.encode('utf8'))

# 给客户端返回消息
client_socket.send('hello world'.encode('utf8'))