# 1-21.02
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('192.168.43.146', 9090))
server_socket.listen(128)  # 128排队长度

client_socket, client_addr = server_socket.accept()

data = client_socket.recv(1024).decode('utf8')
print(data)
'''

GET / HTTP/1.1   # GET请求方式，GET/POST/PUT/DELETE...  /... 请求的路径以及请求参数   HTTP/1.1 HTTP版本号
Accept: text/html, application/xhtml+xml, image/jxr, */*
Accept-Language: zh-CN
Accept-Encoding: gzip, deflate
Host: 192.168.43.146:9090   # 请求的服务器地址
Connection: Keep-Alive

# UA 用户代理，最开始设计的目的是为了能从请求头识别浏览器的类型
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko Core/1.70.3775.400 QQBrowser/10.6.4208.400
'''

client_socket.send('HTTP/1.1 200 OK\n'.encode('utf8'))
client_socket.send('\n'.encode('utf8'))

client_socket.send('hello world'.encode('utf8'))