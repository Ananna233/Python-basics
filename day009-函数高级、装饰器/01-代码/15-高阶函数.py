# 1、一个函数作为另一个函数的参数 （匿名函数 lambda)
# 2、一个函数作为另一个函数的返回值
# 3、函数内部再定义一个函数

def foo():
    print('foo被调用l')
    return 'foo'


def bar():
    print('bar被调用了')
    return foo()


def aaa():
    print('aaa被调用了')
    return foo


x = bar()
print('x的值是{}'.format(x))
'''
bar被调用了
foo被调用l
x的值是foo
'''
y = aaa()  # <function foo at 0x0000016007098280>
print(y)
y()  # foo被调用l  实际上aaa()的返回值是foo   y=foo y就变成了foo函数的别名
print('------------')
z = aaa()()
print(z)  # foo

# ---------------------
print('--------------------')

# 装饰器
def outer():
    m = 100

    def inner():
        n = 90
        print('我是inner函数')

    print('我是outer函数')
    return inner


gg=outer()  # 我是outer函数
print(gg)  # <function outer.<locals>.inner at 0x00000159BC4584C0>

outer()()
# 我是outer函数
# 我是inner函数
# inter只能在函数内部调用
