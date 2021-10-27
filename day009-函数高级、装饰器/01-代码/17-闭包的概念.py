# 闭包=函数块 + 引用环境
def outer():
    x = 10  # 在外部函数里定义了一个变量x，是一个局部变量

    def inner():
        # 在内部函数如何修改外部函数的局部变量
        nonlocal x  # 此时，这里的x不再是新增的变量，而是外部的局部变量x
        y = x + 1
        print('inner里的y=',y)  # inner里的y= 11

    return inner

outer()()