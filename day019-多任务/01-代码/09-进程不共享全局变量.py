# 1-20.08
import threading,os,multiprocessing

n = 100

def test():
    global n
    n+=1
    print('test pid={}里的n值是{},id(n)={}'.format(os.getpid(),n,hex(id(n))))


def demo():
    global n
    n+=2
    print('demo pid={}里的n值是{},id(n)={}'.format(os.getpid(),n,hex(id(n))))

# 同一个主进程里的两个子线程。线程之间可以共享同一进程的全局变量
# t1 = threading.Thread(target=test)  # test pid=26460里的n值是101
# t2 = threading.Thread(target=demo)  # demo pid=26460里的n值是102
#
# t1.start()
# t2.start()

# 不同进程访问全局变量
if __name__ == '__main__':
    # 不同进程各自保存一份全局变量，不会共享全局变量
    p1 = multiprocessing.Process(target=test)  # test pid=9620里的n值是101,id(n)=0x7ffc31d52320
    p2 = multiprocessing.Process(target=demo)  # demo pid=31220里的n值是102,id(n)=0x7ffc31d52340
    # 如果两个n的值是一样的，则会指向同一个内存地址

    p1.start()
    p2.start()