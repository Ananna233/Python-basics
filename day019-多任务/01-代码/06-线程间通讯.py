# 1-20.05
import queue
import threading
import time


def produce():
    for i in range(10):
        time.sleep(0.1)
        print('{}生产了+++++面包{}'.format(threading.current_thread().name, i))
        q.put('{} {}'.format(threading.current_thread().name, i))


def consumer():
    while True:
        # q.get()方法是一个阻塞的方法
        time.sleep(0.3)
        print('{}买到了-----面包{}'.format(threading.current_thread().name, q.get()))


q = queue.Queue()  # 创建一个队列

# 一条生产线
pro1 = threading.Thread(target=produce, name='pro1')
pro2 = threading.Thread(target=produce, name='pro2')
pro3 = threading.Thread(target=produce, name='pro3')

# 一条消费线
con1 = threading.Thread(target=consumer, name='con1')
con2 = threading.Thread(target=consumer, name='con2')

pro1.start()
pro2.start()
pro3.start()

con1.start()
con2.start()
