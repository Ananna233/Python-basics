def test():
    print('我是test函数')
    return 'hello'


def demo():
    print('我是demo函数')
    return test  # 返回的是test函数


def bar():
    print('我是bar函数')
    return test()  # 调用test函数，执行test函数，返回test函数执行结果
    # 加括号就是调用函数

a = bar()  # 我是bar函数  我是test函数
print(a)  # hello
'''
我是bar函数
我是test函数
hello
'''

x = test()  # 我是test函数
print(x)  # hello
print('-----------------')

y = demo()  # 我是demo函数
print(y)  # <function test at 0x0000027C69F38280>   这时候y就是test函数（别名）
z = y()  # 我是test函数
print(z)  # hello

# 2、把一个函数当做另一个函数的参数：lambda表达式的使用
# sort fillter map reduce
# 3、在函数内部再定义一个函数