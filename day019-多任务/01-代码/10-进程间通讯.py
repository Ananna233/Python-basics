# 1-20.09
import multiprocessing ,time ,os


def producer(x):
    for i in range(10):
        time.sleep(0.1)
        print('生产了+++++pid{} {}'.format(os.getpid(),i))
        x.put('pid{} {}'.format(os.getpid(),i))


def consumer(x):
    for i in range(10):
        time.sleep(0.2)
        print('{}消费了-----{}'.format(os.getpid(),x.get()))



if __name__ == '__main__':
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=producer,args=(q,))
    p2 = multiprocessing.Process(target=producer,args=(q,))
    p3 = multiprocessing.Process(target=producer,args=(q,))

    c1 = multiprocessing.Process(target=consumer,args=(q,))
    c2 = multiprocessing.Process(target=consumer,args=(q,))

    p1.start()
    p2.start()
    p3.start()

    c1.start()
    c2.start()