# 1-20.04
import threading
import time

# 多个线程可以同时操作一个全局变量（多个线程共享全局变量）
ticket = 20

# 创建一把锁
lock = threading.Lock()

def sell_ticket():
    global ticket
    while True:
        lock.acquire()
        if ticket > 0:
            ticket -= 1
            time.sleep(0.5)
            lock.release()
            print('{}卖出一张票，还剩{}张'.format(threading.current_thread().name,ticket))
        else:
            print('票卖完了')
            lock.release()
            break


t1 = threading.Thread(target=sell_ticket, name='线程1')
t2 = threading.Thread(target=sell_ticket, name='线程2')

t1.start()
t2.start()
