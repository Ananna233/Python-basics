# 1-20.06
import multiprocessing ,time,os

def dance(m):
    for i in range(m):
        time.sleep(0.3)
        print('正在跳舞,pid = {}'.format(os.getpid()))

def sing(n):
    for i in range(n):
        time.sleep(0.3)
        print('正在唱歌,pid = {}'.format(os.getpid()))


if __name__ == '__main__':
    print('主进程的pid = {}'.format(os.getpid()))
    # 创建了两个进程
    # target 用来表示执行的任务
    # args 用来传参，类型是一个元组
    p1 = multiprocessing.Process(target=dance, args=(10,))
    p2 = multiprocessing.Process(target=sing, args=(15,))

    p1.start()
    p2.start()

