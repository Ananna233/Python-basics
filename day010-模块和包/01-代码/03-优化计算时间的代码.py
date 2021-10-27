import time  # time模块可以获取当前的时间

def cal_time(fn):  # 计算运行时间
    start = time.time()
    fn()
    end = time.time()
    print('代码运行耗时{}秒'.format(end - start))  # 代码运行耗时11.790263175964355秒


def demo():
    x = 0
    for i in range(1,100000000):
        x += i
    print(x)  # 4999999950000000


def test():
    print('hello')
    time.sleep(3)
    print('world')

cal_time(demo)
cal_time(test)