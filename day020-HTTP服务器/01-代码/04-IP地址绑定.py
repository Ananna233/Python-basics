# 1-21.03
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# IP地址只能通过IP地址访问
# server_socket.bind(('192.168.43.146', 9090))

# 能够通过127.0.0.1和localhost来访问
# server_socket.bind(('127.0.0.1',9090))
# 127.0.0.1和0.0.0.0都表示本机
# 表示所有可用地址
server_socket.bind(('0.0.0.0', 8090))

server_socket.listen(128)  # 128排队长度

client_socket, client_addr = server_socket.accept()

data = client_socket.recv(1024).decode('utf8')
print(data)

client_socket.send('HTTP/1.1 200 OK\n'.encode('utf8'))
client_socket.send('\n'.encode('utf8'))
client_socket.send('hello world'.encode('utf8'))