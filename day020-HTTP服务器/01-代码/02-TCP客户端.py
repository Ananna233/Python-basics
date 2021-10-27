import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('172.18.54.94', 8090))

s.connect((('172.18.54.94', 9090)))
s.send('hello'.encode('utf8'))

s.close()