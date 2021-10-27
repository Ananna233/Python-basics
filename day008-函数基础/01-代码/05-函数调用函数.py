def test1():
    print('test1开始了')
    print('test2结束了')

def test2():
    print('test2开始了')
    test1()
    print('test2结束了')

test2()

# 断点调试
# 左边123……可以点断点
# 点右上小绿虫Debug调试
# 下边的调试栏
# 左上绿色（像播放键） |>  运行到下一断点
# 下边长条菜单栏第一个  ^ 下一步step over
#                   -
# console 控制台，可以看运行结果
# 运行顺序：行6-》行8  会直接执行函数test1（）,要进入函数点长条菜单栏第二个step into
# 跳出 第四个step out

# 求[n,m)之间所有整数之和
def add(n,m):
    x = 0
    for i in range(n,m):
        x += i
    return x

print(add(1,101))  # 5050

# 求n的阶乘
def factorial(n):
    x = 1
    for i in range(1,n+1):
        x *= i
    return x

print(factorial(5))  # 120

# 计算m阶乘的和  x = 6 =>1! + 2! +3!+4!+5！+6!
def fac_sum(m):
    x = 0
    for i in range(1,m+1):
        x += factorial(i)
    return x

print(fac_sum(5))  # 153

