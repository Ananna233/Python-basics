import time


def cal_time(fn):
    print('我是外部函数，我被调用了！！')
    print('fn={}'.format(fn))
    def inner(x,*args,**kwargs):
        start = time.time()
        s = fn(x)  # 注意这里，fn是demo，要返回值的就在原demo，，return，用s去接住，再return s
        end = time.time()
        print('代码耗时：', end - start)
        return s

    return inner


@cal_time  # 第一件事调用cal_time;第二件事：把被装饰的函数传递给fn
def demo(n):
    x = 0
    for i in range(1, n):
        x += i
    return x



print('装饰后的demo = {}'.format(demo))
m = demo(100000000,'hello',y=12345)  # demo已经不是之前的demo，是inner

print('m 的值是',m)


# 有点有点乱