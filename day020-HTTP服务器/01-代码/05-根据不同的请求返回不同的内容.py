# 1-21.04
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('0.0.0.0', 9090))

server_socket.listen(128)  # 128排队长度

while True:
    client_socket, client_addr = server_socket.accept()

    data = client_socket.recv(1024).decode('utf8')
    path = ''
    if data:  # 服务器有可能会发送空数据
        print('接收到{}的数据\n{}'.format(client_addr[0], data))
        path = data.splitlines()[0].split(' ')[1]
        print('请求的路径是{}'.format(path))


    response_header = 'HTTP/1.1 200 OK\n'

    if path == '/login':
        response_body = '欢迎来到登录页面'
    elif path == '/register':
        response_body = '欢迎来到注册页面'
    elif path == '/':
        response_body = '欢迎来到首页'
    else:
        response_header ='HTTP/1.1 404 Page Not Found\n'
        response_body = '对不起，你找的页面不存在'
    # 响应头
    response_header += 'content-type:text/html;charset=utf8\n'
    response_header += '\n'
    # 响应体
    #response_body = 'hello world+++'
    # 响应
    response = response_header + response_body

    client_socket.send(response.encode('utf8'))
