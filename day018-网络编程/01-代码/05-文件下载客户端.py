# p247
import socket,os

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('192.168.1.106',9090))  # 链接服务器

# client_socket.send('hello'.encode('utf8'))
file_name = input('请输入一个文件名:')
client_socket.send(file_name.encode('utf8'))

with open('ddd'+file_name,'wb') as file:
    while True:
        content = client_socket.recv(1024)
        if not content:
            break
        file.write(content)

file.close()

client_socket.close()