# 1-20.02
import socket
import threading

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(('192.168.1.106',8080))


def send_msg():
    while True:
        msg = input('8080请输入你要发送的内容:')
        if msg == 'exit':
            break
        s.sendto(msg.encode('utf8'),('192.168.1.106',9090))

def recv_msg():
    while True:
        # data的数据类型是一个元组
        # 元组里第0个元素是接受到的数据
        # 元组里的第一个元素是发送方的IP地址和端口号
        data ,addr= s.recvfrom(1024)
        print('8080接收到了{}地址  {}端口的消息:{}'.format(addr[0],addr[1],data.decode('utf8')))

t1 = threading.Thread(target=send_msg)
t2 = threading.Thread(target=recv_msg)

# 启动线程
t1.start()
t2.start()

# s.close()