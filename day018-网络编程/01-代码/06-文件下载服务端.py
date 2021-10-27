# p247
import socket,os

sever_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sever_socket.bind(('192.168.1.106',9090))  # 绑定端口
sever_socket.listen(128)

# 接受客户端请求
client_socket ,client_addr = sever_socket.accept()
file_name = client_socket.recv(1024)
# print('接收到了来自{}地址  {}端口的数据，内容是:{}'.format(client_addr[0],client_addr[1],data.decode('utf-8')))
if os.path.isfile(file_name):
    with open(file_name,'rb') as file:
        content = file.read()
        client_socket.send(content)

    file.close()

else:
    print('文件不存在')